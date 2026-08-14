from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from . import db
from .models import Product

products_bp = Blueprint("products", __name__, url_prefix="/products")

@products_bp.route("/")
@login_required
def index():
    products = Product.query.order_by(Product.id.desc()).all()
    return render_template("products/index.html", products=products)

@products_bp.route("/add", methods=["GET", "POST"])
@login_required
def add():
    if request.method == "POST":
        db.session.add(Product(
            name=request.form["name"],
            category=request.form["category"],
            price=float(request.form["price"]),
            stock=int(request.form["stock"])
        ))
        db.session.commit()
        flash("Товар добавлен.", "success")
        return redirect(url_for("products.index"))
    return render_template("products/form.html", product=None)

@products_bp.route("/delete/<int:product_id>", methods=["POST"])
@login_required
def delete(product_id):
    product = db.session.get(Product, product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        flash("Товар удалён.", "success")
    return redirect(url_for("products.index"))
