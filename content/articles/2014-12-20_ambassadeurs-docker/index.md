---
title: Ambassadeurs Docker
tags:
  - docker
  - ectd
authors:
  - Thomas Clavier
description: Faire parler des conteneurs Docker entre eux avec des links c'est magique, mais comment faire pour avoir des links entre des conteneurs qui s'exécutent sur plusieurs machines.
date: 2014-12-20
aliases: /2014-12-20.ambassadeurs-docker.html
---

Imaginons un conteneur A qui consomme le service du conteneur B, par exemple une application web qui consomme une base de données. Je vous propose de parcourir ensemble les solutions possibles pour que A et B communiquent.

# Retour aux sources

L'une des promesses de Docker, c'est construire une fois et lancer ou on veux. Pour atteindre cet objectif il n'est pas envisageable de configurer en dure dans le conteneur A la façon de contacter le conteneur B. Nous n'avons donc que quelques solutions pour injecter l'information dans le conteneur durant l'exécution :

- Par des variables d'environnement.
- Par des liens Dockers, ce qui revient à injecter automatiquement des variables d'environnement.
- Par fichier de configuration partagé dans des volumes.

# Les links

La solution la plus simple, préconisée par Docker, c'est d'établir un lien entre A et B :

    docker run --name B imageB
    docker run --name A --link B:B imageA

Avec cette solution Docker injecte dans le conteneur A un certain nombre de variables d'environnement préfixées par B. Gros avantage, il suffit de savoir lire des variables d'environnement pour savoir se connecter au service B. Ce qui peut être fait au démarrage du conteneur pour écrire un fichier de configuration.

Cette solution simple et rapide présente 2 défauts majeurs :

- si l'on relance le conteneur B, il faut aussi relancer A
- il faut que A et B soient sur la même machine.

Il est possible de ne pas injecter automatiquement les variables par des liens et de les ajouter sur la ligne de commande. Ce qui complexifie le lancement, mais permet de s'affranchir de la dernière contrainte.

# Fichier partagé

Certains produits ne savent pas travailler avec des variables d'environnement et préfèrent un fichier de configuration. Dans ce cas, il est possible de spécifier dans un fichier l'information pour contacter le conteneur B. Puis de partager dans le conteneur A par un volume. Par exemple :

    docker run --name B -p PORT_B:PORT imageB
    echo "B=proto://IP:PORT_B" > /path/to/fichier.conf
    docker run --name A -v /path/to/:/etc/monapplie/ imageA

Cette solution peut très bien être mise en œuvre avec un outil de gestion de configuration comme Puppet, Ansible ou Chef. Autre avantage, il est possible de détecter le changement de fichier de configuration et de le recharger à chaud ... Seul problème, je ne connais pas beaucoup d'application qui recharge leur fichier de configuration sans être déclenchée par un signal. On se retrouve donc avec les inconvénients suivant :

- À chaque changement du conteneur B, il faut signaler au processus dans le conteneur A que le fichier de configuration a changé.
- En revanche avec votre outil de gestion de configuration, il est possible de lancer A et B sur deux machines séparer et de changer A et B de machine.

Dans tous les cas étudiés, il faut un tiers pour prévenir A et modifier le fichier ou injecter les variables.

# DNS

Un tiers de confiance que tout le monde connaît et qui maintient une base de correspondance entre noms et adresses, ça fait beaucoup penser au système DNS. En injectant dans le conteneur, un serveur DNS spécifique, il est possible d'avoir une résolution de nom spécifique à chaque environnement.
Seul petit problème, il faut que le conteneur B soit enregistré dans le DNS.
Pour faire ça, nous avons 2 solutions, soit faire en sorte que le conteneur s'enregistre tout seul sur le service, soit utiliser un gestionnaire de configuration pour faire ce travail.

La solution est complexe, pas très pratique, et impose d'avoir un environnement de développement plus complexe que la production. En effet, il est probable que l'environnement de production se basera sur le DNS mondial et que le développeur utilise un DNS local. Au final, c'est une solution peut élégante.

# Ambassadeur

![Schéma ambassadeur]({filename}/images/schema-ambassadeur.png){.pull-left .marge-right}

Avec les links, nous nous retrouvons donc avec des conteneurs qui communiquent facilement quand ils sont sur la même machine. Seulement, il faudrait arriver à les faire communiquer à travers le réseau.
Imaginons que sur la machine de B, nous ayons un conteneur C qui s'occupe de la communication de B et que sur la machine de A nous ayons de la même façon un conteneur D pour la communication réseau de A.
Les conteneurs C et D sont des ambassadeurs, ils sont spécifiques à l'environnement de production et gèrent l'ensemble de la communication réseau entre A et B.

Le conteneur C va se retrouver avec les missions suivantes :

- faire croire à B qu'il est un client comme A.
- exposer le service de B sur le réseau.
- enregistrer le dit service dans un registre clé/valeur comme etcd

Le conteneur D va pour sa part avoir les missions suivantes

- faire croire à A qu'il est la ressource du conteneur B
- lire dans etcd l'adresse et le port du service B et se connecter dessus

Dans cette configuration, il est facile de faire tourner A et B en développement sur une seule machine et d'injecter en production les conteneurs C et D. On peut même imaginer que le conteneur D embarque la capacité de faire de l'équilibrage de charge vers plusieurs instances de C, de faire de la reprise sur erreur ou comprendre le protocole utilisé pour l'optimiser. Dans le cadre d'un service PostgreSQL le conteneur D pourrait embarquer pgpool.
C et D peuvent aussi apporter une couche d'authentification ou de sécurisation, ils sont là pour prendre à leur charge toute la communication distante liée à un environnement complexe.

Comme C et D sont des conteneurs techniques, il n'est pas obligatoire d'en avoir 1 par conteneur applicatif, il est tout à fait possible d'avoir 1 conteneur de type C et 1 conteneur de type D par machine.

En Bref, la solution des ambassadeurs et très élégante mais loin d'être trivial, elle doit en effet être adaptée à chaque contexte.

# Conclusion

L'ambassadeur est sans conteste la solution la plus élégante pour avoir une architecture simple en développement et très robuste en production. Elle permet d'extraire des conteneurs applicatifs un certain nombre de responsabilités techniques comme l'équilibrage de charge, l'authentification ou le dialogue avec des briques techniques externe (etcd, zookeeper, etc.). En revanche, l'implémentation de ces ambassadeurs requiert une bonne connaissance des applications et de l'environnement cible.


---
Photo par [Stéfan](https://www.flickr.com/photos/st3f4n/4012030328/)

