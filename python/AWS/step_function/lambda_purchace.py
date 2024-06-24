# https://www.youtube.com/watch?v=s0XFX3WHg0w&list=PL9nWRykSBSFgQrO66TmO1vHFP6yuPF5G-&index=2&ab_channel=BeABetterDev

from __future__ import print_function

import json
import urllib
import boto3
import datetime

print("Loading functions ......")

def process_purchase(message,context):
    print("Received message")
    print(message)

    response = {}
    response['TransactionType'] = message['TransactionType']
    response['TimeStamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    response['Message'] = "The lambda inside ProcessPurchace funcation"
    return response

# ARN arn:aws:lambda:us-east-1:743292407330:function:ProcessPurchase