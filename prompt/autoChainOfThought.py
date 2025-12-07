
from openai import OpenAI
import json
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
OUTPUT: {step:"OUTPUT", content:"He then receives 5 more apples, so 6 + 5 = 11. Final Answer: 11"}"""

message_history = [{"role": "system", "content": system_few_prompt},]
client = OpenAI(
   api_key="AIzaSyDFjM67t_Ag_4p_ltXxwC-AzkrPHiz6q2s",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
user_input = input("Please enter a math word problem (or type 'exit' to quit): ")
message_history.append({"role": "user", "content": user_input})

while True:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={"type": "json_object"},
        messages= message_history
    )

    response = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": response})
    parsed_response = json.loads(response)
    print("Response:", parsed_response)
    if user_input.lower() == 'exit':
        break
    if parsed_response.get("step") == "PLAN":
        message_history.append({"role": "user", "content": parsed_response.get("content")})
        continue
    if parsed_response.get("step") == "OUTPUT":
        print("Final Answer:", parsed_response.get("content"))
        break