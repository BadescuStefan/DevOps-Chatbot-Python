import nltk
from nltk.chat.util import Chat, reflections

# Defining questions and answer pairs for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright, no problem.",]
    ],
    [
        r"(.*) (good|great|fine)",
        ["Nice to hear that.",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program, I don't have age.",]
    ],
    [
        r"what (.*) want ?",
        ["Make a wish, I'm here to assist you.",]
    ],
    [
        r"(.*) created ?",
        ["I was created by [Your Name].",]
    ],
    [
        r"bye",
        ["Bye, take care. Have a great day!",]
    ],
]

# Initialize the chatbot
def chatbot():
    print("Hello! I am a chatbot. Ask me anything.")
    chat = Chat(pairs, reflections)
    while True:
        user_input = input(">")
        response = chat.respond(user_input)
        if response:
            print(response)
        else:
            print("I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    chatbot()

