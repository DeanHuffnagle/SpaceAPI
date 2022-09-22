import os

import dotenv
from fastapi import FastAPI
from dotenv import dotenv_values

env = dotenv_values(".env")


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

if __name__ == "__main__":
    print(env)


