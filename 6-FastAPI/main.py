from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi. responses import JSONResponse
from fastapi.exception_handlers import request_validation_exception_handler
from fastapi.exceptions import RequestValidationError

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float = None

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.get( "/custom_response")
async def custom_response():
    return JSONResponse(content={"message": "Custom response"}, status_code=200)

@app.get( "/text_response" )
async def text_response():
    return Response(content="Hello World" ,media_type="text/plain")

# @app.get( "/error_example/ " )
# async def error_example(item_id: int):
#     if item id < 1:
#         raise HTTPException(detail="ID must be greater than 0")
#     return {"item_id":item_id}

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body}
        )
