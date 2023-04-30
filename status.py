import requests

url = "https://anty-api.com/browser_profiles/statuses?limit=&page=&query="

payload = {}
headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjM0MTMzNCwidXNlcm5hbWUiOiJhbGFnZW5jeXNlcnZpY2VAZ21haWwuY29tIiwicm9sZSI6ImFkbWluIiwidGVhbUlkIjoyMjgzMzk2LCJ0b2tlbkNyZWF0ZWRBdCI6MTY4Mjc4MzAwNH0.YCVpsd_jt0uD5b7sHFadFSVhDomLa4gXjPb0jg-wi04",
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
