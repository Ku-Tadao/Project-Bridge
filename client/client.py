# client/client.py

import requests # The library used to send HTTP requests

# The address of our server.
# When you're testing on your own machine, it's this "localhost" address.
# LATER, you will change this to your live PythonAnywhere URL.
API_URL = "http://127.0.0.1:5000"

def check_server_connection():
    """
    Sends a request to the server's main page to see if it's online
    and prints the message it gets back.
    """
    print(f"Attempting to connect to the server at {API_URL}...")

    try:
        # Send a GET request to the server's root URL ("/").
        # The 'timeout' is a good practice to prevent the script from hanging forever.
        response = requests.get(API_URL, timeout=5)

        # Raise an exception if the server returned an error code (like 404 or 500).
        response.raise_for_status()

        # If we get here, the request was successful (status code 200).
        # We parse the JSON response from the server into a Python dictionary.
        data = response.json()

        print("\n✅ Success! Connected to the server.")
        print(f"   Server message: {data.get('message')}")
        print(f"   Server status: {data.get('status')}")

    except requests.exceptions.ConnectionError:
        print("\n❌ Failure! Could not connect to the server.")
        print("   Is the server (server/app.py) running?")
    except requests.exceptions.Timeout:
        print("\n❌ Failure! The request timed out.")
    except requests.exceptions.RequestException as e:
        # This catches any other request-related errors.
        print(f"\n❌ An error occurred: {e}")


# This is the main part of our script that runs when we execute the file.
if __name__ == "__main__":
    check_server_connection()
    # Later, you will add more function calls here, like:
    # create_new_note("This is our first shared note!")
    # view_all_notes()