def main():
    
    email = input('Enter your email: ')
  
    emailstr = email.replace('.','')
    emailstr = emailstr.replace('@', '')
    if not emailstr.isalpha(): #check for alpha characters
        result = False
    else:          
        emaillen = len(email)
        if emaillen <= 5 or emaillen >= 30:  #check email length
            result = False
        else:
            idx_at = email.find('@')  #check for @
            if idx_at == -1:
                result = False
            else:
                idx_dot = email.find('.')
                if idx_dot == -1:  #check for dot
                    result = False
                else:
                    if (idx_dot<idx_at): #check to see if dot id after @
                        result = False
                    else:
                        result = True
   
                
            
    print(result)

        


    

    return result


if __name__ == '__main__':
    main()
