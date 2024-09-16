class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)

        if index == -1:
            return word

        left = 0
        right = index
        wrist = list(word)

        while left < right:
            wrist[left], wrist[right] = wrist[right], wrist[left]
            left += 1
            right -= 1
        
        return ''.join(wrist)
