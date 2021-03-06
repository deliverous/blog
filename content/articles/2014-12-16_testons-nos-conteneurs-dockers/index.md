---
title: Testons nos conteneurs Docker
tags:
  - docker
  - tdd
authors:
  - Thomas Clavier
  - Olivier Albiez
description: Vous aussi vous êtes adepte du test driven developpement ? Alors voici comment nous faisions pour construire nos conteneurs Docker depuis les tests.
date: 2014-12-16
publishdate: 2014-12-16
aliases: /2014-12-16.testons-nos-conteneurs-dockers.html
---

Coder à l'endroit. Pour nous, l'ordre normal des choses, c'est identifier un besoin, le tester, s'il n'est pas rempli, le coder et enfin vérifier qu'il est bien présent. Pour tous les adeptes du *Test Driven Developpement*, c'est l'enchainement logique des phases de test et de codage. Seulement voilà, comment faire pour dérouler ces étapes pour réaliser un conteneur Docker.

L'ensemble du code présenté dans cet article est consultable dans un [projet github](https://github.com/Deliverous/docker-extreme_startup)

# Une histoire de services

Après la lecture de [Twelve Factor Apps](2014-05-26.twelve-factor-apps-1.html), il apparait évident qu'un conteneur est une application ou une ressource distante. Donc pour tester ce service, il suffit de se connecter sur le port réseau exposé et de parler la même langue que le service. Aujourd'hui, il est possible de ranger les applications dans 3 grandes catégories :

- les applications web : exposent de l'http et fournissent html, css et javascript
- les services web : exposent de l'http et fournissent des objets sérialisés principalement en json et xml
- les autres services : base de données, xmpp, etc.

On peut affirmer, sans prendre trop de risque, qu'il est possible de tester toutes ces applications dans nos langages de développement. [Capybara](https://github.com/jnicklas/capybara) permet par exemple de naviguer sur des applications web, il est aussi très simple de se brancher sur des services SOAP ou REST, enfin les pilotes pour accéder à des bases de données, des files de messages où d'autres services sont quasiment tous présents dans les langages populaires.

Pour l'exemple, j'ai choisi ruby, mais je vous invites à faire de même avec votre langage favori.

# Extreme Startup

