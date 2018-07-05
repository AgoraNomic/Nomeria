FROM evennia/evennia:latest
WORKDIR /usr/src/game/nomeria
ENTRYPOINT ["evennia", "-i", "start"]
