Title: Une conférence sur Docker et Google Cloud organisé par le ch'tijug
Tags: Docker, ch'tijug
Author: Thomas
Summary: Assuré par David Gageot et Nicolas De Loof, le ch'tijug organisait mercredi soir une conférence sur Docker et le Cloud Google.  C'est avec grand plaisir que j'ai suivi cette session. 
Status: draft
Icon: /images/thumbnails/logojug__square.jpg


Assuré par David Gageot et Nicolas De Loof, le ch'tijug organisait mercredi soir une conférence sur Docker et Google Cloud.  
C'est avec grand plaisir que j'ai suivi cette session. 

![Survol]({filename}/images/logojug.jpg)

David Gageot avait résumé le sujet de cette façon : 
On parle beaucoup de Docker en ce moment. Je vais tenter de vous expliquer comment fonctionne Docker comme j'aurais aimé que l'on me l'explique. Nous allons apprendre à prendre en main Docker pour packager une application web Java 8.

Et effectivement, c'était simple avec une forte vision développeur et plein d'humour.

# Des apprentissages
De nombreux apprentissage étaient à la clé. Le premier et non des moindre à de quoi rassurer sur la maturité des containers. 
Les Cgroups sont arrivés dans le noyau Linux suite aux travaux de 2006 de Paul Menage et Rohit Seth, 2 ingénieur de Google.
Et aujourd'hui Google utilise plus de 2 milliard de containers.

La pédagogie était elle aussi au rendez-vous, en quelques slides ils ont su nous montrer les avantages de performance face à la virtualisation. 

Une autre découverte, boot2docker qui permet de simplifier grandement l'usage de docker sur le poste de développement. 
Imaginez une machine virtuelle de 27Mo qui boot en 5s sur laquelle vous pouvez créer autant de container docker que vous voulez. Avec un répertoire partagé pour continuer à travailler avec votre IDE préféré.

La Dockercon s'étant déroulé les 9 et 10, c'était le moment idéal pour relayer un certain nombre d'annonces parmi lesquelles :
* cAdvisor un outils pour faire des statiques sur les containers
* Kunerbetes un outils de schéduling de container Docker
* la nomination de Éric Brewer (VP of Google Infrastructure) au comité de gouvernace Docker
* libchan, libswarm et libcontainer 3 bibliothèques pour facilité la coopération entre les containers
* et la version 1.0 de Docker fraichement arrivé lundi.
https://twitter.com/DockerCon 

# Des échanges

La communauté java du nord n'étant pas si grande que ça, c'était l'occasion de revoir un certain nombre de gens que j'apprécie. L'occasion aussi de parler de notre projet Deliverous et de son avancement.

Parmi toutes ces personnes 2 échanges notable, avec un impacte direct sur notre modèle économique. 
Certains de nos clients sont des développeurs d'indépendants qui font du site web avec des technologie innovantes (nodejs, rails, play, etc.) et ils cherchent un hébergement simple pour déployer 1 ou 2 containers par site. La bonne nouvelle c'est que nous savons déjà répondre à ce genre de demandes.
A l'opposé de ces clients, il y a de grosses entreprises qui cherchent à s'approprier ce genre de technologie. Pour eux, nous pouvons intervenir pour les aider à monter leur propre plateforme Docker, pour les aider à maitriser l'outil depuis les équipes de développements jusqu'à l'exploitation.

# Futur de Docker

Même s'il est difficile de prédire le futur de Docker, deux indices nous poussent à dire que la technologie ne sera pas abandonné dans quelques mois. 
Le premier c'est l'engouement de certains acteurs comme Google, Coudbees, Red Hat, Rackspace, Amazon, Facebook et bien d'autres. 
L'autre indice c'est l'organisation même du projet, un projet libre avec un comité de gouvernance totalement indépendant de l'éditeur de Docker.

