#https://www.youtube.com/watch?v=H_rRlnSw_5s&list=PL9nWRykSBSFhotGZHIrRyB4zKokDzTpcc&index=13

### Steps to create the trigger 
### follow the 
import json
import urllib
import urllib.parse
def lambda_function(event, context):
    # 1. Get the bucket name
    bucket = event['Records'][0]['s3']['name']
    # 2. Get the file/key name
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    try:
        # 3. Fetch the file from S3
        response = s3.get_object(Bucket = bucket, Key = key)

        # 4. Decerialize the file's content
        text = response['Body'].read().decode()
        data = json.loads(text)

        # 5. Print data
        print(data)

        # 6. Parse and print the transaction
        transactions = data['transactions']
        for record in transactions:
            print(record['transType'])

        return 'Success ! '
    
    except Exception as e:
        print(e)
        raise e



