
Add the following to the base jinja template above the main content

```jinja2
{# Displays flashed messages on a page #}
{% with messages = get_flashed_messages() %}
    {% if messages %}
        <ul>
        {% for message in messages %}
            <li>{{ message }}</li>
        {% endfor %}
        </ul>
    {% endif %}
{% endwith %}
```

Currently our form returns if it doesn’t pass the validation, however we don’t give any feedback to the user
We can access the validation errors of our form object using form.errors. Add the following to signup.html.
```jinja2
{# Display the form validation errors #}
{% if form.errors %}
    <p><strong>The form contains errors:</strong>
    <ul>
    {% for error in form.errors %}        
        <li>{{ error }}</li>
    {% endfor %}
    </ul>
{% endif %}
```
Challenge: Improve the formatting by adding the error messages next to the input box on the form rather than a list at the top of the page.
