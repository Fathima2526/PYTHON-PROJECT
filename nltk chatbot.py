import nltk
from nltk.chat.util import Chat, reflections
nltk.download("punkt")
pairs = [
    [
        r"(hi|hello|hey)",
        ["Hello! How can I help you today?", "Hi there! What do you want to know?"]
    ],

    [
        r"what is your name ?",
        ["I am an NLTK chatbot.",]
    ],

    [
        r"what is nlp ?",
        ["NLP stands for Natural Language Processing. It helps computers understand human language."]
    ],

    [
        r"what is nltk ?",
        ["NLTK is a Python library for natural language processing tasks like tokenizing and tagging."]
    ],

    [
        r"who created python ?",
        ["Python was created by Guido van Rossum in 1991."]
    ],

    [
        r"(.*) your name (.*)",
        ["I am an NLTK-based chatbot."]
    ],

    [
        r"(.*) (help|assist) (.*)",
        ["Sure! Tell me what you need help with."]
    ],

    [
        r"bye",
        ["Goodbye! Have a great day!"]
    ],
]
chatbot = Chat(pairs, reflections)
print("🤖 NLTK Chatbot: Type 'bye' to exit.")
chatbot.converse()
