from dtn_core import Rule, RuleBase
from dtn_reasoner import DTNReasoner

def initialize_knowledge_base():
    rule_base = RuleBase()
    
    initial_rules = [
        Rule("苹果", "是", "水果", confidence=1.0, source="初始"),
        Rule("水果", "有", "颜色", confidence=1.0, source="初始"),
        Rule("香蕉", "是", "水果", confidence=1.0, source="初始"),
        Rule("雪", "是", "白色", confidence=1.0, source="初始"),
        Rule("白色", "是", "颜色", confidence=1.0, source="初始"),
    ]
    
    for rule in initial_rules:
        rule_base.add_rule(rule)
    
    return rule_base

def analyze_results(new_rules):
    print("=" * 60)
    print("结果分析")
    print("=" * 60)
    print()
    
    meaningful_rules = []
    meaningless_rules = []
    
    for rule in new_rules:
        if rule.source == "传递性推理":
            meaningful_rules.append(rule)
        else:
            meaningless_rules.append(rule)
    
    print(f"✓ 传递性推理生成的规则（有意义）：{len(meaningful_rules)} 条")
    for rule in meaningful_rules:
        print(f"  {rule}")
    print()
    
    print(f"⚠ 随机组合生成的规则（可能无意义）：{len(meaningless_rules)} 条")
    for rule in meaningless_rules[:10]:
        print(f"  {rule}")
    if len(meaningless_rules) > 10:
        print(f"  ... 还有 {len(meaningless_rules) - 10} 条")
    print()
    
    print("关键发现：")
    print("-" * 40)
    
    expected_rules = [
        ("苹果", "有", "颜色"),
        ("香蕉", "有", "颜色"),
    ]
    
    found_rules = []
    for expected in expected_rules:
        expected_rule = Rule(expected[0], expected[1], expected[2])
        for rule in new_rules:
            if rule == expected_rule:
                found_rules.append(expected_rule)
                print(f"✓ 成功推导出：{expected_rule}")
                break
    
    if len(found_rules) == len(expected_rules):
        print()
        print("🎉 所有预期规则都已成功推导！")
    else:
        print()
        print(f"⚠ 部分预期规则未推导出（{len(expected_rules) - len(found_rules)}/{len(expected_rules)}）")

def main():
    print("\n")
    print("=" * 60)
    print("DTN 梦境机制验证实验")
    print("=" * 60)
    print()
    print("实验目标：验证 DTN 能否从极少量初始规则出发，")
    print("通过内部逻辑推理和随机组合，生成有意义的、新的规则。")
    print()
    
    rule_base = initialize_knowledge_base()
    reasoner = DTNReasoner(rule_base)
    
    new_rules = reasoner.run_dream_cycle(iterations=50)
    
    analyze_results(new_rules)
    
    print()
    print("=" * 60)
    print("实验完成！")
    print("=" * 60)

if __name__ == "__main__":
    main()
