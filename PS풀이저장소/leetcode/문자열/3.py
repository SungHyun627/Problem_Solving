class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start_idx = 0
        longest_substring_len = 0
        used_char = {}
        for i in range(len(s)):
            if s[i] in used_char and start_idx <= used_char[s[i]]:
                start_idx = used_char[s[i]] + 1
            else:
                longest_substring_len = max(longest_substring_len, i - start_idx + 1)
            
            used_char[s[i]] = i
        return longest_substring_len
            
        