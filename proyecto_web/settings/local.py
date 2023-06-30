from .base import *
import os
DEBUG = False

ALLOWED_HOSTS = ["*"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroku_c55134a282cac58',
        'USER':'b5fd4836081423',
        'PASSWORD':'24ed6d26',
        'HOST': 'us-cdbr-east-06.cleardb.net',
        
       # 'OPTIONS': {
        #    'driver': 'ODBC Driver 17 for SQL Server',
        #},
    }
}


#STATIC_URL = 'static/'
#STATICFILES_DIRS = [BASE_DIR.child('static')]

#MEDIA_URL = "/media/"
#MEDIA_ROOT = BASE_DIR.child('media')

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'arturo948661842@gmail.com'
EMAIL_HOST_PASSWORD = 'hjrekawrcrqrcdgn'
EMAIL_PORT = 587

STATIC_ROOT =os.path.join(BASE_DIR,'staticfiles')
STATIC_TMP = os.path.join(BASE_DIR,'static')
STATIC_URL = 'static/'
os.makedirs(STATIC_TMP,exist_ok=True)
os.makedirs(STATIC_ROOT,exist_ok=True)
STATICFILES_DIRS=(
    os.path.join(BASE_DIR,'static'),
)

