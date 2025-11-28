import ollama
import re


def split_into_new_lines(text: str) -> str:
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    # Join each sentence on a new line
    return "\n".join(sentences)


# for asking text model some query
def call_text_model(prompt: str, model: str) -> str:
    result = ollama.chat(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return result['message']['content']


