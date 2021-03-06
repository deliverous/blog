---
title: Conteneur Minecraft
tags:
  - minecraft
  - scriptcraft
  - Docker
  - coding gouter
  - enfants
  - javascript
authors:
  - Thomas Clavier
description: Il était une fois, des enfants, un conteneur Minecraft et du javascript ...
draft: true
date: 2015-02-21
publishdate: 2015-02-21
aliases: /2015-02-21.conteneurs-minecraft.html
---

Il existe un groupe de parents informaticiens sur Lille qui une fois par mois se réunissent pour coder avec leurs enfants. Les enfants ont entre 5 et 15 ans. Nous appelons ça des [coding gouter](http://codinggouter.org/). Depuis la session de février, sur une idée d'[/ut7](http://gnanclub.ut7.fr/) nous utilisons un "mod" Minecraft qui permet de manipuler les éléments du jeux en javascript : [ScriptCraft](http://scriptcraftjs.org/). Voici le retour d'expérience.

# Les outils

Minecraft est un jeu surprenant, tous les enfants le connaissent, c'est une sorte de dénominateur commun. L'idée de [Raphaël](http://ut7.fr/equipe.html) était simple, si les enfants sont dans un univers qu'ils maitrisent, mais que le seul moyen d'interagir avec, c'est de coder, alors peut-être qu'il découvrirons la puissance et le plaisir de notre métier.

ScriptCraft est un mod Minecraft qui permet de coder en javascript dans le jeu. Il permet entre autres d'écrire ses propres mods. L'API de scriptcraft nous permet de manipuler la totalité des éléments du jeux, de créer des blocs à volonté sans les contraintes des règles du jeu.
Pour utiliser scriptcraft il y a 2 solutions : déposer des fichiers `.js` dans un répertoire ou lancer des commandes dans la console du jeu.

# Docker

Le projet de conteneur est sur [github](https://github.com/tclavier/docker-scriptcraft) et sur le [hub docker](https://registry.hub.docker.com/u/tclavier/scriptcraft/). On retrouve dans ce projet notre façon d'organiser les sources d'un conteneur Docker : un Rakefile pour automatiser les tâches répétitives, des sources dans src/, un Dockerfile et un fichier Deliverous.

Le Rakefile va permettre de télécharger [CanaryMod](http://canarymod.net/) et ScriptCraft avant de construire le conteneur.

Alors que dans le Dockerfile, tout est installé dans `/opt/minecraft`, au démarrage, le conteneur copie l'installation de Minecraft dans le volume `/minecraft`. Ainsi les mondes peuvent être persistants ou pas en fonction d'une simple variable d'environement.

# Paramétrage

Certains éléments de paramétrage sont réalisés par variables d'environnements, pour le reste, il faut soit utiliser vos droits ops pour modifier ce qui peut l'être à chaud, soit refaire votre propre conteneur en modifiant le ficher `src/server.cfg` et celui du monde par défaut dans `default_NORMAL.cfg`.

Si vous souhaitez refaire un conteneur, [gamepedia](http://minecraft-fr.gamepedia.com/Server.properties) est une bonne piste pour bien comprendre les options du fichier.

Si vous préférez passer par les variables d'environements, voici celles qui sont disponibles :

* `OPS` : le pseudo du joueur qui sera le premier ops
* `ONLINE_MODE` : true ou false, c'est l'option qui permet au serveur de vérifier l'identité des joueurs sur les serveurs minecraft
* `WORLD_TYPE` : le type de monde, par défaut FLAT
* `GENERATE_STRUCTURES` : true ou false, cette option n'est pas utilisé pour un monde plat.

# Deliverous

Le déploiement sur nos serveur se fait avec le fichier Deliverous suivant : 

    :::yaml
    scriptcraft:
      image: tclavier/scriptcraft
      ports:
      - ip: my_ip_name
        container_port: 25565
        host_port: 25565
      volumes:
      - name: minecraft
        path: /minecraft
      environment:
        OPS: FooBar
        ONLINE_MODE: false
        WORLD_TYPE: FLAT
      limits:
        memory: 2G

Attention à la limite de mémoire, en effet, Minecraft est très groumand.

# Le jeux

Durant la première expérience, pas facile d'écouter tout le monde en même temps. De comprendre les règles et les limitations de ce serveur.

Dans la pratique, le jeu est très complexe, avec un très grand nombre de règles, c'est un monde complet à lui tout seul. Je pensais pouvoir en comprendre les rudiments en échange de quelques lignes de javascript. Seulement pas vraiment, en effet avec scriptcraft, il est plus facile de créer des blocs que de manipuler les nombreux objets. Et pour tuer les autres, quoi de mieux qu'un arc ou une épée ?

Rapidement, tous les enfants étaient ops, et certains se sont plus amusés sans code. D'autres ont inventés des attaques à base de lave.

En bref, j'ai passé une heure à apprendre quelques règles de Minecraft et à comprendre 2 choses :

* Les bloc sont la matière première qui permet de produire des objets et il faut les "miner" pour pouvoir les utiliser.
* Dans le jeux normale, il y a beaucoup de règles de gestions pour fabriquer les objets.

Dans le mod ScriptCraft, par défaut, les joueurs peuvent utiliser des objets, mais il est impossible de casser des blocs pour récupérer de la matière première, la seule solution pour modifier le monde, c'est de coder. 
C'est pourquoi, les fois suivante, fort de notre expérience, nous avons suivi quelques règles :
* aucun ops
* configuration du jeux en mode créatif
* des parents disponible pour expliquer l'api
* ne pas oublier d'aider les enfants à définir un objectif de création atteignable durant l'après midi.

# Le code

Une fois le conteneur lancé, il faut activer la capacité de coder pour tous les joueurs. C'est ce que les développeurs ont appelés le mode "classroom". Pour faire ça, un ops doit lancer la commande suivante :

    /jsp classroom on

Après, tout le monde peut lancer du javascript `/js 1+1` doit renvoyer `2` ou `/js up().box(blocks.water)` va ajouter un bloc d'eau au-dessus du bloc pointé par la souris. Pour bien comprendre l'API de scriptcraft, je vous invite à lire le document de [référence](https://github.com/walterhiggins/ScriptCraft/blob/master/docs/API-Reference.md) et pour connaitre les id des blocs, un petit tour sur [gamepedia](http://minecraft-fr.gamepedia.com/Valeurs) s'impose.

En bref, nous avons comme d'habitude passé un super moment avec nos enfants.

---
Photo par [Olivier](https://plus.google.com/+OlivierVEREMME)
