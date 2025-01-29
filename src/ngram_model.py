import string
import random


#task 1
def preprocess(filename): 
    with open(filename, 'r') as file:
        text = file.read().lower()
        text = text.translate(str.maketrans('', '', string.punctuation))   #remove punctuations 
        tokens = text.split()   #words=tokens

    return tokens



def create_bigrams(tokens):
    return [(tokens[i], tokens[i+1]) for i in range(len(tokens)-1)]




def from_bigram_to_next_token_counts(bigrams):
    from_bigram_to_next_token_counts = {}

    for b in bigrams:
        if b not in from_bigram_to_next_token_counts:
            from_bigram_to_next_token_counts[b] = {}

        next_token = b[1]
        if next_token not in from_bigram_to_next_token_counts[b]:
            from_bigram_to_next_token_counts[b][next_token] = 1
        else:
            from_bigram_to_next_token_counts[b][next_token] += 1


    return from_bigram_to_next_token_counts




#task 2

def from_bigram_to_next_token_probs(bigram_counts):
    from_bigram_to_next_token_probs  = {}

    for b, next_token in bigram_counts.items():
        total = sum(next_token.values())
        from_bigram_to_next_token_probs [b] = {token: count/total for token, count in next_token.items()}
    return from_bigram_to_next_token_probs 




# def trigram_dict(trigrams): 
#     t_dict = {}
#     for t in trigrams:
#         if t not in t_dict: 
#             t_dict[t] = {}
#         next_token = t[2]
#         if next_token not in t_dict[t]:
#             t_dict[t][next_token] = 1
#         else: 
#             t_dict[t][next_token] += 1
#     return t_dict



#task 3

def sample_next_token(ngram, ngram_prob):
    next_token =  ngram_prob.get(ngram, {})
    if not next_token:
        return random.choice(list(ngram_prob.keys()))
    
    tokens, probs = zip(*next_token.items())
    next_token = random.choices(tokens, probs)[0]

    if next_token == ngram[-1]:
        return random.choice(tokens)
    
    return next_token
    