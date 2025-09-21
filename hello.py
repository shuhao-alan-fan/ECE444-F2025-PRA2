from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap  
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = EmailField('What is your UofT email?', validators=[DataRequired()])
    submit = SubmitField('Submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key'
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        email_input = form.email.data
        if 'utoronto' not in email_input.lower():
            flash('Please use your UofT email address.')
        else:
            old_name = session.get('name')
            old_email = session.get('email')
            if old_name is not None and old_name != form.name.data:
                flash('Looks like you have changed your name!')
            if old_name is not None and old_name != form.name.data:
                flash('Looks like you have changed your email!')
            session['name'] = form.name.data
            session['email'] = email_input

            return redirect(url_for('index'))
    return render_template(
        'index.html',
        form=form,
        current_time=datetime.utcnow(),
        name=session.get('name'),
        email=session.get('email'),
    )


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


print("hello world")
