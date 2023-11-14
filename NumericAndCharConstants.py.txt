import re 
def validate_number(keyword):
    regexForFolats=r'[0-9]*\.[0-9]+'
    regex = re.compile(regexForFolats)
    match = regex.match(keyword)
    if(match):
        return True 
    else: 
        return False

def validate_characters_constant(keyword):
    if keyword[0]== "'" and keyword[len(keyword)-1] == "'":
        char_constant = re.match(r'([^"\\]|\\.)*', keyword)
        if char_constant:
           return True 
        else:
            return False 
    return False

print (validate_number(".42342"))
print (validate_characters_constant("\'23f3s2.44h3\'"))
