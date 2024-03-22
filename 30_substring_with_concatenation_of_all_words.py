class Solution:
    def copy_dict(self, d1: dict, d2: dict):
        d2.clear()
        for k, v in d1.items():
            d2[k] = v

    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        word_len = len(words[0])
        counter = {}
        for word in words:
            if word not in counter:
                counter[word] = 1
            else:
                counter[word] += 1
        result = []
        temp_counter = {}
        self.copy_dict(counter, temp_counter)
        for h in range(len(s)):
            window = s[h:h + word_len]
            if temp_counter.get(window, 0):
                temp_counter[window] -= 1
                word_count = 1
                if word_count >= len(words):
                    result.append(h)
                    self.copy_dict(counter, temp_counter)
                    continue
                for h_i in range(h + word_len, len(s), word_len):
                    sub_word = s[h_i:h_i + word_len]
                    if temp_counter.get(sub_word, 0):
                        temp_counter[sub_word] -= 1
                        word_count += 1
                        if word_count >= len(words):
                            result.append(h)
                            self.copy_dict(counter, temp_counter)

                            break

                    else:
                        self.copy_dict(counter, temp_counter)

                        break
        return result

    def findSubstring_(self, s: str, words: list[str]) -> list[int]:
        if not words or not s:
            return []

        word_length = len(words[0])
        word_count = {}

        # Create a frequency map for words
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        result = []

        # Check each possible window in the string
        for i in range(word_length):
            left = i
            count = 0
            temp_word_count = {}

            for j in range(i, len(s) - word_length + 1, word_length):
                word = s[j:j + word_length]
                if word in word_count:
                    temp_word_count[word] = temp_word_count.get(word, 0) + 1
                    count += 1

                    while temp_word_count[word] > word_count[word]:
                        left_word = s[left:left + word_length]
                        temp_word_count[left_word] -= 1
                        left += word_length
                        count -= 1

                    if count == len(words):
                        result.append(left)
                else:
                    temp_word_count.clear()
                    count = 0
                    left = j + word_length

        return result


if __name__ == "__main__":
    sol = Solution()
    assert set(sol.findSubstring(s="a", words=["a"])) == {0}
    assert set(sol.findSubstring(s="aa", words=["a"])) == {0, 1}
    assert set(sol.findSubstring(s="barfoothefoobarman", words=["foo", "bar"])) == {0, 9}
    assert set(sol.findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"])) == set()
    assert set(sol.findSubstring(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"])) == {6, 9, 12}
    assert set(sol.findSubstring(s="lingmindraboofooowingdingbarrwingmonkeypoundcake",
                                 words=["fooo", "barr", "wing", "ding", "wing"])) == {13}
