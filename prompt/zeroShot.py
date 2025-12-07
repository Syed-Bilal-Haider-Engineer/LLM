from openai import OpenAI
system_zero_prompt = "Translate any language to French."

client = OpenAI(
   api_key="AIzaSyDFjM67t_Ag_4p_ltXxwC-AzkrPHiz6q2s",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
   messages=[
        {"role": "system", "content": system_zero_prompt},
        {"role": "user", "content": "Now translate 'Cow' to Spanish."},
    ]
)

print(response.choices[0].message.content)