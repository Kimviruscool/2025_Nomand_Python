def tax_calculator(): #이때 공백,시작숫자 면 안됨
    print(15000000000 * 0.35) #들여쓰리고 코드 안에 def안에 있는 코드임을 확인 # space2 , tab을 이용해서 안쪽으로 이동가능

tax_calculator() #몇번이고 호출하면 사용가능

#parameter 사용
def tax_calculator(money): #데이터를 받는 공간 할당 (parameter) #placeholder
    print(money * 0.35)

tax_calculator(1000000)

#MultipleParameters
def tax_calculator(money, duty): #다중 데이터를 받을 수 있음 (paramters1, parameters2)
    print(money * duty)

tax_calculator(200000, 0.35)