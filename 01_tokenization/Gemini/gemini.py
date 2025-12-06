from google import genai

client = genai.Client(api_key="AIzaSyDcFwmQFLaUyuYqg9T_OTom4jFNrzqJhCQ")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)