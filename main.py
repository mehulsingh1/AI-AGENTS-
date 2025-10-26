import base64
import os
import json
from groq import Groq

def explain_image(image_path, prompt="Describe and explain this image."):
    # Load API key
    os.environ["GROQ_API_KEY"] = json.load(open("credentials.json", "r"))["groq_token"]
    client = Groq()

    # Encode image as Base64
    with open(image_path, "rb") as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode("utf-8")

    # Call Vision model
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_base64}"}}

                ]
            }
        ]
    )

    return response.choices[0].message.content
