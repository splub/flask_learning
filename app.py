from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return ("Index Page")
@app.route('/user/<int:num_for>')
def user_id(num_for):
    return 'hello %d' % num_for

@app.route('/about')
def about():
    return ('learning flask')

@app.route('/about/')
def path():
    return 'this is a path'

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=True)
