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

retrieved_text = """Article 21:
The Controller shall respond to the requests of the Data Subject pertaining to their rights
under this Law within such period and in such method as set out in the Regulations

Article 22:
The Controller shall conduct an impact assessment of Personal Data Processing in relation
to any product or service, based on the nature of the activity carried out by the Controller,
in accordance with the relevant provisions of the Regulations."""

system_prompt = f"""You are a legal information assistant specializing in the Saudi PDPL.
Answer the question using only the text delimited by triple backticks.
Use a formal tone, maximum 3 sentences, and cite the article number.
If the text does not contain the answer, reply: "No text answers this question."
You provide information only, not legal advice.
Text: ```{retrieved_text}```"""

questions = [
    "Must the Controller conduct an impact assessment?",
    "Within what period must the Controller respond to a Data Subject's request?",
    "What must the Controller do when a personal data breach happens?",
    "What is the best restaurant in Riyadh?"
    ]

for q in questions:
    answer = ask(system_prompt, q)
    print(q)
    print(answer)
    print("-" * 40)