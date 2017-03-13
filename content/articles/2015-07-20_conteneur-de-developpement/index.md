---
title: Travailler dans un conteneur.
tags:
  - docker
  - volume
  - développement
authors:
  - Thomas Clavier
description: Comment utiliser le même conteneur dans tous les environements sans avoir à reconstruire le conteneur à chaque modification de sources ?
draft: true
date: 2015-07-20
aliases: /2015-07-20.conteneur-de-developpement.html
---

Que ce soit durant les meetup Docker ou chez nos clients, la question revient souvant : Comment je fais pour ne pas reconstruire systématiquement mon conteneur ? Comment faire pour avoir les modifications réalisés depuis mon poste de travail directement utilisable dans mon conteneur ? et si je lance des traitements dans mon conteneur, de la génération de code par exemple, je souhaite pouvoir interagire avec depuis mon poste de travail.

Essayons de répondre ensemble à cette épineuse question.

# Un volume partagé

Modifier une virgule dans mon fichier et basculer directement dans mon navigateur pour en voir le résultat. En tant que développeur, j'ai ce besoin là. Que mon language de prédilection soit java, php ou Go, si je doit attendre de longues secondes entre chaque changement je vais avoir l'impression de coder en aveugle.
Pour éviter ça, la solution la plus évidente c'est de partager un volume entre mon poste de dev avec mon éditeur préféré et mon conteneur. Si l'on prend l'exemple suivant : 

    :::dockerfile
    from debian
    env DEBIAN_FRONTEND noninteractive
    run apt-get update && apt-get install -y apache2 libapache2-mod-php5 && apt-get clean



Mais quels sont les actions que je souhaite faire dans mon conteneur ? 


---
Photo par [tetue](https://www.flickr.com/photos/romytetue/109188206)
