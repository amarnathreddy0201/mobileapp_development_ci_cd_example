# https://www.youtube.com/watch?v=UauMQGqaxGo
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Hello Amarnath Reddy World"}


handler = Mangum(app)
