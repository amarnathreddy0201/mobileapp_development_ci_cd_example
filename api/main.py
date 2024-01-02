# AWS+GitHub+CI/CD LINK Deploy into AWS : https://www.youtube.com/watch?v=UauMQGqaxGo

#  How to create Function LINK : https://www.youtube.com/watch?v=RGIM4JfsSk0
from fastapi import FastAPI
from mangum import Mangum

# from api.main1 import getting_call

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Hello Amarnath Reddy World"}


@app.get("/next")
def next():
    return {"message": "Hello Amarnath Reddy World next"}


@app.post("/next")
def next():
    return {"message": "Hello Amarnath Reddy Postrequest"}


handler = Mangum(app)

# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="127.0.0.1", port=8000)
