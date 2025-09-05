import pytest
from core.leets.valid_parenthesis import valid_parenthesis



@pytest.mark.parametrize("a, expected", [
  ("[{}]", True),
  ("[{]", False),
  ("()[]{}", True),
  ("(]", False),
])
def test_valid_parenthesis(a, expected):
  assert valid_parenthesis(a) == expected