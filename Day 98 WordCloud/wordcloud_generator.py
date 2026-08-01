from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read text file
with open("sample_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Generate Word Cloud
wordcloud = WordCloud(
    width=1000,
    height=600,
    background_color="white"
).generate(text)

# Save Image
wordcloud.to_file("wordcloud_output.png")

# Display Image
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud Generator")
plt.show()

print("\n✅ Word cloud generated successfully!")
print("Image saved as 'wordcloud_output.png'")