Title: Flynn.io en détail
Date: 2014-02-28 23:00
Category: Articles
Tags: flynn, tools
Slug: 2014-02-28-flynn-en-détail
Author: Thomas, Olivier
Summary: Première plongé dans le code de fynn.io pour bien comprendre son fonctionnement. De retour de cette expérience très enrichissante.
Status: draft

# Configuration distribué


## [etcd](https://coreos.com/using-coreos/etcd/)

etcd est un conteneur distribué de clé/valeur. Il permet aussi de faire de l'éléction de leader. C'est le composant de coreos pour la configuration des container.

Question: 
D'un côté, ils conseillent une prendre une cluster etcd <= 9 noeuds. De l'autre côté ils disent qu'il faut un etcd client par machine physique. Quel est le déploiement ?


## [discoverd](https://github.com/flynn/discoverd)

discoverd est un système de découverte de service. Il permet de pousser en temps réel les changement dans les services vers les clients.

- enregistrer un service
- trouver un service
- notification quand un service change
- identifier le leader d'un service



# lancer les container docker 
flynn-host

# controller
flynn controller

# un serveur de fichiers http
shelf

# routeur http
Un grand nombre des services sont exposés en http, faire de l'équilibrage de
charge est indispensable. HAproxy c'est bien mais il faut relancer un nouveau
process à chaque changement de configuration. 
Pour compenser ce problème, flynn.io est en train d'écrire un nouveau service
"strowger" qui se chargera justement de faire ce routage et de prendre en
compte dynamiquement depuis discoverd toutes les évolutions de configuration.

# builder
construire les containers et les enregistrer dans shelf

# Runner
lire un container depuis shelf puis lancer ce container et l'enregistrer sur discoverd
