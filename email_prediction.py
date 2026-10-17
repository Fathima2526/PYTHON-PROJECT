import pandas as pd
import string
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay

# 1. Load the dataset (Kaggle version has columns v1 = label, v2 = text)
df = pd.read_csv("spam.csv", encoding="latin-1")[["v1", "v2"]]
df.columns = ["label", "email"]
print(df.head())
print("\nClass counts:\n", df["label"].value_counts())

# 2. Clean the text
def clean_text(text):
    text = text.lower()
    return "".join(ch for ch in text if ch not in string.punctuation)

df["clean_email"] = df["email"].apply(clean_text)

# 3. TF-IDF features
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(df["clean_email"])
y = df["label"]

# 4. Train/test split (stratified so both sets keep the spam ratio)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 5. Train and evaluate
model = MultinomialNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("\nTest samples:", len(y_test))
print("Accuracy:", round(accuracy_score(y_test, y_pred), 3))
print("\n", classification_report(y_test, y_pred))

ConfusionMatrixDisplay(confusion_matrix(y_test, y_pred, labels=["ham", "spam"]),
                       display_labels=["ham", "spam"]).plot()
plt.title("Spam Classifier - Confusion Matrix")
plt.savefig("confusion_matrix.png")
plt.show()

# 6. Predict new emails
def predict_email(text):
    return model.predict(vectorizer.transform([clean_text(text)]))[0]

print("\n'Win free cash now' ->", predict_email("Win free cash now"))
print("'Are we meeting today?' ->", predict_email("Are we meeting today"))
