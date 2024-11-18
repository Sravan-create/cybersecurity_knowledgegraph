
---

# KG-CyberSec: Knowledge Graph and Chatbot from Unstructured Cybersecurity Text

## Project Overview
KG-CyberSec builds a **Knowledge Graph** from unstructured cybersecurity data and integrates a **BERT-powered chatbot** to answer user queries based on extracted entities and relations. This project organizes cybersecurity concepts into structured triples, enabling efficient knowledge retrieval and enhancing educational or analytical insights in cybersecurity.

### Key Features
- **Knowledge Graph Construction**: Extracts entities, relations, and builds structured triples from cybersecurity text.
- **Redundancy Reduction**: Merges similar entities and removes redundancies for an optimized graph.
- **BERT Chatbot**: Responds to cybersecurity queries by retrieving relevant information from the knowledge graph.

## Libraries Used
- **Transformers (BERT)**: For query embedding and similarity matching.
- **spaCy**: For Named Entity Recognition and initial parsing.
- **pandas**: Manages data organization for entity-relation storage.
- **NetworkX & Matplotlib**: Visualizes the knowledge graph structure.

Install the required libraries using:
```bash
pip install transformers spacy pandas networkx matplotlib
python -m spacy download en_core_web_sm
spacy==3.5.1              # For Named Entity Recognition and dependency parsing
transformers==4.34.0      # For using BERT for chatbot and entity matching
pandas==1.5.3             # For data manipulation and storage
matplotlib==3.7.2         # For visualization of the knowledge graph
networkx==3.2             # For building and visualizing knowledge graphs
scikit-learn==1.3.1       # For SVM-based intent classification
jupyter==1.0.0            # To run and manage Jupyter notebooks
numpy==1.24.3             # For numerical computations
PyYAML==6.0               # For managing knowledge base files in YAML format

```

--- 
