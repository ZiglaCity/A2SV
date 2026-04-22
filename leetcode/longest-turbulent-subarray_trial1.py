from typing import List

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        
        l, mx = 0, 1
        status = None
        
        for r in range(1, len(arr)):
            if arr[r] == arr[r - 1]:
                l = r
                status = None
            elif status is None or (status == "greater" and arr[r - 1] > arr[r]) or (status == "lesser" and arr[r - 1] < arr[r]):
                mx = max(mx, r - l + 1)
                status = "greater" if arr[r - 1] < arr[r] else "lesser"
            else:
                l = r - 1
                mx = max(mx, r - l + 1)
                status = "greater" if arr[r - 1] < arr[r] else "lesser"

        return mx
