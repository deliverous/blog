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

    git remote add deliverous git@git.deliverous.com:monprojet.git
    git push deliverous


# Un "Pipeline"

Pour configurer les différentes étapes du déploiement il sera possible de décrire le "pipeline" par exemple : 

- construire l’application
- construire un environnement de test unitaire composé d’un container avec toutes mes briques applicatives
- jouer dans ce container la commande "toto test:unit" qui lance l’ensemble des tests unitaires
- construire un environnement de test d’intégration composé de 6 containers à l’image de la production
- jouer dans le container A de cet environnement jouer la commande "toto test:integration"
- construire un environnement contenant une copie des données de ma production et y déployer mon application

arrivé à cette étape 
