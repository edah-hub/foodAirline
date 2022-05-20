from flask import render_template,redirect,url_for,request,abort,render_template, url_for, flash, redirect, request, abort
from . import main
from flask_login import login_required,current_user
from .. import db,photos
from ..email import mail_message
from ..models import Meal,CustomerOrder,User,Contact,Checkout
from .forms import MealForm,customerLoginForm,Register,ContactForm,checkoutForm
import os
import secrets
# from PIL import Image
# from app import app


def save_picture(form_picture):
  random_hex = secrets.token_hex(8)
  _, f_ext = os.path.splitext(form_picture.filename)
  picture_fn = random_hex + f_ext
  picture_path = os.path.join(app.root_path, 'static/profile_pic', picture_fn)
  output_size = (200,200)
  image = Image.open(form_picture)
  image.thumbnail(output_size)
  image.save(picture_path)
  return picture_fn

# views
# home page
@main.route('/', methods=['GET', 'POST'])
def index():
    """
    :return: index page + data
    """

    title = 'foodAirline'
    
    meal = Meal.query.limit(4).all()
    
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        contact_email = contact_form.contact_email.data
        contact_name = contact_form.contact_name.data
        contact_message = contact_form.contact_message.data

        contact = Contact(contact_email=contact_email, contact_name=contact_name, contact_message=contact_message)

        db.session.add(contact)
        db.session.commit()
        mail_message("You have reached FoodAirline","email/user_contact",contact.contact_email,contact=contact)

        flash('Your message has been sent successfully!', 'success')

        return redirect(url_for('main.index'))


    title = 'New Account'


    return render_template('index.html',title=title,meal=meal,contact_form=contact_form)


# meals page
@main.route('/meals', methods=['GET', 'POST'])
def meals():
    """
    :return: meals page + data
    """

    title = 'Meals-foodAirline'

    meals = Meal.query.all()
    
    # user_id = current_user._get_current_object().id
    
    meals_for_one = Meal.query.filter_by(meal_count='1').all()
    meals_for_two = Meal.query.filter_by(meal_count='2').all()
    meals_for_four = Meal.query.filter_by(meal_count='4').all()
    meals_for_six = Meal.query.filter_by(meal_count='6').all()
    meals_for_eight = Meal.query.filter_by(meal_count='8').all()


    return render_template('meals.html',title=title,meals_for_one=meals_for_one,meals=meals,meals_for_two=meals_for_two,meals_for_four=meals_for_four,meals_for_six=meals_for_six,meals_for_eight=meals_for_eight)

# create meals page
@main.route('/create/<id>', methods=['GET', 'POST'])
def create(id):
    meals = Meal.query.all()
    meal = Meal.query.get(id)

    

    meal_form = MealForm()
    if meal_form.validate_on_submit():
        meal_name = meal_form.meal_name.data
        meal_description = meal_form.meal_description.data
        meal_cost = meal_form.meal_cost.data
        meal_count = meal_form.meal_count.data
        user_id = current_user._get_current_object().id
        

        new_meal_dict = Meal(meal_name=meal_name, user_id=user_id, meal_description=meal_description,meal_cost=meal_cost,meal_count=meal_count)

        new_meal_dict.save_meal()
        db.session.commit()

        flash('Your meal has been created!', 'success')

        return redirect(url_for('main.index'))

    title = 'Add Meal-FoodAirline'

    return render_template('create.html',title=title,meals=meals,meal_form=meal_form,legend='New meal')


@main.route('/upload/<id>', methods=['GET','POST'])
def upload(id):
    meal = Meal.query.get(id)
    # user_id = current_user._get_current_object().id
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        meal.meal_image_path = path
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('upload.html')


@main.route('/orders/<int:id>', methods=['GET', 'POST'])
def orders(id):

    meal = Meal.query.get(id)
    user_id = current_user._get_current_object().id
    
    # meal = Meal.query.get(id)

    user = current_user._get_current_object().username
    # meal_id = Meal.query.get(id)
    # meal = Meal.query.filter_by(meal_id=meal_id).first()

    if user is None:
        abort(404)


    return render_template('orders.html',id=user_id,meal=meal)


