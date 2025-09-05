


def valid_parenthesis(val: str) -> bool:

  pairs = {
    "{": "}",
    "[": "]",
    "(": ")"
  }

  stack = []

  for ch in val:
    print(f"Checking char {ch}")

    if ch == "}" or ch == "]" or ch == ")":
      print("closer")
      prev = stack.pop()

      if pairs[prev] != ch:
        print(f"Wrong closing char {ch} for previous opener {prev}")
        return False
    else:
      print("opener")
      stack.append(ch)

  if len(stack) == 0:
    return True
  else:
    return False