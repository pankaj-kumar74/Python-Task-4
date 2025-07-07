# Task 27: Longest Word in a Sentence
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print("Longest word:", longest_word(sentence))
