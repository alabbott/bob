import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("I had a banana for lunch, 400 calories")

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)