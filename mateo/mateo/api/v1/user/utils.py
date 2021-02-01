import bcrypt

from mateo.app import db
from mateo.models.user import User



def _get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user


def _get_user_by_email(email):
    user = User.query.filter_by(email=email).first()
    return user
    

def _create_user(body):
    user = User(**body) 

    user.password = bcrypt.hashpw(user.password, bcrypt.gensalt())

    db.session.add(user)
    db.session.commit()
    
    return user
    

def _delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()

    db.session.delete(user)
    db.session.commit()

    return True
