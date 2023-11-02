from fastapi import APIRouter
from models.conversation import ConversationRequest, ConversationResponse
from utils.conversation_utils import ChatbotGPT

conversation_router = APIRouter()

@conversation_router.post("/", response_model=ConversationResponse)
async def conversation(request: ConversationRequest):
    message = request.message
    collection = request.collection
    max_tokens = request.max_tokens
    temperature = request.temperature
    top_p = request.top_p
    frequency_penalty = request.frequency_penalty
    presence_penalty = request.presence_penalty
    stop = request.stop
    threshold = request.threshold

    conversation_id = request.conversation_id
    c = ChatbotGPT(ENGINE, threshold=threshold, conversation_id=conversation_id)
    response = c.user_turn(message)
    print(response)

    return ConversationResponse(text=response['content'], conversation_id=c.conversation_id)
