from app import app, db, ToDo  # not `todo` anymore

with app.app_context():
    db.create_all()
    print("✅ DB created!")
