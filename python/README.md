# Data Structures and Algorithms

## Language: `Python`

### Folder and Challenge Setup

Each type of code challenge has slightly different instructions. Please refer to the notes and examples below for instructions for each DS&A assignment type.

### Data Structure: New Implementation

- Create a new folder under the `python` level, with the name of the data structure and complete your implementation there
  - i.e. `linked_list`
- Implementation (the data structure "class")
  - The implementation of the data structure should match package name
    - i.e. `linked_list/linked_list.py`
  - Follow Python [naming conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

    ```python
    class LinkedList:
      def __init__(self):
        # ... initialization code

      def method_name(self):
        # method body
    ```

- Tests
  - Within folder `tests` create a test file called `test_[data_structure].py`
    - i.e. `tests/test_linked_list.py`
    - Your tests will then need to require the data structure you're testing
      - i.e. `from linked_list.linked_list import LinkedList`

### Data Structure: Extending an implementation

- Work within the existing data structure implementation
- Create a new method within the class that solves the code challenge
  - Remember, you'll have access to `self` within your class methods
- Tests
  - You will have folder named `tests` and within it, a test file called `test_[data_structure].py`
    - i.e. `tests/test_linked_list.py`
    - Add to the tests written for this data structure to cover your new method(s)

### Code Challenge / Algorithm

Code challenges should be completed within a folder named `code_challenges` under the `python` level

- Daily Setup:
  - Create a new folder under the `python` level, with the name of the code challenge
    - Each code challenge assignment identifies the branch name to use, for example 'find-maximum-value'
    - For clarity, create your folder with the same name, ensuring that it's `snake_cased`
    - i.e. For a challenge named 'find_maximum_value', create the folder:`code_challenges/find_maximum_value`
  - Code Challenge Implementation
    - Each code challenge requires a function be written, for example "find maximum value"
    - Name the actual challenge file with the name of the challenge, in `snake_case`
      - i.e. `find_maximum_value.py`
    - Reminder: Your challenge file will then need to require the data structure you're using to implement
      - i.e. `from linked_list.linked_list import LinkedList`
    - Your challenge function name is up to you, but name something sensible that communicates the function's purpose. Obvious is better than clever
      - i.e. `find_maximum_value(linked_list)`
  - Tests
    - Ensure there is a `tests` folder at the root of project.
      - i.e. a sibling of this document.
    - within it, a test file called `test_[challenge].py`
      - i.e. `tests/find_maximum_value.py`
      - Your test file would require the challenge file found in the directory above, which has your exported function
        - i.e. `from code_challenges.find_maximum_value import find_maximum_value`

## Running Tests

If you setup your folders according to the above guidelines, running tests becomes a matter of deciding which tests you want to execute.  Jest does a good job at finding the test files that match what you specify in the test command

From the root of the `data-structures-and-algorithms/python` folder, execute the following commands:

- **Run every possible test** - `pytest`
- **Run filtered tests** - `pytest -k some_filter_text`
- **Run in watch mode** - `ptw` or `pytest-watch`

# Code Challenge 01
# Reverse an Array
The challenge that will be done today will have a whitebaord which will include a fucntion that takes in a lsit, prduce an output of the smae list but in reverse.

## Whiteboard Process
[White board challenge 1](img/white_board_01.png)

## Approach & Efficiency
We took the approach in way that was going to show a new array an place the values of the index's and insert the values in decneding order of the reverse of the list. Deciding on repalcing the index's to show the correct reverse order.

# Code Challenge 02
# Insert to Middle of an Array
This challenge was all about attempting to find a way that would allow for a number to be placed into thr middle of a list.

## Whiteboard Process
[White board challenge 2](img/white_board_02.png)

## Approach & Efficiency
With getting this code to work, Ian and I ended up making an for loop that would add the list of numbers into another one. With a sperate number that is inputted will then be placed into the muddle of the list. Ended up using the append method in order to add the second half of the list after the value is placed in the list. Once that shows it would then show the value in the middle of the list.

# Code Challenge 03
# Binary Search of Sorted Array
The chalnege that we are adressing in this code chalenge is finding a given value and using a binary search to find if the value is within the list. Afterwards returning the ouptu of what index the number is residing.

## Whiteboard Process
[White Board 03](img/white_board_03.png)

## Approach & Efficiency
During this code challenge, We wanted to iterate through the lsit to then allow us to find the value of the index for "value". When we did this we would make sure that the value was in the list and if it was not we would return -1. We tried to go through the median of the list and go from there in terms of cycling throuhg the values until the index matched the corresponding value that was inputted.

# Singly Linked List
This code challenge was all about making sure to test out linked lists to ensure that they would be able to be tested to pu values into a liked list as well ass return boolean values. 

## Challenge
The challenge required that there be a way to test out the linked lists in a way that could allow for testing implementation. Using the methods include, to_string, and insert. These all residing in a class then to be called to test things within the testing evironment.

## Approach & Efficiency
In this approahc I was able to partner with other classmates to figure out that we would need to iterarte through the list to find whether the values in the linked list were ther or not. USually what I start with is writing out the tests in order to see if the values will show up or not. 

## API
I ended up getting help with wirting code from my peers like Brandon, Alex, and Eddie. There was alos websites I sued to figure out how to utilize and understand the topics.

1. [linked list inserting](https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/)
2. [All about linked lists](https://www.geeksforgeeks.org/data-structures/linked-list/)

# Code Challenge 08
# Zip

# Code Challenge 10

# Stacks and Queues
In this hcalenge we would utilize stack and queue methodology to simulate using peek, pop, etc. This challenge demonstrates a clear understanding of what queues and stacks can do using python.

## Challenge
In the challenge we were given a lsit of questions to answer for this and made tests that would allow us to meet those requirements. In the challenge we fulfill the 14 quetions that were given: 

1. Can successfully push onto a stack
2. Can successfully push multiple values onto a stack
3. Can successfully pop off the stack
4. Can successfully empty a stack after multiple pops
5. Can successfully peek the next item on the stack
6. Can successfully instantiate an empty stack
7. Calling pop or peek on empty stack raises exception
8. Can successfully enqueue into a queue
9. Can successfully enqueue multiple values into a queue
10. Can successfully dequeue out of a queue the expected value
11. Can successfully peek into a queue, seeing the expected value
12. Can successfully empty a queue after multiple dequeues
13. Can successfully instantiate an empty queue
14. Calling dequeue or peek on empty queue raises exception

## Approach & Efficiency
The approach that I took was making sure there was an estalbished Node that would allow for other class methods to use. When attempting to show that when passing through multiple values there was a use of logic that made sense. I ended up making sure that the logic was clear an concise.

## API
I ended up working with Eddie, Brandon, Clarissa, Alex and David.

# Code Challenge 11

# Stacks and Queues (Psuedo)
In this chalenge We had to use a class instance of Psuedo and make methods that would allow a queue like system to dequeue and enqueue values without making it a cause for using the same stack/queue and making a new one.

## Challenge 
In this challenge we needed to make a class called PsuedoQueue and make methods that would dequeue and enqueue values from a queue. In this I was able to make sure that things were fleshed out by making while loops for the enqueue and dequeue method. This would remove values from a queue as well as add them to a completely new queue.

## Approach & Efficiency
The way I saw this was making a double negative in the logic by having the enqueue method utilize the boolean is_empty method and it would allow for adding values to a new queue to indicate a new queue and pushing the value to the top of the queue. The dequeue method uses the same while loop logic and instead of pushing the value it returns the stack_out method to pop a value out of a queue.

# API
In thisw code challenge I did work with Alex, Michael, Eddie and Brandon. The sites I utilized was geek for geeks.

# Code Challenge 13

# White Board:
[Code Challenge 13, WB](img/code_challenge_13.png)

# Stack Queue Bracket
<!-- Short summary or background information -->
Problem Domain: Write a function called validate brackets that will take in a string and return a boolean based on if all the brackets within are balanced

## Challenge
<!-- Description of the challenge -->
Create a method that will do the above
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Big O
Space: O(n)
Time: O(n)

## API
<!-- Description of each method publicly available to your Stack and Queue-->

validateBrackets

will take in a string and see if the brackets match each other. Then return a boolean of true if they do and false if they don't.

Credit:
Brandon, Eddie, Alex.
