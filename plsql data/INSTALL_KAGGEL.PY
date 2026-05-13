from kaggle.api.kaggle_api_extended import KaggleApi
import boto3
def load_kaggel(link):

    # authenticate
    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files(
        # 'mehmettahiraslan/customer-shopping-dataset'
        link,
        path='kaggel_data',
        unzip=True
    )

    print("Dataset Downloaded Successfully")


def create_bucket(bucket_name):
    
    s3 = boto3.client('s3')

    # bucket_name='regex-rohit-mittal-1234'

    create_b =s3.create_bucket(
        Bucket= bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'ap-south-1'
        }
    )
    print("bucket created sucessfully")
    print(create_b)

def load_data_bucket(file_name,bucket_name,object_name,):
# file_name='C:\\Users\\Rohit\\Downloads\\newplacementdata - newplacementdata.csv'
# bucket_name="regex-rohit-mittal-123"
# object_name='my_first_task'
    
    s3 = boto3.client('s3')
    s3.upload_file(file_name, bucket_name, object_name)

    print("File uploaded successfully")

# create_bucket("regex-rohit-mittal-1234")
load_data_bucket('C:\\Users\\Rohit\\OneDrive\\Desktop\\ptthon code\\kaggel_data\\customer_shopping_data.csv','regex-rohit-mittal-1234','my_first_kaggel_file')