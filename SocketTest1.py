
# 載入必要的套件
import socket
import wave

# 設定IP和Port
ip = "127.0.0.1"
port = 1234

# 建立socket連線
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

# 讀取wav檔案
with open("test1.wav", "rb") as f:
    data = f.read()

# 傳送wav檔案
s.sendall(data)

# 關閉socket連線
s.close()

# 讀取wav檔案
wav_file = wave.open("test1.wav", "rb")

# 分析聲音長度
duration = wav_file.getnframes() / wav_file.getframerate()

# 輸出聲音長度
print("聲音長度為：", duration, " 秒")
