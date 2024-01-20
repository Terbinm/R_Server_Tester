import requests
import json

filename = 'test.wav'
response = requests.post('http://localhost:8002/DoAnalysis', json={'filename': filename})
response_dict = json.loads(response.text)
severity = response_dict['Severity'][0]
handled = response_dict['Handled'][0]

print(f"Severity: {severity}")
print(f"Handled: {handled}")

# 測試 /upload 端點
# 假設我們有一個名為 'test.csv' 的文件
# with open('test1.wav', 'rb') as f:
#     files = {'upload': f}
#     response = requests.post('http://localhost:8002/upload', files=files)
#     print("/upload response: ", response.json())
