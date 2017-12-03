from markovify import Chain

from word_generator import WordGenerator


class Markov(WordGenerator):

    def __init__(self, state_size=2):
        corpus_lists = [list(word) for word in self._get_corpus()]
        self.chain = Chain(corpus_lists, state_size)

    def generate_word(self):
        return ''.join(self.chain.walk())
