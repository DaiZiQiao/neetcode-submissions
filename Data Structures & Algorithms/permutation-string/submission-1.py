class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        hashmap_s1 = {}
        hashmap_s2 = {}
        if n1 > n2:
            return False
        
        for i in range(n1):
            hashmap_s1[s1[i]] = hashmap_s1.get(s1[i], 0) + 1


        for i in range(n1):
            hashmap_s2[s2[i]] = hashmap_s2.get(s2[i], 0) + 1

        if hashmap_s1 == hashmap_s2:
            return True

        for i in range(n1, n2):
            new_char = s2[i]
            old_char = s2[i - n1]

            hashmap_s2[new_char] = hashmap_s2.get(new_char, 0) + 1

            hashmap_s2[old_char] -= 1
            if hashmap_s2[old_char] == 0:
                del hashmap_s2[old_char]
            
            if hashmap_s1 == hashmap_s2:
                return True
        return False

    
