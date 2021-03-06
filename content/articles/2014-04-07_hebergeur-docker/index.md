---
title: Pourquoi devenons-nous hébergeur Docker ?
tags:
  - docker
  - cloud
authors:
  - Thomas Clavier
description: Pour la mise en place de notre solution de déploiement continu, nous avons commencé à étudier tout un ensemble d'outils pour assurer l'hébergement dans le nuage des différentes applications à déployer. Suite aux résultat de nos recherches, nous avons décidé de devenir notre propre hébergeur.
date: 2014-04-07
publishdate: 2014-04-07
aliases: /2014-04-07.hebergeur-docker.html
---

Héberger votre chaîne de déploiement continu implique d'avoir à notre disposition un hébergeur disposant d'une API de haut niveau. Que ce soit pour déployer nos applications ou les vôtres, cet hébergeur est indispensable.

Nous imaginions tout simplement une API capable de prendre en charge des applications au sens [Twelve Factor Apps](http://12factor.net/), que l'on puisse lui dire "voici une application", "elle écoute sur le port 80", ou "la charge va fortement augmenter, il nous faut 7 instances".

N'ayant pas trouvé cet hébergeur, nous souhaitons vous le proposer.

# Le "nuage", c'est quoi ?

Cloud, un mot très à la mode pour décrire ce que d'autres nomment des services hébergés. Ce mot-valise illustre pourtant un réel changement de consommation de l'informatique.

Il était une époque où chaque entreprise entretenait sa propre source d'énergie, une machine à vapeur, une génératrice électrique, etc. Aujourd'hui, toutes les entreprises ou presque utilisent l'électricité. Elles ne se posent même plus la question du courant continu ou alternatif. Nous pensons que de la même façon, demain le logiciel informatique sera une commodité comme l'eau courante ou l'électricité aujourd'hui, l'informatique à la demande, voilà l'avenir.

Dans ce cadre, nous imaginons un hébergeur capable de répondre aux besoins suivants :

- déclarer une application
- configurer une application (déclarer les ressources)
- lancer une application
- changer le nombre d'instances de l'application

Sans se soucier des pannes matériels, des mises à jours de sécurité, du réseau ou des communications entre les centres de données.

# Pourquoi Docker ?

Un certain nombre de contraintes sur la façon de construire et de déployer des applications nous semblaient implicites... Probablement le fruit de nos expériences.
Après avoir lu [Twelve Factor Apps](http://12factor.net/), plus de doute possible, une fois construite, une application doit embarquer l'ensemble de ses dépendances y compris système.

Pour adapter une application à son environnent, il suffit de définir quelques variables d'environnement, ce qui nous rapproche fortement du concept d'appliance. En effet pour embarquer toutes ses dépendances, une application doit être construite avec le système d'exploitation qui permet de la faire fonctionner.

Avec Docker le concept d'appliance est sublimé, il n'y a quasiment pas de surcoût lié à la virtualisation et il n'est plus utile de maintenir le système d'exploitation. À chaque construction du container, la couche système est mise à jour.

Le slogan de Docker résonne en nous comme une vérité :
"Build once... run anywhere".
Ce que l'on peut traduire par "Construire une fois... Lancer n'importe où".
Le sous-titre est encore plus explicite : "Le container que le développeur construit et teste sur son PC, peut tourner et passer à l'échelle en production".

Voilà une devise qui rime avec Deliverous.
Une fois construite, l'application doit pouvoir être testée, éprouvée, dans de nombreux contextes avant de passer en production.
Elle doit pouvoir suivre son pipeline de mise en production sans risquer la remise en cause des tests.

Voilà pourquoi nous avons choisi Docker comme unique format de container d'application.

# Une histoire de cargo.

Une fois Docker sélectionné comme unique format de container, nous avons cherché un hébergeur en Europe capable de faire tourner nos containers.

Pour garder l'analogie avec les containers de marchandises, nous avons cherché un porte-conteneurs universel respectant nos valeurs... Seulement dans le fret, les "UCC" (Universal Container Carrier) se sont généralisés à partir des années 70, alors que dans l'informatique le format universel de container est loin d'être normalisé...

Difficile dans ces conditions de trouver un hébergeur qui nous garantit à la fois une bonne connectivité à internet, la sécurité des données et la protection de la vie privée des clients.

Vous avez été nombreux à nous parler de l'affaire Prism et de ses conséquences sur la confiance de vos clients. Nous avons donc cherché un hébergeur Docker en Europe, pas un hébergeur avec un bureau en Europe et un siège social soumis à "patriot-act" mais une société européenne qui n'utiliserait aucune brique venue des États-Unis (ni [amazon EC2](https://aws.amazon.com/ec2/), ni [digital ocean](https://www.digitalocean.com/), ...).

Et nous n'avons rien trouvé, certains sont capables de monter en charge rapidement, mais ils ne garantissent pas le respect de la vie privée, et pour d'autres, c'est l'inverse.

Nous avons donc décidé de monter notre propre plate-forme Docker.

# Conclusion

Nous avons besoin d'un hébergeur Docker qui respecte nos contraintes mais peut-être que vous aussi ... Nous avons donc décidé de travailler avec vous pour ouvrir notre solution de cloud Docker. Rendez-vous sur le site de [Deliverous](http://deliverous.com/docker) pour participer à l'aventure.

---
Photo par [Kristi](https://www.flickr.com/photos/kristi_decourcy/9154543163)
