from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from . import db
from .models import Client

clients_bp = Blueprint("clients", __name__, url_prefix="/clients")

@clients_bp.route("/")
@login_required
def index():
    clients = Client.query.order_by(Client.id.desc()).all()
    return render_template("clients/index.html", clients=clients)

@clients_bp.route("/add", methods=["GET", "POST"])
@login_required
def add():
    if request.method == "POST":
        db.session.add(Client(
            name=request.form["name"],
            phone=request.form["phone"],
            email=request.form["email"]
        ))
        db.session.commit()
        flash("Клиент добавлен.", "success")
        return redirect(url_for("clients.index"))
    return render_template("clients/form.html")
