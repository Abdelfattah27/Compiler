import argparse
import re 


def is_number(keyword):
    regexForFolats=r'[0-9]+(\.[0-9]+)?'
    regex = re.compile(regexForFolats)
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

def is_operator(tempString:str):
    operators = ['*' ,'/', '%', '-', '=', '+']
    if(tempString in operators):
        return True
    else:
        return False

def is_relational_operator(tempString:str):
    relational_operators = ['<' ,'<=' ,'>' ,'>=','==','!=']
    if(tempString in relational_operators):
        return True
    else:
        return False

def is_special_char(char):
    symbols = [';', ':', ',', '[', ']', '(', ')', '{', '}','#','.','"',"'",'\\']
    
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
    
def is_identifier(tempString:str):
    #test for not a key word, there is an identifier fun
    if(tempString.isidentifier()):
        return True
    else:
        return False

def is_start_of_comment(tempString:str):
    if(tempString=="//" or tempString=="/*"):
        return True
    else:
        return False
    
def token_Type(tempString):
    if(is_operator(tempString)):
        return "Operator" , tempString
    elif (is_relational_operator(tempString)):
        return "relational_operator", tempString
    elif (is_special_char(tempString)):
        return "special_char", tempString
    elif (is_whitespace(tempString)):
        return "whitespace", tempString
    elif (is_identifier(tempString)):
        return "identifier", tempString
    elif (is_start_of_comment(tempString)):
        return "start_of_comment", tempString
    elif (is_characters_constant(tempString)):
        return "characters_constant", tempString
    elif (is_number(tempString)):
        return "number", tempString
       
        

# Create ArgumentParser object
parser = argparse.ArgumentParser(description= 'Simple scanner that tokenize a small part of C language and store them in symbol table \
                                 \n')

# Add command-line arguments
parser.add_argument('filename', type=str, help='Input file to scan')


# Parse the command-line arguments
args = parser.parse_args()



# Access the values of the arguments
filename = open(args.filename,'r')
filelength = len(open(args.filename,'r').read())




tempToken = ""

while filelength >= 0:
    tempChar = filename.read(1)
    filelength-=1
    #just see if the entered character is delmiter or not
    if (is_operator(tempChar) or is_special_char(tempChar) or is_whitespace(tempChar)):
        if tempToken!='':
            print(token_Type(tempToken))
        print(token_Type(tempChar))
        tempToken=""
        continue

    elif (is_relational_operator(tempChar)):
        if tempToken!='':
            print(token_Type(tempToken))
        tempToken=tempChar
        tempChar=filename.read(1)
        filelength-=1
        tempToken+=tempChar
        
        if(is_relational_operator(tempToken)):
            if tempToken!='':
                print(token_Type(tempToken))
            tempToken=""
            continue
        else:
            if tempToken!='':
                print(token_Type(tempToken[0]))
            tempToken=tempToken[1]
            continue

    tempToken+=tempChar


