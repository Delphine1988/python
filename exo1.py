def palindrome():
    is_palindrome = True
    word = input('Votre mot:')
    my_range = range(len(word))
    for i in my_range:

        if word[i] == word[-1 - i]:
            "cas d'un palindrome"
        else:
            "pas un palindrome"
            is_palindrome = False


palindrome()


def isPalindrome(word):
    new_word = ''.join(reversed(word))
    if word == new_word:
        return print("c'est un palindrome")
    return print("ce n'est pas un palindrome")


isPalindrome(input(''))
