FROM maven:3.5.4-jdk-8-alpine as builder
RUN mkdir /app
COPY . /app

RUN cd app && mvn clean package
EXPOSE 80

FROM openjdk:8-jre-alpine
COPY --from=builder /app/target/FileToImage-0.1-jar-with-dependencies.jar /
VOLUME /export
ENTRYPOINT ["java", "-jar", "/FileToImage-0.1-jar-with-dependencies.jar"]
