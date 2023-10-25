import os
import openai
# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("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")
chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])