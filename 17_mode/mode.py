def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    nums_set = set(nums)
    mode = 0
    mode_count = 0
    for num in nums_set:
        if nums.count(num) > mode_count:
            mode_count = nums.count(num)
            mode = num

    return mode
