---
title: Survol de flynn.io et de deis.io
tags:
  - tools
  - flynn
  - deis
authors:
  - Olivier Albiez
description: Rapide comparaison de flynn.io et de deis.io
date: 2014-02-10
publishdate: 2014-02-10
aliases: /2014-02-10.flynn-et-deis.html
---

Deux projets intéressants à regarder pour ceux qui veulent faire du PaaS. Les deux projets sont très jeunes. J'ai eu beaucoup de mal à les mettre en œuvre du à des bugs.

# Flynn.io

J'ai mis en œuvre [flynn dev](https://github.com/flynn/flynn-dev).

Flynn est entièrement écrit en [go](http://golang.org/), basé sur docker pour les containers et sur [etcd](https://github.com/coreos/etcd). Le projet est plutôt cohérent dans les choix technologique et la démo marche bien.


# Deis.io

J'ai essayé de mettre en œuvre deis en utilisant leur [procédure](http://deis.io/get-deis/). Je me suis arrêté au moment ou il fallait installer un serveur chef.

Deis est écrit en Django avec Celery, ils utilisent docker pour les container, chef pour provisionner leur conteneurs et Chef Databag comme centralisation de configuration.


# Conclusion

Mon choix se porterai sur Flynn. Il y a moins d'empilement de technologie.


---
Photo par [Patrick Gaudin](https://www.flickr.com/photos/voyages-provence/6181609778/)
