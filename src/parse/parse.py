import nltk
from nltk.tag import pos_tag, map_tag
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import wordnet
#from nltk.corpus import stopwords

stemmer = SnowballStemmer("english")

# grammar - context free grammars

# first pass: identify domain

# second pass: use domain specific settings to identify command

# general: collocations, bigrams

stopwords = ['the']
stoptypes = ['DT', 'CC']

grammar1 = nltk.CFG.fromstring("""
    S -> NP VP
    VP -> V NP | V NP PP | VB IN
    PP -> P NP
    NP -> NN
    """)


class Parse():

    def __init__(self, query):
        self.query = query

        self.command_verb = ""
        self.synset_verb = ""
        self.object_noun = ""
        self.synset_noun = ""
        
        self.abort = True

        self.stop = []
        self.tokens = None
        self.tags = None
        self.stems = None

        self.tokenize(self.query)
        self.stem(self.tokens)
        self.tag(self.stems)
        self.stopper(self.tags)
        self.synonyms(self.stop)

    def tokenize(self, sent):
        print("Original query:", sent)
        self.tokens = nltk.word_tokenize(sent)
        #print(self.tokens,"\n")

    def tag(self, sent):
        #print("Tagger")
        self.tags = pos_tag(sent)
        #print(self.tags, "\n")

    def stem(self, sent):
        #print("Stemmer")
        self.stems = [stemmer.stem(word) for word in sent]
        #print(self.stems, "\n")

    def stopper(self, sent):
        #print("Stopper")
        #self.stop = [w for w, wtype in self.stems if wtype not in stoptypes]
        for word in sent:
            if word[1] not in stoptypes:
                self.stop.append(word)
        #print(self.stop, "\n")

    def synonyms(self, sent):
        print("Synonyms")
        print(sent)

        for w in sent:
        # isolate verb(s)
            if "V" in w[1]:
                self.command_verb += w[0]
                self.command_verb += " "
                self.synset_verb += w[0]
                self.synset_verb += "_"
                self.abort = False
            if "RP" in w[1]:
                self.command_verb += w[0]
                self.synset_verb += w[0]
            if "IN" in w[1]:
                self.command_verb += w[0]
                self.synset_verb += w[0]

        # isolate nouns/object
            if "NN" == w[1]:
                self.object_noun += w[0]
                self.synset_noun += w[0]

        print("verb:", self.synset_verb)
        print("noun:", self.synset_noun)
        #self.syns = wordnet.synsets(self.synset_verb, pos=wordnet.VERB)

        if self.abort == False:
            print(wordnet.synset(self.synset_verb+'.v.01'))
        else:
            print("No verb identified")

    def verbphrase(self):
        verbphrase = nltk.RecursiveDescentParser(grammar1)
        for tree in verbphrase.parse(self.tags):
            print(tree)
