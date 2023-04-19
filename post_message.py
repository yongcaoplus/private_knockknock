# -*- coding: utf-8 -*-
# @Time    : 2023/4/18 12:19 PM 
# @Author  : Yong Cao
# @Email   : yongcao_epic@hust.edu.cn
from slack_sdk import WebClient


def post_message(message):
    # Channel you want to post message to
    channel_id = "model_knockknock"
    client = WebClient(token="xoxb-294410954262-5150008558496-......")
    # Call the chat.scheduleMessage method using the WebClient
    result = client.chat_postMessage(
        channel=channel_id,
        text=message,
    )
    print(result)


if __name__ == '__main__':
    message = "> It's time to read paper today! \n" \
              "Daily Arxiv🎉: https://www.arxivdaily.com/cate/20/seq/0\n\n" \
              "Paper Notes: https://mluk6mvibg.feishu.cn/share/base/form/shrcnM5oJjSQTTgMWIkiDR1J0ig"
    post_message(message)