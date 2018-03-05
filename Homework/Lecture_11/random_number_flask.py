

from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators
from os import environ
import random



class GuessForm(FlaskForm):
    num = IntegerField('Number to guess', [validators.required(),])


app = Flask(__name__)
app.config.update(
        DEBUG = True,
        SECRET_KEY = 1234,
        WTF_CSRF_ENABLED = False,
        )
random.seed(environ['FLASK_RANDOM_SEED'])
NUM_GUESS = random.randint(1, 100)

@app.route('/')
def home():
    greeting = 'Число загадано!'
    return greeting

@app.route('/guess', methods=['GET', 'POST'])
def guess():
    global NUM_GUESS
    if request.method == 'POST':
        form = GuessForm(request.form)
        print(NUM_GUESS)
        if form.validate():
            if form.num.data > NUM_GUESS:
                return ('>', 200)
            elif form.num.data < NUM_GUESS:
                return ('<', 200)
            elif form.num.data == NUM_GUESS:
                NUM_GUESS = random.randint(1, 100)
                print(NUM_GUESS)
                return ('=', 200)
    else:
        return 'I need a post request!'

    return 'Something went wrong'

if __name__ == '__main__':

    app.run()





















































#from contextlib import contextmanager
#
#
#@contextmanager
#def open_file(filename, mode='r'):
#    try:
#        file = open(filename, mode)
#    except Exception as e:
#        print(e)
#
#    yield file
#
#    if file is not None:
#        file.close()
#
#
#with open_file('does-not-exist') as f:
#    file = f.read()
#    print(file)
#
#print('Done')



# os.environ[]
# simple-settings
