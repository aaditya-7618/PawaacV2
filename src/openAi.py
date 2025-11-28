from openai import OpenAI
import env
import time
import base64

client = OpenAI(api_key=env.API_KEY)

def onlineLLM(image_path):

    # Encode the image as base64
    with open(image_path, "rb") as f:
        image_base64 = base64.b64encode(f.read()).decode("utf-8")

    # Start timer
    start = time.time()

    # Call the model with both text + image
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What's in this image?"},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_base64}"}}
                ],
            }
        ],
    )

    # End timer
    end = time.time()
    print(f"Time taken: {end - start:.4f} seconds")
    return(response.choices[0].message.content)
