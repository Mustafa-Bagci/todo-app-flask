from todo import app, db, User

with app.app_context():
    admin = User(username='admin', email='admin@example.com')
    db.session.add(admin)
    db.session.commit()
    print("New task added to the database.")
