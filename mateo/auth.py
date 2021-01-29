import bcrypt

from  mateo.models.user import User

"""
These functions are required handlers for flask_jwt. 

UserId object needs to be used instead of the standard User object 
because flask_jwt doesn't like the UUID object under User.id

"""
class UserId(object):
    def __init__(self, id):
        self.id = str(id)

def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.checkpw(password, user.password):
        user_id = UserId(user.id)
        return user_id

def identity(payload):
    user_id = payload['identity']
    user = User.query.filter_by(id=user_id).first()
    return user

