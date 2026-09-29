class Solution(object):
    def longestCommonPrefix(self, strs):
        # Start with the first string as the candidate prefix
        prefix = strs[0]

        for s in strs[1:]:
            # Shrink the prefix until the current string starts with it
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        return prefix