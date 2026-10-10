from ollama import chat
import gradio as gr # gr here is just an alias

MODEL="llama3.2"

SYSTEM_MESSAGE = """
You are a helpful assistant in a clothing store.

Only answer the queries related to shoes and clothes and hats. Refuse polietly for any other query and circle them back to the products like shoes, clothes and hats.

Hats are 60 percent off.
Most other items are 50 percent off.

Gently encourage customers to consider items on sale.
If customers are unsure what to buy, suggest hats.

Be friendly, honest, and concise.
"""

def response(mess, his):

    relevant_messagae = SYSTEM_MESSAGE

    if "clothes" or "shoes" or "hats" not in mess.lower():
        relevant_messagae += "The store does not sell the items you asked for neither it can help you to get them anywhere. explain this politely and suggest relevant items that are on sale."

    messages = [{"role": "system", "content": relevant_messagae}]

    for item in his:
        content = item.get("content", "")

        # Gradio may store message content as a list of dictionaries
        if isinstance(content, list):
            content = "".join(
                part.get("text", "")
                for part in content
                if isinstance(part, dict)
            )

        # Handle dictionary-based content too
        elif isinstance(content, dict):
            content = content.get("text", "")

        # Ollama expects content to be a string
        if not isinstance(content, str):
            continue

        messages.append({
            "role": item["role"],
            "content": content
        })

    # Add the latest user message
    messages.append({
        "role": "user",
        "content": mess
    })

    result = chat(
        model=MODEL,
        messages=messages
    )

    return result.message.content

gr.ChatInterface(
    fn=response,
    title="My Local Chatbot"
).launch()