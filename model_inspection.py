# -*- coding: utf-8 -*-
# @Time    : 2023/4/18 12:11 PM 
# @Author  : Yong Cao
# @Email   : yongcao_epic@hust.edu.cn
from knockknock import slack_sender
webhook_url = "https://hooks.slack.com/services/T8NC2U27Q/....."


@slack_sender(webhook_url=webhook_url, task_describ="test knockknock", channel="model_knockknock")
def train_your_nicest_model(hint_string):
    import time
    time.sleep(3)
    return {'loss': 0.9, "hint": hint_string} # Optional return value


train_your_nicest_model("This is a test for knockknock")