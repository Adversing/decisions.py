from typing import TypeVar, Callable

T = TypeVar('T')

class DecisionTree:
    def __init__(self, obj: T):
        self.obj = obj
        self.rules = []
        self.default_action = None

    def case_condition(self, condition: Callable[[T], bool], action: Callable[[T], None]) -> 'DecisionTree':
        self.rules.append((condition, action))
        return self

    def default_case(self, action: Callable[[T], None]) -> 'DecisionTree':
        self.default_action = action
        return self

    def decide(self) -> None:
        if not self.rules:
            raise Exception("No rules defined for DecisionTree")
        if self.default_action is None:
            raise Exception("No default action defined for DecisionTree")
        for condition, action in self.rules:
            if condition(self.obj):
                action(self.obj)
                return
        self.default_action(self.obj)
