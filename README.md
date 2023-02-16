# decisions.py
`decisions.py` is a Python module that allows you to define a set of rules to apply to an object and execute the appropriate action based on the first matching rule. It's useful when you need to make a decision based on a complex set of conditions. 

---

## Usage
To use `decisions.py`, create a new instance of `DecisionTree` by passing an object of the type that you want to evaluate as its argument:
```python
tree = DecisionTree("test")  # in this case we're evaluating a string
```

### Adding rules
Once you have a `decisions.py` instance, you can add rules to it. A rule consists of a condition and an action. The condition is a `function` that takes the object to be evaluated as its argument and returns `True` if the rule should be applied, and the action is a function that specifies what should be done if the rule is applied.

To add a rule to the `DecisionTree`, call the `case_condition()` method with the condition and the action as arguments. Here's an example:
```python
tree.case_condition(lambda s: s == "test", lambda s: print("test"))
```
In this example, we're adding a rule that says "if the string is 'test', then print 'test'".

### Adding default rule
If none of the rules match, you can specify a default action to be executed by calling the `default_case()` method:
```python
tree.default_case(lambda s: print("default"))
```
In this example, we're specifying that if none of the other rules match, the action should be to print "default".

### Applying the rules
Once you've added all the rules, you can apply them to the object by calling the `decide()` method:
```python
tree.decide()
```
This will evaluate the object and execute the first matching rule.

---

## Example
Here's an example of using `decisions.py` to evaluate a person dictionary:
```python
# Create a new DecisionTree with a person dictionary
person = {"name": "Alice", "age": 30}
tree = DecisionTree(person)

# Add a rule
tree.case_condition(lambda p: p["age"] > 18, lambda p: print(p["name"], "is an adult"))

# Add a default rule
tree.default_case(lambda p: print(p["name"], "is a minor"))

# Apply the rules
tree.decide()
```
In this example, we're creating a new `DecisionTree` instance with a person dictionary. We're adding a rule that says "if the person's age is greater than 18, then print 'Alice is an adult'" (where "Alice" is the person's name). We're also adding a default rule that says "print 'Alice is a minor' if none of the other rules match". Finally, we're applying the rules to the person dictionary by calling `decide()`.

You may also use this syntax:
```python
# Create a person dictionary
person = {"name": "Alice", "age": 30}

# Create a DecisionTree object and apply rules
tree = DecisionTree(person)\
        .case_condition(lambda p: p["age"] > 18, lambda p: print(p["name"], "is an adult"))\
        .default_case(lambda p: print(p["name"], "is a minor"))\
        .decide()
```

---

## Error handling & known issues
`decisions.py` provides some basic error handling. If you don't add any rules to the `DecisionTree`, calling `decide()` will result in an `Error`. 

Known issues:
  - If you don't add any rules to the `DecisionTree`, calling `decide()` will NOT result in an error. Similarly, if you don't call `decide()` after adding rules, you won't get an error as well. I might try to fix this issue as soon as possible.

---

###### check out the java version [here](https://github.com/Adversing/Decisions4J/) and the javascript version [here](https://github.com/Adversing/decisions.js/) :)   
