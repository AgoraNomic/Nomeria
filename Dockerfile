FROM evennia/evennia:latest
USER root
RUN apk update && apk add git && pip install pyopenssl pycrypto bcrypt
USER evennia
WORKDIR /usr/src/game/nomeria
ENTRYPOINT ["evennia", "start", "-l"]
