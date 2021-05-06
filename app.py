from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

#額外功能
from imgurpython import ImgurClient
from bs4 import BeautifulSoup
import configparser
import requests
import re
import random
import codecs
import Selffunction as SelF
#引用設定
config = configparser.ConfigParser()
config.read("config.ini")
app = Flask(__name__)

line_bot_api = LineBotApi(config['line_bot']['Channel_Access_Token'])
handler = WebhookHandler(config['line_bot']['Channel_Secret'])
client_id = config['imgur_api']['Client_ID']
client_secret = config['imgur_api']['Client_Secret']
album_id = config['imgur_api']['Album_ID_HS']

#測試區

client = ImgurClient(client_id, client_secret)
images = client.get_album_images(album_id)

print (SelF.PickDrink())

@app.route("/")
def test():
    return "kkk"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

Ordertemp=''
Order =''
totalcost = 0
openorder = 0
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #判斷事件
    global openorder 
    global Order
    global totalcost
    global Ordertemp
    Ifcom = SelF.checkevent(event.message.text)
    if Ifcom[0] == '抽飲料':
        todaydrink = SelF.PickDrink()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=todaydrink))
        return 0
    if Ifcom[0] == '抽圖片':
        client = ImgurClient(client_id, client_secret)
        images = client.get_album_images(album_id)
        index = random.randint(0, len(images) - 1)
        url = images[index].link
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url)
        line_bot_api.reply_message(
            event.reply_token,
            image_message)
        return 0
    if event.message.text == '點餐':
        orderhelp = "開始點餐，格式: 點@Jeremy@珍珠奶茶無糖少冰@60"
        openorder = 1
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=orderhelp))
        return 0
    if Ifcom[0] == '點':
        if openorder == 1:
            #profile = line_bot_api.get_profile(event.source.user_id)
            #name = profile.display_name
            Order = Order + Ifcom[1] + '\n'
            Ordertemp = Ordertemp + Ifcom[1] +'-'+Ifcom[2]+'-金額'+Ifcom[3]+'\n'
            totalcost = totalcost + int(Ifcom[3])
            line_bot_api.reply_message(
            event.reply_token,[TextSendMessage(text='點單成功,以下為已經點過的人'),TextSendMessage(text=Order)]
            )
        return 0
    if Ifcom[0] == '收單':
        openorder = 0
        cost = '總金額'+str(totalcost)
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text=Ordertemp),TextSendMessage(text= cost)])
        Ordertemp=''
        Order = ''
        totalcost = 0
        return 0
    if event.message.text == '測試':
        profile = line_bot_api.get_profile(event.source.user_id)
        name = profile.display_name 
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=name))
        return 0
    if Ifcom[0] == '你說':
        index = random.randint(0,2)
        def matching_dict(type):
            types = {
                 0: 'Betty覺得是這樣沒錯',
                 1: 'Betty不這麼認為',
                 2: '我不知道'
        }
            return types.get(type, '無優惠')
        replytext = matching_dict(index)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=replytext))
        return 0
    if Ifcom[0] == '熱量':
        s = SelF.foodfat(Ifcom[1])
        fat = s[0][2]
        unit = s[0][3]
        message = Ifcom[1]+'的熱量為'+str(fat)+'大卡 '+ unit
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=message))
        return 0

if __name__ == "__main__":
    app.run()