Title: Survol de flynn.io et de deis.io
Date: 2014-02-10 16:00
Category: Articles
Tags: tools
Slug: 2014-02-10-flynn-and-deis
Author: Olivier
Summary: Rapide comparaison de flynn.io et de deis.io
Status: published

Deux projets interessants à regarder pour ceux qui veulent faire du PaaS.

Les deux projets sont très jeunes. J'ai eu beaucoup de mal à les mettre en oeuvre du à des bugs.


# Flynn.io

J'ai mis en oeuvre [flynn dev](https://github.com/flynn/flynn-dev).

Flynn est entièrement écrit en [go](http://golang.org/), basé sur docker pour les containers et sur [etcd](https://github.com/coreos/etcd). Le projet est plutôt cohérent dans les choix technologique et la démo marche bien.


# Deis.io

J'ai essayé de mettre en oeuvre deis en utilisant leur [procédure](http://deis.io/get-deis/). Je me suis arrêté au moment ou il fallait installer un serveur chef.

Deis est écrit en Django avec Celery, ils utilisent docker pour les container, chef pour provisionner leur conteneurs et Chef Databag comme centralisation de configuration.

# Conclusion

Mon choix se porterai sur Flynn. Il y a moins d'empilement de technologie.