from openai import OpenAI

client = OpenAI(base_url="https://api.sambanova.ai/v1", api_key="xyz")

completion = client.chat.completions.create(
    model="Meta-Llama-3.1-405B-Instruct",
    messages=[
        {"role": "system", "content": "Answer the question in a couple sentences."},
        {"role": "user", "content": "tell me how to read papers"}
    ],
    stream=True
)

full_response = ""

for chunk in completion:
    delta = chunk.choices[0].delta
    if hasattr(delta, 'content'):
        full_response += delta.content

print(full_response)


# If you are using the original script in the .pdf, you can set streaming to false, then print(completion.choices[0].message.content)