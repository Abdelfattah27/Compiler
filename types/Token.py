class Scanner():
    def __init__(self, FilePath):
        self.FilePath = FilePath
        self.tokens = []
    
    
    
    
    
    
    
        
    def FilePathError(self):
        raise ValueError(f"Invalid File Path for {self.FilePath}")
    def InvalidCharError(self,index,code):
        raise ValueError(f"Invalid character at index {index}: {code[index]}")