@main.route('/checkout/<int:id>', methods=['GET', 'POST'])
def checkout(id):

    meal = Meal.query.get(id)
    user_id = current_user._get_current_object().id
    
    form = checkoutForm()

    if form.validate_on_submit():
        user = Checkout(email=form.email.data,name=form.name.data,address=form.address.data,phone=form.phone.data)
        db.session.add(user)
        db.session.commit()

        mail_message("Your Order-foodAirline","email/checkout",user.email,user=user)

        return redirect(url_for('main.index'))


    return render_template('checkout.html',id=user_id,meal=meal,form=form)







# @app.route('/getorder')
# @login_required
# def get_order():
#     if current_user.is_authenticated:
#         customer_id = current_user.id
#         invoice = secrets.token_hex(5)
#         try:
#             order = CustomerOrder(invoice=invoice,customer_id=customer_id,orders=session['shoppingcart'])
#             db.session.add(order)
#             db.session.commit()
#             session.pop('shoppingcart')
#             flash('Your order has been sent successfully','success')
#             return redirect(url_for('home'))
#         except Exception as e:
#              print(e)
#              flash('Some thing went wrong while get order','danger')
#              return redirect(url_for('getCart'))
# @app.route('/orders/<invoice>')
# @login_required
# def orders(invoice):
#     if current_user.is_authenticated:
#         grandTotal = 0
#         subTotal = 0
#         customer_id = current_user.id
#         customer = Register.query.filter_by(id=customer_id).first()
#         orders = CustomerOrder.query.filter_by(customer_id=customer_id).first()





# @app.route('/customer/login', methods=['GET','POST'])
# def customerLogin():
#     form = customerLoginForm()
#     if form.validate_on_submit():
#         user = Register.query.filter_by(email=form.email.data).first()
#         if  user and bcrypt.check_password_hash(user.password, form.password.data):
#             login_user(user)
#             flash('You are login now!', 'success')
#             next = request.args.get('next')
#             return redirect(next or url_for('home'))
#         flash('Incorrect email and password','danger')
#         return redirect(url_for('customerLogin'))
#     return render_template('customer/login.html', form=form)
# @app.route('/customer/logout')
# def customer_logout():
#     logout_user()
#     return redirect(url_for('home'))




# @main.route('/getorder')
# @login_required
# def get_order():
#     if current_user.is_authenticated:
#         customer_id = current_user.id
#         invoice = secrets.token_hex(5)
        
#         try:
#             order = CustomerOrder(invoice=invoice,customer_id=customer_id,orders=session['shoppingcart'])
#             db.session.add(order)
#             db.session.commit()
#             session.pop('shoppingcart')
#             flash('Your order has been sent successfully','success')
#             return redirect(url_for('orders',invoice=invoice))
#         except Exception as e:
#              print(e)
#              flash('Some thing went wrong while get order','danger')
#              return redirect(url_for('getCart'))
         
# @main.route('/orders/<invoice>')
# @login_required
# def orders(invoice):
#     if current_user.is_authenticated:
#         grandTotal = 0
#         subTotal = 0
#         customer_id = current_user.id
#         customer = Register.query.filter_by(id=customer_id).first()
#         orders = CustomerOrder.query.filter_by(customer_id=customer_id).order_by(CustomerOrder.id.desc).first()
#         for _key, product in orders.orders.items():
#             discount = (product['discount']/100) * float(product['price'])
#             subTotal += float(product['price']) * init(product['quantity'])
#             subTotal -= discount
#             tax = ("%.2f" % (.06 * subTotal))
#             grandTotal = float("%.2f" % (1.06 * subTotal))
#     else:
#         return redirect(url_for('customerLogin'))
#     return render_template('customer/order.html', invoice=invoice, tax=tax, subTotal=subTotal, grandTotal=grandTotal, customer=customer, orders=orders)