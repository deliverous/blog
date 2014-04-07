Title: Pourquoi devenons nous hébergeur docker ?
Tags: docker, cloud
Author: Thomas
Summary: Pour la mise en place de notre solution de déploiement continu nous avons commencé à étudier tout un ensemble d'outils pour assurer l'hébergement dans le nuage des différents applications à déployer. Nos recherches ne nous ayant rien apporté de concluant nous avons décidé de devenir notre propre hébergeur. Explications ... 
Status: draft
Icon: /images/thumbnails/ontainer__square.jpg

Héberger votre chaine de déploiement continu implique d'avoir à notre disposition un hébergeur disposant d'une API de haut niveau pour déployer chaque application, que ce soit pour nos applications ou les votres.

Nous imaginions une api capable de prendre en charge des applications au sens [12 factor apps](http://12factor.net/), que l'on puisse dire voici une application, elle écoute sur le port 80, ou la charge va fortement augmenter, il nous faut 7 instances. Faire tout ça très simplement.

![Survol]({filename}/images/container.jpg)

# Pour nous le nuage c'est quoi ?

Cloud, un mot très à la mode pour décrire ce que d'autres appel les services hébergés. Ce mot valise illustre pourtant un réel changement de consomation de l'informatique. 
Il était une époque ou chaque entreprise entretenait sa propre source d'énergie, une machine à vapeur, une génératrice électrique, etc. Aujourd'hui toutes les entreprises ou presque utilisent l'électricité. Elles ne se posent même pas la question du courant continu ou alternatif. Nous pensons que de la même façon, demain le logiciel informatique sera une commodité comme l'eau courante ou l'électricité aujourd'hui, l'informatique à la demande, voilà l'avenir.

Dans ce cadre, nous imaginons qu'un hébergeur soit capable de répondre aux besoins suivants : 
- déclarer une application
- configurer une application (déclarer les resources)
- lancer une application
- changer le nombre d'instances de l'application

Et tout ça sans avoir à se soucier des pannes matériel, des mises à jours de sécurité, du réseau ou des communications entre centre de doonées.

# 

---
Photo par [Kristi](https://www.flickr.com/photos/kristi_decourcy/9154543163)
