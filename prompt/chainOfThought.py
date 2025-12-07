
from openai import OpenAI
system_few_prompt = """ You'r expert AI assistant in solving math word problems using chain of thought prompting.
you will break down the problem into smaller steps to arrive at the final answer.
you will always end with 'Final Answer: <answer>'.

Rules:
- Always think step by step.
- Always show your work.
- always double-check your calculations.
- Always end with 'Final Answer: <answer>'.
Examples:
Q:  John has 10 apples. He gives away 4 and then receives 5 more. How many apples does he have?
START:John starts with 10 apples.
PLAN: { "step":"PLAN", content:"He gives away 4."}
PLAN: { "step":"PLAN", content:"He gives away 4, so 10 - 4"}
PLAN: { "step":"PLAN", content:"He gives away 4, so 10 - 4 = 6."}
PLAN: { "step":"PLAN", content:"He gives away 4, so 10 - 4 = 6."}
OUTPUT: {step:"", content:"He then receives 5 more apples, so 6 + 5 = 11. Final Answer: 11"}"""

client = OpenAI(
   api_key="AIzaSyDFjM67t_Ag_4p_ltXxwC-AzkrPHiz6q2s",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
   messages=[
        {"role": "system", "content": system_few_prompt},
        {"role": "user", "content": "Solve this problem of Math input provide "},
        {"role":"assistant","content":"Q: Sarah has 15 candies. She eats 3 and then buys 10 more. How many candies does she have now?"},
    ]
)

print(response.choices[0].message.content)