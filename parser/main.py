
from Cparser import CParser
import pickle
# Example usage
tokens = [('special_char', '#'),('keyword', 'include')]

def read_pairs_from_pickle(file_path):
    with open(file_path, 'rb') as file:
        pairs = pickle.load(file)
        file.close()
    return pairs

tokens=read_pairs_from_pickle("../output.pkl")
parser = CParser(tokens)
parser.parse()
print("Grammar is valid.")