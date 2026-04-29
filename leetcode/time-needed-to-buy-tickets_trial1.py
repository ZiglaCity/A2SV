class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        return sum(min(tickets[i], tickets[k] - (i > k)) for i in range(len(tickets)))