def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    phrase_lst = list(phrase)
    swap_lst = [char.swapcase() if to_swap.casefold() == char.casefold()  else char for char in phrase_lst]
    swap_lst = '.'.join(swap_lst)
    return swap_lst.replace('.','')
