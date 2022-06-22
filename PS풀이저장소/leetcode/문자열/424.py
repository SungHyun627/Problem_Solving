from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest_substring_len = 0
        max_count = 0
        start = 0
        count_char = defaultdict(int)
        
        for i in range(len(s)):
            count_char[s[i]] += 1
            max_count = max(max_count, count_char[s[i]])
            if (i - start + 1 - max_count) > k:
                count_char[s[start]] -= 1
                start += 1
            longest_substring_len = max(longest_substring_len, i-start+1)
        return longest_substring_len