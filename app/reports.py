from flask import Blueprint, render_template, request
from flask_login import login_required
from sqlalchemy import func
from .models import Order

reports_bp = Blueprint("reports", __name__, url_prefix="/reports")

@reports_bp.route("/")
@login_required
def index():
    status = request.args.get("status", "").strip()
    query = Order.query
    if status:
        query = query.filter_by(status=status)
    orders = query.order_by(Order.created_at.desc()).all()
    total = sum(order.total for order in orders)
    return render_template("reports/index.html", orders=orders, total=total, status=status)
