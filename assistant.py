import ollama

def get_response(question):
    response = ollama.chat(
        model="tinyllama",
        messages=[
            {"role": "user", "content": question}
        ]
    )
    return response["message"]["content"]
