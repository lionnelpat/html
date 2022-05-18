from flask import render_template, Flask, request, redirect, url_for
import mailer as mail

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name="accueil")

@app.route('/about')
def about():
    return render_template('about.html', name="A propos")

@app.route('/services')
def services():
    return render_template('services.html', name="Services")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        message = request.form['message']

        mail.send_email(email, message)

        app.logger.info('%s message recieved successfully', fullname)
        return redirect(url_for("contact", name = fullname))
    else:
        return render_template('contact.html', name="Contact")