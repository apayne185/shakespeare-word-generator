from src.ngram_model import *
from src.text_generation import *
from nltk.corpus import shakespeare



def main():
    # tokens = preprocess('data/shakespeare.txt')
    tokens = preprocess()

    if not tokens:
        print("No tokens found. Exiting.")
        return

    while True: 
        try: 
            n = int(input('\nEnter the n-gram size (2,3,4): '))
            if n not in [2,3,4]:
                print("Please enter 2,3,4")
                continue
            break
        except ValueError:
            print("Invalid input. 2,3, or 4 only")


    print(f"\nGenerating text with {n}-grams:")
    ngrams = create_ngrams(tokens,n)
    if not ngrams:
        print(f"Not enough words to form {n} grams, Exiting.")
        return
    
    ngram_counts = from_ngram_to_next_token_counts(ngrams)
    ngram_probs = from_ngram_to_next_token_probs(ngram_counts)

    if not ngram_probs:  
        print(f"Skipping {n}-grams no valid probabilities found")
        return
    

    initial_ngram = random.choice(list(ngram_probs.keys()))
    gen_text = generate_text_from_ngram(initial_ngram, 50, ngram_probs, n)
    print("Generated Text:", gen_text)



if __name__ == "__main__":
    main()
