from Parser import Parser
class CParser(Parser):
    
    
    def parse(self):
        self.advance()  # Start with the first token
        self.program()  # Start parsing the program

    def program(self):
        # Define the grammar rules for the program
        while self.current_token:
            self.statement()
    
    def declare_variable(self):
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
        
    def handle_block(self):
        if(self.current_token[1]==';'):
            self.match(';') 
            self.statement()
        else:
          
            self.match('{')
            self.statement()
            while(self.current_token[1]!="}"):
                self.statement()
            self.match('}')

    def enum_constants(self):
        # Define the grammar rules for enum constants
        self.match('{')
        self.match('ID', 0)
        while self.current_token[1] == ',':
            self.match(',')
            self.match('ID', 0)
        self.match('}')
        self.match(';')
        
    def struct_members(self):
        # Define the grammar rules for struct members
        self.match('{')
        while self.current_token[1] != '}':
            self.declare_variable()     
        self.match('}')
        self.match(';')     
    def recognize_preprocessor(self):
            self.match("#")
            self.match('include')
            self.match('<')
            self.match('keyword',0)
            self.match('>')
    def recognize_void_functions(self):
            self.match("void")
            self.match("ID",0)
            self.match("(")
            self.expression()
            self.match(")")
            self.handle_block()
            
    def recognize_if(self):
        self.match('if')
        self.match('(')
        self.expression()
        self.match(')')
        self.handle_block()
        if self.current_token[1] == 'else':
            self.match('else')
            self.statement()
            
    def recognize_loops(self,type):
        if(type=='while'):
            self.match('while')
            self.match('(')
            self.expression()
            self.match(')')
        elif(type=='for'):
            self.match('for')
            self.match("(")
            self.declare_variable()
            self.expression()
            self.match(";")
            self.term()
            self.match(")")
        self.handle_block()
        
    def recognize_enum(self):
        self.match('enum')
        self.match('ID', 0)
       
        self.enum_constants()
        
    def recognize_struct(self):
        self.match('struct')
        self.match('ID', 0)
        
        self.struct_members()
        

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

    def statement(self):
        # Define the grammar rules for a statement
        if(self.current_token==None):
            return
        
        if self.current_token[1] == '#':
            self.recognize_preprocessor()
        
        elif self.current_token[0] == 'comment':
            self.match("comment",0)
        
        elif self.current_token[1]=="void":
            self.recognize_void_functions()
        
        elif self.current_token[1] == 'if':
            self.recognize_if()
        
        elif self.current_token[1] == 'while':
            self.recognize_loops("while")
        
        elif self.current_token[1] == 'for':
            self.recognize_loops("for")

        elif self.current_token[1] == 'int':
            self.declare_variable()
            
        elif self.current_token[1] == 'enum':
            self.recognize_enum()

        elif self.current_token[1] == 'struct':
            self.recognize_struct()
        
        else:
            # Handle other types of statements as needed
            pass


