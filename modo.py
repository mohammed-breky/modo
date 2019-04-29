from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from form import info

app = Flask(__name__)
app.config['SECRET_KEY'] = '7b41f1b1b3a4e829d6eef16512ad05c7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///modo.db'
db = SQLAlchemy(app)


class form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    item = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"form('{self.name}', '{self.age}', '{self.item}')"


@app.route("/", methods=['GET', 'POST'])
def main():
    add_form = info()
    if add_form.validate_on_submit():
        flash('item add successfuly', 'success')
        items = form(name=add_form.name.data, age=add_form.age.data, item=add_form.item.data)
        db.session.add(items)
        db.session.commit()
        return redirect(url_for('main'))
    return render_template('index.html', form=add_form)


if __name__ == '__main__':
    app.run(debug=True)
