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

def calc_distance_LDN_mean(x, site):
    #site_coords = (51.5121948,-0.1360746)
    place2_coords = (x.lat, x.lon)
    return (distance.geodesic(site, place2_coords).km)*1000

ldn_api_df["Distance"] = ldn_api_df.apply(lambda x: calc_distance_LDN_mean(x, (51.5121948,-0.1360746)), axis = 1).round(2)
ldn_api_df["Distance"].mean()

#-----------------

def calc_distance_BCN(x):
    site_coords = (41.3943113,2.190921)
    place2_coords = (x.lat, x.lon)
    return (distance.geodesic(site_coords, place2_coords).km)*1000

bcn_api_df["Distance"] = bcn_api_df.apply(calc_distance_BCN, axis = 1).round(2)



