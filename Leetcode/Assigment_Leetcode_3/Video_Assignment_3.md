## Question 1
**Explain what a Stack is, covering its basic functionalities such as push, pop, and read/peek. Discuss the time complexities associated with implementing a stack using a list versus a linked list. Explain the reasons behind the differences in time complexities.**<br>

**Stack**:<br>
Stacks are not a new  data structure. Rather, they are simply arrays with restrictions. A stack stores data in the same way arrays do, except that they have three below restrictions.<br>
1.Data can be inserted only at the end of a stack<br>
2.Data can be deleted only from the end of a stack<br>
3.Only the last element of a stack can be read<br>
The beginning of the stack is its bottom and the end of the stack is its top. A stack  follows the Last In, First Out (LIFO) principle. This means the last item you add is the first one you remove.<br>

**Basic Operations of a stack**:<br>

1.**Push**:<br>
Push adds an item to the top of the stack.<br>
Example: If the stack is [1, 2, 3] and if we push 4, the stack becomes [1, 2, 3, 4].<br>

2.**Pop**:<br>
Pop removes and returns the top item from the stack.<br>
Example: If the stack is [1, 2, 3, 4] and if we perform pop, the stack becomes [1, 2, 3], and we get 4.<br>

3.**Peek/Read**:<br>
Peek/Read shows the top element of the stack without removing it.<br>
Example: If the stack is [1, 2, 3, 4] and if we perform peek, we see 4, and the stack remains [1, 2, 3, 4].<br>

**Time complexities associated with implementing a stack using a List**:<br>

**Push**:<br>
Average time complexity of pushing an element to a stack which is implemeneted using a list is O(1). adding an element at the end of a list is called appending and this takes O(1) as it is not required to check/move any of the other elements present in the list to do this. But it has a time complexity of o(1)* when it hits the amortized worst case.<br>

~~~python
def push(self, v):
        self.stack.append(v)
~~~

**Pop**:<br>
Time complexity of popping an element from a stack which is implemeneted using a list is O(1). Removing an element from the end of the stack is called popping and this takes O(1) as it is not required to check/move any of the other elements present in the list to do this.<br>

~~~python
def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty.')
        return self.stack.pop()
~~~

**Peek/Read**:<br>
Time complexity of peeking/Reading an element of a stack which is implemeneted using a list is O(1). Peeking is nothing but accesing last element of the list and this takes o(1) as it is not required to check/move any of the other elements present in the list to do this. when we try to access through index, it just directly access the element in that index without checking other elements.<br>

~~~python
def read(self): #peak
        if self.is_empty():
            return None
        return self.stack[-1]
~~~

**Time complexities associated with implementing a stack using a Linked List**:<br>

**Push**:<br>
Time complexity of pushing an element to a stack which is implemeneted using a Linked list is O(1). Pushing an element to a Linked list is nothing but adding a new node to the start or end of the linked list. And while implementing stack using linked list generally we add the new node to the start and make the new node as head(start) for every push, this is beacuse adding at the start for a linked list is O(1) as we always have access to the start(head).<br>

**Pop**:<br>
Time complexity of popping an element from a stack which is implemeneted using a Linked list is O(1). popping an element from a Linked list is nothing but removing a node from the start or end of the linked list. And while implementing stack using linked list generally we add the new node to the start and make the new node as head for every push.Therefore a last element added to the stack is at the start and we always have access to the start of the linked list. For this reason it takes constant time.<br>

**Peek/Read**:<br>
Time complexity of peeking/Reading an element of a stack which is implemeneted using a linked list is O(1). Peeking is nothing but accesing last element of the linked list.And while implementing stack using linked list generally we add the new node to the start and make the new node as head for every push.Therefore a last element added to the stack is at the start and we always have access to the start of the linked list. For this reason it takes constant time.<br>

**Note**:<br>
If a stack is implemented using a linked list and we add new nodes to the start while the start remains unchanged, all stack operations will have a time complexity of O(n). This is because we need to traverse to the end of the linked list to perform operations.<br>

