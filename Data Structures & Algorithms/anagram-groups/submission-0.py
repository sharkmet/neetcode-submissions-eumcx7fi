class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            count = [0] *26
            for l in s:
                count[ord(l)-ord('a')] +=1

            key = tuple(count)

            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        
        return list(groups.values())