work=""
age=float(input("Age? "))
if age < 15:
  print("Too young for vaccination")
if age > 15: 
  work=input("Are you a hc, st,ss, ct, cs, s or other? ")
if work=="hc"and age >=15:
  print("G1")
elif age >= 65:
  print("G2")
elif work=="st" and age >=15 and age <65:
  print("G3")
elif work=="ss" and age >=15 and age <65:
  print("G3")
elif work=="cs" and age >=15 and age <65:
  print("G4")
elif work=="ct" and age >=15 and age <65:
  print("G4")
elif work=="st" and age >=15 and age <65:
  print("G5")
elif work=="other" and age >=15 and age <65:
  print("G5")