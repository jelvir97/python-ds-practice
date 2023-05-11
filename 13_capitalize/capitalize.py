def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    phrase_lst = list(phrase)
    phrase_lst[0] = phrase_lst[0].upper()
    phrase = '.'.join(phrase_lst)
    return phrase.replace('.','')