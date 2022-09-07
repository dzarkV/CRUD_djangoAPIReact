# CRUD_djangoAPIReact_be
Este es un servicio CRUD para obtener información de compañias. 

* Django como framework de Python
* MongoDB para base de datos
* Docker para empaquetar, deplegar y correr aplicación de Django CRUD.
* Azure Web Service para despliegue

## Modelo

Es un modelo sencillo para obtener información de una compañia a partir de:

* Nombre
* Dirección
* Identificación
* Número de telefono

Puedes tipear:

1) en el directoroi "backend"
   
`docker built -t crud_backend_django`

2) O puedes optar por usar `docer-compose` con el servicio de frontend [aqui](https://github.com/dzarkV/CRUD_djangoAPIReact_fe).
   
`docker-compose up --build`

El servicio de frontend en React fue reorganizado a partir de [este](https://github.com/doremifasollasi/Dockerizing_reactCRUD_djangoAPI/tree/master/frontend)
