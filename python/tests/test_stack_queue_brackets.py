from code_challenges.stack_queue_brackets.stack_queue_brackets import validate_brackets

def test_bracket_one():
  string = '()'
  actual = validate_brackets(string)
  expected = True
  assert actual == expected
