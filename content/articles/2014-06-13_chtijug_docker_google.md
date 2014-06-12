Title: Une conf�rence sur Docker et Google Cloud organis� par le ch'tijug
Tags: Docker, ch'tijug
Author: Thomas
Summary: Assur� par David Gageot et Nicolas De Loof, le ch'tijug organisait mercredi soir une conf�rence sur Docker et le Cloud Google.  C'est avec grand plaisir que j'ai suivi cette session. 
Status: draft
Icon: /images/thumbnails/logojug__square.jpg


Assur� par David Gageot et Nicolas De Loof, le ch'tijug organisait mercredi soir une conf�rence sur Docker et Google Cloud.  
C'est avec grand plaisir que j'ai suivi cette session. 

![Survol]({filename}/images/logojug.jpg)

David Gageot avait r�sum� le sujet de cette fa�on : 
On parle beaucoup de Docker en ce moment. Je vais tenter de vous expliquer comment fonctionne Docker comme j'aurais aim� que l'on me l'explique. Nous allons apprendre � prendre en main Docker pour packager une application web Java 8.

Et effectivement, c'�tait simple avec une forte vision d�veloppeur et plein d'humour.

# Des apprentissages
De nombreux apprentissage �taient � la cl�. Le premier et non des moindre � de quoi rassurer sur la maturit� des containers. 
Les Cgroups sont arriv�s dans le noyau Linux suite aux travaux de 2006 de Paul Menage et Rohit Seth, 2 ing�nieur de Google.
Et aujourd'hui Google utilise plus de 2 milliard de containers.

La p�dagogie �tait elle aussi au rendez-vous, en quelques slides ils ont su nous montrer les avantages de performance face � la virtualisation. 

Une autre d�couverte, boot2docker qui permet de simplifier grandement l'usage de docker sur le poste de d�veloppement. 
Imaginez une machine virtuelle de 27Mo qui boot en 5s sur laquelle vous pouvez cr�er autant de container docker que vous voulez. Avec un r�pertoire partag� pour continuer � travailler avec votre IDE pr�f�r�.

La Dockercon s'�tant d�roul� les 9 et 10, c'�tait le moment id�al pour relayer un certain nombre d'annonces parmi lesquelles :
* cAdvisor un outils pour faire des statiques sur les containers
* Kunerbetes un outils de sch�duling de container Docker
* la nomination de �ric Brewer (VP of Google Infrastructure) au comit� de gouvernace Docker
* libchan, libswarm et libcontainer 3 biblioth�ques pour facilit� la coop�ration entre les containers
* et la version 1.0 de Docker fraichement arriv� lundi.
https://twitter.com/DockerCon 

# Des �changes

La communaut� java du nord n'�tant pas si grande que �a, c'�tait l'occasion de revoir un certain nombre de gens que j'appr�cie. L'occasion aussi de parler de notre projet Deliverous et de son avancement.

Parmi toutes ces personnes 2 �changes notable, avec un impacte direct sur notre mod�le �conomique. 
Certains de nos clients sont des d�veloppeurs d'ind�pendants qui font du site web avec des technologie innovantes (nodejs, rails, play, etc.) et ils cherchent un h�bergement simple pour d�ployer 1 ou 2 containers par site. La bonne nouvelle c'est que nous savons d�j� r�pondre � ce genre de demandes.
A l'oppos� de ces clients, il y a de grosses entreprises qui cherchent � s'approprier ce genre de technologie. Pour eux, nous pouvons intervenir pour les aider � monter leur propre plateforme Docker, pour les aider � maitriser l'outil depuis les �quipes de d�veloppements jusqu'� l'exploitation.

# Futur de Docker

M�me s'il est difficile de pr�dire le futur de Docker, deux indices nous poussent � dire que la technologie ne sera pas abandonn� dans quelques mois. 
Le premier c'est l'engouement de certains acteurs comme Google, Coudbees, Red Hat, Rackspace, Amazon, Facebook et bien d'autres. 
L'autre indice c'est l'organisation m�me du projet, un projet libre avec un comit� de gouvernance totalement ind�pendant de l'�diteur de Docker.

