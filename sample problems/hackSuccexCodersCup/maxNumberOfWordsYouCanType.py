class Solution:
    def maxNumberOfWordsYouCanType(self, text, brokenLetters):
        words_left = set(text.split())
        words = list(words_left)
        for char in brokenLetters:
            for word in words:
                if char in word:
                    words_left.remove(word)
            words = list(words_left)
        return len(words)


if __name__ == "__main__":
    sol = Solution()
    text = "hello world"
    brokenLetters = "ad"
    print(sol.maxNumberOfWordsYouCanType(text, brokenLetters))