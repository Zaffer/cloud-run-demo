# import os
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=int(os.environ.get("PORT", 8080), log_level="info")
