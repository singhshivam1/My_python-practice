# New Tax Regime FY 2026-27
# Progressive slab-wise calculation
# Without cess

gross_salary = float(input("Enter annual gross salary: "))

standard_deduction = 75000
taxable_income = gross_salary - standard_deduction

if taxable_income < 0:
    taxable_income = 0

tax = 0

print("\n----- Income Tax Calculation -----")
print("Gross Salary:", gross_salary)
print("Standard Deduction:", standard_deduction)
print("Taxable Income:", taxable_income)

# Slab 1: Up to 4 lakh
slab_tax = min(taxable_income, 400000) * 0
tax += slab_tax
print("Slab 1 Tax (0%):", slab_tax)

# Slab 2: 4 lakh to 8 lakh
slab_tax = max(0, min(taxable_income, 800000) - 400000) * 0.05
tax += slab_tax
print("Slab 2 Tax (5%):", slab_tax)

# Slab 3: 8 lakh to 12 lakh
slab_tax = max(0, min(taxable_income, 1200000) - 800000) * 0.10
tax += slab_tax
print("Slab 3 Tax (10%):", slab_tax)

# Slab 4: 12 lakh to 16 lakh
slab_tax = max(0, min(taxable_income, 1600000) - 1200000) * 0.15
tax += slab_tax
print("Slab 4 Tax (15%):", slab_tax)

# Slab 5: 16 lakh to 20 lakh
slab_tax = max(0, min(taxable_income, 2000000) - 1600000) * 0.20
tax += slab_tax
print("Slab 5 Tax (20%):", slab_tax)

# Slab 6: 20 lakh to 24 lakh
slab_tax = max(0, min(taxable_income, 2400000) - 2000000) * 0.25
tax += slab_tax
print("Slab 6 Tax (25%):", slab_tax)

# Slab 7: Above 24 lakh
slab_tax = max(0, taxable_income - 2400000) * 0.30
tax += slab_tax
print("Slab 7 Tax (30%):", slab_tax)

print("\nTotal Income Tax (Without Cess):", tax)