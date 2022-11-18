# Prueba Técnica

Aquí en este repositorio se encuentra el punto número 15 de la prueba y la API REST

Además, aquí se tiene en cuenta que el usiario no comete errores

## Punto 15

Para este punto ya se tiene la estructura, tal cual está en el archivo de word
solo es ejecutar el programa y este ya le saca los resultados, 

Librerias Principales:
* No se contempló ninguna para este punto

Estructura:
```
.
├── README.md
├── api
   └── main.py
```

* main.py - Es el archivo que resuelve el punto 15

### Ejecución 

1. Iniciar ejecutando: python punto15\main.py

RESPONSE
```json
70
49
84
```

## API REST

Librerias Principales:
1. Flask - Para hacer la API REST
2. Flask-SQLAlchemy - Para el modelo ORM de la base de datos

Estructura:
```
.
├── README.md
├── api
│   ├── instance
│   │   └── tree.db
│   ├── __init__.py
│   ├── init_app.py
│   ├── models.py
│   ├── routes.py
│   └── wsgi.py
├── requirements.txt
```

* instance - Contiene la base de datos que se crea tree.db
* api - Contiene toda la API REST
* init_app.py - Inicial la instancia de Flask
* models.py - Contiene los modelos ORM
* routes.py - Las rutas de la API REST
* wsgi.py - Este inicia el servicio API REST

## Ejecución 

1. Clonar repositorio.
2. pip install requirements.txt
4. Iniciar servidor ejecutando: python src\wsgi.py

### Uso
#### Crear un Arbol

POST http://127.0.0.1:5000/api/create/tree

REQUEST
```json
{
  "root":70,
  "tree":[
    {"node":84, "parent":70},
    {"node":85, "parent":84},
    {"node":78, "parent":84},
    {"node":80, "parent":78},
    {"node":76, "parent":78},
    {"node":49, "parent":70},
    {"node":54, "parent":49},
    {"node":51, "parent":54},
    {"node":37, "parent":49},
    {"node":40, "parent":37},
    {"node":22, "parent":37}
  ]
}
```
RESPONSE
```json
{
  "created":"successfully"
}
```

#### Con dos nodos mostrar el antecesor más cercano

REQUEST

GET http://127.0.0.1:5000/api/tree/ancester?node1=51%node2=37


RESPONSE
```json
{
  "ancestor": 49,
  "node1": 51,
  "node2": 37
}
```
