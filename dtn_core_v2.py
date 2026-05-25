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
        self.similarity_map = {}
    
    def add_rule(self, rule):
        if rule not in self.rules:
            for existing in self.rules:
                if rule.conflicts_with(existing):
                    return False
            self.rules.append(rule)
            
            if rule.predicate == "是":
                self._update_similarity_from_is(rule)
            
            return True
        return False
    
    def _update_similarity_from_is(self, rule):
        subject = rule.subject
        obj = rule.obj
        
        if subject not in self.similarity_map:
            self.similarity_map[subject] = []
        
        for existing_subject in self.similarity_map[subject]:
            if existing_subject != subject:
                self.similarity_map[existing_subject].append(subject)
                self.similarity_map.setdefault(existing_subject, [])
        
        for other_rule in self.rules:
            if other_rule.predicate == "是" and other_rule.obj == obj and other_rule.subject != subject:
                self.similarity_map.setdefault(subject, [])
                if other_rule.subject not in self.similarity_map[subject]:
                    self.similarity_map[subject].append(other_rule.subject)
                self.similarity_map.setdefault(other_rule.subject, [])
                if subject not in self.similarity_map[other_rule.subject]:
                    self.similarity_map[other_rule.subject].append(subject)
    
    def get_rules_by_subject(self, subject):
        return [r for r in self.rules if r.subject == subject]
    
    def get_rules_by_predicate(self, predicate):
        return [r for r in self.rules if r.predicate == predicate]
    
    def get_rules_by_object(self, obj):
        return [r for r in self.rules if r.obj == obj]
    
    def get_category(self, subject):
        category_rules = [r for r in self.rules if r.predicate == "是" and r.subject == subject]
        if category_rules:
            return category_rules[0].obj
        return None
    
    def get_similar_subjects(self, subject):
        return self.similarity_map.get(subject, [])
    
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
