from sentence_transformers import SentenceTransformer
import chromadb, ollama
model = SentenceTransformer("all-MiniLM-L6-v2")
file_name = "ai_sample.txt"
with open("ai_sample.txt", "r") as file:

    text = file.read()
chunks = []

chunk_size = 30 #20,30,50

chunk_overlap = 10 #5, 15, 30

step = chunk_size - chunk_overlap

for i in range(0,len(text),step):

    chunk = text[i:i+chunk_size]

    chunks.append(chunk)
embeddings = model.encode(chunks)
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name="My_document")
ids = []

for i in range(len(chunks)):

    ids.append(f"{file_name}_{i}")

collection.add(

    ids=ids,

    documents=chunks,

    embeddings=embeddings.tolist()

)
#Query
question = input("Ask a question.....")
question_embedding = model.encode(question)
results=collection.query(
    query_embeddings=[question_embedding.tolist()],
    n_results=3
)
retrieved_results = results['documents'][0]
retrieved_ids = results['ids'][0]
#for i in range(len(results['documents'][0])):

   #print(f"chunk_{i}\n")
   #print(results['documents'][0][i])
#Prompting
context = '\n'.join(retrieved_results)
#print(retrieved_results)
#print(context)
prompt = f'''
Answer the question using the context provided below.context
Question : {question}
Context : {context}
Answer:
'''
print(prompt)
#Connecting to local model
response = ollama.chat(
    model="llama3.2:3b",
    messages=[{
        "role":"User",
        "content":prompt
    }]
)
print(response["message"]["content"])



