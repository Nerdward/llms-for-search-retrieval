from fastapi import APIRouter, UploadFile
from models.document import DocumentInputRequest, DocumentInputResponse, DocumentRetrieveRequest,DocumentResponse, DocumentRetrieveResponse
from utils.chunking_utils import prep_documents_for_vector_storage
from utils import embed
document_router = APIRouter()

@document_router.post("/ingest", response_model=DocumentInputResponse)
async def document_ingest(document: UploadFile, request: DocumentInputRequest):
    # chunking_strategy = request.chunking_strategy

    # if chunking_strategy == "sentence":
    #     chunks = re.split(r' *[\.\?!][\'"\)\]]* *', text)
    # elif chunking_strategy == "paragraph":
    #     chunks = text.split('\n')
    # elif chunking_strategy == "none":
    #     chunks = [text]
    # elif 'overlapping' in chunking_strategy:
    #     _, max_tokens, overlapping_factor = chunking_strategy.split('-')
    #     chunks = overlapping_chunks(text, max_tokens=500, overlapping_factor=5)
    # else:
    #     raise Exception("Invalid chunking strategy")
    print("sending to vector index")
    ids, texts, metadatas = prep_documents_for_vector_storage(document)
    embedding_engine = embed.get_embedding_engine()
    vector_index = embed.create_vector_index(
        embed.INDEX_NAME, embedding_engine, texts, metadatas)

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