from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from . import db
from .models import Order, Client, Product

orders_bp = Blueprint("orders", __name__, url_prefix="/orders")

@orders_bp.route("/")
@login_required
def index():
    orders = Order.query.order_by(Order.created_at.desc()).all()
    return render_template("orders/index.html", orders=orders)

@orders_bp.route("/add", methods=["GET", "POST"])
@login_required
def add():
    products = Product.query.order_by(Product.name).all()
    clients = Client.query.order_by(Client.name).all()
    if request.method == "POST":
        product = db.session.get(Product, int(request.form["product_id"]))
        client_id = request.form.get("client_id") or None
        quantity = int(request.form["quantity"])
        if not product or quantity < 1:
            flash("Проверьте данные заказа.", "danger")
            return redirect(url_for("orders.add"))
        if product.stock < quantity:
            flash("Недостаточно товара на складе.", "danger")
            return redirect(url_for("orders.add"))
        order = Order(
            product_id=product.id,
            client_id=int(client_id) if client_id else None,
            quantity=quantity,
            total=product.price * quantity,
            status="Новый"
        )
        product.stock -= quantity
        db.session.add(order)
        db.session.commit()
        flash("Заказ создан.", "success")
        return redirect(url_for("orders.index"))
    return render_template("orders/form.html", products=products, clients=clients)
