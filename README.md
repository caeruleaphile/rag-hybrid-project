
# RAG Hybrid Search

A Python-based project exploring document ingestion, text chunking, and hybrid information retrieval by combining semantic search and keyword-based search.

**Project status:** Work in progress 🚧

## Overview

The goal of this project is to develop a modular hybrid search system that combines vector-based semantic retrieval with traditional keyword search (BM25).

The project explores the main stages of a document retrieval pipeline, from document ingestion and preprocessing to indexing and retrieval.

It is designed with a modular architecture to facilitate experimentation with different chunking strategies, embedding models, and retrieval techniques.

## Current Implementation

The following components have been implemented:

### 1. Document Ingestion

Support for multiple document formats:

- PDF
- Markdown
- HTML
- TXT

Implemented features:
- Document loading and text extraction.
- Text normalization and preprocessing.
- Document metadata handling, including source, title, section, and page information.
- Separation of raw and processed documents.

### 2. Text Chunking

Two chunking strategies have been implemented:

- **Fixed-size chunking:** Splits documents into chunks of configurable size with overlapping content.
- **Recursive chunking:** Splits text using a hierarchy of separators, prioritizing paragraphs, lines, sentences, and smaller text units.

The chunking architecture uses a common interface to support interchangeable strategies.

## Planned Development

The following components are planned:

- Semantic chunking based on embedding similarity.
- Integration of embedding models.
- Vector indexing using ChromaDB.
- Keyword-based indexing using BM25.
- Hybrid retrieval combining semantic and lexical search.
- Reciprocal Rank Fusion (RRF) for result merging.
- Optional reranking to improve retrieval relevance.
- Retrieval evaluation and experimentation.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming language | Python 3.13 |
| API framework | FastAPI |
| Document processing | pypdf, BeautifulSoup, markdown-it-py |
| Chunking | LangChain Text Splitters |
| Vector database | ChromaDB |
| Keyword retrieval | BM25 |
| Embeddings | Planned: OpenAI embeddings |
| Testing | pytest |
| Code quality | Ruff, Black, mypy |
| Containerization | Docker |
| CI/CD | GitHub Actions |

## Development Approach

The project follows a modular development approach, with separate components for document ingestion, text processing, chunking, indexing, and retrieval.

Each component is developed and tested independently before integration into the complete pipeline.

## Project Status

This repository is an ongoing personal engineering project. The document ingestion and initial chunking components are implemented and tested. Semantic chunking, indexing, and hybrid retrieval remain under development.

The repository reflects the current implementation rather than a completed production system.
