
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.index = 0

    def match(self, expected_token,index=1):
        if self.current_token ==None :
            raise SyntaxError(f"Expected '{expected_token}', but found None")

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
            
  

   