# Powder_data_entry

This is a small project to create a powder data registration system. 

## Ingredient Registration Form

Run the Flask application to start a simple ingredient registration form backed by an SQLite database. The app exposes a small web page where you can register ingredients.

```bash
pip install -r requirements.txt
python app.py  # or `gunicorn app:app` for production
```

Navigate to `http://localhost:5000` in your browser (or the port specified in the `PORT` environment variable) to use the form. The form is a skeleton where you can add new fields in `templates/ingredient_form.html` and modify the table definition in `app.py`.

### Hosting

To run the application on a hosting platform such as Heroku or any container platform, point a web server like `gunicorn` at the `app` module:

```bash
gunicorn app:app
```

Create a `Procfile` containing the above command to make deployment simpler.
