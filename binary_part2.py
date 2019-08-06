#decimal_to_binary(12)
#bin(x) function

input_decimal = int(input('Enter: '))

def decimal_to_binary(input_decimal):
    
    if input_decimal > 0:
        answer = bin(input_decimal).replace('0b','')
    else:
        answer = bin(input_decimal).replace('-0b','')
    print(answer)
      
decimal_to_binary(input_decimal)