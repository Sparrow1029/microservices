from project import db
from project.api.models import User


def add_user(username, email, password):
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return user


def add_admin_user(username, email, password):
    new_user = add_user(username, email, password)
    # update user
    user = User.query.filter_by(email=new_user.email).first()
    user.admin = True
    db.session.commit()
