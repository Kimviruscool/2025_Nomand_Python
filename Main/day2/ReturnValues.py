#Return Values (반환 값)

def tax_calc(money):
    return money * 0.35

def pay_tax(tax):
    print("Thank you for paying", tax)

to_pay = tax_calc(1500000)
pay_tax(to_pay)

# 1. to_pay = tax_calc(1500000) tax_calc 함수를 사용 입력된(argument) 값을 money(parameters)에 전달

# 2. def tax_calc(money):
#     return money * 0.35 #(money)parameter에 값을 계산하여 return 을 통해 반환 이후 to_pay 변수에저장/반환

# 3. pay_tax(to_pay) pay_tax 기능을 호출 저장된/반환된(return) 변수값 입력(argument)

# 4. def pay_tax(tax):
#     print("Thank you for paying", tax) #pay_tax(parameter) 받아온/저장된(parameter) 값을 받아와 출력

