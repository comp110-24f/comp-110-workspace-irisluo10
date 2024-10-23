"""practice with dictionary functions."""

__author__ = "730763981"


def invert(d: dict[str, str]) -> dict[str, str]:
    """
    function: inverts the keys and the values.
    args: d: dictionary to invert
    returns: d: inverted dict
    """

    """# makes list of all values in dict
    vals: list[str] = []
    for key in d:
        vals.append(d[key])

    # looks for duplicate values
    matches: int = 0
    for x in vals:
        for i in range(0, len(vals)):
            if x == vals[i]:
                matches += 1
    # at least one match for each item in list
    # need to test for >1 match
    if matches > len(vals) + 1:
        raise KeyError("error: 2 keys w/ same value")

    for x in d:
        # saves value of key before it's changed to the key
        val: str = d[x]
        # changes value to key
        d[x] = x
        # makes new key w. old val and assigns (w. pop) new
        # val as key that was changed to a val
        d[val] = d.pop(x)"""

    # alternatively...
    inverted_dict = {}

    for key in d:
        value = d[key]
        # check for duplicate values, which would lead to duplicate keys
        # in the inverted dict
        if value in inverted_dict:
            raise KeyError(f"error: multiple keys have the same value '{value}'")
        # swap the key and value
        inverted_dict[value] = key

    return inverted_dict
    """
    print(invert({"a": "z", "b": "y", "c": "x"}))
    output:
    {'a': 'a', 'b': 'y', 'c': 'x'} //line 17
    {'b': 'y', 'c': 'x', 'z': 'a'} //line 20
    1
    {'b': 'b', 'c': 'x', 'z': 'a'}
    {'c': 'x', 'z': 'a', 'y': 'b'}
    2
    {'c': 'c', 'z': 'a', 'y': 'b'}
    {'z': 'a', 'y': 'b', 'x': 'c'}
    3
    """

    return d


def favorite_color(d: dict[str, str]) -> str:
    """
    function: finds which color appears most times.
    args: d: input dict
    returns: answer: most common color
    """

    # makes new dict for color frequency
    color_dict: dict[str, int] = {}
    for item in d:
        color: str = d[item]
        # update color frequency count
        if color not in color_dict:
            color_dict[color] = 1
        else:
            color_dict[color] += 1

    # finds most popular color
    # returns the first color in the dict if
    # tied for most popular color
    answer: str = ""
    max: int = 0
    for item in color_dict:
        # update answer if a color appears more frequently
        if color_dict[item] > max:
            answer = item
            max = color_dict[item]

    return answer


def count(strs: list[str]) -> dict[str, int]:
    """
    function: makes a dict w each key from list
        and val detailing frequency of key
    args: l: input list
    returns: dict w list items and their frequency
    """

    # initialize an empty dictionary to store frequencies
    d: dict[str, int] = {}
    for x in strs:
        # update frequency count for each string in the list
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1

    return d


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """
    function: makes a dict w letter keys and values of words
        that begin w that letter (words from input list)
    args: words: list of words
    returns: d: dictionary
    """

    # initialize an empty dictionary to store words grouped by their first letter
    d: dict[str, list[str]] = {}
    for word in words:
        first: str = word[0].lower()  # get the first letter (converted to lowercase)
        if first not in d:
            # if first letter not in the dictionary, create a new list for words
            # starting with that letter
            words_list: list[str] = []
            words_list.append(word)
            d[first] = words_list
        else:
            # if the letter exists, append the word to the corresponding list
            d[first].append(word)

    return d


def update_attendance(d: dict[str, list[str]], day: str, student: str) -> None:
    """
    function: attendance log dictionary that contains days of the week as keys and a
        list of students who were in attendance as the values
    args: d: dictionary to mutate
        day: day of week
        student: student
    returns: None
    """

    # check if the day already exists in the dictionary
    if day in d:
        # if the student is not already listed for the day, add the student
        if student not in d[day]:
            d[day].append(student)
    else:
        # if the day does not exist, create a new list with the student
        new_log: list[str] = []
        d[day] = new_log
        new_log.append(student)

    return None
