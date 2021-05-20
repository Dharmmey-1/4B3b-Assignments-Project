file_path = r"C:\Users\HP\Documents\UNIVELCITY\DATA_SCIENCE\git\4B3b-Assignments-Project\tochi\files\classwork.txt"

file = open(file_path, 'a')

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# product = num1*num2

# print(f"{num1} * {num2} = {product}", file=file)
 

word = input('please input a word: ')

reversed_word = list(reversed(word))

joined_word = "".join(reversed_word)

print(f"{word} | {joined_word}", file=file)

# print(joined_word, file=file)
