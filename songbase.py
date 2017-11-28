import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY']='ldjakljflajfklj'



basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)

class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    about = db.Column(db.Text)
    songs = db.relationship('Song', backref='artist')

class Song(db.Model):
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    year = db.Column(db.Integer)
    lyrics = db.Column(db.Text)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))

@app.route('/')
def home():
    # return '<h1>hello world!!!!!! lalallal</h1>'
    return render_template('index.html')

@app.route('/artists')
def show_all_artists():
    artists = Artist.query.all()
    return render_template('artist-all.html', artists=artists)

@app.route('/songs')
def show_all_songs():
    songs = Song.query.all()
    return render_template('song-all.html', songs=songs)



@app.route('/form-demo', methods=['GET', 'POST'])
def form_demo():
    if request.method == 'GET':
        first_name = request.args.get('first_name')
        if first_name:
          return render_template('form-demo.html', first_name=first_name)
        else:
          first_name = session.get('first_name')
          return render_template('form-demo.html', first_name=first_name)
    if request.method == 'POST':
        session['first_name'] = request.form['first_name']
        # return render_template('form-demo.html', first_name=first_name)
        return redirect(url_for('form_demo'))

@app.route('/artist/add', methods=['GET', 'POST'])
def add_artists():
    if request.method == 'GET':
        return render_template('artist-add.html')
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        about = request.form['about']

        # insert the data into the database
        artist = Artist(name=name, about=about)
        db.session.add(artist)
        db.session.commit()
        return redirect(url_for('show_all_artists'))

@app.route('/artist/edit/<int:id>', methods=['GET', 'POST'])
def edit_artists():
    artist = Artist.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('artist-edit.html', artist= artist)
    if request.method == 'POST':
        # get data from the form
        artist.name = request.form['name']
        artist.about = request.form['about']

        # insert the data into the database
        artist = Artist(name=name, about=about)
        db.session.add(artist)
        db.session.commit()
        return redirect(url_for('show_all_artists'))

@app.route('/song/add', methods=['GET', 'POST'])
def add_songs():
    if request.method == 'GET':
        return render_template('song-add.html')
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        about = request.form['year']
        lyrics = request.form['lyrics']
        artist_name = request.form['artist_name']

        artist = Artist.query.filter_by(name=artist_name).first()

        # insert the data into the database
        song = Song(name=name, year=year, lyrics=lyrics, artist=artist)
        db.session.add(song)
        db.session.commit()
        return redirect(url_for('show_all_songs'))




# @app.route('/songs')
# def get_all_songs():
#    songs =[
#        'song1',
#        'song2',
#        'song3'
#    ]
#    return render_template('songs.html', songs=songs)


@app.route('/user/<string:name>/')
def get_user(name):
    # return '<h1>hello %s your age is %d</h1>' % (name, 20)
    return render_template('user.html', user_name=name)

if __name__ == '__main__':
    app.run()
