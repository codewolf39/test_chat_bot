from ollama import chat

MODEL="llama3.2"

def generate_responses(mess):
    responses = chat(model=MODEL, messages=[{"role":"user", "content": mess}])
    return responses.message.content

while True:
    userInput = input("")

    if userInput.lower() == "exit":
        break

    answer = generate_responses(userInput)

    print(answer)