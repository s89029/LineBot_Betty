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
    return "ccc"

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



@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #判斷事件
    a = event.message.text
    Ifcom = SelF.checkevent(a)
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

if __name__ == "__main__":
    app.run()