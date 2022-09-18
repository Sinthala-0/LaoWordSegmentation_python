
class Lao_alphabets:

    # Lao characters_____________________________________________________________
    
    # Vowels at the start of a word
    X0 = ['ເ','ແ','ໂ','ໄ','ໃ']

    def is_X0(self, x:str) -> bool:
        for i in self.X0:
            if i == x: 
                return True
        
        return False
    

    # A consonant that can combine with other consonants
    X1 = 'ຫ'

    def is_X1(self,x:str) -> bool:
        return True if x == self.X1 else False
        
        

    # Consonants
    X = ['ກ', 'ຂ', 'ຄ', 'ງ', 'ຈ', 'ສ', 'ຊ', 'ຍ', 'ດ', 'ຕ', 'ຖ', 
        'ທ', 'ນ', 'ບ', 'ປ', 'ຜ', 'ຝ', 'ພ', 'ຟ', 'ມ', 'ຢ', 'ຣ',
         'ລ', 'ວ', 'ຫ', 'ອ', 'ຮ', 'ໜ', 'ໝ']

    def is_X(self, x:str) -> bool:
        for i in self.X: 
            if i == x:
                return True
        return False
    

    # Special Consonants 
    X2 = ['ຼ', 'ຣ', 'ວ']

    def is_X2(self, x:str) -> bool:
        for i in self.X2: 
            if i == x:
                 return True
        
        return False
    

    # Vowels for the main consonant
    X3 = ['ຸ','ູ']

    def is_X3(self, x:str) -> bool:
        for i in self.X3: 
            if i == x:
                 return True
        
        return False
    

    # Vowels for the word
    X4 = ['ິ', 'ີ', 'ຶ', 'ື', 'ໍ', 'ົ', 'ັ','ຳ']

    def is_X4(self, x:str) -> bool:
        for i in self.X4:
            if i == x: 
                return True
        
        return False
    
    # Tone markers
    X5 = ['່','້','໊','໋']

    def is_X5(self, x:str) -> bool:
        for i in self.X5:
            if i == x:
                 return True
        
        return False;
    
    # Consonants
    X6 = ['ວ','ອ','ຽ']

    def is_X6(self ,x:str) -> bool:
        for i in self.X6:
            if i == x:
                 return True
        
        return False;
    
    # Vowels
    X7 = ['ະ','າ','ຳ']

    def is_X7(self, x:str) -> bool:
        for i in self.X7:
            if i == x: 
                return True
        
        return False
    
    # A Vowel
    X7_2 = 'ະ'

    def is_X7_2(self, x:str) -> bool:
        return True if x == self.X7_2 else False
    
    # Consonants
    X8 = ['ກ', 'ງ', 'ຍ', 'ດ', 'ນ', 'ມ', 'ບ', 'ວ']

    def is_X8(self, x:str) -> bool:
        for i in self.X8:
            if i == x:
                 return True;
        
        return False;

    # Consonants
    X9 = ['ຈ', 'ສ', 'ຊ', 'ພ', 'ຟ', 'ລ', 'ຣ']

    def is_X9( self, x:str) -> bool:
        for i in self.X9:
            if i == x:
                 return True
        
        return False
    
    # Special consonants
    X10 = ['ຯ', 'ໆ', '໌']

    def is_X10(self, x:str) -> bool:
        for i in self.X10:
            if i == x:
                 return True
        
        return False
    
    # Consonants
    MIX_CONSONANTS = ['ກ', 'ຂ', 'ຄ', 'ງ', 'ຈ']

    def is_MixConsonants(self, string:str) -> bool:
        chars = [ char for char in string]
        for x in self.MIX_CONSONANTS:
            if x == chars[-1]:
                return True
        
        return False
    

    # Other type of characters_________________________________________

    special_chars = " ,./:'\"!@#$%^&*()_+-=?~“`0123456789"
    SPECIAL_CHARS = [str for str in special_chars]

    def is_SPECIALCHARS(self, x:str) -> bool:
        for i in self.SPECIAL_CHARS:
            if i == x:
                 return True
        
        return False
    
    
    alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ALPHABETS = [letter for letter in alphabets]    #Works the same as .ToCharArray() in java

    def is_ALPHABETS(self, x:str) -> bool:
        for i in self.ALPHABETS:
            if i == x:
                return True
        
        return False
    









