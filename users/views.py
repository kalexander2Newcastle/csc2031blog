from flask import Blueprint, render_template
from users.forms import RegisterForm
from flask import request, redirect, url_for
from wtforms.validators import DataRequired
from wtforms.validators import Email
from wtforms.validators import Length

users_blueprint = Blueprint('users', __name__, template_folder='templates')


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        print(request.form.get('username'))
        # username = username(validators=[DataRequired()])
        print(request.form.get('password'))
        # password = PasswordField(validators=[Length(min=8, max=15)])
        return redirect(url_for('users.login'))

    return render_template('users/register.html', form=form)



@users_blueprint.route('/login')
def login():
    return render_template('users/login.html')
