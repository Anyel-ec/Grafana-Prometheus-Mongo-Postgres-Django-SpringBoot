# Utiliza una imagen base de Java 17
FROM openjdk:17-jdk-slim

COPY target/gateway-0.0.1-SNAPSHOT.jar gateway.jar

# Expone el puerto 8080
EXPOSE 8080

ENTRYPOINT ["java", "-jar", "gateway.jar"]
