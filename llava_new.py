# import ollama

# response = ollama.chat(
#     model='phi3:3.8b',
#     messages=[{
#         'role': 'user',
#         'content': 'What is in this image?',
#         # 'images': ['architecture.png']
#     }],
#     stream=True
# )

# print(response)
import ollama

# Make the chat request
response = ollama.chat(
    model='llava:7b',
    messages=[{
        'role': 'user',
        'content': 'What is in this image?',
         'images': ['architecture.png']
    }],
)
print(response.message['content'])
