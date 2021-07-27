from typing import List


def solution(words: List[str], k: int) -> List[str]:
    result = []
    curr_words_len = 0
    curr_words = []
    for word in words:
        if curr_words_len + len(curr_words) + len(word) > k:
            if len(curr_words) == 1:
                result.append(curr_words[0] + " " * (k - curr_words_len))
            else:
                num_spaces = k - curr_words_len
                spaces_between, extras = divmod(num_spaces, len(curr_words) - 1)
                for i in range(extras):
                    curr_words[i] += " "
                result.append((" " * spaces_between).join(curr_words))
            curr_words = []
            curr_words_len = 0
        curr_words.append(word)
        curr_words_len += len(word)
    result.append(" ".join(curr_words) + " " * (k - curr_words_len - len(curr_words) + 1))
    return result
