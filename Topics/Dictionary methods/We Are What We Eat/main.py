# the list "meals" is already defined
# your code here
result = 0
for i in meals:
    result += i.get("kcal")

print(result)