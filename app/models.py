from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import UserMixin, current_user
from . import login_manager
from datetime import datetime


class User(UserMixin, db.Model):
    """
    defines User objects
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    meals = db.relationship('Meal', backref='user', lazy='dynamic')
    package = db.relationship('Package', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'Users {self.username}'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    

class Contact(db.Model):
    """
    defines Meal objects
    """

    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    contact_id = db.Column(db.Integer)
    contact_name = db.Column(db.String(255))
    contact_email = db.Column(db.String(255))
    contact_message = db.Column(db.String(2500))


    def save_contact(self):
        db.session.add(self)
        db.session.commit()


class Meal(db.Model):
    """
    defines Meal objects
    """

    __tablename__ = 'meals'

    id = db.Column(db.Integer, primary_key=True)
    meal_id = db.Column(db.Integer)
    meal_name = db.Column(db.String(255))
    meal_image_path = db.Column(db.String(255))
    meal_description = db.Column(db.String(2500))
    meal_cost = db.Column(db.Integer)
    meal_count = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    package = db.relationship('Package', backref='meal', lazy='dynamic')

    def save_meal(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_meals(cls, id):
        meals = Meal.query.filter_by(meal_id=id).all()
        return meals


class Package(db.Model):
    """
    defines Package objects
    """

    __tablename__ = 'packages'

    id = db.Column(db.Integer, primary_key=True)
    package_id = db.Column(db.Integer)
    package_name = db.Column(db.String(255))
    package_image_path = db.Column(db.String(255))
    package_description = db.Column(db.String(255))
    package_cost = db.Column(db.String(255), index=True, nullable=False)

    meal_id = db.Column(db.Integer, db.ForeignKey('meals.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)



class CustomerOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_status = db.Column(db.String(20), default='Pending', nullable=False)
    user_order = db.Column(db.String(255))
    user_number = db.Column(db.Integer)
    
    meal_id = db.Column(db.Integer, db.ForeignKey('meals.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    

class Checkout(db.Model):
    id = id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    address = db.Column(db.String(255))
    
    



# class JsonEcodedDict(db.TypeDecorator):
#     impl = db.Text
#     def process_bind_param(self, value, dialect):
#         if value is None:
#             return '{}'
#         else:
#             return json.dumps(value)
#     def process_result_value(self, value, dialect):
#         if value is None:
#             return {}
#         else:
#             return json.loads(value)
        
# class CustomerOrder(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     invoice = db.Column(db.String(20),unique=True, nullable=False)
#     status = db.Column(db.String(20), default='Pending', nullable=False)
#     customer_id = db.Column(db.Integer, unique=False, nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
#     orders = db.Column(JsonEcodedDict)
#     def __repr__(self):
#         return '<CustomerOrder %r>' % self.invoice
#     db.create_all()