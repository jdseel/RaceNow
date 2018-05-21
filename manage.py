from flask_script import Manager
from rownow import app, db, Race, Event

manager = Manager(app)

@manager.command
def deploy():
    print "resetting database..."
    db.drop_all()
    db.create_all()

    print "inserting initial data..."
    hocr = Race(name="Head of the Charles",type="Head", location='Boston, MA', about="The largest Head Race in the world in Boston, MA")
    dvr = Race(name="Dad Vail Regatta", type="Sprint", location='Philly, PA', about="The Jefferson Dad Vail Regatta, now in its 80th year, is the largest collegiate regatta in North America, with over 100 colleges and Universities from the U.S. and Canada participating. ")
    hrr = Race(name="Henley Royal Regatta", type="Henley", location='River-on-Thames, UK', about="Henley Royal Regatta is a rowing event held annually on the River Thames by the town of Henley-on-Thames, England. It was established on 26 March 1839. ")
    hocr1 = Event(name='Directors Challenge Mixed Doubles', race_type="2- - Coxless pair", age_level='Masters', results="Results Not Available", race=hocr)
    hocr2 = Event(name='Mens Alumni Eights', race_type="8+ - Coxed eight", age_level='Club', results="Results Not Available", race=hocr)
    hocr3 = Event(name='Mens Championship Singles', race_type="1X - Single scull", age_level='Collegiate', results="Results Not Available", race=hocr)
    dvr1 = Event(name='Mens V. Hwt Eight - FINAL RICHARD OBRIEN TROPHY', race_type="8+ - Coxed eight", age_level='Collegiate', results="Results Not Available", race=dvr)
    dvr2 = Event(name='Womens V. Hwt Eight - Open - FINAL EVELYN BERGMAN TROPHY', race_type="8+ - Coxed eight", age_level='Collegiate', results="Results Not Available", race=dvr)
    dvr3 = Event(name='Mens Frosh/Novice Four - FINAL LINDY CUP', race_type="4+ - Coxed four", age_level='Collegiate', results="Results Not Available", race=dvr)
    hrr1 = Event(name='THE GRAND CHALLENGE CUP', race_type="8+ - Coxed eight", age_level='Club', results="Results Not Available", race=hrr)
    hrr2 = Event(name='THE QUEEN MOTHER CHALLENGE CUP', race_type="4X - Coxless quadruple scull", age_level='Club', results="Results Not Available", race=hrr)
    hrr3 = Event(name='THE DIAMOND CHALLENGE SCULLS', race_type="1X - Single scull", age_level='Club', results="Results Not Available", race=hrr)
    db.session.add(hocr)
    db.session.add(dvr)
    db.session.add(hrr)
    db.session.add(hocr1)
    db.session.add(hocr2)
    db.session.add(hocr3)
    db.session.add(dvr1)
    db.session.add(dvr2)
    db.session.add(dvr3)
    db.session.add(hrr1)
    db.session.add(hrr2)
    db.session.add(hrr3)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
