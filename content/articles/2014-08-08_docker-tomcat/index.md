---
title: Comment faire un container <em>Tomcat</em>
tags:
  - docker
  - centos
  - tomcat
authors:
  - Thomas Clavier
  - Olivier Albiez
description: Confronté à un problème de construction de container *Tomcat*, voici quelques pistes pour bien commencer.
lastmod: 2014-11-13
date: 2014-08-08
publishdate: 2014-08-08
aliases: /2014-08-08.docker-tomcat.html
---

Non, je ne vais pas vous parler des F14 Tomcat de Top Gun, mais bien de container [*Docker*](http://docker.io) et d'*Apache Tomcat*.
Alors construisons ensemble quelques containers.

# Une base de CentOS

En partant d'une distribution de base, il est facile d'installer *Tomcat*. Avec une *Debian* stable il est même possible de choisir entre *Tomcat 6* et *Tomcat 7*. Avec une *CentOS 6*, c'est encore plus simple, il n'y a pas de choix possible :

    yum install tomcat6

Avec une *CentOS 7* c'est tout aussi simple, le rpm s'appelle tomcat et c'est un *Tomcat 7*.

# Des RPMs

Dans beaucoup d'entreprise, les logiciels s'installent uniquement depuis les rpms officiels, une façon simple de suivre les mises à jour de sécurités et de réduire les coûts de maintenances.
Dans ces conditions, si l'on souhaite un *Tomcat 6* avec un java 7, il faut partir d'une *CentOS 6*. Le Dockerfile va donc commencer par :

```
FROM centos:centos6
RUN yum -y upgrade && yum clean all
RUN yum -y install java-1.7.0-openjdk && yum clean all
RUN yum -y install tomcat6 && yum clean all
```

Jusque-là, rien de très compliquer. Il reste à :

* Ajouter une application,
* exposer le bon port,
* et lancer Tomcat

Ce dernier point présente une petite difficulté, en effet, le script de boot de *Tomcat* lance le serveur d'application en mode démon. Seulement *Docker* s'attend a lancer un processus qui ne se détache pas.
Pour éviter d'avoir à refaire et surtout d'avoir à maintenir un nouveau script startup.sh il est possible de lancer juste après *Tomcat* un second processus qui gardera la main. Par exemple un tail de l'ensemble des fichiers logs.
Le tail apporte en plus la possibilité de consulter les logs du *Tomcat* avec un simple `docker logs`, ce qui est fort pratique.

Pour l'application d'exemple, je propose de profiter de sample.war distribué par *Apache Tomcat 6*. Vous remarquerez au passage qu'il est possible de spécifier une URL pour laisser *Docker* télécharger des composants à la construction du container.

La suite de notre Dockerfile est donc la suivante :

```
ADD http://tomcat.apache.org/tomcat-6.0-doc/appdev/sample/sample.war /var/lib/tomcat6/webapps/
EXPOSE 8080
CMD service tomcat6 start && tail -f /var/log/tomcat6/catalina.out
```

Pour construire notre container lançons :

    docker build -t tomcat6-centos6 .

Puis exécutons le, sans oublier d'exposer le port 8080 :

    docker run -p 8080:8080 tomcat6-centos6

Et enfin, visitez [http://localhost:8080/sample/](http://localhost:8080/sample/) pour admirer votre travail.

Pour stopper le container, il faudra jouer avec `docker ps` et `docker stop`

# L'archive officiel

Pour partir de l'archive officielle distribuée par Apache, le choix de la distribution de base n'a pas d'importance. Je propose donc de partir de la dernière CentOS.
En ajoutant la même application d'exemple, nous obtenons un magnifique container capable de lancer un *Tomcat 7* directement téléchargé chez *Apache*.

Pour le script de boot, nous utilisons la même astuce que précédemment.

```
FROM centos
MAINTAINER Thomas Clavier <tclavier@azae.net>
RUN yum upgrade -y && yum clean all
RUN yum -y install java-1.7.0-openjdk && yum clean all
RUN yum -y install tar && yum clean all

ADD http://mir1.ovh.net/ftp.apache.org/dist/tomcat/tomcat-7/v7.0.57/bin/apache-tomcat-7.0.57.tar.gz /tmp/
RUN mkdir /opt/tomcat
RUN tar -xzvf /tmp/apache-tomcat-7.0.57.tar.gz --directory /opt/tomcat/ --strip 1 && rm /tmp/apache-tomcat-7.0.57.tar.gz

ADD http://tomcat.apache.org/tomcat-6.0-doc/appdev/sample/sample.war /opt/tomcat/webapps/

EXPOSE 8080

CMD /opt/tomcat/bin/catalina.sh start && tail -f /opt/tomcat/logs/catalina.out
```

La grosse différence avec le container précédent, c'est que là le *Tomcat* est installé dans `/opt/tomcat`, ça ne respecte pas vraiment le *Linux Standard Base*, mais ça fonctionne.

# Normalisation

Votre container *Tomcat* va probablement tourner dans un environnement de production normalisé. J'imagine aisément que votre DSI aimerait avoir les mêmes interfaces avec tous les containers.
Les seules interfaces d'entrées-sorties du container sont les suivantes :

* le port de communication et son protocole
* un volume pour partager des fichiers
* stdout pour les logs

Je propose de déposer les logs complémentaire dans `/var/log/tomcat` et d'exposer le port 8080 de *Tomcat* en http.

Pour le port et les logs sur stdout, c'est facile, c'est déjà fait, pour `/var/log/tomcat` il va falloir travailler un peu.

## RPM

Avec le *Tomcat 6* de *CentOS* les logs sont par défaut dans `/var/log/tomcat6`. Changeons ça :

```
RUN rm -rf /var/log/tomcat6/ ;\
    rm -rf /usr/share/tomcat6/logs ;\
    mkdir /var/log/tomcat/ ;\
    ln -s /var/log/tomcat/ /usr/share/tomcat6/logs ;\
    chown tomcat:tomcat /var/log/tomcat
```

Sans oublier de changer le tail pour pointer sur le bon répertoire.

    CMD service tomcat6 start && tail -f /var/log/tomcat/catalina.out

Et à déclarer le volume

    VOLUME ["/var/log/tomcat"]

Une fois le container reconstruit et relancé, on observe que tout fonctionne à merveille. En revanche si l'on teste en montant le volume, on observe la chose suivante :

```
$ docker run -p 8080:8080 -i -t -v /tmp/logs/:/var/log/tomcat tomcat-sample /bin/bash
bash-4.1# ls -la /var/log/tomcat/
total 8
drwxr-xr-x 2 1000 1000 4096 Aug  8 07:13 .
drwxr-xr-x 5 root root 4096 Aug  8 07:09 ..
```

Le répertoire `/tmp/logs` a été créé avec mon utilisateur local d'id 1000. Une fois le volume monté, les droits sont préservés. Pour être certains que tout fonctionnera tout le temps, il est nécessaire de changer les droits depuis le container à chaque lancement.

```
CMD chown tomcat:tomcat /var/log/tomcat; service tomcat6 start && tail -f /var/log/tomcat/catalina.out
```

## Archive

La problématique est identique, seule différence, le *Tomcat* se lance en root et il est installé dans `/opt/tomcat`. Ce qui nous donne :

```
RUN rm -rf /opt/tomcat/logs ;\
    mkdir /var/log/tomcat/ ;\
    ln -s /var/log/tomcat/ /opt/tomcat/logs
VOLUME ["/var/log/tomcat"]
CMD chown root:root /var/log/tomcat; /opt/tomcat/bin/catalina.sh run

```

Attention, la mise à jour de systemd peut produire l'erreur suivante :

    error: unpacking of archive failed on file /usr/sbin/suexec: cpio: cap_set_file

En effet, *CentOS* utilise par défaut les attributs étendus du file-system, or aufs ne les supporte pas tous. Il faut donc changer de backend de stockage, soit vers brtfs, soit vers devicemapper.


# Et après ?

À travers cet article, nous avons appris à construire des containers *Tomcat* sur une base de *CentOS*, le tout, près à être déployé dans un environnement normalisé. La prochaine étape serait de déployer ces containers. Sur Deliverous, le volume de log ne serait pas exploité, en effet seul les logs présent sur stdout et stderr sont collectés. À défaut de configurer *Tomcat* pour ne pas utiliser de fichier, un `tail -f /var/log/tomcat/*` fonctionnerait très bien.

Il est possible de retrouver l'ensemble des fichiers sources sur le projet [GitHub docker-sample](https://github.com/Deliverous/docker-sample).
Pour les plus motivés je vous invite à rejoindre le prochain [meetup *Docker*](http://www.meetup.com/find/events/?keywords=Docker).

---
Photo par [storem](https://www.flickr.com/photos/storem/3198300643/)
