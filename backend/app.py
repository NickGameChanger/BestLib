from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """
    Root endpoint that returns a simple JSON greeting.
    """
    a = 3
    s = 3 + 5
    return {"message": f"Hello, my {s} World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """
    Endpoint that returns an item based on the item_id.
    An optional query parameter 'q' can also be provided.
    """
    return {"item_id": item_id, "q": q}
