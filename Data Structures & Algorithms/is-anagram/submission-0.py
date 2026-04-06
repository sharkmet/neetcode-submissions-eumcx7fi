class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict()
        t_dict = dict()

        for l in s:
            if l not in s_dict:
                s_dict[l] = 1
            else:
                s_dict[l] += 1

        for l in t:
            if l not in t_dict:
                t_dict[l] = 1
            else:
                t_dict[l] += 1

        for key in s_dict:
            if s_dict[key] != t_dict.get(key,0):
                return False
        return len(s_dict) == len(t_dict)
