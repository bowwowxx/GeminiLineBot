# line_base.py
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageMessage,
)

class LineBot:
    def __init__(self, access_token, channel_secret):
        self.line_bot_api = LineBotApi(access_token)
        self.handler = WebhookHandler(channel_secret)

    def create_app(self):
        app = Flask(__name__)

        @app.route("/callback", methods=['POST'])
        def callback():
            signature = request.headers['X-Line-Signature']
            body = request.get_data(as_text=True)
            app.logger.info("Request body: " + body)

            try:
                self.handler.handle(body, signature)
            except InvalidSignatureError:
                print("Invalid signature.")
                abort(400)

            return 'OK'

        @self.handler.add(MessageEvent, message=TextMessage)
        def handle_message(event):
            self.handle_text_message(event)

        @self.handler.add(MessageEvent, message=ImageMessage)
        def handle_image_message(event):
            self.handle_image_message(event)

        return app

    def handle_text_message(self, event):
        pass

    def handle_image_message(self, event):  
        pass