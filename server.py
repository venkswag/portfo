from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def home_0():
    return render_template('index.html')


@app.route('/<string:pagename>')
def page_name(pagename):
    return render_template(pagename)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['text']
        message = data['textarea']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database_csv.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['text']
        message = data['textarea']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'data is not saved or submitted'
    else:
        return 'something wrong'
