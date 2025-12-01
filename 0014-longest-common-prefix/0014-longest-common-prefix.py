class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Handle the edge case of an empty list
        if not strs:
            return ""

        # Initialize the prefix with the first string in the list
        prefix = strs[0]

        # Iterate through the rest of the strings starting from the second one (index 1)
        for i in range(1, len(strs)):
            current_string = strs[i]
            
            # While the current string doesn't start with the current prefix
            # shorten the prefix by one character from the end
            while current_string.find(prefix) != 0:
                # Shorten the prefix by removing the last character
                prefix = prefix[:-1]
                
                # If the prefix becomes empty, there's no common prefix at all
                if not prefix:
                    return ""
        
        # After checking all strings, the remaining prefix is the LCP
        return prefix