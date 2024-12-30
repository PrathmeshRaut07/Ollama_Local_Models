import base64
import requests
import json

def send_image_request(image_path, model="llava", prompt="What is in this picture?"):
    # Convert image to base64
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')

    # Prepare the payload
    payload = {
        "model": model,
        "prompt": prompt,
        "images": [base64_image]
    }

    # Send the POST request
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()  # Parse and return the JSON response
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Example usage
image_path = r"architecture.png"  # Replace with the actual image path
result = send_image_request(image_path)
print(result)
