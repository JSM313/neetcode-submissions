class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bucket = {}
        anagram_list = []
        for word in strs:
            label = ''.join(sorted(word))
            if label in bucket:
                bucket[label].append(word)
            else:
                bucket[label] = [word]
        
        for word in bucket.values():
            anagram_list.append(word)
        return anagram_list
            
        