---
title: Ouverture de la béta publique des volumes
tags:
  - docker
  - volumes
  - ceph
authors:
  - Thomas Clavier
description: Vous étiez nombreux à le demander voici enfin les volumes ouverts à tout le monde sur Deliverous.
date: 2015-01-26
publishdate: 2015-01-26
aliases: /2015-01-26.volumes.html
---

Vous étiez nombreux à nous demander une solution pour garantir la persistance de vos données applicatives.
Les tests ont été longs, il ne reste plus que l'épreuve du feu.

# En théorie
Les volumes Docker permettent de sortir des données du conteneur. C'est particulièrement utile pour ne pas perdre les données de vos applications entre deux démarrages du conteneur.

Notre objectif était simple, vous fournir une solution pour monter des volumes dans vos conteneurs et faire en sorte que ces données suivent les conteneurs.

Imaginons que vous lancez un conteneur A:1 qui monte le volume /upload. La plateforme va le lancer sur un nœud X. Après une mise à jour, vous décidez de relancer la nouvelle version de votre conteneur A en version 2. La plateforme va lancer la nouvelle version de votre conteneur sur le nœud Y. Il est indispensable que les données créées par le conteneur A:1 sur le nœud X soit disponible pour le conteneur A:2 sur le nœud Y.

Pour faire ça de façon scalable et sécurisé, nous avons monté un cluster [Ceph](http://ceph.com/). Pour l'instant, faute de demande, la seule façon d'y accéder, c'est de passer par les volumes si vous cherchez une interface différente (S3 ou Swift) n'hésitez pas à demander.

# En pratique
Pour mettre en œuvre cette nouvelle fonctionnalité dans vos projets, il suffit de modifier le fichier Deliverous comme ceci :

    conteneur:
        image: monimage
        volumes:
        - name: mes_data
          path: /var/lib/data

`volumes` est la liste des volumes à monter dans le conteneur.

Pour chaque volume,

* `name`  identifie un répertoire qui sera créé dans un espace sécurisé et dédié du projet,
* `path`  correspond au point de montage dans le conteneur.

# 12 factor app

Comme évoqué dans [The Twelve Factor Apps 1/2](2014-05-26.twelve-factor-apps-1.html) et en particulier dans le point 6, pour qu'une application soit scalable il est important que chaque processus soit indépendant des autres. Donc n'utilisez pas ce filesysteme pour communiquer entre vos conteneurs. Il n'y a entre autre aucun verrou ni aucune gestion d'accès concurrents.

Si vous aviez dans l'idée d'y partager votre index Lucen ou d'en faire une file d'attente ce n'est pas le bon outils. En revanche, si vous souhaitez enregistrer les uploads de vos utilisateurs pour les servir depuis l'ensemble de vos conteneurs ou y stocker vos fichiers de base de données nous avons construit cette solution pour vous.

---
Photo par [Andreina Schoeberlein](https://www.flickr.com/photos/schoeband/5635366857)
