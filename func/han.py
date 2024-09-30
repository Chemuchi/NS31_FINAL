import requests, json

def temp():
    response = requests.get('https://api.hangang.msub.kr/')
    data = json.loads(response.text)
    temp = data['temp']
    time = data['time']
    sta = data['station']
    print(f"현재 한강의 수온은 {temp}도 입니다.\n기준: {sta}, {time}시")

def hangang():
    print("\n잠시 기다려주세요..\n")
    temp()