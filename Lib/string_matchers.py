from Lib.data_structures import RollingHash


def karp_rabin(text, pattern) -> bool:
    window_size = len(pattern)
    obj = RollingHash(text, window_size, m=101)
    pattern_hash = obj.calculate_hash(pattern)
    while True:
        if pattern_hash == obj.hash:
            if obj.window_text() == pattern:
                return True
        if not obj.roll_window():
            break
    return False


def string_match(text, pattern) -> bool:  # brute force. Don't know why but currently runs faster than karp-rabin. LOL.
    return any(all(pattern[j] == text[i: i + len(pattern)][j] for j in range(len(pattern)))
               for i in range(len(text) - len(pattern)))
