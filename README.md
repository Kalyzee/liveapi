# Kalyzee Live Orchestrator

![Kalyzee Live Orchestrator Build](https://travis-ci.org/Kalyzee/liveapi.svg?branch=master) [![Coverage Status](https://coveralls.io/repos/github/Kalyzee/liveapi/badge.svg?branch=master)](https://coveralls.io/github/Kalyzee/liveapi?branch=master)



This software is an part of "Kalyzee Live Service", which is a set of three docker containers allowing to build live service in your organisation.

## Presentation

Kalyzee Live Orchestrator is an Webservice allowing user to manage transcoder and live streamer services.

The __transcoder__ is the main entrypoint to user want to make a live. The user have to put the transcoder URL to his capture application to stream it. This is an RTMP endpoint.

The __transcoder__ server transform the main video stream given by user to three other stream to be viewable to most users (connections and supports). Theses streams are transmitted to __streamer__. According to the application configuration many __streamer__ instance can exists, to be able to serve stream to more users (Bandwidth limitation).


## Getting started

### Using latest image (fatest)

```bash
  docker pull kalyzee/liveapi
```

### Build your docker images from sources (for developpers or contributors)

```bash
  docker-compose up
```


## Api endpoints

### User Management

#### Create user

#### Update user

#### Remove user


### Transcoder management

#### Add transcoder server

#### Remove transcoder server

#### Remove transcoder server


### Streamer management

#### Add transcoder server

#### Remove transcoder server

#### Remove transcoder server


### Events Managment

#### Add an event

#### Remove an event


## Create a developement environment


### Using docker compose

#### Launching environment

```bash
  docker-compose up
```

#### Launching tests
```bash
  docker-compose run web ./manage.py test
```

## Contributing

* Fork the project
* Create a pull request

## Application documentation

### Models


#### Streamer


#### Transcoder

#### Event
