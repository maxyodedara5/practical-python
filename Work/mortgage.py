# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0


this_was_called = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
current_payment_month = 0
while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    if principal < 0:
        principal = principal * (1 + rate / 12) + payment
        # Final payment only pay the remaining principal amount
        print(
            f"{current_payment_month} {total_paid + principal} {principal - principal}"
        )
        break
    total_paid = total_paid + payment
    if extra_payment_start_month <= current_payment_month <= extra_payment_end_month:
        total_paid += extra_payment
        principal -= extra_payment
        this_was_called += 1
    current_payment_month += 1

    print(f"{current_payment_month} {total_paid} {principal}")


print("Total paid ", round(total_paid + principal, 4))