**differences in time complexities**:<br>
Push, Pop, Peek/Read operations are O(1) for both lists and linked lists. Main difference is that worst case time complexity for push operation of stack using list is o(1)* but o(1) for linked list. <br>

## Question 2:
**explain the code that achieves the linting functionality. Present three scenarios:**<br>
   **a. No mismatch**<br>
   **b. Missing closing brace, which could be any of the following: '([{'**<br>
   **c. Missing opening brace, which could be any of the following: ']})' **<br>

**Solution code**:<br>
~~~python
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, v):
        self.stack.append(v)

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty.')
        return self.stack.pop()
    def read(self): #peak
        if self.is_empty():
            return None
        return self.stack[-1]

    def __repr__(self):
        return "stack:" + str(self.stack)

class Linter:
    def __init__(self):
        self.stack = Stack()

    def is_opening_brace(self, char):
        return char in '([{'

    def is_closing_brace(self, char):
        return char in ')]}'

    def is_not_a_match(self, opening_brace, closing_brace):
        braces = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        return closing_brace != braces[opening_brace]

    def lint(self, text):
        for char in text:
            if self.is_opening_brace(char):
                self.stack.push(char)
            elif self.is_closing_brace(char):
                if self.stack.is_empty():
                    return f'{char} does not have opening brace'
                popped_opening_brace = self.stack.pop()
                if self.is_not_a_match(popped_opening_brace, char):
                    return f'{char} has mismatched opeing brace'
        if self.stack.read():
            return f'{self.stack.read()} does not have closing brace'

        return True
~~~

This code implements a basic linter that checks for mismatched braces in a string. It uses a stack to track opening braces and ensures that every closing brace matches the last opened brace. <br>

**Explanation**:<br>
**Linter Class**:<br>
__init__: Initializes an empty stack.<br>
**is_opening_brace**: Checks if a character is an opening brace ((, [, {).<br>
**is_closing_brace**: Checks if a character is a closing brace (), ], }).<br>
**is_not_a_match**: Checks if an opening brace does not match the corresponding closing brace.<br>
**lint**: The main method that checks for brace mismatches. If the character is an opening brace, it is pushed to the stack and if it is a closing brace, stack is popped and the popped brace is compared with the closing brace. If it doesn't match, we return that charcter has mismatched opeing brace and if it matches, we just continue with the next iteration.

**Explanation of code using below 3 scenarios**:<br>
**a. No Mismatch**:<br>
**Example: '([])'**<br>
Firstly,The stack starts empty.<br>
'(' is checked and as it is opening brace we push the '(' to the stack.<br>
'[' is checked and as it is opening brace we push the ']' to the stack.<br>
] is encountered and as it is closing brace, The last element of the stack is popped and checked if it matches the closing brace of the popped brace. In this case, it matches.<br>
 ) is encountered and as it is closing brace, The last element of the stack is popped and checked if it matches the closing brace of the popped brace. In this case, it matches.<br>
Stack is empty now, indicating all braces are properly matched.<br>

**b. Missing Closing Brace**:<br>
**Example: '([{'**

Firstly,The stack starts empty.<br>
'(' is checked and as it is opening brace we push the '(' to the stack.<br>
'[' is checked and as it is opening brace we push the ']' to the stack.<br>
'{' is checked and as it is opening brace we push the '{' to the stack.<br>
End of input reached, but stack is not empty ([{ remains. This means we do not have any other characters to check if the opening braces are matching with closing.
The linter returns: { does not have a closing brace.

**c. Missing Opening Brace**:<br>
**Example : ']})'**<br>

Firstly,The stack starts empty.<br>
 is encountered and as it is closing brace, The last element of the stack is popped and checked if it matches the closing brace of the popped brace. But the stack is empty to pop anything, this means the given input doesn't have matching opening brace and our code returns '] does not have opening brace'

 
 

