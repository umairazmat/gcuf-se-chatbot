import numpy as np #NumPy is a powerful library for numerical computing in Python, and it provides support for large, multi-dimensional arrays and matrices, along with a collection of high-level mathematical functions.
import nltk #Python library for NLP tasks, such as tokenization, stemming, lemmatization, part-of-speech tagging, and more.
# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer #The PorterStemmer is a widely used stemming algorithm, which is used to reduce words to their base or root form.
stemmer = PorterStemmer()


def tokenize(sentence): #okenization is the process of breaking down a sentence or a piece of text into individual words or tokens. 
    """
    split sentence into array of words/tokens
    a token can be a word or punctuation character, or number
    """
    return nltk.word_tokenize(sentence)


def stem(word): #Stemming helps to normalize words by reducing them to their base or root form
    """
    stemming = find the root form of the word
    examples:
    words = ["organize", "organizes", "organizing"]
    words = [stem(w) for w in words]
    -> ["organ", "organ", "organ"]
    """
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words): #This function takes a tokenized sentence (a list of words) and a list of known words as input.
    """
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bog   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag
