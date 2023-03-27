""""Напишите программу, которая выводит n первых элементов
последовательности 122333444455555… (число повторяется
столько раз, чему оно равно). """

def sequence(n):
    result=''
    for num in range(1, n+1):
        str_num=str(num)
        result+=str_num*num
        if len(result)>=n:
            break
    print(result[:n])

sequence(10)
sequence(1)
sequence(2)
sequence(100)