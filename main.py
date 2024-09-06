import sys
from collections import Counter

class InvalidArgument(Exception):
    pass


def format_results(words_counter: Counter, size_result_list: int):
    """Format our result, returning a list of tuples with the `size_result_list` most common words

    Parameters
    ----------
    words_counter : Counter
    size_result_list : bool, optional

    Returns
    -------
    tuple
        a list of words used and their frequency
    """
    formated_results = words_counter.most_common(size_result_list)
    return formated_results


def run(sentence: str, size_result_list: int):
    """Main entrypoint, returns a list of size `size_result_list` where each element contains
    a word and the frequency of that word in `sentence`

    Parameters
    ----------
    sentence : str
    size_result_list : bool, optional

    Returns
    -------
    list
        a list of words used and their frequency
    """
    if not isinstance(size_result_list, int):
        raise InvalidArgument("The second argument need to be an integer. ")

    splitted_words = sentence.split(" ")
    ordered_words = sorted(splitted_words)
    result_list = format_results(Counter(ordered_words), size_result_list)
    print(result_list)
    return result_list


if __name__ == "__main__":
    sentence = str(sys.argv[1])
    try:
        size_result_list = int(sys.argv[2])
    except ValueError:
        raise InvalidArgument("The second argument need to be an integer. ")
    run(sentence, size_result_list)
