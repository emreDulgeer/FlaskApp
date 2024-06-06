from werkzeug.security import generate_password_hash
from App import db, app
from Models import User

with app.app_context():
    admin_user = User(username='admin', email='admin@blog.com', password=generate_password_hash('123456', method='pbkdf2:sha256', salt_length=8), role='admin')
    db.session.add(admin_user)
    db.session.commit()
    print("Admin kullanıcı başarıyla oluşturuldu!")
