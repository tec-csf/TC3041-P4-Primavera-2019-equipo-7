# Iniciar un contenedor con InfluxDB
docker run --name practica4 -p 8086:8086 -d -v /var/lib/influxdb influxdb

#iniciar un contenedor para conectarse a grafana
docker run --name grafana -p 3000:3000 -v grafana:/var/lib/grafana --link practica4 grafana/grafana:3.1.1