# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if extra_payment_start_month <= month <= extra_payment_end_month:
        month_payment = payment + extra_payment
    else:
        month_payment = payment
    principal = principal * (1+rate/12) - month_payment
    
    total_paid = total_paid + month_payment
    month += 1
    print(f'{month:03d}, {total_paid:010.3f}, {principal:010.3f}')

print(f'Total paid {total_paid:010.3f}')
print(f'Months {month:03d}')
