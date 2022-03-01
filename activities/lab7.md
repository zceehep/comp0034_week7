# Lab 7

## Complete activities 1 to 4 (if you have not already done so)

Complete activities 1 to 4 using the simple `my_flask_app` that you created last week (you hopefully gave it a more
meaningful name than 'my_flask_app'). Or you can use the `my_flask_app` code in this repo.

## Apply the concepts to your coursework

Make a start on applying the concepts covered in activities 1 to 4 to your coursework. For example, you could consider
the list below (this isn't everything you will need to do!)

### Creating Jinja templates

#### Relevant documentation

- [Activity 1: Jinja templates](https://github.com/nicholsons/comp0034_week7/blob/master/activities/1_create_base_jinja_template.md)
- [Jinja Documentation](https://jinja.palletsprojects.com/en/3.0.x/templates/)
- [Bootstrap setup](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
- [Bootstrap navbar](https://getbootstrap.com/docs/5.1/components/navbar/)
- [Flask routes](https://flask.palletsprojects.com/en/2.0.x/quickstart/#routing)

#### Tasks for your coursework

1. Create a `base.html` template with Jinja variables that all includes the HTML structure and page layout elements that
  all the pages will inherit.
    - Consider using your wireframes from COMP0035 coursework 2 as a guide.
    - Use third party CSS such as bootstrap (be consistent with your Dash app!)
2. Create a Jinja template for the home page (`index.html`) that extends the `base.html`
3. Create a route for the home page to render the index template.

### Creating forms

#### Relevant documentation

- [Activity 2: Creating forms](https://github.com/nicholsons/comp0034_week7/blob/master/activities/2_create_signup_form.md)
- [Flask_WTF documentation](https://flask-wtf.readthedocs.io/en/1.0.x/)
- [Flask routes](https://flask.palletsprojects.com/en/2.0.x/quickstart/#routing)
- [Jinja Documentation](https://jinja.palletsprojects.com/en/3.0.x/templates/)
- [Miguel Grinberg: web forms](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms)

#### Tasks for your coursework

4. Enable your app to use CSRF protection by adding this to the main `__init__.py` (see activity 2).
5. Create a python form class using Flask-WTF for a register/sign up form using the fields that you defined in your
   COMP0035 coursework (you likely had a user table in your database design that would be useful, and/or a wireframe for
   signup or register).
6. Create a register/signup Jinja template to match the fields in the form.
7. Create a route for the register/signup page.

Repeat steps 5 - 7 to create a login form.


### Enable Flask flash messaging

#### Relevant documentation

- [Activity 3: Enable flash messaging](https://github.com/nicholsons/comp0034_week7/blob/master/activities/3_enable_flash_messaging.md)
- [Flask message flashing](https://flask.palletsprojects.com/en/2.0.x/patterns/flashing/)

#### Tasks for your coursework

8. Enable Flash messaging. You are not required to do this but you are likely to find it useful as it is a useful way to provide feedback to the
user of your application.


### Create a database and update your routes to interact with it

#### Relevant documentation

- [Activity 4: Database interaction](https://github.com/nicholsons/comp0034_week7/blob/master/activities/4_database_interaction.md)
- [Flask-SQL Alchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application)
- [Viewing SQLite databases with Pycharm Professional](https://www.jetbrains.com/help/pycharm/sqlite.html)
- [SQLite database explorer for VS Code](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite)

#### Tasks for your coursework

Flask-SQLAlchemy classes are use **both** as the classes in your app (e.g. the class diagram from COMP0035 coursework 2)
and the database table design (the ERD from COMP0035 coursework 2). This implements a design pattern called ORM Object
Relation Map; it maps object parameters to the structure of a relational database table. You can still add
methods/functions to the classes that are used in the app but not the database. You do not need to write database CRUD
methods as SQLAlchemy provides these for you.

9. Enable your app to work with Flask-SQLAlchemy by creating a flask SQLAlchemy object and initialising your Flask app to
  it (hint: see `__init__.py` and `create_app()`)
10. Create a `models.py` and define a python User class that matches the user fields in your signup / coursework 2
  database design. The class inherits the Model class from your Flask SQLAlchemy object.
11. Update `create_app()` so that after the Flask app is initialised to SQLAlchemy then you import the classes and the use
  the `create_all()` function to create the tables in the database.
12. Update your signup process so that it saves a new user to the database. Use an appropriate database viewer for your
  IDE to check that the data is stored.



