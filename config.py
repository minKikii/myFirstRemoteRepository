debug=True
import os
SECRET_KEY=os.urandom(24)

DB_USERNAME='root'
DB_PASSWORD='123456'
DB_HOST='127.0.0.1'
DB_PORT='3306'
DATABASE='test'
CMS_USER_ID='HEBOANHERE'

DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8mb4' % (DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

# UEditor的相关配置
UEDITOR_UPLOAD_TO_QINIU = True
UEDITOR_QINIU_ACCESS_KEY = "M4zCEW4f9XPanbMN-Lb9O0S8j893f0e1ezAohFVL"
UEDITOR_QINIU_SECRET_KEY = "7BKV7HeEKM3NDJk8_l_C89JI3SMmeUlAIatzl9d4"
UEDITOR_QINIU_BUCKET_NAME = "hyvideo"
UEDITOR_QINIU_DOMAIN = "http://7xqenu.com1.z0.glb.clouddn.com/"