def fizzbuzz(n):
    if n > 0:
        rangelist = range(1, n + 1)
        
    else:
        rangelist = range(1, n-1, -1)
        
    for i in rangelist:
        
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            
        elif i % 3 == 0:
            print("Fizz")
            
        elif i % 5 == 0:
            print("Buzz")
            
        else:
            print(i)
            
n = int(input("数字を入力してください"))

fizzbuzz(n)