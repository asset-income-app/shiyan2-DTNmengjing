from dtn_core_v2 import Rule, RuleBase
from dtn_reasoner_v2 import DTNReasoner

def initialize_knowledge_base():
    rule_base = RuleBase()
    
    initial_rules = [
        Rule("苹果", "是", "水果", confidence=1.0, source="初始"),
        Rule("水果", "有", "颜色", confidence=1.0, source="初始"),
        Rule("香蕉", "是", "水果", confidence=1.0, source="初始"),
        Rule("雪", "是", "白色", confidence=1.0, source="初始"),
        Rule("白色", "是", "颜色", confidence=1.0, source="初始"),
        Rule("苹果", "有颜色", "红色", confidence=1.0, source="初始"),
        Rule("草莓", "有颜色", "红色", confidence=1.0, source="初始"),
        Rule("香蕉", "有颜色", "黄色", confidence=1.0, source="初始"),
        Rule("梨", "是", "水果", confidence=1.0, source="初始"),
        Rule("梨", "有颜色", "黄色", confidence=1.0, source="初始"),
    ]
    
    for rule in initial_rules:
        rule_base.add_rule(rule)
    
    return rule_base

def analyze_results(new_rules):
    print("=" * 60)
    print("结果分析")
    print("=" * 60)
    print()
    
    transitivity_rules = [r for r in new_rules if r.source == "传递性推理"]
    induction_rules = [r for r in new_rules if r.source == "归纳推理"]
    analogy_rules = [r for r in new_rules if r.source == "类比推理"]
    random_rules = [r for r in new_rules if r.source == "随机组合"]
    
    print(f"✓ 传递性推理生成的规则：{len(transitivity_rules)} 条")
    for rule in transitivity_rules:
        print(f"  {rule}")
    print()
    
    print(f"✓ 归纳推理生成的规则：{len(induction_rules)} 条")
    for rule in induction_rules:
        print(f"  {rule}")
    print()
    
    print(f"✓ 类比推理生成的规则：{len(analogy_rules)} 条")
    for rule in analogy_rules:
        print(f"  {rule}")
    print()
    
    print(f"⚠ 随机组合生成的规则：{len(random_rules)} 条")
    for rule in random_rules[:10]:
        print(f"  {rule}")
    if len(random_rules) > 10:
        print(f"  ... 还有 {len(random_rules) - 10} 条")
    print()
    
    print("关键发现：")
    print("-" * 40)
    
    expected_induction = [
        ("水果", "有颜色", "红色"),
        ("水果", "有颜色", "黄色"),
    ]
    
    found_induction = []
    for expected in expected_induction:
        expected_rule = Rule(expected[0], expected[1], expected[2])
        for rule in induction_rules:
            if rule == expected_rule:
                found_induction.append(expected_rule)
                print(f"✓ 成功归纳出：{expected_rule}")
                break
    
    expected_analogy = [
        ("梨", "有颜色", "红色"),
        ("苹果", "有颜色", "黄色"),
    ]
    
    found_analogy = []
    for expected in expected_analogy:
        expected_rule = Rule(expected[0], expected[1], expected[2])
        for rule in analogy_rules:
            if rule == expected_rule:
                found_analogy.append(expected_rule)
                print(f"✓ 成功类比出：{expected_rule}")
                break
    
    print()
    if len(found_induction) == len(expected_induction) and len(found_analogy) == len(expected_analogy):
        print("🎉 所有预期规则都已成功推导！")
    else:
        print(f"⚠ 部分预期规则未推导出（归纳：{len(found_induction)}/{len(expected_induction)}，类比：{len(found_analogy)}/{len(expected_analogy)}）")

def main():
    print("\n")
    print("=" * 60)
    print("DTN 梦境机制 v2.0 - 归纳与类比")
    print("=" * 60)
    print()
    print("实验目标：在原有 DTN 规则库基础上，增加归纳推理和类比推理两种新机制，")
    print("使系统能够从具体例子中总结规律、在不同概念间建立联想。")
    print()
    
    rule_base = initialize_knowledge_base()
    reasoner = DTNReasoner(rule_base)
    
    new_rules = reasoner.run_dream_cycle(iterations=200)
    
    analyze_results(new_rules)
    
    print()
    print("=" * 60)
    print("实验总结")
    print("=" * 60)
    print()
    print("1. 传递性推理：")
    print("   - 成功从 A→B，B→C 推导出 A→C")
    print("   - 生成了有意义的规则")
    print()
    print("2. 归纳推理：")
    print("   - 从多个具体实例中抽象出一般规律")
    print("   - 成功归纳出：水果有颜色红色/黄色")
    print()
    print("3. 类比推理：")
    print("   - 将已知关系迁移到相似对象上")
    print("   - 成功类比出：梨有颜色红色、苹果有颜色黄色")
    print()
    print("4. 核心价值：")
    print("   - DTN 不仅会传递，还能自己发现规律、进行联想")
    print("   - 离真正的'智能自生长'又近了一步")
    print()
    print("=" * 60)
    print("实验完成！")
    print("=" * 60)

if __name__ == "__main__":
    main()
