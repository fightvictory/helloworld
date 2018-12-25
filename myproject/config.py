import os

basedir = os.path.abspath(os.path.dirname(__file__))

print(basedir)

SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
CSRF_ENABLED = True
SECRET_KEY = 'vdmOnTh2yfytxag7UIZExC0Q6YvsoEhQ'
