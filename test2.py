import requests

# 測試 /upload 端點
# 假設我們有一個名為 'test1.wav' 的文件
with open('test1.wav', 'rb') as f:
    files = {'upload': f}
    response = requests.post('http://localhost:8002/upload', files=files)
    print("/upload response: ", response.json())
