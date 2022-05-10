from fastapi import FastAPI, Request
from fastapi_utils.tasks import repeat_every
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json 
from datetime import datetime
from constants import CORS_URLS
from bitcoin_timestamp import BitcoinTimestamp
from custom_util import get_live_bitcoin_price, convert_date_to_text
from database_connection import DatabaseConnection

# TODO (3.1): define FastAPI app
app = FastAPI()

# TODO (5.4.1): define database connection
app2 = DatabaseConnection()

CORS_URLS = [
    "http://localhost",
    "http://localhost:3000"
]
# TODO (3.2): add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = CORS_URLS,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

# TODO (3.1)
@app.get("/")
async def root():
    content = {"Message": "Hello world! This is a bitcoin monitoring service!"}
    return json.dumps(content)


# TODO (5.4.2)
"""
repeated task to update bitcoin prices periodically
"""
@repeat_every(seconds = 60 * 5)  # 5 minutes

def get_live_bitcoin_price() -> None:
    num = get_live_bitcoin_price()
    if num != -1:
        date = convert_date_to_text(datetime.now())
        new = BitcoinTimestamp(date,num)
    app2.insert_timestamp()


# TODO (5.4.3)
@app.get("/get_bitcoin_prices")
async def get_all_timestampes(): 
    content = app2.get_all_timestampes()
    newList = []

    for i in content:
        newList.append(i.__dict__)
    
    return json.dumps(newList)   

#main function to run the server        
if __name__ == '__main__':
    uvicorn.run(app,host="127.0.0.1", port=8000)