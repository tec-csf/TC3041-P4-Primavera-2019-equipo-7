from time import sleep
import datetime
from influxdb import InfluxDBClient
import numpy as np
import random

#Conexión con la base de datos
client = InfluxDBClient('localhost', 8086, 'root', 'root', 'sensores_casa')

#Creación de una base de datos
client.create_database('sensores_casa')

#Generar información
#Para la serie de temperatura externa usamos como referencia
#el rango de temperaturas en CDMX en abril 7.8 - 27.2 grados centigrados
#https://es.climate-data.org/america-del-norte/mexico/distrito-federal/ciudad-de-mexico-1093/

minTemp = 7.8
maxTemp = 27.2
for i in range(5000000):
    random1 = round(random.uniform(minTemp,maxTemp+1),2)
    random2 = random1 - round(random.uniform(1,7),2)
    temperaturas = [{'measurement': 'temperatura',
                   'tags':{'ubicacion':'fuera'},
                   'time':datetime.datetime.utcnow().isoformat(),
                   'fields': {'gradosCentigrados':random1}},
                   {'measurement': 'temperatura',
                   'tags':{'ubicacion':'dentro'},
                   'time':datetime.datetime.utcnow().isoformat(),
                   'fields': {'gradosCentigrados':random2}}]
    client.write_points(temperaturas)
print("Serie de temperatura completa")

#Para la serie de humedad usamos como referencia
#el promedio de humedad en CDMX en abril 43%, con 
#esta información decidimos usar un rango 33$ a 53%
#https://www.weather-mx.com/es/mexico/ciudad-de-mexico-clima
minHumedad = 33
maxHumedad = 53
for i in range(5000000):
    humedadFuera = round(random.uniform(minHumedad,maxHumedad+1),2)
    humedadDentro = humedadFuera - round(random.uniform(20,25),2)
    humedadArr = [{'measurement': 'humedad',
                  'tags':{'ubicacion':'fuera'},
                  'time':datetime.datetime.utcnow().isoformat(),
                  'fields': {'porcentajeHumedad':humedadFuera}},
                  {'measurement': 'humedad',
                  'tags':{'ubicacion':'dentro'},
                  'time':datetime.datetime.utcnow().isoformat(),
                  'fields': {'porcentajeHumedad':humedadDentro}}]
    client.write_points(humedadArr)
print("Serie de humedad completa")

#Para la serie de índice UV usamos como referencia
#el promedio del índice UV en CDMX en abril. El índice es de 12
# nosotros establecimos un rango de 7 a 17
#https://www.weather-mx.com/es/mexico/ciudad-de-mexico-clima
minUV = 7
maxUV = 17
for i in range(5000000):
    indiceUV = random.randint(minUV,maxUV+1)
    humedadObj = [{'measurement': 'rayosUV',
                   'tags':{'ciudad':'CDMX'},
                   'time':datetime.datetime.utcnow().isoformat(),
                   'fields': {'IndiceUV':indiceUV}}]
    client.write_points(humedadObj)
print("Serie de índice UV completa")