def check_phrase(msg,keyword):
    """
    Checks a message to see whether it includes a specified string.

    Parameters
    ----------
    msg : str
        The string to be parsed.
    keyword : str
        The keyword to be looked for in the string.

    Returns
    -------
    bool
        True if the keyword is in the string, False otherwise.
    """
    msg = str(msg)
    keyword = str(keyword)
    msg = ''.join(filter(str.isalnum,msg))
    msg = msg.lower()
    keyword = ''.join(filter(str.isalnum,keyword))
    keyword = keyword.lower()
    if (keyword in msg):
        return True
    else:
        return False
