sentence = input("enter a sentence:")
word_list = sentence.split()
word_tuple= tuple(word.upper() for word in word_list)

file_name = "sentence_data.txt"


with open(file_name, 'w') as writer:
    writer.write(f'List: {word_list}\n')
    writer.write(f'Tuple: {word_tuple}')

with open(file_name, 'r') as reader:
    line_list = reader.readline()
    line_tuple = reader.readline()
    print(line_list)
    print(line_tuple)