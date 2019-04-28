# TC3041-P4-Primavera-2019

## Problema
Existen diversos sensores comerciales que permiten recopilar información sobre el clima; sin embargo, la información no está centralizada y no se puede visualizar desde una sola aplicación. En este caso, nuestro equipo diseño una base de datos que permite almacenar la información recopilada de los diferentes dispositivos, así como un dashboard que permite visualizar la información de los diferentes sensores a lo largo del tiempo.
Para poder desarrollar el proyecto se empleó Docker, Python, InfluxDB y Grafana.

## Descripción de la base de datos
1. Series:
   - Temperatura, se mide en ᵒC
   -	Humedad relativa, se mide en %H
   -	Rayos UV, se mide con el índice UV
2. Etiquetas: 
   -	Ubicación: Para sensores de humedad y temperatura, dentro y fuera de la casa
   -	Ciudad: Consideramos un sensor de rayos UV, empleamos la etiqueta de ciudad para identificar dónde se encuentra.
3. Valores: Nuestra aplicación genera valores aleatorios basándose en el promedio de temperatura, humedad e índice UV de la ciudad de México. La temperatura y humedad usan números con punto decimal mientras que el índice UV emplea números enteros.

## Archivos
- datos.py: Incluye el código usado para generar y poblar la base de datos.
- dashboard.png: Muestra el dashboard generado en grafana.
- datasource.jpg: Muestra cómo se creó el Data Source en grafana.
- contenedores.js: Incluye los comandos necesarios para crear los contenedores de grafana e influxDB.

## Grafana
Para usar a grafana con la base de datos se debe acceder a la liga [http://localhost:3000/](http://localhost:3000/)
Usuario: admin Contraseña: admin.
Para conectarse a la base de datos, se debe crear un nuevo Data Source (ejemplo en datasource.jpg).
