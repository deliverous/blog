---
title: Vous avez dit contextes ?
tags:
  - docker
  - volume
  - deliverous
  - uploads
authors:
  - Thomas Clavier
description: Quelles sont les bonnes pratiques avec les volumes ? Suite de la série sur les volumes avec la création de contextes.
date: 2015-03-28
publishdate: 2015-03-28
aliases: /2015-03-28.volumes-contexte.html
---

Dans cet article, le second de la série sur les volumes, je vais aborder un nouvel usage des volumes, la création de contextes séparés.
En effet, avoir un nom de répertoire différent entre l'intérieur et l'extérieur du conteneur peut apporter un certain nombre d'avantages.

# Séparation de logs

Prenons l'exemple d'un conteneur avec une application qui log tout dans
/var/log/app/ avec les options de montage des volumes il est possible
de lancer 3 fois cette même application et de sauver les fichiers générés dans
3 répertoires différents :

    :::shell
    docker run -v /data/logs/app1:/var/log/app --name app1 conteneur
    docker run -v /data/logs/app2:/var/log/app --name app2 conteneur
    docker run -v /data/logs/app3:/var/log/app --name app3 conteneur

C'est par exemple utilisé pour sauvegarder les logs d'une application que l'on doit démultiplier pour faire face à la charge.

Pour une bonne analyse, il faudra, à intervalle régulier, collecter l'ensemble
des fichiers. La centralisation de ces logs en continu dans un moteur dédié
serait probablement plus efficace, mais un peu plus complexe à mettre en
œuvre.

Certains vont faire remarquer qu'il est possible de lancer l'application de cette façon :

    :::shell
    docker run -v /data/logs:/var/log/app --name app1 conteneur
    docker run -v /data/logs:/var/log/app --name app2 conteneur
    docker run -v /data/logs:/var/log/app --name app3 conteneur


Mais attention, il est peut probable que notre application lancée 3 fois arrive
à gérer correctement l'accès concurrent aux mêmes fichiers de logs.  Des
applications comme Tomcat ou WebLogic ouvrent les fichiers au démarrage et
écrivent dedans en continue en supposant être les seules au monde.
De plus, en centralisant de cette façon on retombe sur le problème de système
de fichiers partagé, abordé dans l'article précédent.

# Contextes clients

Monter un répertoire différent pour plusieurs conteneurs identique peut aussi
être utilisé pour différencier différentes instances d'un même conteneur.
Prenons l'exemple d'une application qui lit et écrit l'ensemble de ses données
applicatives dans `/home/application`. Il est possible de dédier chaque
instance à un usage donné.

    :::shell
    docker run -v /data/client1:/home/application --name app1 conteneur
    docker run -v /data/client2:/home/application --name app2 conteneur

Avec cette configuration, chaque conteneur va pouvoir vivre sa vie avec ses
propres données. Plus besoins de loadbalancer devant pour agréger le trafic
vers les 2 conteneurs, mais 2 URLs différents pour accéder à 2 contextes
clients différents. On peut imaginer que pour utiliser "app1" il faut visiter
`http://client1.app.com` et pour se retrouver sur app2
`http://client2.app.com`. C'est un bon moyen de cloisonner les clients sans
trop d'efforts, mais attention, si le nombre de clients est trop grand, la
gestion des multiples conteneurs risque fort d'être périlleuse.

# Conclusion

Dans le cas d'une multiplication de conteneur pour faire face à une
augmentation de charge, il est possible de rapidement démultiplier les
répertoires de logs, mais l'usage d'un serveur de centralisation à base de
Logstash sera probablement bien plus générateur de valeur.

Dans le cadre d'une séparation de clients, il est important de regarder le
nombre de contextes à réaliser avant de choisir une solution à base de volumes.

---
Photo par [Ricky Artigas](https://www.flickr.com/photos/ricky_artigas/5656337970)
