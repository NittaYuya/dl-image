
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ① シンプルな GET API
@app.get("/hello")
def hello(name: str = "world"):
    return {"message": f"Hello, {name}!"}


# ② JSON を受け取る POST API
class AddRequest(BaseModel):
    a: float
    b: float

class AddResponse(BaseModel):
    result: float

@app.post("/add", response_model=AddResponse)
def add_numbers(req: AddRequest):
    return AddResponse(result=req.a + req.b)

