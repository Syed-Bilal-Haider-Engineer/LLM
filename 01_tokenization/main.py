import tiktoken

end = tiktoken.encoding_for_model("gpt-4")
text = "Hello, world!"
tokens = end.encode(text)
print(tokens)
print(end.decode(tokens))
print(f"Number of tokens: {len(tokens)}")