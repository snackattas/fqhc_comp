# https://github.com/bradleyg/django-s3direct
import os

# AWS keys
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

# The region of your bucket, more info:
# http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region
S3DIRECT_REGION = os.environ.get('AWS_S3DIRECT_REGION')

# Destinations, with the following keys:
#
# key [required] Where to upload the file to, can be either:
#     1. '/' = Upload to root with the original filename.
#     2. 'some/path' = Upload to some/path with the original filename.
#     3. functionName = Pass a function and create your own path/filename.
# auth [optional] An ACL function to whether the current Django user can perform this action.
# allowed [optional] List of allowed MIME types.
# acl [optional] Give the object another ACL rather than 'public-read'.
# cache_control [optional] Cache control headers, eg 'max-age=2592000'.
# content_disposition [optional] Useful for sending files as attachments.
# bucket [optional] Specify a different bucket for this particular object.
# server_side_encryption [optional] Encryption headers for buckets that require it.


key = os.environ.get('AWS_KEY')
S3DIRECT_DESTINATIONS = {
    AWS_STORAGE_BUCKET_NAME: {
        # REQUIRED
        'key': key,

        # # OPTIONAL
        # 'auth': lambda u: u.is_authenticated, # Default allow anybody to upload
        'allowed': ['application/pdf'], # Default allow all mime types
        # 'bucket': 'pdf-bucket', # Default is 'AWS_STORAGE_BUCKET_NAME'
        # 'acl': 'private', # Defaults to 'public-read'
        # 'cache_control': 'max-age=2592000', # Default no cache-control
        # 'content_disposition': 'attachment' # Default no content disposition
        # 'content_length_range': (5000, 20000000), # Default allow any size
        # 'server_side_encryption': 'AES256', # Default no encryption
    }
}
