import math
height=int(input("Enter The height of The Wall:- "))
width=int(input("Enter The Width of The Wall:- "))
coverage=int(input("Enter The Area Covered By a Can of Paint :- "))
area=height*width
no_of_cans=math.ceil(area/coverage)
print(f"You will Need {no_of_cans} to Paint The Wall")