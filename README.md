# Interview Project

Components 

  - Docker-compose
  - docker
  - sqllite
  - python3.6
  - flask
  - gunicorn
  - nginx

## Installation
Change the API_TOKEN and CHANNEL in `config.py`

Please note you have to give the app the following slack permission 

#### Bot Token scope
  - chat:write
  - chat:write.public

#### User Token scope
  - chat:write



After cloning use this commands

```sh
$ cd interview-project-dr
$ docker-compose build --no-cache
$ docker-compose up -d
$ curl --location --request POST 'http://127.0.0.1:81/msg' --header 'Content-Type: application/json' --data-raw '{
    "msg" : "hi there"
}'
```

## Notes

| Services | Description |
| ------ | ------ |
| n1-service | Running nginx |
| m1-service |  M1 is a client facing microservice that exposes a simple REST endpoint to input a message Running at 81 port in the host machine |
| m2-service |  M2 is a microservice that M1 calls to send the msg and it gets stored in sqlite mounted at db_mount and calls the slack api with 'Received from M1' msg |
| filestore.db | sqlite db store to store the msg from M1 that was send to M2, mounted at db_mount  |

Please note that I have made a demo slack app for this project please create a slack app and install it to get the api token and channel id.


to check the api I have added a ping

For M1
```sh
$ curl --location --request GET 'http://127.0.0.1:81/ping'
```

For M2
```sh
$ curl --location --request GET 'http://127.0.0.1:82/ping'
```
M2 have another endpoint that M1 uses via http to send the msg to M2 /msg_from_client its a post endpoint that also take same input like M1.

This README was made with the help of https://dillinger.io/





