import argparse
import re 
import pickle

def is_language_keyword(keyword) : 

    c_keywords = [
        'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
        'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
        'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static',
        'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while',"include","stdio.h"
    ]
    return keyword in c_keywords


def is_number(keyword):
    regex_for_floats=r'[0-9]+(\.[0-9]+)?'
    regex = re.compile(regex_for_floats)
    match = regex.match(keyword)
    if(match):
        return True 
    else: 
        return False

def is_characters_constant(keyword):
    if keyword[0]== "'" and keyword[len(keyword)-1] == "'":
        char_constant = re.match(r'([^"\\]|\\.)*', keyword)
        if char_constant:
           return True 
        else:
            return False 
    return False

def is_operator(temp_string:str):
    operators = ['*' ,'/', '%', '-', '=', '+']
    if(temp_string in operators):
        return True
    else:
        return False

def is_relational_operator(temp_string:str):
    relational_operators = ['<' ,'<=' ,'>' ,'>=','==','!=']
    if(temp_string in relational_operators):
        return True
    else:
        return False

def is_special_char(char):
    symbols = [';', ':', ',', '[', ']', '(', ')', '{', '}','#','"',"'",'\\']
    
    if char in symbols:
        return True #'special char', char
    else:
        return False #'invalid char'
    
def is_whitespace(char):
    whitespace = [' ', '\t', '\n', '\r', '\v', '\f']
    
    if char in whitespace:
        return True #'whitespace', char
    else:
        return False #'invalid'
    
def is_identifier(temp_string:str):
    #test for not a key word, there is an identifier fun
    if(temp_string.isidentifier()):
        return True
    else:
        return False

def is_start_of_comment(temp_string:str):
    if(temp_string=="//" or temp_string=="/*"):
        return True
    else:
        return False
    
def token_Type(temp_string):
    if(is_operator(temp_string)):
        return "Operator" , temp_string
    elif (is_relational_operator(temp_string)):
        return "relational_operator", temp_string
    elif (is_special_char(temp_string)):
        return "special_char", temp_string
    elif (is_whitespace(temp_string)):
        return "whitespace", temp_string
    elif (is_language_keyword(temp_string)) : 
        return "keyword" , temp_string
    elif (is_identifier(temp_string)):
        return "ID", temp_string
    elif (is_start_of_comment(temp_string)):
        return "start_of_comment", temp_string
    elif (is_characters_constant(temp_string)):
        return "characters_constant", temp_string
    elif (is_number(temp_string)):
        return "number", temp_string
    
    
       
        

# Create ArgumentParser object
parser = argparse.ArgumentParser(description= 'Simple scanner that tokenize a small part of C language and store them in symbol table \
                                 \n')

# Add command-line arguments
parser.add_argument('filename', type=str, help='Input file to scan')


# Parse the command-line arguments
args = parser.parse_args()



# Access the values of the arguments
filename = open(args.filename,'r')
file_length = len(open(args.filename,'r').read())



temp_token = ""
output_result = []

while file_length >= 0:
    temp_char = filename.read(1)
    file_length-=1
    #just see if the entered character is delmiter or not
    if (is_operator(temp_char) or is_special_char(temp_char) or is_whitespace(temp_char)):
        if temp_token!='':
            if(token_Type(temp_token)[0]!="whitespace"):
                output_result.append(token_Type(temp_token))
        if(token_Type(temp_char)[0]!="whitespace"):
            output_result.append(token_Type(temp_char))
        temp_token=""
        continue

    elif (is_relational_operator(temp_char)):
        if temp_token!='':
            output_result.append(token_Type(temp_token))
        temp_token=temp_char
        temp_char=filename.read(1)
        file_length-=1
        temp_token+=temp_char
        
        if(is_relational_operator(temp_token)):
            if temp_token!='':
                output_result.append(token_Type(temp_token))
            temp_token=""
            continue
        else:
            if temp_token!='':
                output_result.append(token_Type(temp_token[0]))
            temp_token=temp_token[1]
            continue

    temp_token+=temp_char



def write_tokens_in_file(file_path,data):
    print(data,type(data[0]))
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)

write_tokens_in_file("../output.pkl",output_result)




