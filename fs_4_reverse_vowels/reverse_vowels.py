def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowel_list = [ltr for ltr in s if ltr.lower() in 'aeiou']
    vowel_list.reverse()
    new_str = ''
    idx = 0
    #print(vowel_list)
    for ltr in s:
        
        if ltr.lower() in 'aeiou':
            new_str = new_str + vowel_list[idx]
            idx +=1
            
        else:
            new_str = new_str + ltr

    return new_str
