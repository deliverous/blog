---
title: Ouverture de la béta de <em>Deliverous</em>
tags:
  - deliverous
authors:
  - Thomas Clavier
  - Olivier Albiez
description: Brève description de ce que nous avons mis en place pour vous ouvrir la béta de *Deliverous*
date: 2014-07-29
publishdate: 2014-07-29
aliases: /2014-07-29.ouverture-de-la-beta.html
---

Cela fait maintenant quelques semaines que nous vous avons invité à vous inscrire pour être prévenu de l'ouverture de la bêta ... Et bien voilà depuis ce matin, pour un certain nombre d'entre vous, une fois identifié sur le site de [*Deliverous*](http://deliverous.com) vous pouvez cliquer en haut à droite sur votre nom pour arriver sur votre page de profil.

Nous vous invitons à travers ce post à découvrir ce qui se cache derrière les quelques écrans auxquels vous pouvez accéder.

# Votre profile

La page de [profil](http://deliverous.com/profile) vous affiche quelques informations personnels illustrées par votre [gravatar](https://gravatar.com/).
Vous y trouvez aussi la liste de vos projets.
Plus tard, vous y trouverez probablement l'historique de vos factures.

# Des projets

Le projet est l'élément central, il est archivé dans un git et le fichier Deliverous présent à la racine du git permet de le décrire.
Un projet est généralement constitué de plusieurs applications qui cohabitent pour former un système capable de rendre un service à vos utilisateurs.
Par exemple il est possible de décrire un projet avec un container pour faire l'équilibrage de charge devant N containers php qui utilisent N containers Redis pour stoker les données.

# Le fichier Deliverous

Le fichier Deliverous permet de decrire la liste des containers et leur organisation. Il est actuellement au format YAML.

    blog:
      image: deliverous/blog
      ports:
      - ip: blog-addr
        host_port: 80
        container_port: 80


Ce fichier Deliverous va démarrer notre blog sur nos infrastructure. Il sera joignable sur l'adresse IP nommée blog-addr dans les IP de votre projet.


La directive 'environment' permet de spécifier des variables d'environnements pour le container. Exemple :

    container:
      image: ...
      environment:
        VAR: value


La directive 'links' permet de lier plusieurs containers, comme la directive [link](https://docs.docker.com/userguide/dockerlinks/) de docker. Exemple :

    front:
      image: ...
      links:
      - name: mysql
        alias: db

    mysql:
      image: ...



# Des triggers

Les triggers ou webhooks dans le jargon des hub http sont là pour déclencher à distance le déploiement de votre projet.
Attention, pour l'instant, déclencher un déploiement entraine une coupure de service.

Comme votre projet peut regrouper plusieurs sources : nombreux dépôt git et nombreuses images de containers, il est possible de créer plusieurs triggers.
En confiant un trigger à chaque fournisseur, il est possible de limiter les risques en cas de corruption de l'un d'entre eux.

Ces webhooks ont été testés avec le [hub docker](https://hub.docker.com/) ainsi qu'avec [github](https://github.com/). Si vous utilisez ces services, il est très facile de déclencher un déploiement suite à la modification du fichier Deliverous ainsi que chaque fois que l'un des containers est reconstruit.

Si vous préférez la ligne de commande vous pouvez utiliser curl ou wget :

    curl -X POST -data="" http://api.deliverous.com/trigger/12345678-abcd-123456789-abcdefghijkl
    wget --post-data="" http://api.deliverous.com/trigger/12345678-abcd-123456789-abcdefghijkl

# Des IPs

Les adresses IPs sont les points d'entrées de vos utilisateurs sur votre projet.
Durant la béta, il est possible de n'avoir qu'une IP par projet.

# Et maintenant ?

{{< figure
  src="oui-nide-iou.jpg"
  alt="We need you"
  class="pull-right marge-left" >}}

Maintenant que la béta s'ouvre un peu plus, nous attendons avec impatience vos remarques et suggestions sur les choses les plus importantes à vos yeux qu'il faudrait implémenter.
Concient que le travail est loin d'être terminé, nous aimerions avoir votre avis pour ordonner les évolutions à venir. Nous vous invitons à rejoindre la [mailing liste](http://ml.deliverous.com/mailman/listinfo/deliverous) pour poursuivre les échanges.

---
Photo de [tableatny](http://commons.wikimedia.org/wiki/File:Starting_blocks.jpg)

Illustration [Superdupont](http://www.amazon.fr/Superdupont-Tome-Oui-nide-iou/dp/2858158428)
