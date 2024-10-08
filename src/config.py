import os

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, '..', 'instance', 'cash_flow.db')

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-default-secret-key-for-development'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_path
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY')
    UPLOAD_FOLDER = os.path.join(basedir, '..', 'uploads')

    # Print the Anthropic API key status for debugging
    print(f"Database path: {db_path}")
    print(f"Anthropic API Key status: {'Set' if ANTHROPIC_API_KEY else 'Not set'}")