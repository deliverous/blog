
Retour d'expérience de l'intégration de Docker dans une grosse entreprise : 810 millions de CA avec plus de 6000 salariés.

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

