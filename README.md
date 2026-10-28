# PDPL RAG

A RAG (Retrieval-Augmented Generation) assistant that answers questions about the Saudi Personal Data Protection Law (PDPL), cites the article number, and replies "No text answers this question." when the law text does not contain the answer.

> **Status:** work in progress. A first prototype answers from manually provided articles; retrieval over the full law is being built.

## Goal

Answer questions only from the law text, never from the model's memory, and refuse when there is no evidence.

## Planned stack

Python, OpenAI API, ChromaDB, LangChain, Streamlit.

## Source document

The project uses the English version of the PDPL published by SDAIA. The PDF is not included in this repository. Download it from:
https://sdaia.gov.sa/en/SDAIA/about/Documents/Personal%20Data%20English%20V2-23April2023-%20Reviewed-.pdf

The Arabic text is the authoritative version of the law; the English text is a translation.

## Disclaimer

This tool provides general information only. It is not legal advice.