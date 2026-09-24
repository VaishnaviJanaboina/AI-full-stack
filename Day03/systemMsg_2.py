import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"system",
            "content":"You are teaching for 5 years old kids."
        },
        {
            "role":"user",
            "content":"explain AI in 5 points"

        }

        
    ]
)
print(response["message"]["content"])