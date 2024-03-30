import requests

url = "https://lnath3u4svkf2jcamufzqtdgde0hanxc.lambda-url.ap-northeast-2.on.aws/"
headers = {'Content-Type': 'application/json'}
data = {
        "name": "최승혁",
        "ec2": "Elastic Compute Cloud",
        "s3": "Simple Storage Service"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.content.decode('utf-8'))