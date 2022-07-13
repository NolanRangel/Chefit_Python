# controller
from flask import render_template, redirect, request, session, flash, json

from flask_app import app
from flask_app.models.model_user import User
from flask_app.models.model_pantry import Item
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


# RESTful architecture

# /user/new
# /user/create
# /user/<int:id>
# user/edit/<int:id>
# user/update<int:id>/
# user/destroy<int:id>/


# pantry edit by produce/starch/protein/dairy
@app.route('/item/create',methods=['POST'])
def item_create():
    # adds new pantry item by pantry and pantry group
    
    #LOGIN CHECK
    if not session.get('id'):
        return render_template('index.html')

    #FIELD VALIDATION/
    else:
        if not Item.validate_item(request.form):
            #REDIRECTS BACK TO SAME PAGE IF FIELDS INVALID/FIELDS NOT UPDATED
            return redirect(request.referrer)
        print(request.form)
        #DOUBLE LOGIN CHECK??
        if not session.get('id'):
            return render_template('index.html')
        #CONSTRUCTS ITEM AND PASSES AS data
        else:
            data = {
            "pantry": request.form["pantry"],
            "pantry_group" : request.form["pantry_group"],
            "description" : request.form["description"],
            "amount" : request.form["amount"],
            "cost" : request.form["cost"],
            "created_at" : request.form["created_at"],
            "user_id": session['id']
            }

            print('***')
            print(request.form)
            print('***')

            #CREATES NEW RECIPE
            Item.item_create(data)

            return redirect(request.referrer)
        
@app.route('/item/add')
def item_add():
    # shows pantry items by specific pantry group
    
    return render_template('item_add.html')







# pantries show by produce/starch/protein/dairy
@app.route('/produce')
def produce():
    # shows pantry items by specific pantry group
    return render_template('pantries_show.html')


@app.route('/protein')
def protein():
    # shows pantry items by specific pantry group
    return render_template('')


@app.route('/starch')
def starch():
    # shows pantry items by specific pantry group
    return render_template('')


@app.route('/dairy')
def dairy():
    # shows pantry items by specific pantry group
    return render_template('')


@app.route('/condiments')
def condiments():
    # shows pantry items by specific pantry group
    return render_template('')


@app.route('/spices')
def spices():
    # shows pantry items by specific pantry group
    return render_template('')

# pantries show by dry goods/ fridge/ freezer/utilities


@app.route('/pantry/dry_goods')
def dry_goods():
    # shows dry_goods pantry by group
    data = {
        'id': id
    }
    user = User.user_get_one(data)

    return render_template('dry_goods.html', user=user)


@ app.route('/pantry/fridge')
def fridge():
    # shows fridge pantry by group
    data = {
        'id': id
    }
    user = User.user_get_one(data)
    return render_template('fridge.html', user=user)


@ app.route('/pantry/freezer')
def freezer():
    # shows freezer pantry by group
    data = {
        'id': id
    }
    user = User.user_get_one(data)
    return render_template('freezer.html', user=user)


@ app.route('/pantry/utilities')
def utilities():
    # shows utilities pantry by group
    data = {
        'id': id
    }
    user = User.user_get_one(data)
    return render_template('utilities.html', user=user)



# pantry route from dashboard link
@ app.route('/pantry')
def pantry():
    # pull in total items, cost of items, and last update formatted
    
    user_id = session['id']
    context = {
    # 'user': User.user_get_one(data),
    'dg': User.get_totals_by_pantry('dry_goods',user_id),
    'fr': User.get_totals_by_pantry('fridge',user_id),
    'fe': User.get_totals_by_pantry('freezer',user_id),
    'ut': User.get_totals_by_pantry('utilities',user_id),

    }
    # print(user)
    return render_template('pantry.html', **context)





# # SHOW -- RENDERS TO SHOW


# @app.route('/recipe/<int:id>')
# def recipe_show(id):

#     #LOGIN CHECK
#     if not session.get('id'):
#         return render_template('index.html')

#     else:
#         data = {
#             'id':id
#         }
#         #RETREIVS RECIPE
#         recipe=Recipe.recipe_get_one(data)
#         print(recipe)

#         return render_template("recipe_show.html",recipe=recipe)


# # EDIT -- RENDERS TO EDIT


@app.route('/item/edit/<int:id>')
def recipe_edit(id):

    #LOGIN CHECK
    if not session.get('id'):
        return render_template('index.html')

    else:
        data ={
            "id":id
        }
        #UPDATES RECIPE ON BUTON CLICK AND GRABS THE RECIPE ON PAGE LOAD
        Item.item_update(request.form)
        item=Item.item_get_one(data)

        print(item)

        return render_template("item_edit.html", item=item)



# # UPDATE -- REDIRECTS TO DASHBOARD



@app.route('/item/update/<int:id>' ,methods=['POST'])
def item_update(id):

    # LOGIN CHECK
    if not session.get('id'):
        return render_template('index.html')
    #FIELD VALIDATION
    else:
        if not Item.validate_item(request.form):
            return redirect(request.referrer)

        print(request.form)

        data = {
            **request.form,
            'id': id
        }

        # print(request.form)

        #UPDATE RECIPE
        Item.item_update(data)

        return redirect('/pantry')


# # DESTROY -- REDIRECTS TO DASHBOARD


@app.route('/recipe/destroy/<int:id>')
def recipe_destroy(id):

    #LOGIN CHECK
    if not session.get('id'):
        return render_template('index.html')

    else:
        data = {
            'id':id
        }

        # print(data)

        #DELETES RECIPE ROUTES BACK TO DASHBOARD
        Item.item_destroy(data)

        return redirect(request.referrer)
