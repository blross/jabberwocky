from abc import ABC, abstractmethod

class WordGenerator(ABC):

    def _get_corpus(self, corpus_file='corpus.txt'):
        with open(corpus_file) as f:
            corpus_raw = f.read()
            corpus_list = corpus_raw.split()
            return corpus_list

    @abstractmethod
    def generate_word(): pass
