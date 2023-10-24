from fastapi import FastAPI

app = FastAPI()

@app.post("/conversation")
def conversation(request):
    message = request.message
    collection = request.collection
    max_tokens = request.max_tokens
    temperature = request.temperature
    top_p = request.top_p
    frequency_penalty = request.frequency_penalty
    presence_penalty = request.presence_penalty
    stop = request.stop
    threshold = request.threshold

    