Title: The Twelve Factor Apps 1/2
Tags: 12factor, heroku
Author: Thomas, Olivier
Summary: Etude de *The Twelve Factor Apps*. La théorisation d'une bonne application par Adam Wiggins l'un des fondateurs de [Heroku](https://www.heroku.com/)
Status: draft

*The Twelve Factor Apps* c'est la définition des bonnes pratiques que doivent suivre un développeur pour produire une application portable et capable de passer à l'échelle. Ces 12 règles ont été rédigées par Adam Wiggins l'un des fondateurs de [Heroku](https://www.heroku.com/). 
Pour certains, il ne s'agit que de prendre en compte une certaine catégorie d'utilisateur : les administrateurs systèmes. 
Dans la pratique, ces règles sont la garantie qu'une grande partie de l'administration sera automatisable. 
Alors que le mouvement devops vise à aligner les équipes de l'entreprise sur des objectifs commun, Adam a résolu le conflit entre développeurs et administrateurs systèmes en fixant des règles communes.

Cette série de 2 articles va nous permettre de comprendre ces règles.

![Cluster]({filename}/images/sky_cluster.jpg)

# 1 - La base de code

Un unique dépôt de code pour une application et de multiples déploiements.

Premier point et non des moindres, une application a un unique dépôt de code géré par un gestionnaire de version comme git, mercurial, bazard ou subversion.
Chaque changement est traqué et un déploiement correspond à une révisons identifiable du code. 
Une application n'a qu'un unique dépôt de code :

- s'il y a plusieurs dépôts de code alors ce n'est plus une application, mais un système distribué composé de plusieurs applications.
- si de multiples applications partagent le même dépôt de code, vous avez sans doute de quoi extraire des librairies.

Alors qu'il ne peut exister qu'un dépôt de code par application, il y aura probablement plusieurs déploiements de cette application. 
Par exemple, un déploiement par développeur, la qualification et la production.

# 2 - Les dépendances

Gérer explicitement les dépendances et isoler l'application.

La majorité des langages de programmation permettent de distribuer des librairies, CPAN pour Perl ou Rubygems pour Ruby. 
Une application 12 factors doit explicitement déclarer ses dépendances, jamais elle ne doit présumer de la présence d'une dépendance. 
Avec la description des dépendances, il doit être possible de reconstruire intégralement toute l'application avant de l'exécuter. 
En ruby il est par exemple possible d'utiliser bundler et les Gemfile, en java, maven ou ivy seront de bons candidats.

Pour installer ces dépendances, il existe 2 écoles : 
- le tout système
- un sous-répertoire (vendors dans pas mal de cas)
Utiliser l'une ou l'autre de ces solutions sera fortement dépendant du gestionnaire de dépendances et de la façon d'isoler l'application (container, répertoire, etc.).

Attention, des dépendances implicites sur des outils systèmes comme ImageMagick, curl ou wget sont à proscrire de la même façon que les dépendances implicite vers des librairies. 
Pour résoudre des dépendances de ce type, il sera utile d'embarquer ces dépendances ou d'utiliser une plateforme qui fait de l'isolation par container.

# 3 - La configuration

La configuration, c'est ce qui peut varier en fonction de l'environnement :

- les éléments qui permettent d'accéder à des ressources de stockages (base de données, base de cache, services en lignes, etc.) 
- les éléments d'authentification sur ces ressources externe
- des variables spécifiques au déploiement pour générer les assets par exemple.

Enregistrer la configuration dans le dépôt de code est une très mauvaise idée, en effet la configuration varie beaucoup en fonction de l'environnement alors que le code non.
Bien séparer les 2 permet par exemple de ne pas déclencher toute la chaine de construction pour un changement de mot de passe. 
Elle permet aussi de libérer le code sans compromettre un accès privé.

Certains frameworks ou modules demandent de la configuration ... Mais ce n'est pas de la même configuration dont on parle. En effet la configuration d'un framework ou d'un module ne change pas en fonction de l'environnement d'exécution. 

Il existe 2 pratiques couramment utilisées : un fichier de configuration qui ne sera pas enregistré dans le dépôt ou des variables d'environnements. 
Le problème du fichier de configuration, c'est qu'il peut très facilement être enregistré par erreur. 
12 factors Apps utilise donc des variables d'environnements.

Une autre pratique courante consiste à regrouper ces variables par environnement, par exemple *qualification*, *production*, *dev*. 
Le problème de cette pratique, c'est qu'elle ne tient pas vraiment la mise à l'échelle. 12 Factors Apps utilise donc des variables gérées indépendamment par déploiement.

# 4 - Les ressources distantes

Les ressources distantes sont les ressources qui peuvent être consommées à travers le réseau comme la base de données, les files de messages, un service SMTP ou un système de cache. 

Il est fréquent que la base de données et l'application soient administrées par les mêmes personnes. D'autres services sont en revanche confiés à des tiers comme Twitter, Newrelic ou amazon S3.

Une application 12 Factors ne fait pas la différence entre ces services locaux et distants. Chaque ressource peut être attachée ou détachée en fonction de l'environnement.

À l'image des ressources sqlite remplacé par du PostgreSQL en production, toutes les ressources d'une application sont branchés par de la configuration en fonction de l'environnement.

Il sera, par exemple, possible de remplacer un serveur de base de données cassé par un autre remonté depuis une sauvegarde sans toucher au code de l'application.

# 5 - Construire puis exécuter

Il est très important de séparer la phase de construction des phases d'exécutions. 

La transformation du code de l'application en un *déploiement* se fait en suivant 3 étapes : 

- La construction : en C ou en java cette étape consiste à compiler le code après avoir été chercher les dépendances. Pour les langages interprétés cette étape se résume à télécharger les dépendances et compiler les assets.
- Releaser : fusionner le code compilé avec la configuration spécifique à un environnement permet d'enregistrer des versions identifiables de l'application.
- Exécuter : cette étape consiste à lancer l'application dans une version et un environnement donné.

Les applications 12 Factors respectent scrupuleusement la séparation entre ces 3 étapes. 
Il est, par exemple, impossible de modifier du code exécuté en production sans repasser par les phases précédentes. 
Le temps de déroulement de ces 3 phases correspond au time to market il doit donc être le plus court possible.

Un retour en arrière se fera très facilement en reprenant une version précédente. Il est donc très important que chaque version ait un identifiant unique. 

Une construction va être déclenchée par le développeur alors qu'une exécution pourra être déclenchée en automatique, un reboot de serveur par exemple.

# 6 - Processus

Exécuter l'application avec 1 ou N processus indépendant.

Dans les cas simples, l'exécution se résume à lancer 1 processus 

    mon_script.rb

Dans les cas complexes, un système, c'est un ensemble de processus qui coopèrent.

Un processus d'une application 12 factors est indépendant, il ne partage rien avec les autres processus sans passer par une ressource distante. 
Jamais un processus ne doit supposer qu'il existe un fichier ou un élément en mémoire pour correctement fonctionner. 
Ainsi, le passage à l'échelle est très simple, il suffit de lancer plus de processus.

Un grand nombre d'applications web utilisent une session en mémoire pour sauver des données de l'utilisateur.
Pour garantir l'indépendance des processus il est préférable d'utiliser memcahed ou redis pour partager ces sessions entre les processus
