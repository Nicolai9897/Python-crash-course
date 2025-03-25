# 10-7 cats and dogs
def cats_and_dogs(filename):
    print(f"these are all the animals in {filename}:")
    try:
        with open(filename, encoding='utf-8') as f:
          contents = f.read()
    except FileNotFoundError:
        #kommenter bort linje 10 for oppgave 10-8,
        #kommenter bort linje 11 for oppgave 10-9
        pass
        #print(f"Sorry, the file {filename} cannot be found.")
    else:
        print(f"{contents} \n")


filenames = ['cats.txt', 'dogs.txt']



#cats_and_dogs(filenames)
for filename in filenames:
    cats_and_dogs(filename)