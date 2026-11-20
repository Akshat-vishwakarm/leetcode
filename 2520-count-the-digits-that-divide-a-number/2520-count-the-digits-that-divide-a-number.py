class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        n = num

        while n > 0:
            r = n % 10

            if num % r == 0:
                count += 1

            n = n // 10

        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna