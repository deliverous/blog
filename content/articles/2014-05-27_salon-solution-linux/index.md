---
title: Solution Linux 2014
tags:
  - salon
authors:
  - Thomas Clavier
  - Olivier Albiez
description: Retour sur deux jours d'échanges et d'apprentissage au salon Solution Linux 2014.
date: 2014-05-27
publishdate: 2014-05-27
aliases: /2014-05-27.salon-solution-linux.html
---

Étant membre du réseau [Libre Entreprise](http://www.libre-entreprise.org/) chaque année nous nous retrouvons tous avec grand plaisir au salon [Solutions Linux, Libres et Open Source](http://www.solutionslinux.fr/), cette année c'était les 20 et 21 mai. Le Stand de l'association était comme chaque année un lieu d'échange. L'occasion de présenter nos valeurs associatives, mais aussi nos différents produits.

Avec un stand à la jonction des mondes industriel et associatifs, nous avons passé 2 très bonnes journées riches en enseignements.

# Des apprentissages


## Premier en France
Convaincu durant nos travaux de début d'année par Docker, heureux d'être les premiers en France à faire de l'hébergement Docker, nous avons été surpris de voir beaucoup de visiteurs ne connaitre Docker que très superficiellement. Il y avait bien quelques personnes l'utilisant quotidiennement, mais la grande majorité avaient à peine testé la création d'un container. Nous avons donc appris que nous sommes en avance, et ça, c'est une bonne nouvelle.


## Que pour moi
Le second apprentissage était beaucoup moins surprenant, notre expérience des grosses structures Française nous avait déjà montrée que bon nombre d'entre eux souhaitent garder la maitrise totale de leur hébergement. C'est dans cette logique que quelques hauts responsables nous ont demandés si nous étions capables de vendre notre solution pour un "cloud privé". Notre réponse les a enthousiasmés : notre solution n'est qu'un agencement de produits libre et nous serions heureux de vous aider à les installer chez vous !


# Encore des apprentissages

Il n'y avait pas que les utilisateurs de Docker qui étaient source d'apprentissages, les bénévoles impliqués dans de nombreux projets libres nous ont aussi beaucoup appris.

## Cloud Management Platforms

Pour nous, les Cloud Management Platforms (CMP) étaient des outils pour gérer des machines virtuelles et pas des containers. Cela nous paraissait détourner l'outil que de vouloir les utiliser pour gérer des containers Docker. D'autre part, ces solutions nous semblaient lourdes et complexes à mettre en place.

Nous cherchions des solutions simples et efficaces (KISS) pour notre objectif. Nous pensions bien utiliser des briques d'*OpenStack* comme swift mais tout prendre semblait aberrant. Nos échanges avec des spécialistes d'Openstack ont remis nos choix en cause.

Lors du salon, nous avons pu échanger avec [Loïc](http://dachary.org/) qui nous a convaincu de redonner une chance à *OpenStack*. En effet, ce CMP gère déjà énormément de choses, comme le réseau, les clients, les projets, ... D'autant plus qu'il y a des projets pour supporter *Docker* dans *OpenStack*.

Voici quelques liens qui nous ont été conseillés :

- [Projet *Fuel*](http://software.mirantis.com/key-related-openstack-projects/project-fuel/)
- [*OpenStack* chez *Redhat*](http://openstack.redhat.com/)
- [*OpenStack*](https://www.openstack.org/)

Du coup nous allons aussi regarder :

- [*OpenNebula*](http://opennebula.org/)
- [*CloudStack*](http://cloudstack.apache.org/)
- [*Eucalyptus*](https://www.eucalyptus.com/)

Nous avons aussi rencontré deux personnes qui travaillent sur le projet [Solum](https://wiki.openstack.org/wiki/Solum) et qui semblent vouloir utiliser *Docker*.


## [Ceph](http://ceph.com/)

Nous avons profité du salon pour chercher un filesystem utilisable pour stocker les données des containers clients et faciliter la migration des containers d'une machine à une autre.

Nous avions en tête une solution genre SAN, mais nous souhaitions aussi une solution libre.

Le seul inconvénient de Ceph que nous avons perçu est qu'il faille au moins 3 nœuds pour démarrer un cluster.

# Table ronde

Le mercredi, nous avons participé à la table ronde sur l'adoption du logiciel libre dans le datacenter. Après avoir aborder les évolutions de matériel, nous avons rapidement parlé des évolutions d'architecture. En effet, nous avons tous observé une migration des infrastructures de nos clients. Il y avait l'époque des gros serveurs centralisé, puis est venu l'époque de la virtualisation, avec l'avènement des outils de gestion de configuration comme puppet ou chef. Seulement gérer plusieurs centaines de serveurs virtuelles, même avec puppet ça n'est pas simple. Un certain nombre d'acteurs commencent très sérieusement à migrer vers de gros serveurs capables d'héberger des containers d'applications.

Les échanges suivant ont principalement porté sur la capacité à proprement surveiller ces applications. Sur la capacité des différentes équipes de l'entreprise à s'approprier les outils de collecte de métrique, sur les partages d'outils dans l'ensemble de l'entreprise, sur l'alignement de toutes ces équipes sur un même objectif... En bref nous avons parlé devops.

---
Image par [Tarsus](http://www.solutionslinux.fr/)

