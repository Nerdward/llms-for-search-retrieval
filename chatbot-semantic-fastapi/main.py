from fastapi import FastAPI
from routes.conversation import conversation_router
import uvicorn


app = FastAPI()

app.include_router(conversation_router, prefix="/conversation")


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)