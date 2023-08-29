import requests
import json
import argparse

def get_endpoints(url):
  """Gets all endpoints from the API."""
  response = requests.get(url)
  if response.status_code != 200:
    raise Exception("Failed to get endpoints: {}".format(response.status_code))

  data = json.loads(response.content)
  endpoints = []
  for endpoint in data["paths"]:
    endpoints.append(endpoint["path"])

  return endpoints

def get_security_features(url, endpoints):
  """Gets the security features for each endpoint."""
  security_features = {}
  for endpoint in endpoints:
    response = requests.get(url + endpoint)
    if response.status_code != 200:
      continue

    data = json.loads(response.content)
    security_features[endpoint] = data["security"]

  return security_features

def save_to_file(security_features, filename):
  """Saves the security features to a file."""
  with open(filename, "w") as f:
    json.dump(security_features, f)

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--url", help="The URL of the API")
  parser.add_argument("--filename", help="The name of the file to save the security features to")
  args = parser.parse_args()

  url = args.url
  filename = args.filename

  endpoints = get_endpoints(url)
  security_features = get_security_features(url, endpoints)
  save_to_file(security_features, filename)

if __name__ == "__main__":
  main()
