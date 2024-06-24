from __future__ import print_function

import json
import urllib
import boto3
import datetime

print("Loading functions refund......")

def process_purchase_refund(message,context):
    print("Received message")
    print(message)

    response = {}
    response['TransactionType'] = message['TransactionType']
    response['TimeStamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    response['Message'] = "The lambda inside ProcessPurchaceRefund funcation"
    return response


# ARN arn:aws:lambda:us-east-1:743292407330:function:ProcessRefund