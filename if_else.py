price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = price * 0.1
elif has_good_credit:
    down_payment = price * 0.2
print(f"Down_payment: ${down_payment}")

name = "sanchi"

if len(name) < 3:
    print('name must be at least 3')
elif len(name) > 50:
    print('name must be less than 50')
else:
    print('name looks good')