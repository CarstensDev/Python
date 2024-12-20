class Restaurant:
    name = ""
    category = ""
    rating = 0.0
    delivery = False


def bobs_burgers_info():
    bobs_burgers = Restaurant()
    bobs_burgers.name = "Bob's Burgers"
    bobs_burgers.category = "American Diner"
    bobs_burgers.rating = 4.7
    bobs_burgers.delivery = False
    return bobs_burgers

print(vars(bobs_burgers_info()))

