"""Let's practice dictionary functions!"""

__author__: str = "730774862"


# start of 1. invert
def invert(original: dict[str, str]) -> dict[str, str]:
    """takes values of the original dict and makes them keys makes the keys values"""
    inverted: dict[str, str] = {}  # makes an empty dict for inversion
    for key in original:  # runs through the keys in original dict
        value = original[key]
        if value in inverted:
            raise KeyError("Duplicate key found while inverting")
        inverted[value] = key  # sets the key in inverted dict as value and value as key
    return inverted


# start of 2. count
def count(original: list[str]) -> dict[str, int]:
    """counts the number of times a value is in the original list and adds to a dict"""
    count_dict: dict[str, int] = {}  # establishing empty dict to store build-up results
    if len(original) == 0:
        return count_dict
    else:
        for i in original:  # goes through the values in the list
            if i in count_dict:
                count_dict[i] += 1  # if str in list is a key it adds 1 to the count
            else:
                count_dict[i] = (
                    1  # if str in list is not yet a key, it adds a new key and value
                )
    return count_dict


# start of 3. favorite_color
def favorite_color(colors: dict[str, str]) -> str:
    """Returns the color that appears most frequently in the dict"""
    count: dict[str, int] = (
        {}
    )  # creates an empty dict for count of color occurence to be held in
    for key in colors:  # goes through the names of colors
        if colors[key] in count:  # detects if color is already a key in count
            count[
                colors[key]
            ] += 1  # if it is the value at the given color, key increases by 1
        else:
            count[colors[key]] = (
                1  # if not already a key, it is added and value set to 1
            )
    max_count: int = 0
    most_frequent: str = ""
    for color in count:
        if max_count < count[color]:
            most_frequent = color
            max_count = count[color]
    return most_frequent


# Start of 4. bin_len
def bin_len(original: list[str]) -> dict[int, set[str]]:
    """stores string len as key and str with same length as list values"""
    bins: dict[int, set[str]] = {}  # create empty dict for storing later
    for word in original:
        length = len(word)  # goes through list and counts values of strings
        if length not in bins:
            bins[length] = set()
        words = list(bins[length])
        if word not in words:
            words.append(word)
            bins[length] = set(words)
    return bins
