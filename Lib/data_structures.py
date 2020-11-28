class RollingHash:
    def __init__(self, inp, window_size, m=11, a=256):
        self._inp = inp
        self._text_size = len(inp)
        self._m = m  # a random prime number. size of m inversely proportional to collisions.
        self._a = a  # universe size of the characters. 256 for ASCII.
        self.hash = 0
        self._window_size = window_size
        self._window_start = 0
        self._window_end = window_size - 1
        for i in range(window_size):
            self.hash = (self.hash * a + ord(inp[i])) % m

    def roll_window(self) -> bool:
        if self._window_end + 1 >= self._text_size:
            return False
        # recalculate hash
        self.hash = (self.hash * self._a - (
                    (ord(self._inp[self._window_start]) * (self._a ** self._window_size)) % self._m)
                     + ord(self._inp[self._window_end + 1])) % self._m
        # update start and end
        self._window_start += 1
        self._window_end += 1
        return True

    def window_text(self) -> str:
        return self._inp[self._window_start:self._window_end + 1]

    def calculate_hash(self, text) -> int:
        hash_val = 0
        for i in range(len(text)):
            hash_val = (hash_val * self._a + ord(text[i])) % self._m
        return hash_val
