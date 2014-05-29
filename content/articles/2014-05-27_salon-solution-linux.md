Title: Solution Linux 2014
Tags: salon
Author: Thomas, Olivier
Summary: Notre présence au salon Solution Linux 2014.
Status: draft
Icon: /images/thumbnails/solution-linux-2014__square.png

Étant membre du réseau [Libre Entreprise](http://www.libre-entreprise.org/) chaque année nous nous retrouvons tous avec grand plaisir au salon [Solutions Linux, Libres et Open Source](http://www.solutionslinux.fr/), cette année c'était les 20 et 21 mai. Le Stand de l'association était comme chaque année un lieux d'échange. L'occasion de présenter nos valeurs associative mais aussi nos différents produits. 

Avec un stand à la jonction des mondes industriel et associatifs nous avons passé 2 très bonne journées riche en enseignement.

![Solution Linux]({filename}/images/solution-linux-2014.png)


# Des apprentissages  

## Premier en France
Convaincu durant nos travaux de début d'année par Docker, heureux d'être les premier en france à faire de l'hébergement Docker, nous avons été surpris de voir beaucoup de visiteurs ne connaitre Docker que très superficiellement. Il y avait bien quelques personnes l'utilisant quotidiennement, mais la grande majorité avaient à peine testé la création d'un container. Nous avons donc appris que nous sommes en avance, et ça c'est une bonne nouvelle.

## Que pour moi
Le second apprentissage était beaucoup moins surprenant, notre expérience des grosses structures Française nous avait déjà montré que bon nombre d'entre eux souhaite garder la maitrise totale de leur hébergement. C'est dans cette logique que quelques haut responsables nous ont demandés si nous étions capable de vendre notre solution pour un "cloud privé". Notre réponse les a entousiamé : notre solution n'est qu'un agencement de produits libre et nous serions heureux de vous aider à les installer chez vous ! 

# Encore des apprentissages  

Il n'y avait pas les utilisateurs de Docker qui étaient source d'apprentassage, les bénévoles impliqués dans de nombreux projet libre nous ont aussi beaucoup appris.

## Cloud Management Platforms

Pour nous les Cloud Management Platforms (CMP) étaient des outils pour gérer des machines virtuelles et pas des containers. Cela nous paraissait détourner l'outil que de vouloir les utiliser pour gérer des containers Docker. D'autre part ces solutions nous semblaient lourdes et complexes à mettre en place.

Nous cherchions des solutions simples et efficaces (KISS) pour notre objectif. Nous pensions bien utiliser des briques d'*OpenStack* comme swift mais tout prendre semblait abérant. Nos échanges avec des spécialistes d'Openstack ont remis nos choix en cause.

Lors du salon, nous avons pu échanger avec Loïc qui nous a convaincu de redonner une chance à *OpenStack*. En effet, ce CMP gère déjà enormément de choses, comme le réseau, les clients, les projets, ... D'autant plus qu'il y a des projet pour supporter *Docker* dans *OpenStack*



[*OpenStack*](https://www.openstack.org/)


[OpenNebula](http://opennebula.org/)

## [Ceph](http://ceph.com/)

## [Solum](https://wiki.openstack.org/wiki/Solum)

# Table ronde

Le mercredi, nous avons participé à la tabe ronde sur l'adoption du logiciel libre dans le datacenter. Après avoir aborder les évolutions de matériel nous avons rapidement parlé des évolutions d'architecture, en effet nous avons tous observé une migration des infrastructures de nos clients. Il y avait l'époque des gors serveurs centralisé, puis est venu l'époque de la virtualisation, avec l'avènement des outils de gestion de configuration comme puppet ou chef. Seulement gérer plusieurs centaines de serveurs virtuelles, même avec puppet ça n'est pas simple. Un certains nombre d'acteurs commencent très sérieusement à migrer vers de gros serveurs capable d'éberger des containers d'applications.

Les échanges suivant ont principalement porté sur la capacité à proprement surveiller ces applications. Sur la capacité des différentes équipes de l'entreprises à s'approprié les outils de collecte de métrique, sur les partages d'outils dans l'ensemble de l'entreprise, sur l'aligement de toutes ces équipes sur un même objectif ... en bref nous avons parlé devops.
