# 1
import random
d=open('lines.txt','r')
dv=(random.choice(list(d)))
print(dv)
# 3
file=open('lines.txt','r')
d3=(file.read())
print("чётные:", d3[::2])
print("нечётные:", d3[1::2])

# 4
with open("lines.txt", "r") as file: 
    words =file.read().split()  
    max_word_len =max(len(word) for word in words) 
    longest_words = [word for word in words if len(word) == max_word_len]
    print("max длина", max_word_len) 
    print("Слова max:") 
    for word in longest_words: 
        print(word)
# 5
file=open('lines.txt','r')
d3=(file.read())
str1 = d3
output = [i for i in str1]
d4=(len(output)) #1 символ= 8бит
f1=(d4*8) #8мбит=1байт
f2=(f1/8) #264 бита в байт
print("байт",f2)