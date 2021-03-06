---
title: Comment installer et exploiter Docker sur Red Hat ou CentOS
tags:
  - docker
  - centos
  - redhat
authors:
  - Thomas Clavier
description: Confronté au problème de l'installation d'une plate-forme Docker sous Red Hat pour un client, voici les détails d'une installation réussie.
date: 2014-07-10
publishdate: 2014-07-10
aliases: /2014-07-10.docker-tomcat-centos.html
---

Alors que [Docker](http://www.docker.com/) est développé sous [ubuntu](http://www.ubuntu.com/) et principalement empaqueté pour debian et ubuntu, il est courant de trouver en entreprise des parcs entier de serveurs sous [Red Hat](http://www.redhat.com/) ou [CentOS](https://www.centos.org/).
Comment faire dans ces conditions pour y déployer Docker ?

À travers cet article, je vais vous montrer les recettes que j'ai mises en place pour déployer de nombreux serveurs Red Hat 6.5, d'autres en CentOS 6.5 et des containers CentOS.

# Docker et Red Hat

Commençons par un peu de techniques, par défaut Docker utilise Aufs pour gérer les layers des images.
Seulement Aufs n'est pas compatible SELinux, or Red Hat garantie la compatibilité totale de la distribution avec SELinux.
Si l'on s'arrête là, l'utilisation de Docker sur CentOS ou Red Hat est totalement impossible.
Mais depuis septembre 2013, Red Hat et Docker travaillent ensemble pour produire une version compatible.
Le résultat est là, depuis la version 0.7 de Docker il est possible d'utiliser device-mapper comme backend pour gérer les layers des images.

Docker utilise lxc et les cgroupes pour isoler les containers entre eux, or c'est une portion du noyau Linux qui bouge beaucoup. Un certain nombre de corrections lié aux cgroups ont été intégrés dans le noyau de la Red Hat 6.5. Il est donc vivement recommandé d'utiliser la dernière Red Hat ... J'écris ça alors que la 7 est disponible depuis presque 1 mois, seulement dans de nombreuses entreprises changer le socle Linux est un gros projet, donc la dernière Red Hat disponible se limitera à la 6.5 :-D

# Red Hat ou CentOS ?

Ça commence par une histoire de licence, d'argent, de niveau d'expertise ... Et ça finit par un choix.
En bref, l'histoire du jour s'inspire d'un master en Red Hat 6.2, à migrer en CentOS pour appliquer les mises à jour et de temps en temps à remettre en Red Hat avant l'enregistrement sur le [rhn](http://rhn.redhat.com).

## Migration en CentOS

Les différences entre CentOS et Red Hat sont faibles, il est facile de passer de l'une à l'autre, voilà comment passer une RedHat en CentOS :

    mkdir /tmp/centos
    cd /tmp/centos
    wget http://mirror.centos.org/centos/6.5/os/x86_64/RPM-GPG-KEY-CentOS-6
    wget http://mirror.centos.org/centos/6.5/os/x86_64/Packages/centos-release-6-5.el6.centos.11.1.x86_64.rpm
    rpm --import RPM-GPG-KEY-CentOS-6
    sed -e 's/$releasever/6.5/g' -i /etc/yum.repo.d/CentOS-Base.repo
    rpm -Uvh --force *.rpm
    rpm -e redhat-release-server-6Server-6.4.0.4.el6.x86_64
    yum -y upgrade


# Docker
## Installation de Docker

Pour installer Docker, il faut brancher la machine sur le répo EPEL :

    cd /tmp/centos
    wget http://epel.mirrors.ovh.net/epel/6/i386/epel-release-6-8.noarch.rpm
    rpm -Uvh epel-release-6-8.noarch.rpm
    yum -y upgrade

Puis installer Docker:

    yum install docker-io

Enfin, ne pas oublier de relancer le serveur pour prendre en compte le nouveau noyau.

## Une registry privée

Déployer une registry privé, c'est possible. Même si Docker fait beaucoup pour que l'on utilise [le hub Docker](https://hub.docker.com/) ils fournissent aussi un container de [registry](https://github.com/dotcloud/docker-registry).
L'objectif est de garder l'ensemble des containers dans la société, bien à l'abri des regards indiscrets.
Pour avoir de la haute disponibilité, dans le cas présent nous avons choisi d'installer la registry sur un serveur virtuel dédié. En utilisant la flexibilité de la virtualisation il est possible de garantir un bon niveau de service sans avoir à multiplier les instances de registry.

    mkdir -p /srv/registry

éditer /srv/registry/config.yaml

    common:
        loglevel: info

    prod:
        loglevel: info
        standalone: true
        storage: local
        storage_path: /srv/registry/data
        secret_key: 58555486803be0218c63cd626d5e0117
        search_backend: sqlalchemy
        sqlalchemy_index_database: sqlite:////srv/registry/docker-registry.db

Création d'un script de lancement

    wget https://raw.githubusercontent.com/tclavier/scripts/master/centos/docker_container_init_script  -O /etc/init.d/registry

éditer /etc/init.d/registry

    NAME=registry
    VERSION=latest
    CONTAINER=$NAME:$VERSION
    CONTAINER_OPTS="-p 80:5000 -v /srv/registry:/srv/registry -e DOCKER_REGISTRY_CONFIG=/srv/registry/config.yaml -e SETTINGS_FLAVOR=prod"

La registry est lancé par un script d'init standard :

    /etc/init.d/registry (start|stop|restart)

# Conclusion

Arrivé là, vous avez un serveur Docker avec une registry, de quoi rapidement monter un environnement pour démontrer par l'exemple de la viabilité de Docker.
L'étape suivante, qui sera le sujet d'un autre article, consiste à trouver la façon de travailler avec Docker qui apportera le plus à l'entreprise.

---
Le logo est la propriété du [projet CentOS](http://centos.org)
