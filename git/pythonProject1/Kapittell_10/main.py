#10-1 Learning python

filename = 'learning_python.txt'

with open('learning_python.txt') as file_object:
    contents = file_object.read()
print(contents)
print("--------------------")

with open(filename) as file_object:
    for line in file_object:
        print(line.strip())
print("--------------------")



with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print("--------------------")


#10-2 Learning C
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.replace('python', 'C').rstrip())








