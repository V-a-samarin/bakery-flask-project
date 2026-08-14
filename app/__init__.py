from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "change-this-secret-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bakery.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    from .auth import auth_bp
    from .dashboard import dashboard_bp
    from .products import products_bp
    from .clients import clients_bp
    from .orders import orders_bp
    from .reports import reports_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(clients_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(reports_bp)

    with app.app_context():
        db.create_all()
        seed_data()

    return app

def seed_data():
    from .models import User, Product, Client
    from werkzeug.security import generate_password_hash

    if not User.query.first():
        db.session.add(User(
            username="admin",
            password_hash=generate_password_hash("admin123"),
            full_name="Администратор"
        ))
    if not Product.query.first():
        db.session.add_all([
            Product(name="Батон нарезной", category="Хлеб", price=65, stock=40),
            Product(name="Круассан классический", category="Выпечка", price=120, stock=25),
            Product(name="Торт «Медовик»", category="Торты", price=1450, stock=8),
            Product(name="Эклер ванильный", category="Кондитерские изделия", price=180, stock=20),
        ])
    if not Client.query.first():
        db.session.add_all([
            Client(name="Иванов Иван Иванович", phone="+7 900 000-00-01", email="ivanov@example.com"),
            Client(name="Петрова Анна Сергеевна", phone="+7 900 000-00-02", email="petrova@example.com"),
        ])
    db.session.commit()
