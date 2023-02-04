# Thanks for your interest in working with us at Emeritus!

We view data engineering as primarily a software engineering role, applied to problems around making use of data. Good infrastructure and tooling is paramount to making use of real world data.

In that vein, please help us to understand how you think about writing software by writing code to solve the following problem.

If time drags on, please feel free to simplify your approach and note how it could be improved. We care that you can write quality code, but we care far more about how you approach software problems than that your answer has the best possible runtime complexity.

#### You are given a collection of N *streams* (not arrays) of integers, all monotonically increasing. Build an iterator that yields the values from across all of the streams in ascending order.

example with assumed generated values and appropriate output order:

```
# ... implies potentially arbitrarily (maybe infinitely?) many more values.
inputs = [
    RandomIncreasingIterator(10000), # -> [1, 7, 7, 12, ...]
    RandomIncreasingIterator(10000), # -> [2, 3, 8, ...],
    RandomIncreasingIterator(10000)  # -> [3, 9, 25, ...],
    ...
]

answers = AnswerGenerator(inputs)

[print(a) for a in answers] # 1, 2, 3, 3, 7, 7, 8, 9, 12, 25, ...
```

Feel free to use builtin (or similarly standard) utility libraries, like `sorted(vals)`, etc. *You can do better than `sorted([i for j in inputs for i in j])` anyway.*

Describe your approach, its limitations, and how it scales, as well as providing the code.

An example iterator is provided to test against for convenience and reference, written in Python, but feel free to work in whatever language you feel most comfortable in. Coding ability is incomparably more important than expertise in any particular language.
