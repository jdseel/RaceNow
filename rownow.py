import os
from flask import Flask, session, render_template, request, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

class Race(db.Model):
    __tablename__='races'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    about = db.Column(db.Text)
    events = db.relationship('Event', backref='race', cascade="delete")
class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    age_level = db.Column(db.String(256))
    results = db.Column(db.Text)
    race_id = db.Column(db.Integer, db.ForeignKey('races.id'))

@app.route('/races')
def show_all_races():
    races = Race.query.all()
    return render_template('all-races.html', races=races)


@app.route('/race/add', methods=['GET', 'POST'])
def add_races():
    if request.method == 'GET':
        return render_template('add-race.html')
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        about = request.form['about']

        # insert the data into the database
        race = Race(name=name, about=about)
        db.session.add(race)
        db.session.commit()
        return redirect(url_for('show_all_races'))


@app.route('/api/race/add', methods=['POST'])
def add_ajax_races():
    # get data from the form
    name = request.form['name']
    about = request.form['about']

    # insert the data into the database
    race = Race(name=name, about=about)
    db.session.add(race)
    db.session.commit()
    # flash message type: success, info, warning, and danger from bootstrap
    flash('Race Inserted', 'success')
    return jsonify({"id": str(race.id), "name": race.name})


@app.route('/race/edit/<int:id>', methods=['GET', 'POST'])
def edit_race(id):
    race = Race.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('race-edit.html', race=race)
    if request.method == 'POST':
        # update data based on the form data
        race.name = request.form['name']
        race.about = request.form['about']
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_races'))


@app.route('/race/delete/<int:id>', methods=['GET', 'POST'])
def delete_race(id):
    race = Race.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('race-delete.html', race=race)
    if request.method == 'POST':
        # delete the race by id
        # all related events are deleted as well
        db.session.delete(race)
        db.session.commit()
        return redirect(url_for('show_all_races'))


@app.route('/api/race/<int:id>', methods=['DELETE'])
def delete_ajax_race(id):
    race = Race.query.get_or_404(id)
    db.session.delete(race)
    db.session.commit()
    return jsonify({"id": str(race.id), "name": race.name})


@app.route('/events')
def show_all_events():
    events = Event.query.all()
    return render_template('event-all.html', events=events)


@app.route('/event/add', methods=['GET', 'POST'])
def add_events():
    if request.method == 'GET':
        races = Race.query.all()
        return render_template('event-add.html', races=races)
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        age_level = request.form['age_level']
        results = request.form['results']
        race_name = request.form['race']
        race = Race.query.filter_by(name=race_name).first()
        event = Event(name=name, age_level=age_level, results=results, race=race)

        # insert the data into the database
        db.session.add(event)
        db.session.commit()
        return redirect(url_for('show_all_events'))


@app.route('/event/edit/<int:id>', methods=['GET', 'POST'])
def edit_event(id):
    event = Event.query.filter_by(id=id).first()
    races = Race.query.all()
    if request.method == 'GET':
        return render_template('event-edit.html', event=event, races=races)
    if request.method == 'POST':
        # update data based on the form data
        event.name = request.form['name']
        event.age_level = request.form['age_level']
        event.results = request.form['results']
        race_name = request.form['race']
        race = Race.query.filter_by(name=race_name).first()
        event.race = race
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_events'))


@app.route('/event/delete/<int:id>', methods=['GET', 'POST'])
def delete_event(id):
    event = Event.query.filter_by(id=id).first()
    races = Race.query.all()
    if request.method == 'GET':
        return render_template('event-delete.html', event=event, races=races)
    if request.method == 'POST':
        # use the id to delete the event
        # event.query.filter_by(id=id).delete()
        db.session.delete(event)
        db.session.commit()
        return redirect(url_for('show_all_events'))


@app.route('/api/event/<int:id>', methods=['DELETE'])
def delete_ajax_event(id):
    event = Event.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({"id": str(event.id), "name": event.name})

@app.route('/about')
def user():
    return "About page!"


if __name__ == '__main__':
    app.run(debug=True)
