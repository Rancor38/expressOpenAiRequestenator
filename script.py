import requests

def make_request():
    url = "http://localhost:4000/"  # Change this URL to the desired endpoint

    # Set the user input
    user_input = input("Please send a message: ")

    # Update the body with the user input
    body = {"message": user_input}  # Change this body to the desired payload
    print(body)
    try:
        response = requests.post(url, json=body)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Access the 'content' property from the JSON response
            content = response.json()['choices'][0]['message']['content']
            print("Assistant's response:")
            print(content)
        else:
            print(f"Request failed with status code: {response.status_code}")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    make_request()
