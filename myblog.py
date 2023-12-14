import os
from app import create_app
from app.module import User

app = create_app(os.getenv('MYBLOG_CONFIG') or 'default')