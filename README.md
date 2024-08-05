# Docker Compose Project - Grafana-Prometheus-Mongo-Postgres-Django-SpringBoot

This project uses Docker Compose to configure and run a set of interdependent services, including Django-based applications, Spring Boot, PostgreSQL and MongoDB databases, and monitoring tools like Prometheus and Grafana.

## Services

### Defined Services

- **Grafana**
  - **Image:** `grafana/grafana`
  - **Port:** `3000:3000`
  - **Description:** Visualization and monitoring tool.

- **Prometheus**
  - **Image:** `prom/prometheus`
  - **Port:** `9090:9090`
  - **Description:** Monitoring and alerting system.
  - **Configuration:** Mounts a `prometheus.yml` configuration file from the host.

- **Postgres Exporter**
  - **Image:** `prometheuscommunity/postgres-exporter`
  - **Port:** `9187:9187`
  - **Description:** Exporter for PostgreSQL metrics.

- **Mongo Exporter**
  - **Image:** `ssheehy/mongodb-exporter:latest`
  - **Port:** `9216:9216`
  - **Description:** Exporter for MongoDB metrics.

- **PostgreSQL**
  - **Image:** `postgres:latest`
  - **Port:** `5433:5432`
  - **Description:** PostgreSQL database.

- **Django App**
  - **Build:** From the `./Django_Rest` directory
  - **Port:** `8000:8000`
  - **Description:** Django-based web application.

- **MongoDB**
  - **Image:** `mongo:latest`
  - **Port:** `27020:27017`
  - **Description:** MongoDB database.

- **Spring Boot App**
  - **Build:** From the `./SpringBoot` directory
  - **Port:** `8082:8082`
  - **Description:** Spring Boot-based application.

- **Eureka Server**
  - **Build:** From the `./Eureka` directory
  - **Port:** `8761:8761`
  - **Description:** Eureka service discovery server.

- **Spring Cloud Gateway**
  - **Build:** From the `./Gateway` directory
  - **Port:** `8081:8080`
  - **Description:** Spring Cloud API gateway.

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed.
- [Docker Compose](https://docs.docker.com/compose/install/) installed.

## Configuration

1. **Environment Variables**

   Create a `.env` file in the root directory of the project with the following variables:

   ```env
   POSTGRES_DB=your_database
   POSTGRES_USER=your_user
   POSTGRES_PASSWORD=your_password
   ```

2. **Prometheus Configuration**

   Ensure that the `prometheus.yml` file in the root directory of the project is configured correctly for your monitoring needs.

## Usage

To start all the services defined in the `docker-compose.yml`, run the following command in the root directory of the project:

```sh
docker-compose up
```

To start the services in the background, use:

```sh
docker-compose up -d
```

To stop and remove all containers, networks, and volumes created, use:

```sh
docker-compose down
```

## Access

- **Grafana:** [http://localhost:3000](http://localhost:3000)  
  Username: `admin`  
  Password: `admin`

- **Prometheus:** [http://localhost:9090](http://localhost:9090)

- **Django App:** [http://localhost:8000](http://localhost:8000)

- **Spring Boot App:** [http://localhost:8082](http://localhost:8082)

- **Spring Cloud Gateway:** [http://localhost:8081](http://localhost:8081)

- **Eureka Server:** [http://localhost:8761](http://localhost:8761)

## Notes

- The Django container is configured to run migrations and collect static files on startup.
- The Spring Boot container is configured to run with Java 17.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
