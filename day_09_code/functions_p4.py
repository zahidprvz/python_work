# 8-12 Sandwiches

def sandwich(*items):
    print(items)

sandwich('item_1')
sandwich('item_1', 'item_2')
sandwich('item_1', 'item_2', 'item_3')

print("\n")


# 8-13 User Profile

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Zahid', 'Parviz', location='Lahore', company='Devsinc', salary='00000')

print(user_profile)

print("\n")



# 8-14 Cars

def car_info(manufacturer, model, **related_info):
    related_info['manufacturer'] = manufacturer
    related_info['model'] = model
    return related_info

car = car_info('subaru', 'outback', color='blue', tow_package='True')
print(car)
print("\n")