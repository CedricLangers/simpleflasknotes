from flask import Blueprint, render_template, request, flash, jsonify, url_for, redirect
from flask_login import login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from . models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note,user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category = 'success')
            
    return render_template("home.html", user=current_user)

@views.route('/delete-note/<int:id>')
def delete_note(id):
    note_to_delete = Note.query.get_or_404(id)

    try:
        db.session.delete(note_to_delete)
        db.session.commit()
        return redirect(url_for('views.home'))
    except:
        flash("Problem deleting the note!", category='error')