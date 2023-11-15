def validate_special_char(char):
    symbols = [';', ':', ',', '[', ']', '(', ')', '{', '}']
    
    if char in symbols:
        return 'special char', char
    else:
        return 'invalid char'
        
        
        
def validate_whitespace(char):
    whitespace = [' ', '\t', '\n', '\r', '\v', '\f']
    
    if char in whitespace:
        return 'whitespace', char
    else:
        return 'invalid'
        
        
        
print(validate_special_char(','));     
print(validate_whitespace('\t'));     
