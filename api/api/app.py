from typing import Optional
from fastapi import FastAPI
from fastapi import status
import uvicorn
from api.routes import predictions_router

app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK)
async def ping():
    return {"message": "ping!"}

app.include_router(predictions_router, prefix="/predictions")

# @app.get("/users/{user_id}", tags=["Users"])
# async def user(user_id: int):
#     """
#     Extract id from path and return
#     """
#     return {"user_id": user_id}

# @app.get("/query")
# async def query(skip: int = 0, limit: int = 10, search: Optional[str] = None):
#     return {"items": search, "skip": skip, "limit": limit}

# if __name__ == '__main__':
#     uvicorn.run('app:app', host='127.0.0.1', port=8000, reload=True)
