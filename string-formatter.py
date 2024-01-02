import re
import requests
import os
import sys

debug = True

def format_question(question):
    question = question.lower()

    # Remove non-alphanumeric characters, keep hyphens
    question = re.sub(r'[^a-z0-9- ]+', '', question)
    question = question.replace(' ', '-')

    question = question[:198] # this worked when I tested it, now it doesn't
    return question

if __name__ == "__main__":
    if len(sys.argv) > 1:
        question = sys.argv[1]
    else:
        question = input("Enter a question: ")
    formatted_question = format_question(question)

url = "https://itexamanswers.net/question/" + formatted_question

# make a request to the url, and return the html of the page
html = requests.get(url).text
answers = re.findall(r'<span style="color: #ff0000;">(.*?)</span>', html)

# remove html tags from answer

answers = [re.sub(r'<.*?>', '', answer) for answer in answers]

os.system('cls' if os.name == 'nt' else 'clear')

print("\"" + question + "\"" + "\n")
if (debug): print(url)

if (len(answers) == 1):
    for answer in answers:
        print("Answer: " + answer)
elif (len(answers) > 1):
    print("Answers: \n")
    for answer in answers:
        print(answer + ", ")
else:
    print("No answers found, check your question or search manually at itexamanswers.net")