Title: Flynn.io en détail
Date: 2014-02-28 23:00
Category: Articles
Tags: flynn, tools
Slug: 2014-02-28-flynn-en-détail
Author: Thomas, Olivier
Summary: Première plongé dans le code de fynn.io pour bien comprendre son fonctionnement. De retour de cette expérience très enrichissante.
Status: draft

Flynn.io se présente comme un ensemble de briques Légo du PaaS. Basé sur le
travail de 
[Russell Ackoff](http://knowledge.wharton.upenn.edu/article/idealized-design-how-bell-labs-imagined-and-created-the-telephone-system-of-the-future/)
les briques sont toutes indépendantes et communiquent entre elles. On se
retrouve avec un système modulaire et extensible composé de briques simple.

# Une histoire de container

Rêvons un peu, imaginons un système capable d'héberger des applications
scalable à volonté. Chaque application est isolé dans un container et pour
faire face à la charge il suffit d'en multiplier le nombre. Pour le projet
Flynn on lance les containers dans la grille et cette grillle est capable
d'utiliser au mieux le matériel tout en garantissant la bonne marche des
containers.

Dans ce cadre, il est important de séparer la configuration (l'addresse de mon
service de persistance par exemple), l'application (le code compilé et toutes
ses dépendaces) et les données. 

Pour lancer un container, il suffit alors de fusionner l'application et sa
configuration et de demander au système une place dans la grille.

# Les briques de base de la grille

## Configuration distribué

La configuration de chaque application doit donc être enregistré dans une
brique dédié et distribué sur l'ensemble de la grille.

### [etcd](https://coreos.com/using-coreos/etcd/)

etcd est un conteneur distribué de clé/valeur. Il permet aussi de faire de
l'éléction de leader. C'est le composant de coreos pour gérer la configuration
des container.

### [discoverd](https://github.com/flynn/discoverd)

discoverd est un système de découverte de service. Il permet de pousser en temps réel les changement dans les services vers les clients.

- enregistrer un service
- trouver un service
- notification quand un service change
- identifier le leader d'un service

## lancer les container docker 

La grille est composé de machines physiques. Chaque machine héberge un docker
mais il faut aussi un agent capable de lancer localement de nouveau containers
et de remmonter un certains nombre de métriques pour aider le controlleur a
prendre ses décisions.
Cet agent c'est [flynn-host](https://github.com/flynn/flynn-host), il est lancé
dans un container et communique avec le démon docker via l'api.

=> Question API REST HTTP ou socket unix monté dans le container ?

## controlleur

Les 3 sceduleurs et une remonté d'info pour le client
flynn controller

# Au niveau supérieur

Au dessus de la grille nous trouvons les briques capable de router les
services, de construire des applications et de les lancer.

## routeur http
Un grand nombre des services sont exposés en http, faire de l'équilibrage de
charge est indispensable, surtout si pour faire face à la charge on augmente le
nombre d'instances du service. HAproxy est très bien mais il faut relancer un
nouveau process à chaque changement de configuration. 
Pour compenser ce problème, flynn.io est en train d'écrire un nouveau service
"strowger" qui se chargera justement de faire ce routage et de prendre en
compte dynamiquement depuis discoverd toutes les évolutions de configuration.

## builder
construire les containers et les enregistrer dans shelf

## un serveur de fichiers http
shelf

## Runner
lire un container depuis shelf puis lancer ce container et l'enregistrer sur discoverd

# Un système construit avec lui même 

Il existe quelques briques qui ne sont pas automatiquement lancé et distribué dans le
système, le cluster etcd en fait parti. La liste des noeuds du cluster etcd est
connue et partagé par tous. 

