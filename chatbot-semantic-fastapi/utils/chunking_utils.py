import hashlib
from datetime import datetime

from langchain.document_loaders.parsers import PyPDFParser
from langchain.text_splitter import RecursiveCharacterTextSplitter


def my_hash(s):
    # Return the MD5 hash of the input string as a hexadecimal string
    return hashlib.md5(s.encode()).hexdigest()

def prep_documents_for_vector_storage(documents, chunk_size=500):
    documents = PyPDFParser().lazy_parse(documents)

    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=chunk_size, chunk_overlap=100, allowed_special="all"
    )
    ids, texts, metadatas = [], [], []
    for document in documents:
        doc_texts = text_splitter.split_text(document)
        doc_metadatas = [dict(text=doc_texts,date_uploaded=datetime.utcnow())]
        ids += [my_hash(doc_texts)]
        texts += doc_texts
        metadatas += doc_metadatas

    return ids, texts, metadatas