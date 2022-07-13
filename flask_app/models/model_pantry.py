from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
import re


#MAKE SURE TO UPDATE

DATABASE = 'chefit_db'





class Item:      # update init to reflect table data
    def __init__(self, data):
        self.id = data['id']
        self.pantry = data['pantry']
        self.pantry_group = data['pantry_group']
        self.description = data['description']
        self.amount = data['amount']
        self.cost = data['cost']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']


    

# *******************************************CREATE

    @classmethod        #update to reflect table data (returns a row id number)
    def item_create(cls, data:dict):
        query = "INSERT INTO items (pantry, pantry_group, description , amount, cost, created_at, updated_at, user_id) VALUES (%(pantry)s, %(pantry_group)s, %(description)s, %(amount)s, %(cost)s, %(created_at)s, NOW(),  %(user_id)s);"

        result = connectToMySQL(DATABASE).query_db(query,data)
        return result
    
# *******************************************RETRIEVE
    
    @classmethod
    def item_get_all(cls):    # returns a list of dictionaries
        query = "SELECT * FROM items;"
        results = connectToMySQL(DATABASE).query_db(query)
        recipes = []
        for u in results:
            recipes.append( cls(u) )
        return recipes
    

    @classmethod        # returns a list of a single dictionary
    def item_get_one(cls,data:dict):
        query  = "SELECT * FROM items WHERE id =%(id)s";
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])
    
    
# *******************************************UPDATE


    @classmethod
    def item_update(cls,data:dict):        # update to reflect table (returns nothing)
        query = "UPDATE items SET description=%(description)s, amount=%(amount)s, cost=%(cost)s, created_at= %(created_at)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)


# *******************************************DESTROY

    @classmethod
    def item_destroy(cls,data:dict):        # returns nothing
        query  = "DELETE FROM items WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    
#**********************************************VALIDATOR
    
    
    @staticmethod
    def validate_item(data:dict): #returns bool
        is_valid = True
        
        
        if len(data['description']) < 2:
            is_valid = False
            flash("Description must be more than 2 characters", "err_description")
            
        if len(data['amount']) < 1:
            is_valid = False
            flash("Please enter an amount", "err_amount")

        # if len(data['cost']) < 2:
        #     flash("Please enter cost of the item", "err_cost")
        #     is_valid = False
        
        if len(data['created_at']) < 2:
            is_valid = False
            flash("Please enter a date", "err_created_at")
            
        # if data['pantry'] == 'none':
        #     is_valid = False
        #     flash("Please pick a pantry", "err_pantry")

       
            
        return is_valid