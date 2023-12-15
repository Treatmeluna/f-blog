import os
from app import create_app
from app.models import User

app = create_app(os.getenv('MYBLOG_CONFIG') or 'default')