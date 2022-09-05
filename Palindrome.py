def palindrome_fun(str):
    if str == str[::-1]:
        return True
    return False


if __name__=='__main__':
    print(palindrome_fun('sis'))
