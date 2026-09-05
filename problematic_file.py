# Barangay Electric Bill Calculator — REPORTED BROKEN, PLEASE FIX

name = input("Enter resident name: ")
consumption = input("Enter kWh consumed this month: ")
is_senior = input("Senior citizen? (yes/no): ")

if consumption <= 100:
    rate = 9.00
elif consumption < 200
    rate = 11.00
else:
    rate = 14.00

total = consumption * rate

if is_senior = "yes"
    discount = total * 0.05
    total = total - discount
    print("Senior discount applied: ₱" + discount)

print("----- ELECTRIC BILL -----")
print("Name: " + name)
print("Consumption: " + consumption + " kWh")
print("Rate applied: ₱" rate "/kWh")
print("Total Due: ₱" + total)
