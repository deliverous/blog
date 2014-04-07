Title: Pourquoi devenons nous hébergeur docker ?
Tags: docker, cloud
Author: Thomas
Summary: Pour la mise en place de notre solution de déploiement continu nous avons commencé à étudier tout un ensemble d'outils pour assurer l'hébergement dans le nuage des différents applications à déployer. Nos recherches ne nous ayant rien apporté de concluant nous avons décidé de devenir notre propre hébergeur. Explications ... 
Status: draft
Icon: /images/thumbnails/ontainer__square.jpg

Héberger votre chaine de déploiement continu implique d'avoir à notre disposition un hébergeur disposant d'une API de haut niveau pour déployer chaque application, que ce soit pour nos applications ou les vôtres.

Nous imaginions une api capable de prendre en charge des applications au sens [12 factor apps](http://12factor.net/), que l'on puisse dire voici une application, elle écoute sur le port 80, ou la charge va fortement augmenter, il nous faut 7 instances. Faire tout ça très simplement.

![Survol]({filename}/images/container.jpg)

# Pour nous le nuage c'est quoi ?

Cloud, un mot très à la mode pour décrire ce que d'autres appel les services hébergés. Ce mot valise illustre pourtant un réel changement de consommation de l'informatique. 
Il était une époque ou chaque entreprise entretenait sa propre source d'énergie, une machine à vapeur, une génératrice électrique, etc. Aujourd'hui toutes les entreprises ou presque utilisent l'électricité. Elles ne se posent même pas la question du courant continu ou alternatif. Nous pensons que de la même façon, demain le logiciel informatique sera une commodité comme l'eau courante ou l'électricité aujourd'hui, l'informatique à la demande, voilà l'avenir.

Dans ce cadre, nous imaginons qu'un hébergeur soit capable de répondre aux besoins suivants : 
- déclarer une application
- configurer une application (déclarer les ressources)
- lancer une application
- changer le nombre d'instances de l'application

Et tout ça sans avoir à se soucier des pannes matériel, des mises à jours de sécurité, du réseau ou des communications entre centre de données.

# Pourquoi docker ?

L'expérience aidant, un certain nombre de contraintes sur la façon de construire et de déployer des applications nous semblaient évidentes ... Mais près avoir lut [12 factor apps](http://12factor.net/), plus de doute possible, une fois construite, une application doit embarquer l'ensemble de ses dépendances y compris système. Pour adapter une application à son environnent, il suffit de définir quelques variables d'environnements. Ce qui nous rapproche fortement du concept d'appliance. En effet pour embarquer toutes ses dépendances, une application doit être construite avec le système d'exploitation qui permet de la faire fonctionner.

Avec docker le concept d'appliance est sublimé, il n'y a quasiment pas de surcout lié à la virtualisation et il n'est plus utile de maintenir le système d'exploitation, en effet à chaque reconstruction la couche système est elle aussi mise à jour.

Le slogan de docker résonne en nous comme une vérité : 
"Build once ... run anywhere" Ce que l'on peut traduire par "Construire une fois ... Lancé n'importe où". Le sous titre est plus explicite : "Le même container que le développeur construit et test sur son PC, peut tourner et passer à l'échelle en production".

Voilà une devise qui rime avec deliverous, en effet, une fois construite l'application doit pouvoir être tester éprouver dans de nombreux contexte avant de passer en production. Elle doit pouvoir suivre son pipeline de mise en production sans risquer la remise en cause des tests.

Voilà pourquoi nous avons choisis docker comme unique format de container d'application.

# Une histoire de cargo.

Une fois docker sélectionné comme unique format de container, nous avons cherché un hébergeur en Europe capable de faire tourner nos container. Pour garder l'analogie avec les containers de marchandise, nous avons cherché un porte-conteneurs universel respectant nos valeurs... Seulement dans le fret les "UCC" (Universal Container Carrier) se sont généralisés à partir des années 70, alors que dans l'informatique le format universel de container est loin d'être normalisé ... 
Difficile dans ces conditions de trouver un hébergeur qui nous garantisse à la fois une bonne connectivité à internet, la sécurité des données et la protection de la vie privée des clients. Vous avez en effet été nombreux à nous parler de l'affaire Prism et de ses conséquences sur la confiance de vos clients. Nous avons donc cherché un hébergeur docker en Europe, pas un hébergeur avec des bureau en Europe et un siège social soumis à "patriot-act" mais une société européenne qui n'utiliserait aucune brique venue des États-Unis (ni [amazon EC2](https://aws.amazon.com/ec2/), ni [digital ocean](https://www.digitalocean.com/), ...). 
Et nous n'avons rien trouvé, certains sont capables de monter en charge rapidement mais ils ne garantissent pas le respect de la vie privé. D'autres sont européens mais ne sont pas correctement connecté à internet. 
Nous avons donc décidé de monter notre propre plate-forme docker. 

# Conclusion

Nous avons besoins d'un hébergeur docker qui respecte nos contraintes mais peut-être que vous aussi ... Nous avons donc décidé de travailler avec vous pour ouvrir notre solution de cloud docker à la vente. Rendez-vous sur le site de [deliverous](http://deliverous.com/docker) pour participer à l'aventure.

---
Photo par [Kristi](https://www.flickr.com/photos/kristi_decourcy/9154543163)
