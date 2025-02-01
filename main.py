from src.ngram_model import *
from src.text_generation import *

def main():
    tokens = preprocess('data/shakespeare.txt')

    # bigrams = create_bigrams(tokens)
    # print(f"Bigrams: {bigrams[:10]}")
    # bigram_counts = from_bigram_to_next_token_counts(bigrams)
    # bigram_probs = {}

    for n in [2,3,4]: 
        ngrams = create_ngrams(tokens,n)
        ngram_counts = from_ngram_to_next_token_counts(ngrams)
        ngram_probs = from_ngram_to_next_token_probs(ngram_counts)

        # initial_ngram = random.choice(ngrams)   #find first ngram/prefix
        initial_ngram = random.choice(list(ngram_probs.keys()))

        print(f"\nGenerating text with {n}-grams:")
        gen_text = generate_text_from_ngram(initial_ngram, 50, ngram_probs)
        print("Generated Text:", gen_text)



if __name__ == "__main__":
    main()