C'est un petit jeu que j'utilise de temps en temps en cours. Il permet de découvrir en quelques heures quelques bonnes pratiques du développement logiciel. Pour en savoir plus je vous invite à visiter la page [github](https://github.com/rchatley/extreme_startup)

C'est l'application que nous allons "dockerifier"

# Un peu d'organisation

Pour nos conteneurs, nous avons pris l'habitude de ranger notre dossier de travail de la façon suivante :

- Le fichier *Dockerfile* qui permet la construction automatique du conteneur
- Un fichier *Rakefile* pour automatiser l'ensemble des taches
- Un fichier *Gemfile* pour gérer nos dépendances ruby
- un dossier *src* pour héberger les fichiers utile à la construction du conteneur et les sources de l'application si vous en êtes l'auteur.
- un dossier *test* pour ranger tous nos tests
- un dossier *.target* qui sert de répertoire de travail

## Des dépendances

Les fichiers Gemfile et Rakefile sont là pour automatiser les taches récurrentes, typiquement :

- Préparer l'environnement de travail
- Construire le conteneur
- Lancer le conteneur
- Lancer les tests

Les 3 premières opérations se font avec la gem rake-docker qui automatise toutes les opérations de base sur les conteneurs docker. La dernière est gérée par la gem docker-tdd.
Bien évidemment dans un but pédagogique, nous aurions pu tout réécrire en plus simple. Ce sera certainement le sujet d'un nouvel article.

## Rakefile en détail

    require 'rake/docker_lib'

Permet de charger rake-docker

    directory '.target/app'  => '.target' do
      sh "git clone git@github.com/rchatley/extreme_startup.git .target/app"
    end

.target/app est le répertoire avec les sources du projet amont, cloné à la création du répertoire.

    Rake::DockerLib.new("tclavier/extreme-startup") do
      prepare do
         sh "cd app/ && git pull"
      end
    end

On force un pull à chaque préparation. Cela implique de toujours avoir le réseau.

    task test: :build
    task prepare: '.target/app'

Quelques dépendances forcées.

# TDD power !

Pour que docker ne hurle pas durant la phase de build, nous pouvons faire un premier Dockerfile presque vide

    from deliverous/wheezy
    cmd tail -f /var/log/*

Notez la présence du tail dans la commande à démarrer par défaut, il faut en effet être certain que le conteneur se lance et reste actif.

## Premier test

Pour ce premier test, on va travailler dans le fichier test/test_extreme_startup.rb.
Pour lancer le test, il faut lancer le conteneur ça se fait dans la fonction containers :

    describe "Extreme-startup" do
      include DockerTdd::ContainerPlugin
      def containers
        @xs = DockerTdd::Container.new "tclavier/extreme-startup", boottime: 1
      end
      ...
    end

L'application doit écouter en http sur le port 3000.

    it "must listen in http on port 3000" do
      open("http://#{@xs.address}:3000/")).status[0].must_equal '200'
    end


Notez que l'attribut @xs contient quelques attributs fort pratique entre autres l'adresse IP attribué par docker au conteneur.

Le "rake test" nous dit que le test est bien en échec, tout va bien.

## Première implémentation

Passons à l'implémentation. Donc retour dans le fichier Dockerfile.
On installe ruby et unicorn

    run apt-get update && \
        apt-get install -y --no-install-recommends ruby && \
        apt-get clean

On installe les dépendances ruby

    run apt-get update && \
        apt-get install -y bundler sudo libxslt-dev libxml2-dev && \
        cd /opt/extreme_startup && bundle update && \
        apt-get remove -y bundler libxslt-dev libxml2-dev &&\
        apt-get autoremove -y &&\
        apt-get clean

Je fais un bundle update et pas un bundle install, en effet la version de nokogiri présente dans le Gemfile.lock ne compile plus sous Debian stable.

Et on lance le service

    cmd cd /opt/extreme_startup && ruby web_server.rb

Puis on relance le test

    rake build test

Et voilà ! Premier test OK.

## Warmup

Pour que le premier sprint ne génère pas d'inégalité technique, il y a une option warmup qui permet d'avoir toujours la même question.

Pour faire ce test, comme le conteneur est lancé durant le setup il faut faire une seconde classe de test pour passer les bonnes options au conteneur.

    @xs = DockerTdd::Container.new "tclavier/extreme-startup", env: ['WARMUP=1'], boottime: 1

Une fois encore le conteneur doit écouter sur le port 3000, mais il doit aussi déclencher une erreur au changement de round

    it "must listen in http on port 3000" do
      open(url('/')).status[0].must_equal '200'
    end

    it "must restart to change round" do
      params = {'param1' => 'value1'}
      url = URI.parse(url('/advance_round'))
      resp = Net::HTTP.post_form(url, params)
      resp.code.must_equal '500'
    end

On lance les tests et tout est vert.

## Dernier test

Nous avons bien testé que le changement de round déclenche une erreur en cas de warmup. Mais dans le cas nominal que ce passe-t-il ? Nous allons donc ajouter le test suivant dans test/test_extreme_startup.rb.

    it "can change round" do
      params = {'param1' => 'value1'}
      url = URI.parse(url('/advance_round'))
      resp = Net::HTTP.post_form(url, params)
      resp.code.must_equal '200'
    end

Il suffit de lancer le test pour voir que les 4 tests sont vert.

# Conclusion

Nous avons fait 4 tests dans 2 classes avec une implémentation simple. Ce qui nous a permis de voir une bonne partie de notre environnement de test. Nous avons en particulier appris à :

- déclarer un conteneur dans le fichier Rakefile
- aller chercher le code source dans un autre projet durant la phase de préparation
- déclarer des variables d'environnement à l'exécution du conteneur
- utiliser la lib Net::HTTP pour interroger le conteneur
published
Ce qui couvre une grande partie de nos tests.

---
Photo par [Med](https://www.flickr.com/photos/prodiffusion/5684301592)

