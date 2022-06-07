This repo is an initiative to help College students to understand & learn FastAPI as part of a Workshop
Also added a basic powerpoint on the same with this repo.
And ofcourse, this is a very basic setup

# Lets Learn FastAPI by building URLShortener :)
This is a basic setup and sample URL Shortening backend web API
A simple application developed using FastAPI.
This is used for creating a short URLs and sharing across for easy usage.
This sharable short URL will be captive and act as Proxy

## Backend
- Python 3.10.4
- FastAPI
- Pydantic
- Sqlalchemy
- sqlite

(check the pipefile for detailed info on the required packages -- install them using `pipenv install` after `cd <project_repo>`)

##### API Endpoints
- `[GET] ​/api​/urls`
- `[POST] ​/api​/shorten`
- `[GET] ​/`

Swagger UI documentation will be available on running the application on

` [GET] /docs`
` [GET] /redoc`
` [GET] /openapi.json`

And to run the application,
`pipenv run uvicorn URLShortener:app`

##### Ways to Improve:
- Update the ORM modals and the definition of the Scheme with the additional data for improvised URL shortening system.
- Setup a UI/UX frontend for backend interaction.
