import os, django
from pathlib import Path

#...
#DEBUG = False
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    #...    
    'yourapp',  ### [ Modify this ] ###
    'rest_framework', 
    'corsheaders', 
]

MIDDLEWARE = [
    #...
    'corsheaders.middleware.CorsMiddleware', 
]

#...
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# (Optional) If you want to use AWS S3 storage for static files and media files,
#AWS_STORAGE_BUCKET_NAME = ""
#AWS_S3_ACCESS_KEY_ID = """
#AWS_S3_SECRET_ACCESS_KEY = ""
#AWS_S3_REGION_NAME = "ap-northeast-2"

#AWS_QUERYSTRING_AUTH = False
#
#if AWS_S3_ACCESS_KEY_ID and AWS_S3_SECRET_ACCESS_KEY and AWS_STORAGE_BUCKET_NAME:
#    # 장고 4.2부터 스토리지 클래스 지정방법이 변경되었습니다.
#    if django.VERSION < (4, 2):
#        DEFAULT_FILE_STORAGE = "storage.AwsMediaStorage"
#        STATICFILES_STORAGE = "storage.AwsStaticStorage"
#    else:
#        STORAGES = {
#            "default": {
#                "BACKEND": "storage.AwsMediaStorage",
#            },
#            "staticfiles": {
#                "BACKEND": "storage.AwsStaticStorage",
#            },
#        }

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

