import os 

class Config:
	SECRET_KEY ='78d6cc4fff558ed2003e0e72b340026b'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	Mail_SERVER ='smtp.googleemail.com'
	Mail_PORT = 587
	Mail_USE_TLS = True
	Mail_USERNAME = os.environ.get('EMAIL_USER')
	Mail_PASSWORD = os.environ.get('EMAIL_PASS')