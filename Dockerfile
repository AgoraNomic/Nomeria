FROM evennia/evennia:latest
RUN apk update && apk add git
WORKDIR /usr/src/game/nomeria
ENTRYPOINT ["evennia", "-i", "start"]
