import json
import boto3
from covid19scraper import scrapeGlobalCase

# S3 object to store the last call
US_STATE = 'PA'
bucket_name = 'wawf-covid-bucket'
file_name = 'current_webpage.txt'
object_s3 = boto3.resource('s3') \
                 .Bucket(bucket_name) \
                 .Object(file_name)
# read in old results
old_page = object_s3.get().get('Body').read()

# List of phone numbers to send to
phone_numbers = ['5555555555']

# Connect to AWS Simple Notification Service
sns_client = boto3.client('sns', region_name='us-east-1')

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    print ("[INFO] Request COVID-19 data...")
    update_covid_cases = scrapeGlobalCase(US_STATE)
    BUCKET_NAME = "wawf-covid-bucket"
    DATE = f"{update_covid_cases['date']}"
    OUTPUT_NAME = f"dataKeyTest{DATE}.json"
    OUTPUT_BODY = json.dumps(update_covid_cases)
    print (OUTPUT_BODY)
    print (f"[INFO] Saving Data to S3 {BUCKET_NAME} Bucket...")
    s3.Bucket(BUCKET_NAME).put_object(Key=OUTPUT_NAME, Body=OUTPUT_BODY)
    print (f"[INFO] Job done at {DATE}")
    newCases = int(update_covid_cases['confirmedCases'])
    oldCases = int(old_page.decode('utf-8').replace(',', ''))
    print('oldCases: ', str(oldCases))
    print('newCases: ', str(newCases))
    difCases = newCases - oldCases
    print('difCases: ', str(difCases))
    print(update_covid_cases['us_state'])
    
    if difCases == 0:
        print('No new updates.')
    else:
        print("-- New Update --")
        # Loop through phone numbers
        for cell_phone_number in phone_numbers:
            try:
                # Try to send a text message
                print(cell_phone_number)
                sns_client.publish(
                    PhoneNumber=cell_phone_number,
                    #Message= f'Local COVID19 Update: {url}',
                    Message= f'{US_STATE} COVID19 Update: {DATE} - Cases: {str(newCases)} - Increase: {str(difCases)}',
                )
                print(f"Successfuly sent to {cell_phone_number}")
            except:
                print(f"FAILED TO SEND TO {cell_phone_number}")
        # Write new data to S3
        object_s3.put(Body = str(newCases))
        print("Successfully wrote new data to S3")

#lambda_handler(0,0)
