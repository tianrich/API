import requests
import json

def get_api_info(api_url):
    response = requests.get(api_url)
    if response.status_code != 200:
        raise ValueError("API call failed")

    return json.loads(response.content)

def main():
    api_url = "https://your-api-url.com/"
    api_info = get_api_info(api_url)

    # Print the information about the API
    print("API name:", api_info["name"])
    print("API version:", api_info["version"])
    print("API endpoints:", api_info["endpoints"])

if __name__ == "__main__":
    main()
