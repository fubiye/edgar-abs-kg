import boto3
import os
import logging

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.INFO)

S3_BUCKET_NAME = 'edgarabs'
S3_ARCHIVE_PATH = r'D:\data\edgar\enrich\s3'

s3 = boto3.resource('s3')
bucket = s3.Bucket(S3_BUCKET_NAME)

def get_local_files():
    local_files = set()
    for file in os.listdir(S3_ARCHIVE_PATH):
        local_files.add(file)
    return local_files

def get_files_in_s3():
    files = set()
    objects = bucket.objects.all()
    count = 0
    for obj in objects:
        key = obj.key
        # print(key)
        files.add(key)
        count = count + 1
    print(count)
    return files
    # print(response)
    # for content in response['Contents']:
    #     files.add(content['Key'])
    # return files
# s3 = boto3.client('s3')
# response = s3.list_objects(Bucket="edgarabs")

# Output the bucket names
# print('Existing buckets:')
# print(len(response['Contents']))

# for bucket in response['Buckets']:
#     print(f'  {bucket["Name"]}')

def download_file(filename):
    logging.info("start downloading file: {}".format(filename))
    with open(os.path.join(S3_ARCHIVE_PATH,filename),'wb') as data:
        bucket.download_fileobj(filename, data)

    logging.info("file download completed: {}".format(filename))
if __name__ == '__main__':
    local_files = get_local_files()
    s3_files = get_files_in_s3()
    print(s3_files)
    total = len(s3_files)
    count = 0
    for index,file in enumerate(s3_files):
        if file in local_files:
            # logging.info("File already exist: {}".format(file))
            print("touch {}".format(file))
            continue
        # logging.info("[{}/{}] - {}".format(count, total, file))
        count = count + 1
        # download_file(file)
    