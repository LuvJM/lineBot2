from flask import Flask, jsonify, request
import os
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    a=os.environ['Authorization']
    return a

@app.route("/webhook", methods=['POST'])
def webhook():
    if request.method == 'POST':
        return "OK"

@app.route('/callback', methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded['originalDetectIntentRequest']['payload']['data']['replyToken']
    userText = decoded['queryResult']['intent']['displayName']
   if (userText == 'วันสำคัญทางพระพุทธศาสนา มีวันอะไรบ้าง') :
       sendText(user,'วันมาฆบูชา ขึ้น 15 ค่ำ เดือน 3 วันวิสาขบูชา ขึ้น 15 ค่ำ เดือน 6 วันอาสาฬหบูชา ขึ้น 15 ค่ำ เดือน 8')
    elif (userText == 'อริยสัจ 4 คือ') :
       sendText(user,'อริยสัจ 4 คื่อ หลักความจริง 4 ประการ ได้แก่ ทุกข์ สมุทัย นิโรธ มรรค')
    else :
       sendText(user'มีอะไรให้น้อง สาละ ช่วยมั้ย??')
    return '',200
              
def sendText(user, text):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': os.environ['Authorization']    # ตั้ง Config vars ใน heroku พร้อมค่า Access token
  }
  data = json.dumps({
    "replyToken":user,
    "messages":[{"type":"text","text":text}]
  })
  r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล

if __name__ == '__main__':
    app.run()
