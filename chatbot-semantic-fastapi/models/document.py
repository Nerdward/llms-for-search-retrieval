from pydantic import BaseModel
from typing import List

class DocumentInputRequest(BaseModel):
    text: str
    chunking_strategy: str = "paragraph"

class DocumentInputResponse(BaseModel):
    chunks_count: int

class DocumentRetrieveRequest(BaseModel):
    query: str
    re_ranking_strategy: str
    num_results: int

class DocumentResponse(BaseModel):
    text: str
    date_uploaded: datetime
    score: float
    id: str

class DocumentRetrieveResponse(BaseModel):
    document = List[DocumentResponse]