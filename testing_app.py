import re
import random
from typing import List


def random_integers_list(size, start, end):
    list = [random.randint(start, end) for _ in range(size)]
    list.sort()
    return list

def split_on_numbers_and_text(s):
    # This pattern splits the string into alternating numbers and text
    return re.findall(r'[A-Za-z]+|\d+', s)

with open("data.txt", 'r') as file:
    data = list(file.read())
    data = "".join(data).replace("\n", "").split(" ")
    data = [split_on_numbers_and_text(dato) for dato in data]
    data = [item for sublist in data for item in sublist]
    output = dict()
    key = None
    value = None
    for dato in data:
        if dato.isnumeric():
            key = dato
        else:
            output[int(key)] = dato

def extract_xxxxx(input_string):
    # Match the first pattern: any amount of integers followed by a dot and anything else
    match = re.match(r'(\d+)\..*', input_string)
    if match:
        return match.group(1)  # Return the first captured group (xxxxx)
    
    # If it doesn't match the first pattern, check the second
    match_second = re.match(r'(\d+)\.(\d+).*', input_string)
    if match_second:
        return False  # Return False for the second pattern
    
    return None  # If neither pattern matches



class Question():
    def __init__(self, number: int, text: str = "") -> None:
        self.number: int = number
        self.question: str = text
        self.answer_a: str = ""
        self.answer_b: str = ""
        self.answer_c: str = ""




def extract_questions_answers():
    state = None
    question = None
    questions = []
    with open("data2.txt", 'r', encoding='utf-8') as file:
        for line in file:
            line = line.replace("\n", "")
            question_number = extract_xxxxx(line)
            if question_number:
                # print(question_number)
                state = 'q'
                question = Question(int(question_number), line.removeprefix(question_number+". "))
                continue
            if line.startswith("a)"):
                state = 'a'
                question.answer_a += line
                continue
            if line.startswith("b)"):
                state = 'b'
                question.answer_b += line
                continue
            if line.startswith("c)"):
                state = 'c'
                question.answer_c += line
                continue
            if state == 'q':
                question.question += line
                continue
            if state == 'a':
                question.answer_a += line
                continue
            if state == 'b':
                question.answer_b += line
                continue
            if question:
                questions.append(question)
    return questions

def print_line():
    print("_"*30)

answer_list: List[Question] = extract_questions_answers()

for question in answer_list:
    if question.answer_a == "":
        raise ValueError("Wrong question!")

print("Welcome to test!")
print_line()
print("How many questions you you want?")
user_input = int(input("Number: "))
for i in range(user_input):
    question = random.choice(answer_list)
    print(f"Question number {question.number}: ")
    print(f"{question.question}: ")
    print(f"{question.answer_a}: ")
    print(f"{question.answer_b}: ")
    print(f"{question.answer_c}: ")
    user_input = input("Select ABC: ")
    if user_input == output[question.number]:
        print("Good answer!")
    else:
        print("You dumbass!")
        print(f"Correct was: {output[question.number]}")
    print_line()
