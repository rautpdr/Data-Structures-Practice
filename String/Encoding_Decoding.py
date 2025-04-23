from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            word_len = int(s[i:j])
            i = j + 1
            j = i + word_len
            word = s[i:j]
            result.append(word)
            i = j
        return result

# Main function
def main():
    strings = ["I", "am", "Bat", "Man"]
    sol = Solution()

    encoded = sol.encode(strings)
    print("Encoded:", encoded)

    decoded = sol.decode(encoded)
    print("Decoded:", decoded)

# Run main
if __name__ == "__main__":
    main()
