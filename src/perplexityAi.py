import requests
import env
import base64
from sanitize_model_output import sanitize_model_output
from improve_message import improve_message

# Perplexity API endpoint (check documentation for the latest endpoint)
API_URL = "https://api.perplexity.ai/chat/completions"

def online_llm_perplexity(image_path):
    # Encode the image as base64
    with open(image_path, "rb") as f:
        image_base64 = base64.b64encode(f.read()).decode("utf-8")

    # Prepare headers for Perplexity API
    headers = {
        "Authorization": f"Bearer {env.PERPLEXITY_API_KEY}",
        "Content-Type": "application/json"
    }

    # Prepare payload (follow Perplexity's API message structure for multimodal input)
    payload = {
        "model": "sonar-pro",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": env.PROMPT_ONLINE_LLM_PERPLEXITY_V2},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{image_base64}"
                        }
                    }
                ]
            }
        ]
    }

    # start = time.time()
    # Call the Perplexity API
    response = requests.post(API_URL, headers=headers, json=payload)

    # end = time.time()
    # print(f"Time taken: {end - start:.4f} seconds")

    # Check if request was successful
    if response.status_code != 200:
        print(f"Error: API request failed with status code {response.status_code}")
        print(f"Response text: {response.text}")
        return None

    # Try to parse JSON response
    try:
        response_json = response.json()
    except requests.exceptions.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON response")
        print(f"Response status code: {response.status_code}")
        print(f"Response text: {response.text}")
        return None
    
    outp = response_json['choices'][0]['message']['content']
    res = improve_message(outp)
    print(res)
    print("\n")


# print(online_llm_perplexity(env.IMAGE_PATH3))
# Time taken: 6.4616 seconds
