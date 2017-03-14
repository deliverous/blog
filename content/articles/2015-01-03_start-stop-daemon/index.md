---
title: start-stop-daemon et Docker
tags:
  - docker
  - debian
  - tomcat
  - start-stop-daemon
authors:
  - Thomas Clavier
description: Pourquoi tomcat7 démarre très bien dans une debian fraichement installé et pas dans un conteneur Docker ?
date: 2015-01-03
publishdate: 2015-01-03
aliases: /2015-01-03.start-stop-daemon.html
---

Toute l'histoire a commencé par la nécessité de faire un conteneur Docker pour un Tomcat 7 basé sur une debian.

# Le problème

La construction d'un conteneur tomcat sur base de debian semble pourtant trivial :

    from deliverous/wheezy
    run apt-get update && \
        apt-get install -y --no-install-recommends openjdk-7-jdk tomcat7 && \
        apt-get clean
    expose 8080
    cmd /etc/init.d/tomcat7 start; tail -f /var/log/tomcat7/*

Seulement avec ce Dockerfile impossible de lancer tomcat. En étudiant le problème on s'apperçoit que le script d'init lance un "start-stop-daemon --test" qui tombe en erreur. Pourtant un ps nous montre un processus java qui fonctionne et netstat nous indique que le port 8080 est occupé par ce même processus java.

Pourquoi start-stop-daemon considère que tomcat n'est pas correctement démarré ?

# Un manque de droits

En lisant le [code de start-stop-daemon](http://anonscm.debian.org/cgit/dpkg/dpkg.git/tree/utils/start-stop-daemon.c) on voit que si les options --test et --exec sont utilisés sous GNU/Linux alors start-stop-daemon va lire le lien /proc/%d/exec pour vérifier que c'est bien le même que l'argument --exec.
Or pour avoir le droit de lire ce lien il faut les droits SYS_PTRACE, droits qui ont été supprimés de Docker en version 1.0.1 (cf [bug 6607](https://github.com/docker/docker/issues/6607)). Alors comment faire pour faire fontionner mon conteneur ? Surtout que la fonctionnalité --test de start-stop-daemon n'est pas utilisé que par tomcat7.

La première idée c'est de lancer le conteneur avec les bons droits :

    docker run --cap-add SYS_PTRACE -p 8080:8080 tomcat

Et effectivement tout fonctionne parfaitement. Seulement comment faire pour lancer ce conteneur sur Deliverous ? Et sur les autres plate-forme d'hébergement Docker ?

La seconde idée c'est de maintenir un nouveau script de boot ... seulement maintenir un script c'est du travail, faut s'adapter aux changements de la distribution, prendre en compte les mises à jours de Tomcat et suivre les failles de sécurités. Ce n'est donc pas forcément une bonne idée.

# La solution

Après la lecture du code de start-stop-daemon et de [cet article](https://chris-lamb.co.uk/posts/start-stop-daemon-exec-vs-startas) la solution était évidente, le comportement de start-stop-daemon n'est pas le même si l'on utilise l'option --startas. Il faut donc changer tous les appels en "--test --exec" par des "--test --startas" dans le script d'init. La maintenance est bien plus simple, c'est en effet un simple patch à appliquer à la construction du conteneur. C'est automatique et sauf gros changement, patch s'occupe tout seul de fusionner le travail des mainteneurs avec le miens.

Le script d'init de tomcat n'utilise que 4 fois la commande start-stop-daemon avec --test et --exec, le remplacement est simple et le patch très léger.

```
--- tomcat7.org 2014-02-22 22:42:27.000000000 +0100
+++ tomcat7 2014-12-31 11:05:46.000000000 +0100
@@ -195,7 +195,7 @@

  log_daemon_msg "Starting $DESC" "$NAME"
  if start-stop-daemon --test --start --pidfile "$CATALINA_PID" \
-   --user $TOMCAT7_USER --exec "$JAVA_HOME/bin/java" \
+   --user $TOMCAT7_USER --startas "$JAVA_HOME/bin/java" \
    >/dev/null; then

    # Regenerate POLICY_CACHE file
@@ -217,7 +217,7 @@
    catalina_sh start $SECURITY
    sleep 5
          if start-stop-daemon --test --start --pidfile "$CATALINA_PID" \
-     --user $TOMCAT7_USER --exec "$JAVA_HOME/bin/java" \
+     --user $TOMCAT7_USER --startas "$JAVA_HOME/bin/java" \
      >/dev/null; then
      if [ -f "$CATALINA_PID" ]; then
        rm -f "$CATALINA_PID"
@@ -257,7 +257,7 @@
    status)
  set +e
  start-stop-daemon --test --start --pidfile "$CATALINA_PID" \
-   --user $TOMCAT7_USER --exec "$JAVA_HOME/bin/java" \
+   --user $TOMCAT7_USER --startas "$JAVA_HOME/bin/java" \
    >/dev/null 2>&1
  if [ "$?" = "0" ]; then

@@ -282,7 +282,7 @@
  ;;
   try-restart)
         if start-stop-daemon --test --start --pidfile "$CATALINA_PID" \
-   --user $TOMCAT7_USER --exec "$JAVA_HOME/bin/java" \
+   --user $TOMCAT7_USER --startas "$JAVA_HOME/bin/java" \
    >/dev/null; then
    $0 start
  fi

```

Bilan, voilà une solution simple et maintenable pour contourner un conflit de sécurité entre Debian et Docker. Pour appeler le patch dans le Dockerfile j'ai ajouté les lignes suivantes :

```
add tomcat7.patch /tmp/
run apt-get update && \
    apt-get install -y --no-install-recommends patch && \
    patch /etc/init.d/tomcat7 < /tmp/tomcat7.patch && \
    rm -f /tmp/tomcat7.patch && \
    apt-get remove --purge -y patch && \
    apt-get clean
```

Si vous préférez utiliser directement mon conteneur [tclavier/tomcat](https://registry.hub.docker.com/u/tclavier/tomcat/) vous pouvez le trouver sur le hub Docker.

---
Photo par [Brian K YYZ](https://www.flickr.com/photos/bk_/5109620862)
