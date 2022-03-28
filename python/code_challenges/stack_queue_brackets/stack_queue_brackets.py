from code_challenges.stack_and_queue.stack_and_queue import Stack

def validate_brackets(string):
  stack_stuff = Stack()
  dict_brackets = {'{' :'}', '(' : ')', '[': ']'}

# i is the character of the brackets that would need
  for i in string:
    if i in '[{(':
      stack_stuff.push(i)
    elif i in ')}]':
      if dict_brackets[stack_stuff.pop()] != i:
        return False
  if stack_stuff.is_empty():
    return True
  else:
    return False

# Worked with Alex, Eddie and Brandon for this solution. 
