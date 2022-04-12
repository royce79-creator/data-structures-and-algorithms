from msilib.schema import Class
from typing_extensions import Self
from code_challenges.stack_and_queue.stack_and_queue import Stack

class depth_first(self, next):
  list = []
  visited = set()
  stack = Stack()
  while stack:
    head = stack.pop()
    if stack in visited:
      continue
    visited.add(head)
    for child in 
