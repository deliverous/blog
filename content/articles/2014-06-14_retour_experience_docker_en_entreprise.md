Title: Retour d'expérience sur l'intégration de Docker en entreprise
Tags: docker
Author: Thomas
Summary: Après avoir regarder comment installer Docker sur des Red Hat et des CentOS, nous attaquons le domaine de l'organisation des équipes autour de Docker.
Status: draft
Icon: /images/thumbnails/fourmis__square.jpg

Imaginons une entreprise : plus de 800 millions de CA et plus de 6000 salariés.
Dans cette entreprise les gens en charge de l'intégration et de la bonne exécution des serveurs sont dans une situation difficile : mettre à jour un serveur pour les besoins d'une application représente un cout exorbitant, l'impacte sur les autres services n'est pas maitrisé et les tests impactent la production de l'entreprise. 
Pour réduire les risques et facilité la maintenance, cette entreprise a décidé de nous demander conseil.

![Cluster]({filename}/images/fourmis.png)


# Pourquoi Docker ?
 
Comment cloisonner plus d'une trentaines d'applications web répartient dans une dixaine de tomcats sur seulement quelques serveurs ? la première réponse était : virtualisation ! Migrons chaque application dans un serveur et dupliquons le pour garantir la haute disponibilité et ... dupliquons le pour monter en charge. On arrive rapidement à plusieurs dixaines de servers à maintenir sans outil de gestion de configuration centralisé comme puppet, chef ou CFEngine. Pour les financiers c'était aussi un problème, la supervision de nuit facture à l'alerte mais aussi au nombre de serveurs surveillé.
Donc nous avions deux options, monter un gestionaire de configuration de machines et le brancher sur les nouvelles machines ou monter du Docker. Les contraintes financières ont finalement tranchées, Docker avait gagné.

# Question d'organisation

Dans cette entreprise, les études s'occupent d'acheter, de développer ou de paramétrer les applications métiers et les équipes de "Run", s'occupent de les faire fonctionner.
Les études ont donc besoins de pouvoir faire tourner un grand nombre d'application en cous de paramétrage ou de développement. 
Côté production, 

# Architecture choisi

# Une politique de version

2 nouveaux exemples de containers docker pour du tomcat : 
- docker-centos-tomcatX
- docker-centos-tomcat

workflow d'utilisation :
- intégration reçois un war et des éléments de configuration
- intégration produit un container avec tout les éléments de conf pour tous les environements et son expertise (sécurité, normalisation, etc)
- intégration publie le container sur la registry avec un numéro de version
- intégration déploie le container en recette
- une fois la recette de validé par les équipe équipe de développements ou les acheteurs l'équipe de run va déployer le container en qualif 
- une fois validé en qualification l'exploitation va déployer en production

Comme chaque container est versionné le retour arrière est simplifié, il suffit de relancer l'ancien container.


