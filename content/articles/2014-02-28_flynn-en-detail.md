Title: Flynn.io en détail
Tags: flynn, tools
Author: Thomas, Olivier
Summary: Première plongé dans le code de fynn.io pour bien comprendre son fonctionnement. De retour de cette expérience très enrichissante.
Status: draft

*Flynn.io* se présente comme le Légo du PaaS. Basé sur le travail de [Russell Ackoff](http://knowledge.wharton.upenn.edu/article/idealized-design-how-bell-labs-imagined-and-created-the-telephone-system-of-the-future/) les briques sont toutes indépendantes et communiquent entre elles. On se retrouve avec un système modulaire et extensible composé de briques simples.


# Une histoire de container

Rêvons un peu, imaginons un système capable d'héberger des applications scalables à volonté. Chaque application est isolée dans un container et pour faire face à la charge, il suffit d'en multiplier le nombre. Pour le projet Flynn, on lance les containers dans la grille et cette grille est capable d'utiliser au mieux le matériel tout en garantissant la bonne marche des containers.

Dans ce cadre, il est important de séparer la configuration (l'adresse de mon service de persistance par exemple), l'application (le code compilé et toutes ses dépendances) et les données. 

Pour lancer un container, il suffit alors de fusionner l'application et sa configuration et de demander au système une place dans la grille.

![Architechture Flynn]({filename}/images/flynn-arch.png)
 
# Les briques de base de la grille


## Configuration distribuée

La configuration de chaque application doit donc être enregistrée dans une brique dédiée et distribuée sur l'ensemble de la grille.


### [etcd](https://coreos.com/using-coreos/etcd/)

etcd est un conteneur distribué de clé/valeur. Une sorte de Redis simplifié et très robuste garantissant la cohérence des données enregistrées. Il permet aussi de faire de l'élection de leader et de la gestion de verrou distribué. 

C'est le composant de [coreos](https://coreos.com/) pour gérer la configuration des containers.


### [discoverd](https://github.com/flynn/discoverd)

discoverd est un système de découverte de service. Il permet de pousser en temps réel les changements dans les services vers les clients.

- enregistrer un service
- trouver un service
- notification quand un service change
- identifier le leader d'un service


## Lancer les container docker 

La grille est composée de machines physiques. Chaque machine héberge un docker mais il faut aussi un agent capable de lancer localement de nouveaux containers et de remonter un certain nombre de métriques pour aider le contrôleur à prendre ses décisions. 

Cet agent c'est [flynn-host](https://github.com/flynn/flynn-host), il est lancé dans un container et communique avec le démon docker via l'api.

=> Question API REST HTTP ou socket unix monté dans le container ?


## Contrôleur

Vue de l'extérieur de la grille, les différentes tâches dévolues au contrôleur sont les suivantes :

- lancer de nouveaux containers
- surveiller que les containers sont encore en vie et le cas échéant les relancer

C'est théoriquement l'unique point d'entrer de la grille c'est le composant flynn-controller qui s'en charge. Dans la pratique nous verrons plus tard que ce n'est pas le cas.

Lancer un container va prendre du temps, pour gérer la reprise sur erreur et les pics d'activité le projet *Flynn.io* a choisi d'implémenter 3 files d'attentes : 

- les services : pour lancer des processus très longs comme apache ou nginx;
- les éphémères : pour lancer des traitements court comme un traitement "batch" ou une session shell interactive;
- les constructeurs : pour lancer les constructions d'application.


# Au niveau supérieur

Au-dessus de la grille nous trouvons les briques capables de router les services, de construire des applications et de les lancer.


## Routeur http

Un grand nombre des services sont exposés en http, faire de l'équilibrage de charge est indispensable, surtout si pour faire face à la charge on augmente le nombre d'instances du service. HAproxy est une solution presque parfaite elle est robuste et performante, mais il faut relancer un nouveau processus à chaque changement de configuration. 

Pour compenser ce problème, *Flynn.io* est en train d'écrire un nouveau service "strowger" qui se chargera justement de faire ce routage et de prendre encompte dynamiquement depuis discoverd toutes les évolutions de configuration.


## Construire

Construire une application c'est dans la majorité des cas rapatrier les dépendances et compiler le code source. Pour Heroku c'est dérouler le Buildpack. 

Pour que la démonstration soit parlante, *Flynn.io* a réalisé une première implémentation de flynn-builder capable de construire les applications en suivant un Buildpack.


## un serveur de fichiers http

Une fois les containers construits et prêts à être lancer il est nécessaire d'avoir un référentiel d'images. Le projet a fait le choix d'un référentiel accessible en REST : "shelf" au départ un simple dépôt de fichier et plus tard probablement un proxy vers swift, S3 ou hubic.

À la fin de la construction, flynn-builder se charge aussi de sauvegarder l'image du container dans shelf


## Exécuter

Toujours dans une optique de démonstration nous trouvons le processus flynn-runner capable de lire une image de container dans shelf, de la lancer avant d'enregistrer le service correspondant dans discoverd. 

Malheureusement ce processus lance les containers en se connectant directement sur discoverd et flynn-host... Probablement l'effet démo.


# Un système construit avec lui-même 

Il existe quelques briques qui ne sont pas automatiquement lancées et distribuées dans le système, le cluster etcd en fait partie. La liste des nœuds du cluster etcd est connue et partagée par tous. 
