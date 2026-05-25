import random

class Rule:
    def __init__(self, subject, predicate, obj, confidence=1.0, source="initial"):
        self.subject = subject
        self.predicate = predicate
        self.obj = obj
        self.confidence = confidence
        self.source = source
        self.usage_count = 0
    
    def __str__(self):
        return f"({self.subject}, {self.predicate}, {self.obj})"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        if not isinstance(other, Rule):
            return False
        return (self.subject == other.subject and 
                self.predicate == other.predicate and 
                self.obj == other.obj)
    
    def __hash__(self):
        return hash((self.subject, self.predicate, self.obj))
    
    def conflicts_with(self, other):
        if self.subject != other.subject:
            return False
        if self.predicate != other.predicate:
            return False
        if self.obj == other.obj:
            return False
        return True

class RuleBase:
    def __init__(self):
        self.rules = []
        self.generation = 0
    
    def add_rule(self, rule):
        if rule not in self.rules:
            for existing in self.rules:
                if rule.conflicts_with(existing):
                    return False
            self.rules.append(rule)
            return True
        return False
    
    def get_rules_by_subject(self, subject):
        return [r for r in self.rules if r.subject == subject]
    
    def get_rules_by_predicate(self, predicate):
        return [r for r in self.rules if r.predicate == predicate]
    
    def get_rules_by_object(self, obj):
        return [r for r in self.rules if r.obj == obj]
    
    def random_rule(self):
        if not self.rules:
            return None
        return random.choice(self.rules)
    
    def size(self):
        return len(self.rules)
    
    def print_rules(self):
        print(f"当前规则库（共 {self.size()} 条）：")
        print("-" * 40)
        for i, rule in enumerate(self.rules, 1):
            print(f"{i}. {rule} [置信度: {rule.confidence:.2f}, 来源: {rule.source}]")
        print()
