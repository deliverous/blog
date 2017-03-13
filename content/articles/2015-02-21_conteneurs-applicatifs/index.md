---
title: Conteneurs applicatifs
tags:
  - docker
  - rocket
  - lxc
  - lxd
  - openvz
authors:
  - Thomas Clavier
description: Lxc et OpenVZ sont ils des conteneurs applicatif ?
draft: true
date: 2015-02-21
aliases: /2015-02-21.conteneurs-applicatifs.html
---

Régulièrement j'entends des gens annoncer haut et fort que Docker n'a rien apporté de nouveau, que les conteneurs GNU/Linux existent depuis très longtemps avec LXC et OpenVZ. Certe, mais revenons en détails sur les caractéristiques de chacun avant de conclure.

# Conteneurs Linux 

Les conteneurs GNU/Linux sont avant tout une forme d'isolation des applications. Pensé par des administrateurs systèmes, ils permettent de lancer dans un environnement totalement isolé l'ensemble des processus d'une machine. C'est à dire que comme dans une machine virtuelle, on retrouve l'ensemble de la séquence de lancement. Donc par exemple les scripts de nettoyage des répertoires temporaire, le montage des systèmes de fichiers réseau, le lancement des services de base comme smtp, cron ou syslog. 
Un conteneur construit de cette façon pourra être administré de la même façon qu'une machine virtuelle. Il sera par exemple possible d'automatiser un grand nombre de tâches récurrentes avec Puppet, Chef ou Ansible. 

Le gros avantage des conteneurs Linux c'est qu'ils sont beaucoup moins gourmand en ressources que des machines virtuelles ou para-virtualisés. Le conteneur Linux tire sont efficacité d'une choses, il partage le même noyau que la machine 

et d'autre part il est caen grande partie des "control groups" et des "name spaces" 

# Conteneurs applicatifs



---
Photo par [tetue](https://www.flickr.com/photos/romytetue/109188206)
