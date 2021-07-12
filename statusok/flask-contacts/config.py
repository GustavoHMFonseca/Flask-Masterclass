class Config:
    SECRET_KEY = "SECRET"
    SQLALCHEMY_DATABASE_URI = "sqlite:///contacts.db"
    SQLALCHEMY_TRACK_MODIFICATION = False

class Development(Config):
    Debug=True
    
    

class Testing(Config):
    pass

config = {
    "development": Development,
    "testing": Testing
}