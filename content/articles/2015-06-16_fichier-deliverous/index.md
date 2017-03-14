---
title: Le fichier Deliverous
tags:
  - docker
  - deliverous
authors:
  - Thomas Clavier
  - Olivier Albiez
description: Documentation du fichier Deliverous
date: 2015-06-16
publishdate: 2015-06-16
aliases: /2015-06-16.fichier-deliverous.html
---

Le fichier Deliverous est le fichier de configuration utilisé par notre service, il est au format yaml et décrit l'ensemble des conteneurs ainsi que leurs relations.

Pour définir un conteneur, il suffit de le nommer en début de ligne, par exemple pour un conteneur que l'on appelle "front" :

    :::yaml
    front:
      clé1: valeur1
      clé2: valeur2

Certaines clés demandent simplement une valeur, d'autres, une liste de valeurs, voir même une liste de sous-clés et de valeurs. Par exemple :

    :::yaml
    front:
      clé1: valeur1
      clé2:
      - sous_clé1 : valeur2
      - sous_clé2 : valeur3


Voici en détail et par ordre alphabétique la liste de toutes les directives qu'il est possible de spécifier.

# command

Définit la commande à exécuter. Cette valeur est ajoutée à la fin de la commande 'docker run'

Exemple:

    :::yaml
    front:
      image: deliverous/container
      command: --start --front 1.2.3.4

Dans cet exemple, le conteneur sera démarré avec `docker run deliverous/container --start --front 1.2.3.4`

# deploy_conflict

Définit une restriction de déploiement, permet de s'assurer que 2 conteneurs seront déployés sur des machines physiques différentes.

Exemple:

    :::yaml
    front1:
      image: deliverous/blog
      deploy_conflict:
      - front2
    front2:
      image: deliverous/blog


# deploy_with

Définit une affinité de déploiement, permet de s'assurer que 2 conteneurs seront déployés sur la même machine physique.

Exemple:

    :::yaml
    front:
      image: deliverous/container
      deploy_with:
      - mysql
    mysql
      image: mysql

# dns

Définit un serveur DNS spécifique pour le conteneur. Correspond à l'option `--dns` de `docker run`

Exemple:

    :::yaml
    front:
      image: deliverous/blog
      dns:
      - 127.0.0.1

Dans cet exemple, le conteneur sera démarré avec `docker run --dns=127.0.0.1 deliverous/blog`. Cette option en plus de l'installation d'un serveur dnsmasq à l'intérieur du conteneur permet entre autres de résoudre les problèmes de modification du fichier `/etc/hosts` par le conteneur lui-même.

# entrypoint

Définition du point d'entré. Cette valeur sera donnée à l'option `--entrypoint` de `docker run`

Exemple:

    front:
      image: deliverous/container
      entrypoint: /usr/local/bin/debug

Dans cet exemple, le conteneur sera démarré avec `docker run --entrypoint /usr/local/bin/debug deliverous/container`.

# environment

Permet de définir des variables d'environnement par une liste de clés valeur.

Exemple:

    front:
      image: deliverous/blog
      environment:
        DB_NAME: blogdb
        DB_USER: blog
        ENVIRONEMENT: prod


# hostname

Définit le nom réseau du conteneur, correspond à l'option `--hostname` de la ligne de commande

Exemple:

    front:
      image: deliverous/container
      hostname: toto

Dans cet exemple, le conteneur sera démarré avec `docker run --hostname=toto deliverous/container`.

# image <i class="fa fa-star"></i>

Définition du nom de l'image Docker à utiliser. C'est la seule clé obligatoire. Le nom doit correspondre à un tag complètement qualifié, par exemple "deliverous/blog" pour une image hébergé sur le hub Docker ou "registry.company.com/user/image" pour une image hébergé sur votre propre registry.

    :::yaml
    front:
      image: deliverous/blog


# limits

Définition des limites du conteneur.
Pour l'instant, il n'est possible de limiter que la mémoire. C'est la directive `memory: <limit><unité>` avec `unité` qui peut prendre une des valeurs `b`, `k`, `m` ou `g`.

Sans définition, les limites sont les suivantes:

* memory: 4G

Exemple:

    front:
      image: deliverous/blog
      limits:
        memory: 1G


# links

Définition des liens entre les conteneurs avec une liste de lien. Chaque lien doit avoir une valeur `name` qui référence un autre conteneur et une valuer `alias` qui lui donnera son nom dans ce conteneur.

Exemple:

    :::yaml
    front:
      image: deliverous/container
      links:
      - name: mysql
        alias: db
    mysql:
      image: mysql

Dans cet exemple, le conteneur 'front' demande à être lié au conteneur mysql qu'il nommera 'db'.


# `monitor`


# ports

Définitions de la configuration réseau. Permet d'appliquer des règles de routage sur les conteneurs. Par exemple :

    :::yaml
    front:
      image: deliverous/blog
      ports:
      - ip: blog.deliverous.com
        container_port: 8080
        host_port: 80

Dans cet exemple, alors que le conteneur expose le port 8080, le conteneur `front` sera accessible sur le port 80 de l'adresse IP `blog.deliverous.com` (c'est le nom qui lui a été donné dans le manager). Il est possible de définir l'ip soit par son nom, soit par l'ip elle-même.


# snat

Permet de spécifier l'adresse source qui sera utilisé pour toutes les connections sortante du conteneur. Comme pour l'option 'ports' il est possible de définir l'ip soit par son nom, soit par l'ip elle-même.

Exemple:

    front:
      image: deliverous/smtp
      snat: 1.2.3.4


# volumes

Permet de définir des volumes pour persister les données à l'extérieur du conteneur. Je vous invite à lire l'article détaillé sur [les volumes](/2015-01-26.volumes.html) pour en savoir plus sur ce que nous avons mis en place. Si vous souhaitez en apprendre plus sur ce que les volumes peuvent apporter, alors je vous conseille la lecture de cette série d'articles : [Les uploads](/2015-03-12.volumes-uploads.html)

Exemple:

    demo:
      image: deliverous/blog
      volumes:
      - name: photos
        path: /srv/photos


---
