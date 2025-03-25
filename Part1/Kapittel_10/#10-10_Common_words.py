def count_certain_words(filename):
    """method for counting the number of the given word in different books"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"the file {filename} could not be found")
    else:
        word = "e"
        certain_words = contents.lower().count(word)
        print(f"The file {filename} have {certain_words} cases of the word {word}")


filenames = ['moby_dick.txt', 'Pride_or_prejudice.txt', 'the_count_of_monty_cristo.txt']
for filename in filenames:
    count_certain_words(filename)