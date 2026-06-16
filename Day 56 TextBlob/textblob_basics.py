from textblob import TextBlob

# Create TextBlob object
text = TextBlob(
    "Python is an amazing programming language!"
)

# Sentiment Analysis
print("Sentiment:")

print(text.sentiment)

# Words
print("\nWords:")

print(text.words)

# Correct spelling
wrong_text = TextBlob(
    "I realy love Pythn programming"
)

print("\nCorrected Text:")

print(wrong_text.correct())