# Interacting with the database for signup

## In this activity we will improve the signup process by adding a custom validator that queries the database to check if

an email address has already been registered before sign up is completed, and once the signup form passes validation,
save a new user to the database in the user table.

You are likely to need to refer to the following documentation:

- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/#flask_sqlalchemy.SQLAlchemy)
- [Flask contexts]((https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/))
- [SQLAlchemy](https://www.sqlalchemy.org)

Note: It can be confusing to work out which functions are in Flask-SQLAlchemy and which are in SQLAlchemy.
Flask-SQLAlchemy adds further functionality to SQLAlchemy to make it easier to work with for Flask applications. The
extensions provided by Flask-SQLAlchemy
are [summarised here](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#road-to-enlightenment).

The steps to carry out in this activity are:

1. Create a SQLAlchemy object and register the app.
2. Create a model class for a `user` that maps fields in the database table `user` to a `user` class in the Flask app.
3. Create the database when the app starts.
4. Add a custom validation to the SignupForm class to check whether an email address is already registered in the
   database.
5. Update the signup route to save the new user data to the database.

### Create global instance of the SQLAlchemy object and initialise for your Flask app

The `SQLAlchemy` class is used to control the SQLAlchemy integration to one or more Flask applications.

Create the SQLAlchemy object globally and then initialise it within the Flask app (i.e. in `create_app()`).

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_class_name):
    # Existing code here

    # Initialise 
    db.init_app(app)

    return app
```

Stop and restart the app to check it still runs.

## Create a model class for a `user` that maps fields in the database table `user` to a `user` class in the Flask app.

A model in this context is a class, or number of classes, that represent the data used in your application.

Since many applications save the same data from the class to a database, then SQLAlchemy provides functionality that
lets us more easily map a table in a database to a class in an application. One object of that class represents a row in
a table. It implements a design pattern called ORM, Object Relational Mapper.

Create a python file called `models.py`. The models are used in all the modules for the app, so let's create `models.py`
in the `my_flask_app` directory.

Add a class for a user. This needs to contain all the fields for the signup data (though it can contain other fields
than that).:

- firstname (Text, required)
- lastname (Text, required)
- email (Text, required)
- password (Text, required) Note: we will later save this in hashed rather than plain text format

The following example states the tablename that the class maps to. You don't need to do this if the class name is the
same as the table name as Flask-SQLAlchemy handles it for you unless you override it. The table name is derived from the
class name converted to lowercase and with “CamelCase” converted to “camel_case”. To override the default table name,
set the `__tablename__` class attribute.

There is then a definition for each field. Table relationships will be covered later in the course.

The code will look like the following:

```python
from example_app import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"{self.id} {self.first_name} {self.last_name} {self.email} {self.password}"
```

## Create the database when the app starts

You already created a global SQLAlchemy database object in `__init__.py` and initialised it to allow access in the Flask
app in the `create_app()` function.

Now create the user table for the database to match the User class defined in `models.py`.

This uses the Flask-SQLAlchemy `create_all()` method which is placed in `create_app` in a context.

The tables to be created need to be imported from `models.py`:

```python
def create_app(config_class_name):
    app = Flask(__name__)
    app.config.from_object(config_class_name)
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        from my_flask_app.models import User
        db.create_all()

    # blueprints here

    return app
```

Stop and restart the Flask app. You should see that it creates a database in the location you defined in the config
class e.g. `app.config['SQLALCHEMY_DATABASE_URI']`.

If you have set `SQLALCHEMY_ECHO = True` in the config then you should also see the SQL to create the table printed out
in the console in your IDE.

If you are using PyCharm Professional you
can [create a DataSource mapping](https://www.jetbrains.com/help/pycharm/sqlite.html) to view the database contents and
access a SQL console.

You can also browse the SQLite database contents using a SQLite database app such
as [DB Browser for SQLite](https://sqlitebrowser.org)

## Add a custom validation to the SignupForm class to check whether an email address is already registered

Return to `auth.forms.py` and add
a [custom validator](https://wtforms.readthedocs.io/en/2.3.x/validators/#custom-validators) that checks whether the
email address exists before it allows use to register a new user account.

```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, EqualTo, ValidationError

from my_flask_app.models import User


class SignupForm(FlaskForm):
    first_name = StringField(label='First name', validators=[DataRequired(message='First name required')])
    last_name = StringField(label='Last name', validators=[DataRequired(message='Last name required')])
    email = EmailField(label='Email address', validators=[DataRequired(message='Email adddress required')])
    password = PasswordField(label='Password', validators=[DataRequired(message='Password required')])
    password_repeat = PasswordField(label='Repeat Password',
                                    validators=[DataRequired(), EqualTo('password', message='Passwords must match')])

    def validate_email(self, email):
        users = User.query.filter_by(email=email.data).first()
        if users is not None:
            raise ValidationError('An account is already registered for that email address')
```

### Add custom validation to the LoginForm class too!

Use the knowledge you just gained in writing a custom validator for the signup form to implement custom validatios for
the login form:

- email: check if the email account exists, it not tell the user that the email address isn't registered.
- password: check that the password is valid for that email address, if not tell them the password is invalid.

## Update the signup route to save the new user data to the database

First add a methods to improve the user class so that othe password is not saved as plain text and instead is set
using the werkzeug `generate_password_hash` and retrieved using the `check_password_hash` function.

```python
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = "user"

    # etc

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
```

Modify `auth/auth.py` so that if the form passes validation then a new user is added to the database by creating a User
object with the form field data.

If there is an error when saving to the database subsequent code would fail so a try/except is used to handle any errors:

```python
from flask import Blueprint, render_template, flash, redirect, url_for, request
from sqlalchemy.exc import IntegrityError

from example_app import db
from example_app.auth.forms import SignupForm, LoginForm
from example_app.models import User

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data)
        user.set_password(form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash(f"Hello, {user.first_name} {user.last_name}. You are signed up.")
        except IntegrityError:
            db.session.rollback()
            flash(f'Error, unable to register {form.email.data}. ', 'error')
            return redirect(url_for('auth.signup'))
        return redirect(url_for('main.index'))
    return render_template('signup.html', title='Sign Up', form=form)
```

Restart the app, signup a user and then try to sign up again with the same email address. You
can check the database to see if your details have been saved.

# Working with existing databases

You can use the above method to work with an existing database too so long as you match the tablenames and fields in the
database to the table names and the fields in your models.py classes (take care to match upper/lower case).

However, you can save yourself from defining the columns in the classes by using a technique referred to as reflection
in the SQLAlchemy documentation. In this case the process for working with the database is slightly different.

In `create_app` you need to remove `db.create_all()` and replace it with:

```python
    with app.app_context():
        db.Model.metadata.reflect(bind=db.engine)
```

In `models.py` use this syntax instead:

```python
from my_flask_app import db


class User(db.Model):
    __table__ = db.Model.metadata.tables['user']
```

There is another technique you could use that is explained in this
video, [Interacting with an existing SQLite database using reflection and automap](https://www.youtube.com/watch?v=UK57IHzSh8I)