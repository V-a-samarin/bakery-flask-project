from flask import Blueprint, render_template
from flask_login import login_required
from sqlalchemy import func
from .models import Product, Client, Order

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
@login_required
def index():
    products = Product.query.count()
    clients = Client.query.count()
    orders = Order.query.count()
    sales = db_sum = db_sum = Order.query.with_entities(func.coalesce(func.sum(Order.total), 0)).scalar()
    return render_template("dashboard/index.html",
                           products=products, clients=clients, orders=orders, sales=sales)
