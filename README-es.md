# Proyecto Docker Compose - Grafana-Prometheus-Mongo-Postgres-Django-SpringBoot


Este proyecto utiliza Docker Compose para configurar y ejecutar un conjunto de servicios interdependientes, incluyendo aplicaciones basadas en Django, Spring Boot, bases de datos PostgreSQL y MongoDB, y herramientas de monitoreo como Prometheus y Grafana.

## Servicios

### Servicios Definidos

- **Grafana**
  - **Imagen:** `grafana/grafana`
  - **Puerto:** `3000:3000`
  - **Descripción:** Herramienta de visualización y monitoreo.
  
- **Prometheus**
  - **Imagen:** `prom/prometheus`
  - **Puerto:** `9090:9090`
  - **Descripción:** Sistema de monitoreo y alertas.
  - **Configuración:** Se monta un archivo de configuración `prometheus.yml` desde el host.
  
- **Postgres Exporter**
  - **Imagen:** `prometheuscommunity/postgres-exporter`
  - **Puerto:** `9187:9187`
  - **Descripción:** Exportador para métricas de PostgreSQL.
  
- **Mongo Exporter**
  - **Imagen:** `ssheehy/mongodb-exporter:latest`
  - **Puerto:** `9216:9216`
  - **Descripción:** Exportador para métricas de MongoDB.
  
- **PostgreSQL**
  - **Imagen:** `postgres:latest`
  - **Puerto:** `5433:5432`
  - **Descripción:** Base de datos PostgreSQL.
  
- **Django App**
  - **Construcción:** Desde el directorio `./Django_Rest`
  - **Puerto:** `8000:8000`
  - **Descripción:** Aplicación web basada en Django.
  
- **MongoDB**
  - **Imagen:** `mongo:latest`
  - **Puerto:** `27020:27017`
  - **Descripción:** Base de datos MongoDB.
  
- **Spring Boot App**
  - **Construcción:** Desde el directorio `./SpringBoot`
  - **Puerto:** `8082:8082`
  - **Descripción:** Aplicación basada en Spring Boot.
  
- **Eureka Server**
  - **Construcción:** Desde el directorio `./Eureka`
  - **Puerto:** `8761:8761`
  - **Descripción:** Servidor de descubrimiento Eureka.
  
- **Spring Cloud Gateway**
  - **Construcción:** Desde el directorio `./Gateway`
  - **Puerto:** `8081:8080`
  - **Descripción:** Puerta de enlace API de Spring Cloud.

## Requisitos Previos

- [Docker](https://www.docker.com/get-started) instalado.
- [Docker Compose](https://docs.docker.com/compose/install/) instalado.

## Configuración

1. **Archivos de Entorno**

   Crea un archivo `.env` en el directorio raíz del proyecto con las siguientes variables:

   ```env
   POSTGRES_DB=tu_basedatos
   POSTGRES_USER=tu_usuario
   POSTGRES_PASSWORD=tu_contraseña
   ```

2. **Configuración de Prometheus**

   Asegúrate de que el archivo `prometheus.yml` en el directorio raíz del proyecto esté configurado correctamente según tus necesidades de monitoreo.

## Uso

Para iniciar todos los servicios definidos en el `docker-compose.yml`, ejecuta el siguiente comando en el directorio raíz del proyecto:

```sh
docker-compose up
```

Para iniciar los servicios en segundo plano, usa:

```sh
docker-compose up -d
```

Para detener y eliminar todos los contenedores, redes y volúmenes creados, usa:

```sh
docker-compose down
```

## Acceso

- **Grafana:** [http://localhost:3000](http://localhost:3000)  
  Usuario: `admin`  
  Contraseña: `admin`

- **Prometheus:** [http://localhost:9090](http://localhost:9090)

- **Django App:** [http://localhost:8000](http://localhost:8000)

- **Spring Boot App:** [http://localhost:8082](http://localhost:8082)

- **Spring Cloud Gateway:** [http://localhost:8081](http://localhost:8081)

- **Eureka Server:** [http://localhost:8761](http://localhost:8761)

## Notas

- El contenedor de Django está configurado para ejecutar migraciones y recopilar archivos estáticos al iniciar.
- El contenedor de Spring Boot está configurado para ejecutarse con Java 17.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

