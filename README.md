# KG-CyberSec: Building a Knowledge Graph from Unstructured Text

## Project Overview
KG-CyberSec is a comprehensive project aimed at building a **Knowledge Graph** from unstructured cybersecurity data. Using **Named Entity Recognition (NER)**, **relation extraction**, and **ontology development**, the project transforms raw text from lab manuals and course materials into structured triples, which can be visualized in a knowledge graph. This project helps organize and understand cybersecurity concepts, making it easier for cybersecurity education and analysis.

### Key Features:
- Extracts **subject-object pairs** and identifies relations using NER and custom rule-based patterns.
- Creates a **knowledge graph** that visually maps key cybersecurity entities and their relationships.
- Integrates custom **entity matching** to enhance the precision of extracted entities.
- Employs relation extraction to determine the interaction between cybersecurity concepts.
- Builds an interactive **chatbot** to answer cybersecurity-related queries using the knowledge graph.

## Libraries Used
Below are the main libraries and tools utilized in the project:
- **spaCy**: For NER (Named Entity Recognition) and dependency parsing.
- **pandas**: For handling data storage and manipulation (e.g., storing triples in a DataFrame).
- **re**: For regular expressions used in text processing.
- **csv**: For reading and writing CSV files (for storing entity-relation data).
- **Matplotlib/NetworkX**: (Optional) For visualizing the knowledge graph.

Install the required libraries using:
```bash
pip install spacy pandas
python -m spacy download en_core_web_sm  # For the small English model
