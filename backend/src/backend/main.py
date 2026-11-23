from fastapi import FastAPI

app = FastAPI(title="Deerwalk MUN 4.0")

# middleware / cors 

@app.get("/")
def health_check():
    return {"status" : "ok"}
