# Intro to API's

Welcome to the "Intro to APIs with Flask" GitHub repository! This repository contains code and resources for creating a beginner-friendly application on web APIs using the Flask web framework in Python.
This repo contains an example on how to use API's in development with the example being Complimentr - An application to send a compliment to someone using Twilio API. This application was created from my
understandings of [Introduction to APIs course](https://github.com/craigsdennis/intro-to-apis-course)

## Local Installation

To get your hands on the project, you can fork the repository to get your copy of the repository or you can clone the repository on your local machine with `git clone https://github.com/JustAnda7/intro-to-apis-flask.git
`

### Getting Started

- `cd intro-to-apis-flask`
- Copy `variables.env.example` to `variables.env` and update it with your Twilio and MongoDB credentials.

### Running the application normally

Assuming that you have Python installed in your local machine

- `python -m venv .venv`
- `source ./.venv/bin/activate`
- `pip install -r requirements.txt`
- `FLASK_ENV=development flask run`

#### In Development mode

- Run ngrok on port 5000
- Visit your ngrok url!

### Running the application using Docker

Assuming you want to run the application as a dockerized container. Just run the `.yaml` file.

- Run `docker-compose up`

Note: You can change the `docker-compose.yaml` according to the requirements
