class Config:
    SECRET_KEY = "SECRET"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgre:admin@localhost/flask_contacts"
    SQLALCHEMY_TRACK_MODIFICATION = False

class Development(Config):
    Debug=True
    
    

class Testing(Config):
    pass

config = {
    "development": Development,
    "testing": Testing
}