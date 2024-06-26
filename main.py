def main():
    email = input('Enter your email: ')
   
    result = True
    
    if not 5 <= len(email) <= 30:
        result = False
    else:
        if not email.find('@'):
            result = False
        else:
            if not email.isalpha():
                result = False

    print(result)    

    return result


if __name__ == '__main__':
    main()
