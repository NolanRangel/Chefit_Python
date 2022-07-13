# controller
from flask import render_template, redirect, request, session, flash, json

from flask_app import app
from flask_app.models.model_user import User
from flask_app.models.model_pantry import Item
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)








@app.route('/recipe/finder')
def recipe_find():
    # shows pantry items by specific pantry group
    data = {
        'id': id
    }
    user_id = session['id']

    context = {
    'user': User.user_get_one(data),
    'dg': User.get_all_by_pantry('dry_goods', user_id),
    'fr': User.get_all_by_pantry('fridge', user_id),
    'fe': User.get_all_by_pantry('freezer', user_id),
    'ut': User.get_all_by_pantry('utilities', user_id),

    }
    return render_template('recipe_find.html',**context)