#Reverse a sentence using stack
# s = "Hey, how are you doing ?"
# stack = []
# word = ""
# for i in range(len(s)):
#     if s[i] == " " or i == len(s)-1:
#         if i == len(s) - 1:
#             word += s[i]
#         stack.append(word)
#         word = ""
#     word += s[i]

# while(stack):
#     print(stack.pop(), end=" ")

#Reverse a stack
# def insertatbottom(st, ele):
#     if not st:
#         st.append(ele)
#         return
#     topele = st[-1]
#     st.pop()
#     insertatbottom(st, ele)
#     st.append(topele)
# def reverses(st):
#     if not st:
#         return
#     ele = st[-1]
#     st.pop()
#     reverses(st)
#     insertatbottom(st, ele)
# st = [1,2,3,4,5]
# reverses(st)
# print(st)

#Prefix evalution - backwards
# def evaluate_prefix(expression):
#     stack = []
#     for i in range(len(expression) - 1, -1, -1):
#         if expression[i].isdigit():
#             stack.append(int(expression[i]))
#         else:
#             op1 = stack.pop()
#             op2 = stack.pop()
#             if expression[i] == '+':
#                 stack.append(op1 + op2)
#             elif expression[i] == '-':
#                 stack.append(op1 - op2)
#             elif expression[i] == '*':
#                 stack.append(op1 * op2)
#             elif expression[i] == '/':
#                 stack.append(op1 / op2)
#     return stack[0]
# expression = "*+23+34"
# print(evaluate_prefix(expression))  

#Postfix evaluation - forward
# def evaluate_postfix(expression):
#     stack = []
#     for char in expression:
#         if char.isdigit():
#             stack.append(int(char))
#         else:
#             op2 = stack.pop()
#             op1 = stack.pop()
#             if char == '+':
#                 stack.append(op1 + op2)
#             elif char == '-':
#                 stack.append(op1 - op2)
#             elif char == '*':
#                 stack.append(op1 * op2)
#             elif char == '/':
#                 stack.append(op1 / op2)
#     return stack[0]
# expression = "23+34+*"
# print(evaluate_postfix(expression))

#Infix to postfix
# def infix_to_postfix(expression):
#     precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
#     stack = []
#     output = []
#     for char in expression:
#         if char.isalnum():  # Operand
#             output.append(char)
#         elif char == '(':  # Left Parenthesis
#             stack.append(char)
#         elif char == ')':  # Right Parenthesis
#             while stack and stack[-1] != '(':
#                 output.append(stack.pop())
#             stack.pop()  # Pop the left parenthesis
#         else:  # Operator
#             while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]:
#                 output.append(stack.pop())
#             stack.append(char)
#     while stack:
#         output.append(stack.pop())
#     return ''.join(output)
# expression = "a+b*(c^d-e)^(f+g*h)-i"
# print(infix_to_postfix(expression))  # Output: abcd^e-fgh*+^*+i-

#Infix to Prefix
# def infix_to_prefix(expression):
#     # Reverse the infix expression
#     expression = expression[::-1]

#     # Swap parentheses
#     expression = list(expression)
#     for i in range(len(expression)):
#         if expression[i] == '(':
#             expression[i] = ')'
#         elif expression[i] == ')':
#             expression[i] = '('

#     expression = ''.join(expression)

#     # Precedence dictionary
#     precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

#     stack = []
#     output = []

#     for char in expression:
#         if char.isalnum():  
#             output.append(char)
#         elif char == '(':  
#             stack.append(char)
#         elif char == ')':  
#             while stack and stack[-1] != '(':
#                 output.append(stack.pop())
#             stack.pop()  
#         else:  
#             # Operator
#             while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]:
#                 output.append(stack.pop())
#             stack.append(char)

#     while stack:
#         output.append(stack.pop())
#     return ''.join(output[::-1])
# expression = "(a-b/c)*(a/k-l)"
# print(infix_to_prefix(expression))  

#Balenced paranthesis
# s = "[{()}]"
# def isValid(s):
#     stack = []
#     for i in range(len(s)):
#         if s[i] in '([{':
#             stack.append(s[i])
#         elif s[i] in ')]}':
#             if not stack:
#                 return False
#             if (s[i] == ')' and stack[-1] != '(') or \
#                (s[i] == ']' and stack[-1] != '[') or \
#                (s[i] == '}' and stack[-1] != '{'):
#                 return False
#             stack.pop()
#     return len(stack) == 0
# if (isValid(s)):
#     print("balanced")
# else:
#     print("not balanced")

