from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = ''  # any string
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps(URL)', validators=[DataRequired(), URL(message="Invalid URL")])
    open_time = StringField('Opening Time(eg: 8AM)', validators=[DataRequired()])
    close_time = StringField('Closing Time(eg: 5:30PM)', validators=[DataRequired()])
    coffee_rating = SelectField(u'Coffee Rating', choices=["☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi_rating = SelectField(u'WiFi Rating', choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power_rating = SelectField(u'Power Rating', choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])

    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    form.validate_on_submit()
    if form.validate_on_submit():
        cafe_name = form.cafe.data
        cafe_loc = form.location.data
        opening_time = form.open_time.data
        closing_time = form.close_time.data
        coffee_rate = form.coffee_rating.data
        wifi_rate = form.wifi_rating.data
        power_rate = form.power_rating.data

        input_data = []
        input_data.extend((cafe_name, cafe_loc, opening_time, closing_time, coffee_rate, wifi_rate, power_rate))

        with open('cafe-data.csv', newline='', encoding="utf-8", mode="a") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(input_data)
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        length_of_list = len(list_of_rows)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows, length=length_of_list)


if __name__ == '__main__':
    app.run(debug=True)
