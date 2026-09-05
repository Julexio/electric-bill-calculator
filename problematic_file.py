# Barangay Electric Bill Calculator — REPORTED BROKEN, PLEASE FIX

name = str(input("Enter resident name: "))
consumption = float(input("Enter kWh consumed this month: "))
is_senior = str(input("Senior citizen? (yes/no): "))

if consumption <= 100:
    rate = 9.00
elif consumption < 200:
    rate = 11.00
else:
    rate = 14.00

total = consumption * rate

if is_senior == "yes":
    discount = total * 0.05
    total = total - discount
    print(f"Senior discount applied: ₱{discount}")
    print(f"Total is: {total}")
elif is_senior == "no":
    print(f"Senior discount is not applied")
    print(f"Total is: {total}")
else:
   print("Please input yes or no")
print("----- ELECTRIC BILL -----")
print(f"Name:  {name}")
print(f"Consumption: {consumption} kWh")
print(f"Rate applied: ₱ {rate} /kWh")
print(f"Total Due: ₱{total}")