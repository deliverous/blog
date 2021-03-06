---
title: Une bassine de travail
tags:
  - docker
  - bassine
  - pair-programming
authors:
  - Olivier Albiez
  - Etienne Charignon
description: Comment utiliser un conteneur Docker pour faire un espace de travail collaboratif.
date: 2015-03-06
publishdate: 2015-03-06
aliases: /2015-03-06.bassine.html
---

Depuis quelque temps, [Olivier](http://deliverous.com/team) de Deliverous et
[Étienne](https://fr.linkedin.com/in/etiennecharignon) d'[/ut7](http://ut7.fr/)
expérimentent le pair programming à distance sur le code de Deliverous.

Nous utilisons un container en ligne (évidemment !) que nous appelons une
*bassine*. Si vous voulez comprendre l'origine de ce nom, Étienne vous parle
plus en détail de l'origine des *bassines* sur le [blog
d'/ut7](http://ut7.fr/posts/blog/2015/03/05/les-pieds-dans-la-bassine.html)
mais pour faire simple, disons que c'est un espace de travail créé à
l'occassion de chaque session de programmation : chacun se connecte en `ssh` et
nous utilisons [`tmux`](http://tmux.sourceforge.net/) pour partager le même
terminal (en fait pour être précis, nous utilisons [`byobu`](http://byobu.co/)
qui est une sur-couche pour `tmux`).

Évidemment, c'est en mode texte, mais heureusement, nous avons à notre
disposition des éditeurs très puissants qui ont fait leurs preuves : `vim ` et
`emacs`.

Ci-après, nous allons vous expliquer en détail comment nous avons configuré
notre bassine pour que vous puissiez faire la vôtre. Pour instancier vos bassines,
vous êtes les bienvenus sur Deliverous ;-).

Nous avons construit deux containers :

* Une bassine de base contenant `sshd` et `vim`.
* Une bassine "Déliverous", dérivant de la bassine de base, et ajoutant tout
  ce qui est nécessaire pour notre session de travail. Cette bassine est un
  exemple de spécialisation de la bassine de base, dont vous pourrez vous inspirer
  pour construire votre propre bassine.

# La bassine de base

Voici le début de notre fichier `Dockerfile`. Pour information, vous pouvez
trouver la définition complète de la bassine de base sur
[github](https://github.com/Deliverous/docker-bassine/tree/master/base).

On commence par installer les packages de base. A priori, ici, `vim` a pris le
dessus sur `emacs`...


    :::dockerfile
    FROM ubuntu:trusty

    ENV DEBIAN_FRONTEND noninteractive

    RUN apt-get update \
     && apt-get dist-upgrade -y \
     && apt-get install -y \
          vim-scripts \
          vim-syntax-docker \
          vim-syntax-go \
          build-essential \
          byobu \
          ca-certificates \
          curl \
          git \
          man \
          mercurial \
          openssh-server \
          openssl \
          time \
          vim \
          vim-addon-manager \
          vim-nox \
     && apt-get clean \
     && locale-gen en_US.UTF-8 fr_FR.UTF-8 \
     && mkdir /var/run/sshd


On créé ensuite un utilisateur, pierre, et on configure `sshd`. Comme vous le voyez,
l'utilisateur Pierre n'a pas de mot de passe. En effet, l'idée ici est de ne
s'authentifier que par clé ssh.  Les clés ssh ne sont pas connue de la bassine
de base. Il est de la responsabilité de la bassine spécifique de s'en occuper
comme nous le verrons au chapitre suivant.


    :::dockerfile
    RUN adduser --disabled-login --gecos "Pierre D'eau,,," pierre \
     && adduser pierre sudo

    ADD sshd_config /etc/ssh/sshd_config
    ADD sudoers /etc/ssh/sudoers


Nous continuons en ajoutant deux fichiers de configurations pour `git` et `vim`.
Nous ajoutons aussi un script utilitaire, qui nous permetra de configurer `git` pour
un utilisateur (nom et email de l'auteur des commits) une fois que nous serons
connetés dans le container.


    :::dockerfile
    ADD gitconfig /home/pierre/.gitconfig
    ADD vimrc /home/pierre/.vimrc
    ADD set-git-user /usr/local/bin/set-git-user


Il ne faut pas oublier de mettre les bons droits sur les différents fichiers ajoutés.


    :::dockerfile
    RUN chmod 755 /usr/local/bin/set-git-user \
     && chmod 440 /etc/sudoers \
     && chown -R pierre:pierre /home/pierre


Et on finit par lancer le service `sshd` après avoir défini son port.


    :::dockerfile
    EXPOSE 22

    CMD ["/usr/sbin/sshd", "-D"]


# La bassine deliverous

Pour notre projet deliverous, nous avons construit une bassine
[deliverous](https://github.com/Deliverous/docker-bassine/tree/master/deliverous)
dérivant de la bassine de base. Voici le début du `Dockerfile`.


    :::dockerfile
    FROM deliverous/base-bassine

    ENV GOVERSION 1.3.3
    ENV RUBYVERSION 2.1.5

    RUN apt-get update \
     && apt-get install -y qt4-dev-tools qt4-qmake \
     && apt-get clean


Puis, on install le langage `Go`


    :::dockerfile
    RUN curl -sSL https://storage.googleapis.com/golang/go$GOVERSION.linux-amd64.tar.gz  | tar -v -C /usr/local -xz


Il ne faut pas oublier de rajouter `Go` dans le path. On en profite pour rajouter le chargement de notre environnement à chaque démarrage de bash.


    :::dockerfile
    USER pierre
    RUN echo "export PATH=/usr/local/go/bin:$PATH" >> /home/pierre/.bashrc \
     && echo "[ -f ~/workspace/bin/env.sh ] && source ~/workspace/bin/env.sh" >> /home/pierre/.bashrc


Ensuite, on installe le langage `Ruby` en utilisant `rvm`


    :::dockerfile
    RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3 \
     && curl -sSL https://get.rvm.io | bash -s stable \
     && /bin/bash -l -c "rvm requirements" \
     && /bin/bash -l -c "rvm install ruby-$RUBYVERSION" \
     && /bin/bash -l -c "rvm use --default ruby-$RUBYVERSION" \
     && /bin/bash -l -c "rvm rvmrc warning ignore allGemfiles"


Comme nous utilisons `Go` et `Docker`, nous rajoutons les plugins respectifs dans `vim`


    RUN vim-addon-manager install go-syntax dockerfile



On rajoute un script qui nous permet de mettre à jour notre workspace
(rendez-vous sur
[github](https://github.com/Deliverous/docker-bassine/tree/master/deliverous)
pour en consulter le contenu)


    :::dockerfile
    USER root

    ADD get-deliverous /usr/local/bin/get-deliverous
    RUN chmod 755 /usr/local/bin/get-deliverous


On déploie les clé ssh pour l'utilisateur pierre. Ce fichier doit contenir
la clé publique de chaque utilisateur qui voudra se connecter pour
travailler dans ce container.


    :::dockerfile
    ADD authorized_keys /home/pierre/.ssh/authorized_keys
    RUN chown -R pierre:pierre /home/pierre/ \
     && chmod 600 /home/pierre/.ssh/authorized_keys


On déploie `clustergit` qui est bien pratique pour mettre à jour une
arborescence de repo git.


    :::dockerfile
    RUN git clone https://github.com/mnagel/clustergit /usr/local/src/clustergit \
     && ln -s /usr/local/src/clustergit/clustergit /usr/local/bin/clustergit


On installe [`pelican`](https://github.com/getpelican/pelican) avec ses
dépendances. C'est notre moteur de blog.


    :::dockerfile
    RUN apt-get install -y \
          libfreetype6-dev \
          libjpeg8-dev \
          liblcms2-dev \
          libtiff5-dev \
          libwebp-dev \
          python-pip \
          python-dev \
          python-tk \
          tcl8.6-dev \
          tk8.6-dev \
          zlib1g-dev \
     && pip install pelican Markdown Pillow

En phase de rédaction, pour relire avec la mise en forme final, il est possible de lancer un serveur web sur le port 8000. Nous exposons donc le port 8000 en plus du 22.

    :::dockerfile
    EXPOSE 8000 22

Pour finir, on profite des [volumes](/2015-01-26.volumes.html) pour conserver
notre workspace.


    :::dockerfile
    VOLUME ["/home/pierre/workspace"]
    CMD ["/usr/sbin/sshd", "-D"]


Et voilà, notre bassine de travail est prête à être construite.


    docker build -t deliverous/bassine .


Il ne reste plus qu'a envoyer l'image sur le registre Docker.


    docker push deliverous/bassine


Et enfin, pour déployer cette image sur notre infrastructure, nous avons besoins d'un fichier `Deliverous`


    :::text
    bassine:
      image: deliverous/bassine
      ports:
      - ip: bassine.ut7.fr
        container_port: 22
        host_port: 22
      - ip: bassine.ut7.fr
        container_port: 8000
        host_port: 8000
      volumes:
      - name: workspace
        path: /home/pierre/workspace
      hostname: bassine

---
Photo par [tetue](https://www.flickr.com/photos/romytetue/109188206)
