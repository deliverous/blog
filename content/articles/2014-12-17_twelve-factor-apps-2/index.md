---
title: The Twelve Factor Apps 2/2
tags:
  - 12-factor
  - heroku
authors:
  - Thomas Clavier
  - Olivier Albiez
description: Etude de *The Twelve Factor Apps*. La théorisation d'une bonne application par Adam Wiggins l'un des fondateurs de [Heroku](https://www.heroku.com/) seconde partie
date: 2014-12-17
publishdate: 2014-12-17
aliases: /2014-12-17.twelve-factor-apps-2.html
---

[The Twelve Factor Apps](http://12factor.net/) c'est la définition des bonnes pratiques que doivent suivre un développeur pour produire une application portable et capable de passer à l'échelle. Ces 12 règles ont été rédigées par Adam Wiggins l'un des fondateurs de [Heroku](https://www.heroku.com/).

Cet article est la suite de notre traduction libre entammé dans [The Twelve Factor Apps 1/2](2014-05-26.twelve-factor-apps-1.html)

# 7 - Exposition de port

La seule façon de contacter un service, c'est par le réseau. Pour exposer un service il suffit donc de déclarer le port réseau utilisé.

Par exemple, une application web en PHP pourra etre exécuté dans un *Apache* avec le module PHP et exposé sur le port 80. Une application Java pourra être lancé dans un *Tomcat* et exposé sur le port 8080.

Une application *12-factor* est auto-suffisante elle ne doit pas dépendre d'éléments à l'exécution pour bien fonctionner. Elle écoute et parle sur un port réseau.

En développement il sera par exemple possible d'utiliser le service avec l'url `http://localhost:8000`. En production un loadbalancer pourra servir de point d'entrée vers de nombreuses instances de l'application.

C'est typiquement mis en place par l'introduction d'une librairie de service web dans l'application. Par exemple [Tornado](http://www.tornadoweb.org/) pour Python, [Unicorn](http://unicorn.bogomips.org/) pour Ruby ou [Jetty](http://www.eclipse.org/jetty/) pour Java.

Le protocole HTTP n'est qu'un exemple des services réseau disponible. MySQL, Redis ou ejabberd utilisent des protocoles différents sur d'autres ports réseaux.

Notez qu'en exposant un service sur le réseau, il est alors utilisable comme une resource distante comme évoqué dans le point 4 en décrivant le service par son URL dans la configuration (cf point 3).


# 8 - Concurrence

La montée se charge se fait en augmentant le nombre d'instances des composants applicatifs.

C'est une base d'Unix, pour augmenter la capacité de traitement d'une application, il suffit bien souvent d'augmenter le nombre de processus. C'est par exemple vrai avec Apache httpd mais aussi avec Postifx ou Spamassassin. À l'inverse de Java qui réserve un ensemble de ressources au près du système et se débrouille avec.

Une application *12-factor* doit suivre ce même principe pour augmenter la capacité, il faut pouvoir augmenter le nombre de nombre d'instance de composants applicatifs.

L'architecture de l'application doit permettre ce mode de fonctionnement. Par exemple pour prendre en charge les requêtes HTTP on pourra instanciés des processus web, pour prendre en compte les traitements longs on pourra instancier des composants "worker" si la charge lié à l'une ou l'autre des types de requête augmente il suffit d'augmenter le nombre de worker ou de processus web.

Cela n'influe en rien sur le fonctionnement interne d'un composant applicatif. Que l'architecture soit basé sur une consommation d'événements asynchrone comme avec node.js ou EventMachine ou sur des processus ou des threads Unix dédié à chaque client.

Chaque processus ne doit jamais passer en mode démon, écrire dans un fichier PID ou dépendre d'un systeme comme systemd, upstart ou un autre "process manager" cela reviendrait à dépendre d'un composant tierce et violerais le point 2.


# 9 - Disponibilité

Maximiser la robustesse grace à des démarrages rapides et des arrêts progressifs

Pour qu'une application soit robuste et scalable, il est important qu'elle démarre rapidement. Que ce soit pour déployer du nouveau code, un nouveau paramétrage ou faire face à un pic de charge. Plus le temps de démarrage est court, plus il sera simple de réduire le time to market.

La réception d'un signal `SIGTERM` doit permettre l'arrêt propre de l'application. Dans le cas de requêtes HTTP, à la réception du signal l'application pourra refuser les nouvelles connections et finir de répondre aux requêtes en cours. Dans le cas de requête de type long pooling, il faudra que le client soit capable de se reconnecté tout seul.

Pour un processus de type worker, la réception du signal doit remettre le travail dans la file pour qu'un autre worker le consomme, attention à la gestion des verrous. Dans l'idéal un worker doit être idempotent.

Les principes sont les mêmes en cas de crash d'un processus que ce soit lié à une erreur applicative ou un problème physique. Ce qui rejoint le principe du "Crash-only design".


# 10 - Équivalence des environnements

Garder l'environnement de développement, de test et de production aussi similaire que possible. Dit comme ça, certains diront que ça tombe sous le sens. Mais en regardant en détail les différences sont là et facilement explicable.

* Les différences temporelles : le développeur travaille le code et ça prend du temps, des jours voir des semaines avant que ce code arrive en production.
* Les différences humaines : le développeur code et l'admin système fait les déploiements. Deux équipes différentes donc potentiellement des différences.
* Les différences d'outil : en développement, il est plus facile d'utiliser un micro serveur web sous OS X alors qu'en production, c'est apache sous GNU/Linux.

Une application *12-factor* est conçue pour du déploiement continu. Afin de réduire les différences entre les environnements, il est possible de se concentrer sur les points suivants :

* Les différences temporelles : une nouvelle ligne de code doit pouvoir arriver en production quelques minutes après avoir été écrite.
* Les différences humaines : les gens qui codent devraient être impliqués dans le déploiement et la surveillance de leur code.
* Les différences d'outil : essayer d'avoir les mêmes outils partout.

Utiliser une librairie d'abstraction pour certains services et exploiter une implémentation différente sur chaque environnement est globalement une fausse bonne idée. Par exemple, il vaut mieux utiliser *PostgreSQL* en développement si c'est la base de données utilisé en production, plutôt que *SQLite*. En effet, malgré les librairies d'abstractions, il reste des différences qui pourront entraîner des déploiements en erreur.

Les outils modernes (apt-get, Homebrew, Docker) simplifient grandement l'installation de ces outils à l'identique de la production, utilisez les.


# 11. Logs

Traiter les logs comme des flux d'evenements.

Une application *12-factor* n'est pas concerné par le routage ou le stockage des logs. Chaque processus écrit son flux d'evenements, non bufferisé, sur `stdout`.

Pendant le développement, les développeurs pourront voir ses flux dans leur terminal.

En production, chaque flux de processus sera capturé par l'environnement d'exécution, assemblé avec les autres flux de l'application et routé vers une destination d'affichage ou d'archivage. Ces destinations ne sont pas visibles ou configurables par l'application. Elles sont complétement gérées par l'environnement d'exécution.


# 12. Processus d'Admin

Exécuter les tâches d'administration et de gestion comme des processus ponctuels.

Indépendamment du service rendu par une application, les développeurs ont souvent le besoin de réaliser des tâches d'administration ou de maintenance comme :

* Réaliser des migrations de base de données,
* Lancer une console pour lancer des commandes ou inspecter les données de l'application,
* Lancer des scripts à usage unique, stockés dans le dépôt de code de l'application.

Ces actions doivent s'exécuter dans des environnements identiques à l'application. En particulier, elles s'exécutent pour une version en utilisant le même code et la même configuration que l'application. Ces taches d'administrations doivent être livrées avec le code applicatif pour éviter les problèmes de synchronisation.

---
Photo par [endolith](https://www.flickr.com/photos/omegatron/438268407)


