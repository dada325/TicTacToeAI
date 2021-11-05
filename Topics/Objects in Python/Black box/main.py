# use the function blackbox(lst) that is already defined
lst = [0, 1]
lst3 = blackbox(lst)
if id(lst) ==id(lst3):
    print("modifies")
else :
    print("new")

