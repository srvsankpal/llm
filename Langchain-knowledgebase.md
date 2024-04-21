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

## Chain Types

**Refine**:

**Stuff**:

**Map reduce**:
