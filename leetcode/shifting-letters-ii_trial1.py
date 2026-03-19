class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0] * (len(s) + 1)
        for start, end, value in shifts:
            arr[start] += 1 if value == 1 else -1
            arr[end + 1] -= 1 if value == 1 else -1
        
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]
        
        print(arr)
        res = ""
        for i in range(len(s)):
            res += chr(ord('a') + ((ord(s[i]) - ord('a') + arr[i] ) % 26 ) )
        return res