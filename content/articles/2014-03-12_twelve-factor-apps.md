Title: The Twelve Factor Apps
Tags: 12factor, heroku
Author: Thomas, Olivier
Summary: Etude de *The Twelve Factor Apps*. La théorisation d'une bonne application par Adam Wiggins l'un des fondateurs de [Heroku](https://www.heroku.com/)
Status: draft

[*CoreOS*](https://coreos.com) est un projet qui vise à abstraire des nœuds pour créer un cluster. Ce projet se base sur un *Linux* minimal, de la découverte de service (*etcd*), *docker* et *systemd*.

![Cluster]({filename}/images/sky_cluster.jpg)

# 1 - La base de code

Premier point et non des moindres, une application a un unique dépôt de code géré par un gestionnaire de version comme git, mercurial, bazard ou subversion.
Chaque changement est traqué et un déploiement correspond à une révisons identifiable du code. 
Une application n'a qu'un unique dépôt de code :

- s'il y a plusieurs dépôts de code alors ce n'est plus une application mais un système distribué composé de plusieurs applications.
- si de multiples applications partagent le même dépôt de code alors il faut absolument changer ça et factoriser le code commun dans des librairies et utiliser un gestionnaire de dépendances pour gérer ces librairies.

Alors qu'il ne peut exister qu'un dépôt de code par application, il y aura probablement plusieurs déploiements de cette application. 
Chaque développeur peut par exemple en avoir une version qui tourne sur son poste de travail, la qualification et la production aurons elles aussi des versions en cours d'exécutions.

Pour résumer : un unique dépôt de code == une application => de multiples déploiements.

# 2 - Les dépendances

Gérer explicitement les dépendances et isoler l'application.

La majorité des langages de programmation permettent de distribuer des librairies, CPAN pour Perl ou Rubygems pour Ruby. 
Pour installer ces dépendances il existe 2 écoles : 
- le tout système
- le sous répertoire (vendors dans pas mal de cas)
Utiliser l'une ou l'autre de ces solution sera fortement dépendant de la façon d'isoler l'application (container, répertoire, etc.).

Une application 12 factors doit explicitement déclarer ses dépendances, jamais elle ne doit présumer de la présence d'une dépendance. 
Avec la description des dépendances il doit être possible de reconstruire intégralement toute l'application avant de l'exécuter. 
En ruby il est par exemple possible d'utiliser bundler et les Gemfile, en java, maven ou ivy seront de bon candidats.

Attention, des dépendances implicite sur des outils systèmes comme ImageMagick, curl ou wget sont à proscrire de la même façon que les dépendances implicite vers des librairies. 
Pour résoudre des dépendances de ce type, il sera utile d'embarquer ces dépendances ou d'utiliser une plateforme qui fait de l'isolation par container.

# 3 - La configuration

La configuration c'est ce qui peut varier en fonction de l'environnement :

- les éléments qui permettent d'accéder à des resources de stockages (base de donnée, ) 

Enregistrer la configuration dans le dépôt de code est une très mauvaise idée. 
