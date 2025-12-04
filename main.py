from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
return {"message": "Deployment Successful! Hello from the Test Repo."}
