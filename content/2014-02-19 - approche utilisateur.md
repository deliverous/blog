Title: Approche utilisateur
Date: 2014-02-19 18:00
Category: Articles
Tags: utilisateur
Slug: 2014-02-19-approche-utilisateur
Author: Thomas
Summary: Après avoir recueilli l'avis de beaucoup de personne voici comment nous imaginons l'usage de deliverous
Status: draft

La compilation fut longue, plusieurs mois pour interroger patiemment de très nombreuses personnes. Le résultat est là voici ce que nous imaginons, à vous de nous dire si nous vous avons correctement compris.


# Rapide et simple

Après avoir créé un compte sur la plateforme deliverous.com, l'utilisateur va pouvoir ajouter un nouveau remote dans sa copie locale de travail. Un simple git push vers ce nouveau dépôt de code déclenchera la chaîne de déploiement continu.

Par exemple : 

`
git remote add deliverous git@git.deliverous.com:monprojet.git
git push deliverous
`


# Des "pipeline"

Déployer un logiciel c'est dérouler automatiquement un ensemble d'étapes. Celà
permet par exemple de passer du dépot de code au logiciel déployé et
utilisable. Ces étapes seront décrites dans un "pipeline". Chaque utilisateur
est libre de décrire autant de pipeline que souhaité. Le pipeline par défaut
permet de déployer en production. 

Voici par exemple un pipeline préproduction :

- construire l’application
- construire un environnement de test unitaire composé d’un container avec toutes mes briques applicatives
- jouer dans ce container la commande `toto test:unit` qui lance l’ensemble des tests unitaires
- construire un environnement de test d’intégration composé de 6 containers à l’image de la production
- jouer dans le container A de cet environnement jouer la commande `toto test:integration`
- construire un environnement contenant une copie des données de ma production et y déployer mon application

arrivé à cette étape votre application est disponible et utilisable dans un environement de préproduction.

Pour passer de la préproduction à la production il faudra déclencher le pipeline prodcution. 

# Déclancheurs

Il sera possible de déclancher des pipelines de deux façons différentes : 

- un hook sur le dépot de code
- une action manuelle

de cette façon nous pensons pouvoir couvrir tous les cas d'usages.

