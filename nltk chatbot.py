from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"^(hi|hello|hey)\b.*",
        ["Hello! How can I help you today?", "Hi there! What do you want to know?"],
    ],
    [
        r".*\byour name\b.*",
        ["I am an NLTK-based chatbot."],
    ],
    [
        r"what is nlp\??",
        ["NLP stands for Natural Language Processing. It helps computers understand human language."],
    ],
    [
        r"what is nltk\??",
        ["NLTK is a Python library for natural language processing tasks like tokenizing and tagging."],
    ],
    [
        r"who created python\??",
        ["Python was created by Guido van Rossum and first released in 1991."],
    ],
    [
        r".*\b(help|assist)\b.*",
        ["Sure! Tell me what you need help with."],
    ],
    [
        r"^bye\b.*",
        ["Goodbye! Have a great day!"],
    ],
    # Fallback: runs when nothing above matches (must stay last)
    [
        r"(.*)",
        [
            "Sorry, I didn't understand that. Try asking about NLP, NLTK, or Python.",
            "I can answer questions about NLP, NLTK, and Python. Could you rephrase?",
        ],
    ],
]

chatbot = Chat(pairs, reflections)
print("NLTK Chatbot: Type 'bye' to exit.")
chatbot.converse(quit="bye")
