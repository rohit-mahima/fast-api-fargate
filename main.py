from fastapi import FastAPI

app=FastAPI()

@app.get("/hello")
def get_helo():
    return {"message":"healthcheck"}