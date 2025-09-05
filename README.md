pyalgolab
=========

Terse algorithms lab in Python. Classic problems, variants, and test-driven reps. Focus: clues → patterns → trade-offs.

## Requirements

- Python ≥ 3.13
- uv (recommended) or pip
- pytest (already declared)

## Install

Using uv:

```
uv venv
uv sync
```

Using pip:

```
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Run tests

```
uv run pytest -q
# or focused:
uv run pytest tests/core/search/test_search_range.py::test_basic
uv run pytest -k "binary and not range" -vv
```

## Layout

```
.
├── main.py                 # scratch/runner
├── pyproject.toml          # project + pytest config
├── src/
│   ├── core/
│   │   ├── leets/
│   │   │   ├── merge_two_sorted_lists.py
│   │   │   ├── two_sum.py
│   │   │   └── valid_parenthesis.py
│   │   └── search/
│   │       ├── binary_search.py
│   │       ├── search_insert.py
│   │       └── search_range.py
│   └── helpers/
│       ├── __init__.py
│       └── list_node.py
└── tests/
    └── core/
        ├── leets/
        │   ├── test_merge_two_sorted_lists.py
        │   ├── test_two_sum.py
        │   └── test_valid_parenthesis.py
        └── search/
            ├── test_binray_search.py     # TODO: rename -> test_binary_search.py
            ├── test_search_insert.py
            └── test_search_range.py
```

## Quick usage

```python
# main.py
from core.search.binary_search import binary_search
from core.leets.two_sum import two_sum

print(binary_search([1,3,5,7,9], 7))   # -> 3
print(two_sum([2,7,11,15], 9))         # -> (0, 1) or [0, 1]
```

## Conventions

- Typing: PEP 585/604 (list[int], dict[str, int], int | None).
- Tests: pytest paramization; explicit edge cases.
- Helpers: helpers.list_node.ListNode for linked-list tasks (repr/eq-friendly).
- Style: early returns, no cleverness, small functions.

## Patterns (clues → families)

- sorted array ⇒ BS family (binary_search, search_insert, search_range)
- monotone predicate ⇒ BS on answer
- prefix/suffix ⇒ scans + prefix sums (TBD)
- intervals ⇒ sort + sweep/merge (TBD)
- overlap subproblems ⇒ DP (TBD)
- kth/top-k ⇒ heap/quickselect (TBD)

## Roadmap

- Add rotated-array BS variants.
- Add two-pointers (3-sum, container, remove-dups).
- Add heap set (k-largest, merge k lists).
- Add DP basics (stairs, coin change).
- Optional: ruff/black/isort pre-commit; CI with coverage.

## License

MIT