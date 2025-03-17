from datetime import date, datetime, timedelta
import os

three_days_ago = datetime.today() - timedelta(days=3)
start_string = three_days_ago.strftime('%Y-%m-%d')
#end_string = '2022-10-21';
today = datetime.today()
end_string = today.strftime('%Y-%m-%d')

gee_token = 'gee_token.json'
gcs_token = 'gcs_token.json'

bucket_name = 'gee_image_download'
# bucket_name = os.environ.get("GS_BUCKET_NAME")
# service_account_key_file = os.environ.get("GS_SERVICE_ACCOUNT_KEY_FILE")

# mongo_username = os.environ.get("MONGO_USERNAME")
# mongo_password =  os.environ.get("MONGO_PASSWORD")
# mongo_ip_address = os.environ.get("MONGO_IP")
# database_name = os.environ.get("MONGO_DB_NAME")
# collection_name = os.environ.get("MONGO_COLLECTION_NAME")
