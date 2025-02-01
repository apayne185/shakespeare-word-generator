from src.ngram_model import sample_next_token



def generate_text_from_ngram(initial_ngram, length, ngram_probs):
    # gen_text = [initial_ngram[0], initial_ngram[1]]
    gen_text = list(initial_ngram)
    current_ngram = initial_ngram

    for _ in range(length - len(initial_ngram)):
        next_token = sample_next_token(current_ngram, ngram_probs)
        if next_token is None:
            print("No valid continuation found. Stopping generation.")
            break

        print(f"Current Ngram: {current_ngram}, Next Token: {next_token}")  

        if next_token != gen_text[-1]:
            gen_text.append(next_token)

        current_ngram = tuple(gen_text[-(len(initial_ngram)-1):]) + (next_token,)



    return ' '.join(gen_text)

