---
title: Des volumes et des utilisateurs
tags:
  - docker
  - volume
  - deliverous
authors:
  - Thomas Clavier
description: Quelles sont les bonnes pratiques avec les volumes ? Suite et fin de la série sur les volumes.
draft: true
date: 2015-04-02
publishdate: 2015-04-02
aliases: /2015-04-02.volumes-users.html
---

Dans cet article, le dernier de la série sur les volumes, je vais aborder le problème de la gestion des utilisateurs.

# Le problème

Il n'est pas rare d'avoir un conteneur qui lance une application avec un
utilisateur particulier. Il va donc écrire ses fichiers dans le volume avec
l'utilisateur en question :

    :::dockerfile
    user tomcat
    cmd /opt/tomcat/bin/catalina.sh start

Mais comment garantir que l'utilisateur `tomcat` dans le conteneur va bien avoir
le droit d'écrire dans un volume géré par l'hyperviseur ?  
Comment faire correspondre un utilisateur du conteneur avec un utilisateur du host ? 

Le principe d'idempotence des conteneurs apporte de nombreux avantages. Quel bonheur de pouvoir lancer autant d'instances d'un conteneur sur n'importe quel serveur pour pouvoir faire face à une augmentation de charge. 
Et que dire de la simplicité de pouvoir lancer le même conteneur aussi bien sur le poste du développeur que sur un serveur de production sans avoir à présupposer de l'existence d'éléments de configuration externe.

Si l'on souhaite respecter ce principe il faut soit configurer le conteneur pour le rendre totalement autonome, soit systématiquement le déployé avec ses dépendances. Il existe donc 2 solutions.

# Un conteneur autonome

Regardons en détail comment rendre autonome notre conteneur.

Impossible de supposer que les droits sur le volume sont correctement
configurés, or, le volume n'est visible par le conteneur qu'au démarrage. Le conteneur doit donc le configurer quand il se lance. La solution la plus simple, c'est de lancer un script de
boot en `root`, qui va corriger les droits sur le volume, puis de lancer l'application avec le bon utilisateur.

Exemple : 

    :::dockerfile
    cmd chown -R tomcat:tomcat /opt/tomcat/logs && \
        su tomcat -c "/opt/tomcat/bin/catalina.sh start"
    
Le défaut de ce système c'est l'incapacité d'anticiper l'identifiant de
l'utilisateur dans le conteneur. Si un processus dans un autre conteneur doit collecter les fichiers avec le bon utilisateur la gymnastique des pré-requis risque fort de nous bloquer. On se retrouve à nouveau devant un choix : le conteneur de collecte est-il un composant de mon application ou un élément extérieur devant interagir avec d'autres applications ? Si c'est un système applicatif, alors le déploiement de tous les conteneurs doit se faire de façon cohérente.

Le second défaut de ce système, c'est le temps de démarrage du conteneur. Vérifier les droits sur un gros disque peut prendre de longues minutes.

# Un système autonome

Quand le conteneur seul n'est pas idempotent, il est probablement possible de construire un ensemble de conteneurs formant un système idempotent. Par exemple un conteneur applicatif, un conteneur de données et un conteneur de collecte. 
Pour orchestrer ses conteneurs, `docker-compose` est la solution la plus simple pour le poste de développement, pour la production, le fichier `Deliverous` nous parait être la meilleur des solutions.

La création des différents conteneurs sera la partie la plus délicate, en effet dans un soucis d'optimisation des identifiants des utilisateurs système, la majorité des distributions linux ajoutent les utilisateurs système au fur et à mesure des besoins. Il est donc possible d'avoir 2 conteneurs avec deux utilisateurs tomcat ayant des ids différents. Une solution consiste à créer un conteneur commun qui portera la responsabilité de créer les utilisateurs, soit en installant le bon package, soit en utilisant la bonne commande.
Ce socle commun sera la base des autres conteneurs (voir la commande `from` dans le fichier `Dockerfile`).

Dans le cas de migration en douceur de système complexe existant vers Docker, obtenir un système autonome en cours de transformation est probablement l'une des principales difficultés. Et aucune recette miracle ne permet de résoudre le problème de façon simple et systématique. Le passage par un conteneur autonome avec des pré-requis sera sans doute un passage obligatoire pour éviter une migration violente et risqué.


# Conclusion

Le plus important, c'est de ne pas perdre de vue qu'un conteneur applicatif doit pouvoir se lancer n'importe ou. Rendre un conteneur ou un ensemble de conteneurs autonomes demandera probablement du travail à la fois aux experts systèmes et au experts applicatif, avec en contre partie de cette collaboration un système capable de rendre un grand service à toutes les personnes impliqués dans la chaine de production de valeur de l'entreprise.

---
Photo par [tetue](https://www.flickr.com/photos/romytetue/109188206)
