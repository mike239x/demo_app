from fastapi import FastAPI

app = FastAPI(title="Demo App")

@app.get("/")
def read_root():
    return {"Hello": "Bob"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
