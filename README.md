# Shakespearean Text Generator using N-Gram Model & NLTK
#### By Anna Payne

This repository is code to generate text in the style of William Shakespeare using an n-gram language model. It uses the NLTK library's Shakespeare Corpus for training the model and can generate text based on bigrams, trigrams, and quadgrams (2,3,4-grams).

## Requirements
* Python 3.x
* NLTK

To install run : `pip install nltk`   and  `pip install pytest`


## To Run the Code

1. `python main.py`
2. The code will ask you for an input of a n-gram: 2,3,4
3. Then the code will display all ngrams made and the generated text. 
4. If you would like to test the code: 
    * cd tests
    * run  `pytest` 


## File Structure

### /src
* ngram_model.py : Contains the functions to preprocess the NLTK Corpus Shakespeare text, create n-grams, calculate the n-gram counts/propability, and to sample the next tokens. 
* text_generation.py : Contains the text gen. function for the ngrams. 

### /tests
* testcases.py : Contains test cases for the code. 

### /data
* Test shakespeare data for quicker code. Not necessary to use now. 

### /docs 
* documentation.md : Complete documentation of the code
* surveys.md : User surveys 


* main.py : Entry code of the program, connects the code for the different files. 



