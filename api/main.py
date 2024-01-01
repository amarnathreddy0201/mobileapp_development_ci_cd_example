# https://www.youtube.com/watch?v=UauMQGqaxGo
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Hello Amarnath Reddy World"}


@app.get("/next")
def next():
    return {"message": "Hello Amarnath Reddy World next"}


handler = Mangum(app)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
