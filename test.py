import sys

# a = 10
# b = 30

a = int(sys.argv[1])
b = int(sys.argv[2])

inputList = []
for i in range(1,5):
    inputList.append((sys.argv[i]))
print(inputList)
print(tuple(inputList))

print("Input1: {}".format(a))
print("Input2: {}".format(b))
print("Result: {}".format(a+b))
