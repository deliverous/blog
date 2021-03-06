---
title: <em>CoreOS</em>
tags:
  - coreos
  - tools
authors:
  - Thomas Clavier
  - Olivier Albiez
description: Après avoir étudié Flynn.io, nous nous sommes intéressé à *CoreOS*. Voici quelques mots sur nos découverte de cet outils de plus en plus populaire.
date: 2014-03-08
publishdate: 2014-03-08
aliases: /2014-03-08.coreos.html
---

[*CoreOS*](https://coreos.com) est un projet qui vise à abstraire des nœuds pour créer un cluster. Ce projet se base sur un *Linux* minimal, de la découverte de service (*etcd*), *docker* et *systemd*.

# Les composants

L'idée principale de *CoreOS* est de lancer des applications dans des containers *docker* sur un cluster de machines. Pour cela, ils s'appuient sur 3 outils : *docker*, *systemd*, *etcd*.

Par rapport à *Flynn.io*, *CoreOS* se focalise sur les couches basses, que *Flynn* appelle "layer 0" ou grille. *CoreOS* utilise des outils plus simples que *Flynn* pour arriver à ce résultat. Il reste cependant à vérifier le passage à l'échelle de ces deux solutions.


## [*docker*](http://docker.io)

Il n'est plus utile de présenter la technologie qui permet de gérer des containers.


## [*systemd*](http://freedesktop.org/wiki/Software/systemd/)

*systemd* est un manager de services pour Linux. Il a pour vocation de remplacer les SysV et les LSB init scripts. Un service est appelé _unit_ et est décrit par un simple fichier. Voici par exemple une description pour lancer un container redis, appelé redis.service :


    :::ini
    [Unit]
    Description=Redis Service
    After=docker.service
    Requires=docker.service

    [Service]
    ExecStart=/usr/bin/docker --name redis run dockerfile/redis

    [Install]
    WantedBy=local.target


Il est possible d'utiliser des variables dans le fichier de description d'une _unit_ :

    :::ini
    [Unit]
    Description=Redis Service
    After=docker.service
    Requires=docker.service

    [Service]
    ExecStart=/usr/bin/docker --name "redis-%p" run dockerfile/redis

    [Install]
    WantedBy=local.target

Dans cet exemple, le nom du container dépendra du nom du ficher service. Il est donc possible de faire un lien symbolique appelé polop@redis.service pointant sur redis.service. Au démarrage le %p prendra la valeur polop. La liste des variables utilisables est consultable dans la [section specifier du manuel de *systemd*](http://www.freedesktop.org/software/systemd/man/systemd.unit.html#Specifiers).


## [*etcd*](https://coreos.com/using-coreos/etcd/)

*etcd* est un conteneur distribué de clé/valeur, une sorte de *Redis* simplifié et très robuste garantissant la cohérence des données enregistrées. Il permet aussi de faire de l'élection de leader et de la gestion de verrou distribuée.

*CoreOS* utilise *etcd* pour faire de la découverte de service et de la configuration partagée.

Pour l'instant *CoreOS* lance un agent *etcd* sur chaque nœud, la prochaine évolution consiste à remplacer une partie de ces agents par des proxy.

Une application peut donc, une fois lancée, s'enregistrer sur le service *etcd*.
Les applications consommatrices pourront ainsi être correctement configurées.

# [*Fleet*](https://github.com/coreos/fleet)

*Fleet* est l'outil de *CoreOS* qui permet de lancer les containers en oubliant qu'il y a plusieurs nœuds. L'outil se présente en ligne de commande en lançant *fleetctl*. Par exemple, pour lancer notre service redis, il faudrait lancer la commande suivante :


    :::bash
    $ fleetctl start polop@redis.service

*Fleet* se charge de trouver un nœud disponible et démarre le service sur ce nœud. *Fleet* connaît donc l'ensemble des services tournant sur le cluster et monitore ceux-ci. Si un nœud du cluster tombe, *Fleet* relancera automatiquement les services ailleurs.


---
Photo par [Jamie Ball](https://www.flickr.com/photos/jamieball83/6021235777/)
