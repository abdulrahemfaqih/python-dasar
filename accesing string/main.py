# accesing string 

data = 'abdul rahem faqih'
print(data[0])

data = 'abdul rahem faqih'
print(data[2:7])

data = 'abdul rahem faqih'
print(data[-1])

data = 'abdul rahem faqih'
print(data[:6])

data = 'abdul rahem faqih'
print(data[6:])

# using iteration/looping
# len(StrVar)

print(data, len(data))
num = len(data)
for i in range (num) :
    print('offset-',i,':',data[i])


for huruf in data :
    print(huruf)

