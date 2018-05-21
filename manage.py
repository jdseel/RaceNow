from flask_script import Manager
from rownow import app, db, Race, Event

manager = Manager(app)

@manager.command
def deploy():
    print "resetting database..."
    db.drop_all()
    db.create_all()

    print "inserting initial data..."
    hocr = Race(name="Head of the Charles", about="The largest Head Race in the world in Boston, MA")
    dvr = Race(name="Dad Vail Regatta", about="Collegiate championship race")
    event1 = Event(name='Mens Single', age_level='Masters', results="Results Not Available", race=dvr)
    db.session.add(hocr)
    db.session.add(dvr)
    db.session.add(event1)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
