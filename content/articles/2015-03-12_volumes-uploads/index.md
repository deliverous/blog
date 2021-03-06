---
title: Vous avez dit volumes ?
tags:
  - docker
  - volume
  - deliverous
  - uploads
authors:
  - Thomas Clavier
description: Quelles sont les bonnes pratiques avec les volumes ? C'est une question récurrente que ce soit dans les conférences que nous donnons, dans les meetups ou de la part de nos clients.
date: 2015-03-12
publishdate: 2015-03-12
aliases: /2015-03-12.volumes-uploads.html
---

À défaut de pouvoir vous apporter une réponse unique à la question : *Quelles sont les bonnes pratiques avec les volumes ?* À travers cette série d'articles, je propose de vous apporter quelques pistes de réflexions.

Le premier cas d'utilisation que nous aborderons ici concerne les uploads utilisateurs.
Le second explore la notion de [contextes](/2015-03-28.volumes-contexte.html).

# Une histoire d'upload

Imaginons une application qui sauvegarde ses données utilisateurs dans un
répertoire local, c'est le cas le plus classique.
Wordpress, Magento et bien d'autres sauvegardent certains fichiers téléversés
par les utilisateurs dans un répertoire du système de fichier. Ces fichiers
sont des données applicatives, impossible de les laisser dans le conteneur.
D'autant plus si ces données doivent être partagées entre plusieurs conteneurs.

La solution technique la plus évidente pour répondre à ce besoin, c'est d'avoir un
système de fichier partagé à travers le réseau.

Seulement, sans passer par des technologies spécifiques et probablement
onéreuses (agrégation de flux réseaux, fiber channel, ceph, Réseau de stockage spécialisé, ...) le
passage à l'échelle d'un filesystème partagé pose problème. L'équilibre entre
la taille du système et le coût de mise en œuvre est fragile, sans parler de certains
paliers qui impliquent des changements de technologie très onéreux.

La majorité des plateformes de cloud ont résolue ce problème en mettant en
avant des solutions beaucoup plus scalable comme du stockage clé/valeur. Par
exemple, chez Amazon, il est impossible d'avoir ce genre de service sans monter
son propre cluster dédié à ce service, en revanche, il est possible d'utiliser
S3 pour sauver ses données.

Le problème est donc le suivant : une plateforme de PAAS ne peut pas proposer
un système de fichier partagé efficace et scalable à volonté qui soit simple et
efficace. Si vous souhaitez garder la possibilité d'utiliser ce genre de
plateforme, il faut respecter le point 6 des 12 factors apps. Pour partager des
éléments entre processus, on utilise une ressource distante à travers le réseau
et c'est encore mieux si c'est en utilisant des connections non-persistante.

Voici donc quelques solution pratique qu'il est possible de mettre en place
pour faire un stockage déporté de vos uploads.

# Un serveur CDN

Monter son propre CDN, je devrais plus dire : monter un conteneur de statiques.
L'idée, c'est de monter un conteneur qui distribuera à vos clients l'ensemble de
vos statiques. Le premier avantage sera de pouvoir configurer ce conteneur pour
ne pas avoir de session et imposer à vos clients la mise en cache des statiques.
Un bon moyen pour optimiser les performances de votre site sans avoir à payer
les services d'un réel CDN, et si vraiment vous avez besoins d'un CDN, rien
n'empêchera de mettre la totalité de ce nouveau domaine derrière un CDN comme
cloudflare. Ce conteneur de statiques pourra quand à lui enregistrer ses données
sur un volume, il sera en effet le seul à accéder aux fichiers d'uploads.

{{figure
  src="cdn.svg"
  alt="Schéma CDN"
  class="pull-left marge-right"}}

Avec ce nouveau conteneur, le client va uploader son image sur 1 des conteneurs
applicatifs, une fois l'upload terminé, l'application va déplacer l'image en
ftp sur le serveur de statiques. À l'affichage des pages, l'application va
injecter la bonne adresse de l'image avec le bon domaine.

Avec ce système, augmenter le nombre de conteneur applicatif est très simple,
il suffit de leur donner l'adresse du conteneur de statiques. Pour augmenter
les performances du conteneur de statiques, il suffit de lui ajouter une série de
reverse proxy cache type [Varnish](https://www.varnish-cache.org/) ou de le
mettre derrière un véritable CDN.

Le plus difficile reste à modifier l'application pour qu'elle gère correctement
ce nouveau service. Avec Wordpress, il est possible d'utiliser le plugin W3
Total Cache pour réaliser ça. C'est l'option "personnal CDN" qui permet de
configurer proprement les accès ftp et le nom du domain dédié aux statiques.

# Stockage clé / valeur

Sans passer par un conteneur de statiques, il est possible de déporter le
stockage de vos fichiers du disque vers un service de stockage d'objet
clé/valeur comme S3 ou swift. Dans ce cas, le scénario est le suivant :

Le client upload son image, votre application stock le fichier dans le cluster
swift et chaque appel de l'image dans les pages web se fait à travers votre
application qui ira chercher le fichier dans le service de stockage avant de le
renvoyer au client.
Avec un peu de cache sur chaque serveur applicatif, tout fonctionnera sans
aucune perte de performance, et ce, même si vous avez un très grand nombre de
conteneurs applicatif. Déployer cette solution permet de ne pas avoir à
configurer un conteneur supplémentaire, en revanche, elle dépend d'un service
tiers.

Que ce soit avec Magento ou Wordpress, il existe des plugins pour faire ça. Si
vous développer en rails ou en danjgo, il existe des gems et des packages
python capable de vous aider à résoudre cette problématique.

# Conclusion

Malgré ces défauts, le volume est une solution simple et efficace pour une
application ne nécessitant pas d'avoir plus d'un conteneur.

En revanche, si l'on augmente le nombre de conteneurs il est préférable
d'utiliser un système tièrs pour s'occuper des uploads.  Qu'il soit fait maison
avec un conteneur ou hébergé sur la toile, dans tous les cas, il est préférable
de séparer les responsabilités pour éviter d'utiliser un système de fichier
partagé.

---
Photo par [Ben Grey](https://www.flickr.com/photos/ben_grey/4582294721)
