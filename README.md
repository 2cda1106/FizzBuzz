## 使用方法
1. リポジトリをクローンするか、`fizzbuzz.py`ファイルをダウンロードします。
2. 以下のコマンドを使ってPythonでスクリプトを実行します。

def fizzbuzz(n):
    if n > 0:   //正の場合
        rangelist = range(1, n + 1)   //正の数1~n
    else:
        rangelist = range(1, n-1, -1)   //負の数n~-1
        
    for i in rangelist:
        
        if i % 3 == 0 and i % 5 == 0:   //3と5で割り切れる
            print("FizzBuzz")
            
        elif i % 3 == 0:   //3で割り切れる
            print("Fizz")
            
        elif i % 5 == 0:   //5で割り切れる
            print("Buzz")
            
        else:
            print(i)
            
n = int(input("数字を入力してください"))   //入力

fizzbuzz(n)



$ python fizzbuzz.py
Enter a number: 15
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
