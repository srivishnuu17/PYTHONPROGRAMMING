# Mini Project: Electric Bill Generator

print("=" * 40)
print("       ELECTRIC BILL GENERATOR")
print("=" * 40)

customer_name = input("Enter customer name: ")
customer_id = input("Enter customer ID: ")
units = float(input("Enter electricity units consumed: "))

# Slab-based tariff
if units <= 100:
    energy_charge = units * 1.50
elif units <= 200:
    energy_charge = (100 * 1.50) + ((units - 100) * 2.50)
elif units <= 500:
    energy_charge = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)
else:
    energy_charge = (100 * 1.50) + (100 * 2.50) + (300 * 4.00) + ((units - 500) * 6.00)

fixed_charge = 50.00
tax = (energy_charge + fixed_charge) * 0.05
total_bill = energy_charge + fixed_charge + tax

print("\n" + "=" * 40)
print("             ELECTRICITY BILL")
print("=" * 40)
print(f"Customer Name : {customer_name}")
print(f"Customer ID   : {customer_id}")
print(f"Units Used    : {units:.2f}")
print(f"Energy Charge : ₹{energy_charge:.2f}")
print(f"Fixed Charge  : ₹{fixed_charge:.2f}")
print(f"Tax (5%)      : ₹{tax:.2f}")
print("-" * 40)
print(f"Total Bill    : ₹{total_bill:.2f}")
print("=" * 40)
print("Thank you for using the Electric Bill Generator!")
