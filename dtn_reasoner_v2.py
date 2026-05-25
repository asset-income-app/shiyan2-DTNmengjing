import random
from dtn_core_v2 import Rule, RuleBase

class DTNReasoner:
    def __init__(self, rule_base):
        self.rule_base = rule_base
        self.new_rules_generated = []
    
    def transitivity_inference(self):
        rules = self.rule_base.rules
        new_rules = []
        
        for rule1 in rules:
            if rule1.predicate != "是":
                continue
            
            subject_rules = self.rule_base.get_rules_by_subject(rule1.obj)
            for rule2 in subject_rules:
                if rule2.predicate == "有":
                    new_rule = Rule(
                        subject=rule1.subject,
                        predicate="有",
                        obj=rule2.obj,
                        confidence=min(rule1.confidence, rule2.confidence) * 0.9,
                        source="传递性推理"
                    )
                    new_rules.append(new_rule)
        
        return new_rules
    
    def random_combination(self):
        rules = self.rule_base.rules
        if len(rules) < 2:
            return []
        
        new_rules = []
        for _ in range(5):
            rule1, rule2 = random.sample(rules, 2)
            
            if random.random() < 0.5:
                new_subject = rule1.subject
                new_predicate = rule2.predicate
                new_object = rule2.obj
            else:
                new_subject = rule2.subject
                new_predicate = rule1.predicate
                new_object = rule1.obj
            
            new_rule = Rule(
                subject=new_subject,
                predicate=new_predicate,
                obj=new_object,
                confidence=0.5,
                source="随机组合"
            )
            new_rules.append(new_rule)
        
        return new_rules
    
    def induce(self):
        rules = self.rule_base.rules
        new_rules = []
        
        predicate_value_map = {}
        for rule in rules:
            if rule.predicate == "有":
                if rule.predicate not in predicate_value_map:
                    predicate_value_map[rule.predicate] = {}
                if rule.obj not in predicate_value_map[rule.predicate]:
                    predicate_value_map[rule.predicate][rule.obj] = []
                predicate_value_map[rule.predicate][rule.obj].append(rule.subject)
        
        for predicate, value_map in predicate_value_map.items():
            for value, subjects in value_map.items():
                if len(subjects) >= 2:
                    category_counts = {}
                    for subject in subjects:
                        category = self.rule_base.get_category(subject)
                        if category:
                            category_counts[category] = category_counts.get(category, 0) + 1
                    
                    if category_counts:
                        max_category = max(category_counts, key=category_counts.get)
                        count = category_counts[max_category]
                        
                        if count >= 2:
                            new_rule = Rule(
                                subject=max_category,
                                predicate=predicate,
                                obj=value,
                                confidence=0.7,
                                source="归纳推理"
                            )
                            new_rules.append(new_rule)
        
        return new_rules
    
    def analogize(self):
        rules = self.rule_base.rules
        new_rules = []
        
        for rule in rules:
            if rule.predicate == "有":
                subject = rule.subject
                obj = rule.obj
                
                similar_subjects = self.rule_base.get_similar_subjects(subject)
                
                for similar_subject in similar_subjects:
                    similar_rules = self.rule_base.get_rules_by_subject(similar_subject)
                    for similar_rule in similar_rules:
                        if similar_rule.predicate == rule.predicate:
                            new_rule = Rule(
                                subject=similar_subject,
                                predicate=rule.predicate,
                                obj=rule.obj,
                                confidence=0.6,
                                source="类比推理"
                            )
                            new_rules.append(new_rule)
        
        return new_rules
    
    def check_consistency(self, new_rule):
        for existing in self.rule_base.rules:
            if new_rule.conflicts_with(existing):
                return False
        return True
    
    def reason_step(self):
        self.rule_base.generation += 1
        candidates = []
        
        method_choice = random.random()
        
        if method_choice < 0.5:
            candidates = self.transitivity_inference()
            method = "传递性推理"
        elif method_choice < 0.7:
            candidates = self.induce()
            method = "归纳推理"
        elif method_choice < 0.85:
            candidates = self.analogize()
            method = "类比推理"
        else:
            candidates = self.random_combination()
            method = "随机组合"
        
        added_count = 0
        for candidate in candidates:
            if candidate not in self.rule_base.rules:
                if self.check_consistency(candidate):
                    if self.rule_base.add_rule(candidate):
                        self.new_rules_generated.append(candidate)
                        added_count += 1
        
        return method, added_count
    
    def run_dream_cycle(self, iterations=200):
        print("=" * 60)
        print("DTN 梦境机制 v2.0 开始运行")
        print("=" * 60)
        print()
        
        self.rule_base.print_rules()
        
        for i in range(iterations):
            method, added = self.reason_step()
            
            if added > 0:
                print(f"第 {i+1} 轮 [{method}]: 新增 {added} 条规则")
                for rule in self.new_rules_generated[-added:]:
                    print(f"  → {rule}")
        
        print()
        print("=" * 60)
        print("梦境循环结束")
        print("=" * 60)
        print()
        self.rule_base.print_rules()
        
        return self.new_rules_generated
