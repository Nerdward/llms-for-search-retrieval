from fastapi import APIRouter
from models.document import DocumentInputRequest, DocumentInputResponse, DocumentRetrieveRequest,DocumentResponse, DocumentRetrieveResponse

document_router = APIRouter()

@document_router.post("/ingest", response_model=DocumentInputResponse)
async def document_ingest(request: DocumentInputRequest):
    text = request.text
    chunking_strategy = request.chunking_strategy

    if chunking_strategy == "sentence":
        chunks = re.split(r' *[\.\?!][\'"\)\]]* *', text)
    elif chunking_strategy == "paragraph":
        chunks = text.split('\n')
    elif chunking_strategy == "none":
        chunks = [text]
    elif 'overlapping' in chunking_strategy:
        _, max_tokens, overlapping_factor = chunking_strategy.split('-')
        chunks = overlapping_chunks(text, max_tokens=500, overlapping_factor=5)
    else:
        raise Exception("Invalid chunking strategy")
    
    chunks = [c.strip() for c in chunks if len(c.strip()) > 0]

    embeddings = get_embeddings(chunks, engine=ENGINE)

@document_router.post("/retrieve", response_model=DocumentRetrieveResponse)
async def document_retrieve(request: DocumentRetrieveRequest):
    query = request.query
    re_ranking_strategy = request.re_ranking_strategy
    num_results = request.num_results
    results = get_results()

    results = [
        DocumentResponse(
            text=r['metadata']['text'],
            date_uploaded=r['metadata']['date_uploaded'],
            score=r['score'],
            id=r['id']
        ) for r in results
    ]

    return results