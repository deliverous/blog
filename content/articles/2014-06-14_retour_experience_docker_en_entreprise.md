
Retour d'exp�rience de l'int�gration de Docker dans une grosse entreprise : 810 millions de CA avec plus de 6000 salari�s.

2 nouveaux exemples de containers docker pour du tomcat : 
- docker-centos-tomcatX
- docker-centos-tomcat

workflow d'utilisation :
- int�gration re�ois un war et des �l�ments de configuration
- int�gration produit un container avec tout les �l�ments de conf pour tous les environements et son expertise (s�curit�, normalisation, etc)
- int�gration publie le container sur la registry avec un num�ro de version
- int�gration d�ploie le container en recette
- une fois la recette de valid� par les �quipe �quipe de d�veloppements ou les acheteurs l'�quipe de run va d�ployer le container en qualif 
- une fois valid� en qualification l'exploitation va d�ployer en production

Comme chaque container est versionn� le retour arri�re est simplifi�, il suffit de relancer l'ancien container.

