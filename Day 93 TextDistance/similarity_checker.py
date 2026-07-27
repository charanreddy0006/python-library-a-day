import textdistance

print("=" * 50)
print("        TEXT SIMILARITY CHECKER")
print("=" * 50)

text1 = input("\nEnter First Text : ")
text2 = input("Enter Second Text: ")

similarity = textdistance.cosine.normalized_similarity(text1, text2)

print("\nResults")
print("-" * 30)
print(f"Similarity Score : {similarity:.2f}")
print(f"Similarity Percentage : {similarity * 100:.2f}%")

if similarity > 0.8:
    print("Status : Very Similar")
elif similarity > 0.5:
    print("Status : Moderately Similar")
else:
    print("Status : Different")