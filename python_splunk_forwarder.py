import json
import requests

data = {"test": "HelloWorld"}
your_splunk_url = "https:splunk:port/services/collector"

def post_to_splunk(data):
    requests.post(your_splunk_url, headers={'Authorization': f'Splunk {token}',
    'Content-Type': 'application/json'},data=json.dumps({'index':f'{index}','event':{ 'query_data' : f'{data}'}}),verify=False)


def main():
    post_to_splunk(data)

if __name__ == "__main__":
    main()
