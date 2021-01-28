from mateo.app import db
from mateo.models.user import User

def _create_user(body):
    user = User(**body) 

    db.session.add(user)
    db.session.commit()
    
    return user
    
