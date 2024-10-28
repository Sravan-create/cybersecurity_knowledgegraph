import pandas as pd
import joblib
import torch
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity

reduced_kg_path = "reduced_knowledge_graph.pkl"
reduced_kg_df = joblib.load(reduced_kg_path)

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

def get_embedding(text):
    inputs = tokenizer(text, return_tensors='pt')
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach().numpy()

kg_embeddings = []
for _, row in reduced_kg_df.iterrows():
    source_embedding = get_embedding(row['source'])
    target_embedding = get_embedding(row['target'])
    kg_embeddings.append((source_embedding, row['source'], row['edge'], target_embedding, row['target']))

def chatbot_query(query, previous_responses):
    query_embedding = get_embedding(query)

    best_match = None
    highest_similarity = 0
    similarity_threshold = 0.7

    for source_emb, source, edge, target_emb, target in kg_embeddings:
        source_similarity = cosine_similarity(query_embedding, source_emb)[0][0]
        target_similarity = cosine_similarity(query_embedding, target_emb)[0][0]

        if source_similarity > highest_similarity and source_similarity >= similarity_threshold:
            highest_similarity = source_similarity
            best_match = f"{source} {edge} {target}"
        if target_similarity > highest_similarity and target_similarity >= similarity_threshold:
            highest_similarity = target_similarity
            best_match = f"{source} {edge} {target}"

    if best_match and best_match not in previous_responses:
        previous_responses.append(best_match)
        if len(previous_responses) > 2:
            previous_responses.pop(0)
        return best_match
    else:
        return "There is no relevant answer to this question from the database."

previous_responses = []

print("Cybersecurity Chatbot. Type 'exit' to end the chat.")
while True:
    user_query = input("Ask a question about the knowledge graph: ")
    if user_query.lower() == 'exit':
        print("Exiting the chat. Goodbye!")
        break
    answer = chatbot_query(user_query, previous_responses)
    print("Answer:", answer)
