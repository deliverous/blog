Title: Approche utilisateur
Category: Articles
Tags: utilisateur
Author: Thomas
Summary: Après avoir recueilli l'avis de beaucoup de personnes voici comment nous imaginons l'usage de deliverous
Status: published

La compilation fut longue, plusieurs mois pour interroger patiemment de très nombreuses personnes. Le résultat est là voici ce que nous imaginons, à vous de nous dire si nous vous avons correctement compris.


# Rapide et simple

Après avoir créé un compte sur la plateforme deliverous.com, l'utilisateur va pouvoir ajouter un nouveau remote dans sa copie locale de travail. Un simple git push vers ce nouveau dépôt de code déclenchera la chaîne de déploiement continu.

Par exemple : 

    git remote add deliverous git@git.deliverous.com:monprojet.git
    git push deliverous

Toute la configuration se fait à travers des fichiers textes commités dans le dépôt.

# Des "pipelines"

Déployer un logiciel c'est dérouler automatiquement un ensemble d'étapes. Cela
permet par exemple de passer du dépôt de code au logiciel déployé et
utilisable. Ces étapes seront décrites dans un "pipeline". Chaque utilisateur
est libre de décrire autant de pipelines que souhaité. Le pipeline par défaut
permet de déployer en production. 

Voici par exemple un pipeline préproduction :

- construire l’application
- construire un environnement de test unitaire composé d’un container avec toutes mes briques applicatives
- jouer dans ce container la commande `toto test:unit` qui lance l’ensemble des tests unitaires
- construire un environnement de test d’intégration composé de 6 containers à l’image de la production
- jouer dans le container A de cet environnement jouer la commande `toto test:integration`
- construire un environnement contenant une copie des données de ma production et y déployer mon application

Quand vous arrivez à cette étape, votre application est disponible et utilisable dans un environnement de préproduction.

Pour passer de la préproduction à la production il faudra déclencher le pipeline production. 

# Déclencheurs

Il sera possible de déclencher des pipelines de deux façons différentes : 

- un hook sur le dépôt de code
- une action manuelle

de cette façon nous couvrons tous les cas d'usages.

# Pour continuer

Le sujet vous intéresse, abonnez-vous à la [mailing liste](http://ml.deliverous.com/mailman/listinfo/deliverous)

