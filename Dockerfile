FROM node:14-alpine

RUN apk add git openssh && \
    ssh-keygen -t rsa -q -N "" -f /root/.ssh/id_rsa && \
    cat /root/.ssh/id_rsa.pub

RUN npm install

VOLUME [ "/wiki" ]

WORKDIR /wiki

CMD ["npm", "run", "dev"]
