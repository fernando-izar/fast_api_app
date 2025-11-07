from fastapi import FastAPI

app = FastAPI()


@app.get("/api-test")
async def api_test():
    return {"message": "API is working!"}
