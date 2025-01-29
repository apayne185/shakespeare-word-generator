from src.ngram_model import *
from src.text_generation import *

def main():
    tokens = preprocess('data/shakespeare.txt')

    bigrams = create_bigrams(tokens)
    print(f"Bigrams: {bigrams[:10]}")
    bigram_counts = from_bigram_to_next_token_counts(bigrams)

    bigram_probs = {}
    for b in bigram_counts: 
        total_count = sum(bigram_counts[b].values())
        bigram_probs[b] = {token: count / total_count for token, count in bigram_counts[b].items()}

    initial_bigram = random.choice(bigrams)   #find first bigram
    print(f"Initial Bigram: {initial_bigram}")

    gen_text = generate_text_from_ngram(initial_bigram, 50, bigram_probs)
    print("Generated Text:", gen_text)



if __name__ == "__main__":
    main()
