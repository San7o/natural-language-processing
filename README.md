# natural-language-processing

This repo contains my notes and tests all about natural language processing with LLM.

The repo was created in date 30-05-2024 (DD/MM/YYYY)

## Index
- [pipeline-basic-examples](pipeline-basic-examples.py): Basic usage of pipelines


## short summary

There are many tipes of pipelines, such as:
- `feature-extraction`: get the vector representation of a text
- `fill-mask`: fill in the blanks in a text
- `ner`: named entity recognition, find entities in a text
- `question-answering`: answer questions based on a text
- `sentiment-analysis`: classify the sentiment of a text
- `summarization`: summarize a text
- `text-generation`: generate text
- `translation`: translate text
- `zero-shot-classification`: classify a text without any training data

You can call a pipeline like this:
```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
classifier("I've been waiting for a HuggingFace course my whole life.")
```

# Ollama

You can run local LLM with ollama, keep in mind that you need a lot of computing power.
With a 1060 3G I can run a maximum of 1B parameters wich is only barely decent. You can run a model withf.
```bash
sudo ollama serve
```
and
```
ollama run tinyllama
```
