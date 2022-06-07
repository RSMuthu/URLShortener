## Different Endpoints for URL Shortening
from fastapi import Depends, Body, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from database.db import get_db
from pydantic import HttpUrl
from database.model import Url
from URLShortener import app

@app.get("/{url_ref}") # does not start ``/api` as this needs redirect response
async def redirect(url_ref: str, db: Session = Depends(get_db)):
    '''
    Get the URL reference & redirect to original URL
    '''
    entity = db.query(Url).filter(Url.short_ref == url_ref).first()
    if not entity:
        raise HTTPException(status_code=404, detail="Url not found")
    return RedirectResponse(url=entity.original_url)

@app.post("/api/shorten")
async def short_it(url: HttpUrl = Body(..., embed=True) , db: Session = Depends(get_db)):
    '''
    Creates a new shorten reference for input URL
    '''
    # try:
    entity = db.query(Url).filter(Url.original_url == url).first()
    # If we already have shorten the url, return exiting
    if entity: return entity
    # if we have not shortened the input before then proceed
    url_obj = Url(original_url=url)
    db.add(url_obj)
    db.commit() # or we can set autocommit on the DB setup
    db.refresh(url_obj)
    return url_obj
    # except:
    #     raise HTTPException(status_code=500, detail="Url shortening Failed !")

@app.get("/api/urls")
async def get_url_list(db: Session = Depends(get_db)):
    '''
    Creates a new shorten reference for input URL
    '''
    try:
        entity = db.query(Url).all()
        return entity
    except:
        raise HTTPException(status_code=500, detail="Url shortening Failed !")
