from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/name/{name}")
async def helloName(name):
    return {"message":f"Hello {name}"}