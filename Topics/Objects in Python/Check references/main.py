def check(obj1, obj2):
    print('True') if id(obj2) == id(obj1) else print('False')