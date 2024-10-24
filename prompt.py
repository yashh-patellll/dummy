from .counter import count_occurrences

def report_count(token):
    """Generate a report of how many times a token appears in the corpus."""
    count = count_occurrences('corpus.txt', token)
    return f"The term {token} shows up in the corpus {count} times."