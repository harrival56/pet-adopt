from flask import Flask, request, redirect, render_template, flash
from flask.helpers import flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPet


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://:5433/adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "harrison"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


connect_db(app)

pet_default_img = "https://images.unsplash.com/photo-1597176116047-876a32798fcc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=667&q=80"


@app.route("/")
def home_page():
    """List pets to the home page"""
    pets = Pet.query.all()
    return render_template("home.html", pets=pets, pdi=pet_default_img)

@app.route("/<int:p_id>/detail")
def detail(p_id):
    """show full information about a pet"""
    pet = Pet.query.get_or_404(p_id)
    return render_template("detail.html", pet=pet)

@app.route("/pet/new", methods=["GET", "POST"])
def add_pet():
    """display form to the user"""
    form = AddPet()
    if form.validate_on_submit():
        name = form.name.data
        specie = form.species.data
        photo = form.photo_url.data
        age = form.age.data
        note = form.note.data
        av = form.available.data
        new_pet = Pet(name=name, species=specie, photo_url=photo, age=age, note=note, available=av)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{name} has been added to the list for adoption.")
        return redirect("/")
    else:    
        return render_template("add_pet.html",form=form )


@app.route("/pet/<int:p_id>/edit", methods=["GET", "POST"])
def edit_pet(p_id):
    """shows form and update the database after edit"""
    pet = Pet.query.get_or_404(p_id)
    form = AddPet(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.note = form.note.data
        pet.available = form.available.data
        flash(f"{pet.name} has been updated.")
        db.session.commit()
        return redirect(f"/{p_id}/detail")
    else:
        return render_template("edit_pet.html", form=form)
