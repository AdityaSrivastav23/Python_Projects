#  LOVE CALCULATOR

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is Your Lover's name? \n")
combo_name=name1+name2
lower_name=combo_name.lower()

t=lower_name.count("t")
r=lower_name.count("r")
u=lower_name.count("u")
e=lower_name.count("e")

l=lower_name.count("l")
o=lower_name.count("o")
v=lower_name.count("v")
e=lower_name.count("e")

count_name=int(str(t+r+u+e)+str(l+o+v+e))
print(count_name)

if count_name>=80:
  print("WoW , Your Love % is {count_name} ,It is Phenomenal! Cheers")
elif count_name>=50 and count_name<80:
  print(f"Your Love % is {count_name} ,Average ! Average bond, Sambhal ke Chalo")
elif count_name>=30 and count_name<=50:
    print(f" Your love % is  {count_name} , Poor Bond , Breakup Kar Lo")
elif count_name<=30:
      print(f"Your Love % is  {count_name} , Very Poor !  Dusri Pataao")