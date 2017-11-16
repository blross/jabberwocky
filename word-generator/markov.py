from markovify import Chain


def build_chain(corpus_file='corpus.txt', state_size=2):
    with open(corpus_file) as f:
        corpus_raw = f.read()
    corpus_list = [list(word) for word in corpus_raw.split()]
    return Chain(corpus_list, state_size)

def generate_word():
    mc = build_chain()
    return ''.join(mc.walk())
