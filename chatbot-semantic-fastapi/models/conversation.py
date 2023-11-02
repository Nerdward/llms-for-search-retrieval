from pydantic import BaseModel

class ConversationRequest(BaseModel):
    message: str
    max_tokens: int = 100
    temperature: float = 0.9
    top_p: float = 1
    frequency_penalty: float = 0
    presence_penalty: float = 0
    stop: list = None
    threshold: float = 0.9
    conversation_id: str = None

class ConversationResponse(BaseModel):
    text: str
    conversation_id: str