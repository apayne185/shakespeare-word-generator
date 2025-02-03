import sys
import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
sys.path.insert(0, r"C:\Users\annap\Desktop\Year3\nlp\assignment1\shakespeare-word-generator\src")


from src.ngram_model import *
from src.text_generation import *
import pytest


# File - ngram_model.py

def test_preprocess():
    tokens= preprocess()

    assert isinstance(tokens, list), "Preprocessed data- needs to be a list."
    assert len(tokens)>0, "Preprocessed data- needs to not be empty."
    assert all(isinstance(t, str) for t in tokens),  "All tokens have to be strings."

  

def test_create_ngrams():
    tokens= preprocess()
    bigrams=create_ngrams(tokens, 2)

    assert isinstance(bigrams, list), "Bigrams - needs to be a list."
    assert all(isinstance(ngram, tuple) and len(ngram) == 2 for ngram in bigrams), "Each bigram needs to be a tuple of two tokens."




def test_from_ngram_to_next_token_counts():
    tokens = preprocess()
    bigrams= create_ngrams(tokens, 2)  
    counts = from_ngram_to_next_token_counts(bigrams)    

    assert isinstance(counts, dict), "Output - needs to be a dictionary."
    assert all(isinstance(value, dict) for value in counts.values()), "Each value in dictionary needs to be a dictionary."

         

def test_from_ngram_to_next_token_probs():
    tokens= preprocess()
    bigrams= create_ngrams(tokens, 2)    
    counts= from_ngram_to_next_token_counts(bigrams)
    probs = from_ngram_to_next_token_probs(counts)

    assert isinstance(probs, dict), "Output - shoud be dictionary."
    assert all(isinstance(value, dict) for value in probs.values()), "Each value in dictionary needs to be a dictionary."
    assert all(0 <= prob <= 1 for subdict in probs.values() for prob in subdict.values()), "Probablities needs to be between 0-1."








# File - text_generation.py


def test_generate_text_from_ngram():       
    tokens = preprocess()
    bigrams = create_ngrams(tokens, 2)
    counts = from_ngram_to_next_token_counts(bigrams)
    probs = from_ngram_to_next_token_probs(counts)
    initial_ngram = random.choice(list(probs.keys()))
    generated_text = generate_text_from_ngram(initial_ngram, 50, probs, 2)

    assert isinstance(generated_text, str), "Generated text has be a string."
    assert len(generated_text.split()) == 50,"Generated text should have 50 words."
