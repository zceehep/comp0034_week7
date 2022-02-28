# Lab 7

## Complete activities 1 to 4 (if you have not already done so)

Complete activities 1 to 4 using the simple `my_flask_app` that you created last week (you hopefully gave it a more
meaningful name than 'my_flask_app'). Or you can use the `my_flask_app` code in this repo.

- [Jinja Documentation](https://jinja.palletsprojects.com/en/3.0.x/templates/)
- [Flask routes](https://flask.palletsprojects.com/en/2.0.x/quickstart/#routing)
- [Flask_WTF documentation](https://flask-wtf.readthedocs.io/en/1.0.x/)
- [Flask-SQL Alchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application)

## Consider creating the following for your coursework

Make a start on applying the concepts covered in activities 1 to 4 to your coursework. For example, you could consider the list below (this
isn't everything you will need to do!)

If you are not using blueprints then you can ignore the 'main' and 'auth' prefixes in the following.

- Add a base/layout html template that all pages will inherit. You may want to try and recreate the basic layout using your wireframes from COMP0035 coursework 2.
- Create a Jinja2 template for the home page (index.html) that extends the base/layout.html
- Create a route for the home page in main/routes.py to render the template.
- Create a form using Flask-WTF for a register/sign up form using the fields that you defined in your COMP0035
  coursework (you likely had a user table in your database design that would be useful, and/or a wireframe for signup or
  register). Don't forget to enable CSRF protection.
- Create a register/signup Jinja2 template to match the fields in the form.
- Create a route in auth/routes.py for the register/signup page.
- Create a form using Flask-WTF for a login using appropriate fields from your signup
- Create a login Jinja2 template to match the fields in the form.
- Create a route in auth/routes.py for the login.
- Enable your app to work with Flask-SQLAlchemy (hint: `create_app()`)
- Create a models.py and define a table that matches the user fields in your signup / coursework 2 database design for a
  user
