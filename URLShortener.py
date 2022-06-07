from fastapi import FastAPI
from database import initialize_db

## Initialise the FastAPI object to process
app = FastAPI()
## Initialise the database and tables as needed
initialize_db()

## Pull in the endpoints for Rest View
from endpoints import shortener_endpoints
