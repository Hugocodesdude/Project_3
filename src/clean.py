# Functions

# ----------------

def millionbillion_company_finder(x):
    
    filter_1 = {"total_money_raised": {"$regex": "M|B"}}
    filter_city_1 = {"offices.0.city": x }
    
    city_conditions = [filter_1,filter_city_1]
    city_finder_list = list(c.find({"$and": city_conditions}, {"_id":0, "name":1,"offices":1}))
    return city_finder_list

# ---------------

def design_company_finder(x):
    #place = x
    filter_2 = {"tag_list": {"$regex": "design"}}
    filter_city_1 = {"offices.0.city": x }
    
    city_conditions = [filter_2,filter_city_1]
    city_finder_list = list(c.find({"$and": city_conditions}, {"_id":0, "name":1,"offices":1}))
    return city_finder_list

#-----------------

def videogame_company_finder(x):
    #place = x
    filter_3 = {"category_code": "games_video"} 
    filter_city_1 = {"offices.0.city": x }
    
    city_conditions = [filter_3,filter_city_1]
    city_finder_list = list(c.find({"$and": city_conditions}, {"_id":0, "name":1,"offices":1}))
    return city_finder_list

# -----------------

