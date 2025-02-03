import string
import random
import nltk
from nltk.corpus import shakespeare

nltk.download('shakespeare')

    
def preprocess():
    shakespeare_txt = []
    for fild_id in shakespeare.fileids():
        shakespeare_txt.extend(shakespeare.words(fild_id))

    text = " ".join(shakespeare_txt).lower()
    text = text.translate(str.maketrans('', '', string.punctuation))   #no punctuations
    tokens = text.split()

    return tokens




def create_ngrams(tokens, n):
    if len(tokens) < n:
        return []
    return [tuple(tokens[i:i+n]) for i in range(len(tokens)-n+1)]




def from_ngram_to_next_token_counts(ngrams):
    ngram_counts = {}

    for n in ngrams:
        prefix = n[:-1]
        next_token = n[-1]

        if prefix not in ngram_counts:
            ngram_counts[prefix] = {}

        # next_token = n[1]
        if next_token not in ngram_counts[prefix]:
            ngram_counts[prefix][next_token] = 1
        else:
            ngram_counts[prefix][next_token] += 1

    return ngram_counts




#task 2

def from_ngram_to_next_token_probs(ngram_counts, alpha=1):
    ngram_probs  = {}

    for prefix, next_token_counts in ngram_counts.items():
        total = sum(next_token_counts.values())
        ngram_probs [prefix] = {
            token: count /total for token, count in next_token_counts.items()}
        
    return ngram_probs 





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
    next_token_probs =  ngram_prob.get(ngram, {})

    if not next_token_probs:
        for _ in range(3):
            current_ngram= random.choice(list(ngram_prob.keys()))
            next_token_probs = ngram_prob.get(current_ngram, {})
            if next_token_probs:
                break
            # return random_gram[-1]

        if not next_token_probs:
            return None
    
    tokens, probs = zip(*next_token_probs.items())
    next_token = random.choices(tokens, probs)[0]

    return next_token
    