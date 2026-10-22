class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n=len(s)
        m=len(p)

        #edge cases
        if not s or not p or len(p)>len(s):
            return []
        
        output = []

        memory = {} #char:freq
        for i in p:
            memory[i]=1+memory.get(i,0)

        for i in range(n-m+1): #all valid windows
            j=0
            window = {}

            while j<m:
                char=s[i+j]
                window[char]=1+window.get(char,0)
                j+=1
            
            if window == memory:
                output.append(i)
        return output 

                

        
        #s = "cbaebabacd"
        #p = "abc"
        #Output: [0, 6]
