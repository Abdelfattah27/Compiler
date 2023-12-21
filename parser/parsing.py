import pickle
class CParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.index = 0

    def match(self, expected_token,index=1):
        if self.current_token[index] == expected_token:
            self.advance()
        else:
            raise SyntaxError(f"Expected '{expected_token}', but found '{self.current_token}'")

    def advance(self):
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
            self.index += 1
        else:
            self.current_token = None

    def parse(self):
        self.advance()  # Start with the first token
        self.program()  # Start parsing the program

    def program(self):
        # Define the grammar rules for the program
        while self.current_token:
            self.statement()

    def statement(self):
        # Define the grammar rules for a statement
        if(self.current_token==None):
            return
        if self.current_token[1] == '#':
            self.match("#")
            self.match('include')
            self.match('<')
            self.match('keyword',0)
            self.match('>')
        elif self.current_token[1]=="void":
            self.match("void")
            self.match("ID",0)
            self.match("(")
            self.expression()
            self.match(")")
            self.match("{")
            self.statement()
            self.match("}")
            
        elif self.current_token[1] == 'int':
            num =False
            self.match('int')
            self.match('ID',0)  # Assuming 'ID' represents an identifier
            try:
                self.match("=")
                num=True
            except:
                pass 
            if(num):
                self.match("number",0)
            self.match(';')
            self.statement()
        elif self.current_token[1] == 'if':
            self.match('if')
            self.match('(')
            self.expression()
            self.match(')')
            if self.current_token[1]==';':
                self.match(";")
                self.statement()
            else:
                self.match("{")
                self.statement()
                self.match("}")
                self.statement()
            if self.current_token[1] == 'else':
                self.match('else')
                self.statement()
        elif self.current_token[1] == 'while':
            self.match('while')
            self.match('(')
            self.expression()
            self.match(')')
            if(self.current_token[1]==';'):
                self.match(';') 
                self.statement()
            else:
                self.match('{')
                self.statement()
                self.match('}')
                self.statement()
        else:
            # Handle other types of statements as needed
            pass

    def expression(self):
        # Define the grammar rules for an expression
        # This is a simplified example; you'll need to extend it based on C's grammar
        self.term()
        while self.current_token[1] in ['*' ,'/', '%', '-', '=', '+','<' ,'<=' ,'>' ,'>=','==','!=',","]:
            self.match(self.current_token[1])
            self.term()

    def term(self):
        # Define the grammar rules for a term
        # This is a simplified example; you'll need to extend it based on C's grammar
        self.factor()
        while self.current_token[1] in ['*' ,'/', '%', '-', '=', '+','<' ,'<=' ,'>' ,'>=','==','!=',","]:
            self.match(self.current_token[1])
            self.factor()

    def factor(self):
        # Define the grammar rules for a factor
        if self.current_token[1] == '(':
            
            self.match('(')
            self.expression()
            self.match(')')
        elif self.current_token[0] == 'ID':
            self.match('ID',0)  # Assuming 'ID' represents an identifier
        elif self.current_token[1].isdigit():
            self.match('number',0)  # Assuming 'NUM' represents a number
        else:
            raise SyntaxError(f"Unexpected token: {self.current_token}")

# Example usage
tokens = [('special_char', '#'),('keyword', 'include')]

def read_pairs_from_pickle(file_path):
    with open(file_path, 'rb') as file:
        pairs = pickle.load(file)
        file.close()
    return pairs

tokens=read_pairs_from_pickle("../output.pkl")
print(tokens)
parser = CParser(tokens)
parser.parse()
print("Grammar is valid.")