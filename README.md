# FastAPI sur AWS EC2 utilisant une base de données RDS PostgreSQL
 
## Objectif

L'objectif de ce projet est d'utiliser plusieurs services AWS afin d'établir une API sur une VM EC2 ainsi qu'une base de données PostgreSQL sur RDS. Il faut donc pouvoir ouvrir l'accès de la base de données à la VM et ouvir les ports nécessaires pour accéder à l'API depuis n'importe où.

## RDS
J'ai créé une base ```PostgreSQL``` sur une instance ```db.t2.micro```. 

J'ai du ajouter une autorisation d'accès sur le port ```5432``` afin que la VM EC2 puisse y accéder.

J'ai ensuite inséré le fichier SQL dans la base en utilisant une commande psql en CLI.

## EC2

J'ai utilisé la version gratuite de EC2 qui propose une VM ```Ubuntu 20.04``` sur une instance ```t2.micro```.

Je m'y suis connecté avec VS Code en SSH afin de pouvoir modifier les fichiers dans la VM et accéder au terminal.

### Docker

Afin de faciliter le déploiement de l'API j'ai créé un docker-compose qui crée l'environement python et lance le script ```FastAPI```

### API

Nous pouvons accéder à l'API via l'url [35.180.191.25:8080](http://35.180.191.25:8080)

On a 2 endpoint qui nous permettent d'obtenir les informations d'une réservation à partir de son ID et l'autre qui permet d'avoir toutes les réservations d'une personne à l'aide du nom.

- [/booking_by_id/4040](http://35.180.191.25:8080/booking_by_id/4040)

![id](/resources/id.png)

- [/bookings_by_name?firstname=Florence&surname=Bader](http://35.180.191.25:8080/bookings_by_name?firstname=Florence&surname=Bader)

![name](/resources/name.png)
