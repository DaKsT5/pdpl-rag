from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

def ask(system_prompt, user_prompt):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    response = client.chat.completions.create(
        model = "gpt-6-luna",
        messages = messages,
        max_completion_tokens = 300
    )
    prompt_tokens = response.usage.prompt_tokens
    completion_tokens = response.usage.completion_tokens
    input_cost = prompt_tokens * 0.10 / 1_000_000
    output_cost = completion_tokens * 0.50 / 1_000_000
    total = input_cost + output_cost
    print(prompt_tokens, completion_tokens, total)
    return response.choices[0].message.content

answer = ask("You are a PDPL assistant.", "What is a data controller?")
print(answer)