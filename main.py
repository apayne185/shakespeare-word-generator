from src.ngram_model import *
from src.text_generation import *

def main():
    tokens = preprocess('/data/shakespeare.txt')

    bigrams = create_bigrams(tokens)
    bigram_counts = from_bigram_to_next_token_counts(bigrams)

    bigram_probs = {bigram: {token: count/sum(bigram_counts[bigrams].values()) for token, count in bigram_counts[bigrams].items()} for bigram in bigrams}

    initial_bigram = () #find first bigram
    gen_text = generate_text_from_ngram(initial_bigram, 50, bigram_probs)

    print("Generated Text:", gen_text)


if __name__ == "__main__":
    main()
