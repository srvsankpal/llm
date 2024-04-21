# Knowledge Base

## Retreivers
- https://www.youtube.com/watch?v=KQjZ68mToWo
- https://python.langchain.com/docs/modules/data_connection/retrievers/

**ParentDocumentRetreiver**: Does a symantic search on a smaller chunk and fetches a bigger chunk

**MultiQueryRetreiver**: Creates different version of queries

**ContextualCompressionRetriever**: Retrieves the document and compresses them before feeding to final llm.

**EnsembleRetiever**: Can use multiple retrievers in one retrievers

**SelfQueryRetrivers**: You can use metadata to provide additional context to llm through this. Need to provide additional arg to describe each field(key) in metadata.

**TimeWeightedVectorStoreRetriever**: It decays older documents, needs to provide last_accessed at in meta data. Does not work with all vectordb. works with faiss though.

## QA Chains

**load_qa_chain**: Loads all documents, does not do a semantic search

**RetrievalQA**: We can add a retriever which can do a lot type of semantic searches, cosine similarity, mmr

## Chain Types

**Refine**:

**Stuff**:

**Map reduce**:

## Semantic Search techniques

**Similarity Search**

- Euclidean
- Cosine

**MMR**:
- https://medium.com/tech-that-works/maximal-marginal-relevance-to-rerank-results-in-unsupervised-keyphrase-extraction-22d95015c7c5
- https://www.cs.cmu.edu/~jgc/publication/The_Use_MMR_Diversity_Based_LTMIR_1998.pdf

## Text Splitters:
https://python.langchain.com/docs/modules/data_connection/document_transformers/

