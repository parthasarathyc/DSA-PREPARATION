'''LeetCode 772. Basic Calculator III (Python)
Approach: Stack + Recursion

Idea:

Use recursion to evaluate expressions inside parentheses.
Maintain a stack to handle +, -, *, and /.
When encountering '(', recursively evaluate the subexpression.
When encountering ')', return the computed value.

Time Complexity: O(n)
Space Complexity: O(n)

Python Solution'''
class Solution:
    def calculate(self, s: str) -> int:
        def helper():
            stack = []
            num = 0
            sign = '+'

            while self.i < len(s):
                ch = s[self.i]

                if ch.isdigit():
                    num = num * 10 + int(ch)

                elif ch == '(':
                    self.i += 1
                    num = helper()

                if (not ch.isdigit() and ch != ' ') or self.i == len(s) - 1:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack.append(stack.pop() * num)
                    elif sign == '/':
                        stack.append(int(stack.pop() / num))

                    sign = ch
                    num = 0

                if ch == ')':
                    break

                self.i += 1

            return sum(stack)

        self.i = 0
        return helper()
'''Example

Input

s = "(2+6*3+5-(3*14/7+2)*5)+3"

Output

-12
Another Example

Input

s = "2*(5+5*2)/3+(6/2+8)"

Output

21
Interview Explanation
Traverse the expression character by character.
Build numbers from consecutive digits.
When '(' is encountered, recursively evaluate the expression inside it.
Use a stack to process operators:
+ → push number
- → push negative number
* → multiply with the top of the stack
/ → divide the top of the stack (truncate toward zero)
When ')' is reached, return the sum of the stack for that subexpression.
The final answer is the sum of the stack for the entire expression.
Driver Code
s = input()

sol = Solution()
print(sol.calculate(s))
Sample Input
2*(5+5*2)/3+(6/2+8)
Sample Output
21

This is the optimal O(n) solution using Stack + Recursion, which is the standard interview approach for Basic Calculator III.'''