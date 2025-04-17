# William Starks
# 4/16/2025
# lab21.py
# NO AI

def isAlpha(data):
    letterscheck = data.isalpha()
    if letterscheck == True:
        return True
    else:
        return False
      
    
def isDigit(data):
    digitcheck = data.isdigit()
    if digitcheck == True:
        return True
    else:
        return False

def main():
    
    letters = 0
    digits = 0
    lines = 0
    
    try:
        
        userfile = str(input("Enter the name of the file to open for read: "))
        
        file = open(userfile, 'r')
        line = file.readline()
        while line != '':
                lines += 1
                for char in line:
                
                    a_check = isAlpha(char)
                    d_check = isDigit(char)
                    if a_check == True:
                        letters += 1
                    if d_check == True:
                        digits += 1
                            
                line = file.readline()

        file.close()


    
        print(f'The number of alphabetic letters is {letters}\nThe number of digits is {digits}\nThe number of lines is {lines}')      
        
    except FileNotFoundError:
        print(f'[Errno 2] No such file or directory: {userfile}')
          
             
main()
