from flask import render_template, url_for, flash, redirect, request, jsonify
from app import app, db
from app.forms import RegistrationForm
from app.models import Employee

#route for the home page
@app.route('/')
@app.route('/home')
def home():
    employee = []
    if Employee.query.all():
        employee = Employee.query.filter_by(is_deleted='0')
    return render_template('home.html', posts = employee)

#route for delete the employee
@app.route('/deleteEmployee', methods=['GET', 'POST'])
def deleteEmployee():
    if request.method == 'POST':
        id = request.form['data']
        employee = Employee.query.filter_by(id=id).first()
        employee.is_deleted = '1'
        db.session.commit()
        return '1'
        
#route for add the employee
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = Employee(name = form.name.data, designation = form.designation.data,
                            address = form.address.data, phone = form.phone.data)
            db.session.add(user)
            db.session.commit()
            flash('Employee Added successfully','success')
            return redirect(url_for('home'))
        else:
            flash('Somthing went wrong', 'danger')
    return render_template('register.html', title='Register', form=form)

#route for 404 page
@app.errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404

#route for 500 page
@app.errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 404
