num=int(input("Ingrese un numero: "))
palabra=" "
resp=0
for i in range(1,num+1):
    if (i%3==0 and i%5!=0):
        resp=i
        palabra="Fizz"
        print(str(resp)+" "+palabra)
    elif (i%5==0 and i%3!=0):
        resp=i
        palabra="Buzz"
        print(str(resp)+" "+palabra)
    elif (i%3==0 and i%5==0):
        resp=i
        palabra="FizzBuzz"
        print(str(resp)+" "+palabra)
    
        
    




