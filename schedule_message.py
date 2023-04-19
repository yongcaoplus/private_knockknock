# -*- coding: utf-8 -*-
# @Time    : 2023/4/18 10:28 AM 
# @Author  : Yong Cao
# @Email   : yongcao_epic@hust.edu.cn
import datetime
from slack_sdk import WebClient


def post_scheduled_message(channel_id, client, text, post_ats):
    for i, post_at in enumerate(post_ats):
        print(post_at, text)
        result = client.chat_scheduleMessage(
            channel=channel_id,
            text=text + str(i+1),
            post_at=post_at.strftime('%s')
        )
        print(result)
        print("-"*30)


def format_time(time):
    schedule_timestamp = []
    scheduled_time = datetime.time(hour=time[1][0], minute=time[1][1])
    if time[0] == "everyday":
        for i in range(7):
            remind_day = datetime.date.today() + datetime.timedelta(days=i+1)
            schedule_timestamp.append(datetime.datetime.combine(remind_day, scheduled_time)) # .strftime('%s')
    else:
        schedule_timestamp.append(datetime.datetime.combine(datetime.date.today(), scheduled_time)) # .strftime('%s')
    return schedule_timestamp


def read_paper(channel_id, client):
    message = "> It's time to read paper today! \nDaily Arxiv🎉: https://www.arxivdaily.com/cate/20/seq/0\n\n" \
              "Paper Notes: https://mluk6mvibg.feishu.cn/share/base/form/shrcnM5oJjSQTTgMWIkiDR1J0ig"
    time = ["everyday", [9, 0]]
    schedule_timestamp = format_time(time)
    post_scheduled_message(channel_id, client, message, schedule_timestamp)


def daily_record(channel_id, client):
    message = "> It's time to record today's work: https://teamup.com/c/djzbkq/daily-recording"
    time = ["everyday", [21, 0]]
    schedule_timestamp = format_time(time)
    post_scheduled_message(channel_id, client, message, schedule_timestamp)


if __name__ == '__main__':
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    channel_id = "model_knockknock"
    client = WebClient(token="xoxb-294410954262-51500...")
    read_paper(channel_id, client)
    daily_record(channel_id, client)