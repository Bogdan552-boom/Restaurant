from online_restaurant_db import Base, engine, Users
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash

# ---- Створюємо таблиці ----
Base.metadata.create_all(engine)

# ---- Додаємо адміна ----
with Session(engine) as cursor:
    # Перевіримо, чи адмін вже існує
    admin = cursor.query(Users).filter_by(nickname='Admin').first()

    if not admin:
        admin = Users(
            nickname='Admin',
            email='admin@gmail.com',
            password=generate_password_hash('12345678')
        )
        cursor.add(admin)
        cursor.commit()
        print("Адміна створено!")
    else:
        print("Адмін вже існує")