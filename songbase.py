from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    # return '<h1>hello world!!!!!! lalallal</h1>'
    return render_template('index.html')

@app.route('/songs')
def get_all_songs():
    songs =[
        'song1',
        'song2',
        'song3'
    ]
    return render_template('songs.html', songs=songs)


@app.route('/user/<string:name>/')
def get_user(name):
    # return '<h1>hello %s your age is %d</h1>' % (name, 20)
    return render_template('user.html', user_name=name)

if __name__ == '__main__':
    app.run()
