---
title: Retour d'expérience sur l'intégration de <em>Docker</em> en entreprise
tags:
  - docker
authors:
  - Thomas Clavier
description: Après avoir regarder comment installer [Docker sur des Red Hat et des CentOS](2014-07-10.docker-tomcat-centos.html), nous attaquons le domaine de l'organisation des équipes autour de *Docker*.
date: 2014-07-31
publishdate: 2014-07-31
aliases: /2014-07-31.retour-experience-docker-en-entreprise.html
---

Imaginons une entreprise : plus de 800 millions de CA et plus de 6&nbsp;000 salariés.
Dans cette entreprise, les gens en charge de l'intégration et de la bonne exécution des serveurs sont dans une situation difficile : mettre à jour un serveur pour les besoins d'une application représente un cout exorbitant, l'impacte sur les autres services n'est pas maitrisé et les tests impactent la production de l'entreprise.
Pour réduire les risques et facilité la maintenance, cette entreprise a décidé de nous demander conseil.


# Pourquoi *Docker* ?

Comment cloisonner plus d'une trentaine d'applications web réparties dans une dizaine de tomcats sur seulement quelques serveurs ? La première réponse était : virtualisation ! Migrons chaque application dans un serveur et dupliquons le pour garantir la haute disponibilité et... dupliquons-le pour monter en charge. On arrive rapidement à plusieurs dizaines de serveurs à maintenir sans outil de gestion de configuration centralisé comme puppet, chef ou CFEngine. Pour les financiers, c'était aussi un problème, la supervision est externalisé et facture à l'alerte, mais aussi au nombre de serveurs surveillés.
Donc nous avions deux options, monter un gestionnaire de configuration de machines et le brancher sur les nouvelles machines ou monter du *Docker*. Les contraintes financières ont finalement tranché, *Docker* avait gagné.


# Question d'organisation

Dans cette entreprise, les études s'occupent d'acheter, de développer ou de paramétrer les applications métiers et les équipes de "Run", s'occupent de les faire fonctionner.
Les études ont donc besoin de pouvoir faire tourner un grand nombre d'applications en cours de paramétrage ou de développement.
Côté production, il faut industrialiser le déploiement et le suivi d'un grand nombre d'applications. C'est en effet cette équipe qui s'occupe à la foi du déploiement et de la bonne marche de l'ensemble des applicatifs métier et système.

La première étape de l'accompagnement a permis la mise en place de *Docker* côté production.


# Architecture choisi

Tous les choix ont été fait avec l'équipe de production, en prenant en compte leurs compétences, les outils de supervisions et les procédures déjà en place, ainsi que les contraintes de licences.

![Infra](/articles/2014-07-31_retour-experience-docker-en-entreprise/infra.svg){.pull-left .marge-right}

Les machines de recette servent à la fois à déployer les applications en mode mono-instance pour une première validation et à construire les containers versionnés qui seront déployés en pré-prodcution puis en production.

Tous les containers sont archivés sur la registry. L'ensemble des serveurs savent lire dans la registry pour récupérer la dernière version des containers.

Tous les serveurs sont identiques... à l'exception des points suivants :

* les machines sont branchés sur le bon vlan : recette, pré-production et production
* les habilitations de l'active directory permettent de filtrer les accès aux serveurs
* les machines de production sont en Red Hat alors que les autres sont des CentOS

![Détail serveur](/articles/2014-07-31_retour-experience-docker-en-entreprise/server.svg){.pull-right .marg-left}
Si l'on regarde en détail un serveur on peut voir que le point d'entrée utilisateur c'est un apache en mode reverse-proxy http préconfiguré pour faire du cache.
En dessous, tous les tomcats présentent les mêmes interfaces :

* le port 8080 qui permet de contacter le tomcat en http
* un volume /var/log/tomcat qui permet de récupérer l'ensemble des logs applicatifs


# Une politique de version

Le container apache qui est en entrée de serveur *Docker* est versionné et il embarque un fichier yaml qui décrit l'ensemble des versions de tous les containers tomcats à démarrer sur l'ensemble du parc.
L'objectif de ce fichier est triple :

* maintenir une vision global de référence de la plateforme
* permettre l'auto-configuration de chaque serveur
* simplifier les changements de versions applicatives

Une fois la plate-forme mise en place, nous avons adopté le workflow d'utilisation suivant :
* la production reçois un war et des éléments de configuration
* la production construit un container avec tous les éléments de conf pour tous les environements. Elle y apporte toute son expertise (sécurité, normalisation, etc.)
* la production publie le container sur la registry avec un numéro de version
* la production met à jour le container apache de référence
* la production déploie la dernière version du container apache de référence ce qui a pour effet de déployer les bonnes versions de container tomcat
* une fois la recette validée, il est possible de déployer la dernière version du container apache de référence
* une fois validé en qualification l'exploitation va déployer en production

Comme chaque container est versionné le retour arrière est très simple, il suffit de relancer l'ancien container.


# Et après ?

La prochaine étape va être de déployer boot2docker dans les équipes études. Ainsi, tout le monde utilisera les mêmes outils.
Les premiers tests seront faits avec des containers, comme en production.
Faire confiance, c'est bien... "*Mais si les études nous foirent la conf, c'est nous qui allons perdre nos primes !*"
Pour éviter ça, l'équipe de production gardera la main sur la génération du container qui partira en production, mais partagera avec les études l'ensemble des définitions de containers à travers l'outil de gestion de version de l'entreprise.
L'objectif, très devops, est d'amener les études et la production à collaborer sans avoir peur pour leurs responsabilités.

---
Photo par [Gundy](https://www.flickr.com/photos/nzgundy/1508769593)
