## DB Models definitions
from sqlalchemy import Column, String, Integer
from datetime import datetime
import hashlib
import base64

from .db import Base

def create_url_ref(context):
    # The argument `context` is something passed
    # by the sqlalchemy during Data Insert
    # for now lets use timestamp for ref
    # return datetime.utcnow().strftime('%Y%m%d%H%M%S%f')

    # Use the below logic to add more uniqueness
    # IF this also not enough, we can use UUID v4 or CUID
    url = context.get_current_parameters()['original_url']
    timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
    to_encode = f'{url}{timestamp}'
    b64_encoded_str = base64.urlsafe_b64encode(hashlib.sha256(to_encode.encode()).digest()).decode()
    return b64_encoded_str[:7]

class Url(Base):
    __tablename__ = "shortened_urls"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    original_url = Column(String, unique=True, nullable=False)
    short_ref = Column(String, nullable=False, default=create_url_ref)
