from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item["q"] = q
    if not short:
        item["description"] = "This is an amazing item that has a long description"
    return item
