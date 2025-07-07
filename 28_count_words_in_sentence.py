# Task 28: Count Words in a Sentence
def count_words(sentence):
    return len(sentence.split())

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print("Word count:", count_words(sentence))
