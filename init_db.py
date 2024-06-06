from App import db, app

with app.app_context():
    db.create_all()
    print("Veritabanı başarıyla oluşturuldu!")
