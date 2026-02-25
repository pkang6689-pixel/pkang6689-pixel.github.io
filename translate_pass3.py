#!/usr/bin/env python3
"""
Third pass: translate the remaining short answer options and phrases.
"""
import json, re

with open("/workspaces/ArisEdu/algebra2_full_translations.json", "r", encoding="utf-8") as f:
    translations = json.load(f)

# ALL remaining manual translations
remaining = {
    # ── Short answer options ──
    "yes": "是",
    "all": "全部",
    "any": "任意",
    "fit": "拟合",
    "ray": "射线",
    "both": "两者",
    "down": "向下",
    "none": "无",
    "skew": "偏斜",
    "weak": "弱",
    "line": "线",
    "9 min": "9 分钟",
    "fixed": "固定",
    "all t": "所有 t",
    "any r": "任意 r",
    "any λ": "任意 λ",
    "other": "其他",
    "point": "点",
    "solid": "实线",
    "sin²x": "sin²x",
    "tan²x": "tan²x",
    "all x": "所有 x",
    "error": "误差",
    "skips": "跳过",
    "mixed": "混合",
    "use 5": "用 5",
    "maybe": "可能",
    "prime": "质数",
    "no sol": "无解",
    "visual": "可视",
    "z-dist": "z分布",
    "varies": "变化",
    "spread": "分散",
    "unique": "唯一",
    "dashed": "虚线",
    "dotted": "点线",
    "2sin x": "2sin x",
    "2tan x": "2tan x",
    "left 2": "左移2",
    "down 2": "下移2",
    "down 3": "下移3",
    "left 3": "左移3",
    "left 5": "左移5",
    "down 5": "下移5",
    "both 1": "两者为1",
    "use −5": "用 −5",
    "use 5x": "用 5x",
    "product": "乘积",
    "1.5 hrs": "1.5 小时",
    "2.5 min": "2.5 分钟",
    "all pos": "全部正",
    "x-asymp": "x渐近线",
    "take ln": "取自然对数",
    "573 yrs": "573 年",
    "average": "平均值",
    "depends": "取决于",
    "no calc": "无需计算",
    "n value": "n 值",
    "removed": "已去除",
    "2 hours": "2 小时",
    "3 hours": "3 小时",
    "4 hours": "4 小时",
    "5 hours": "5 小时",
    "6 hours": "6 小时",
    "correct": "正确",
    "≠ const": "≠ 常数",
    "right 2": "右移2",
    "dec all": "全部递减",
    "inc all": "全部递增",
    "no real": "无实数",
    "right 3": "右移3",
    "right 5": "右移5",
    "max = 2": "最大值 = 2",
    "min = 2": "最小值 = 2",
    "max = 3": "最大值 = 3",
    "all neg": "全部负",
    "no root": "无根",
    "touches": "相切",
    "crosses": "相交",
    "use 1/5": "用 1/5",
    "18/5 min": "18/5 分钟",
    "at asymp": "在渐近线处",
    "no asymp": "无渐近线",
    "position": "位置",
    "velocity": "速度",
    "change e": "改变 e",
    "5730 yrs": "5730 年",
    "rise/run": "升/距",
    "any dist": "任意分布",
    "kurtosis": "峰度",
    "randomly": "随机",
    "have AAS": "有 AAS",
    "have SSA": "有 SSA",
    "all real": "所有实数",
    "down π/4": "下移 π/4",
    "left π/4": "左移 π/4",
    "disc = 0": "判别式 = 0",
    "one root": "一个根",
    "compress": "压缩",
    "diagonal": "对角线",
    "sideways": "横向",
    "equals 0": "等于 0",
    "both →+∞": "都趋向+∞",
    "both →−∞": "都趋向−∞",
    "inclusive": "包含",
    "exclusive": "不包含",
    "15/18 min": "15/18 分钟",
    "satisfies": "满足",
    "opens L-R": "左右开口",
    "opens U-D": "上下开口",
    "10000 yrs": "10000 年",
    "57300 yrs": "57300 年",
    "alternate": "交替",
    "widens CI": "扩大置信区间",
    "all types": "所有类型",
    "1.5 hours": "1.5 小时",
    "2.5 hours": "2.5 小时",
    "incorrect": "不正确",
    "all above": "以上全部",
    "all equal": "全部相等",
    "right π/4": "右移 π/4",
    "interpret": "解释",
    "exactly 4": "恰好4个",
    "stretch 2": "拉伸2倍",
    "root at 0": "在0处有根",
    "exactly 5": "恰好5个",
    "all linear": "全部线性",
    "change a,b": "改变 a,b",
    "only x > 1": "仅 x > 1",
    "yes, x > 0": "是，x > 0",
    "both equal": "两者相等",
    "y when x=0": "x=0 时的 y",
    "regression": "回归",
    "narrows CI": "缩小置信区间",
    "only upper": "仅上界",
    "only lower": "仅下界",
    "fixed n, p": "固定 n, p",
    "stays same": "保持不变",
    "unique sol": "唯一解",
    "one corner": "一个顶点",
    "impossible": "不可能",
    "acute only": "仅锐角",
    "right only": "仅直角",
    "any config": "任意配置",
    "only first": "仅第一个",
    "2cos²x − 1": "2cos²x − 1",
    "compress 2": "压缩2倍",
    "all nonneg": "全部非负",
    "at least 4": "至少4个",
    "no divison": "无除法",
    "slant asymp": "斜渐近线",
    "traces path": "描绘路径",
    "none exists": "不存在",
    "x = log₂ 50": "x = log₂ 50",
    "x = log₅₀ 2": "x = log₅₀ 2",
    "x = log₁₀ e": "x = log₁₀ e",
    "direct only": "仅直接",
    "1.875 hours": "1.875 小时",
    "any pattern": "任意模式",
    "valid if x≠2": "当 x≠2 时有效",
    "displacement": "位移",
    "linear combo": "线性组合",
    "exponentiate": "取指数",
    "linear scale": "线性刻度",
    "all except 0": "除0外全部",
    "goodness fit": "拟合优度",
    "have SAS/SSS": "有 SAS/SSS",
    "same for all": "对所有相同",
    "2sin x cos x": "2sin x cos x",
    "root bet 1&2": "根在1和2之间",
    "vertices only": "仅顶点",
    "when have SSS": "当有 SSS 时",
    "cos²x − sin²x": "cos²x − sin²x",
    "1. log₂ 32 = ?": "1. log₂ 32 = ?",
    "2. log₃ 27 = ?": "2. log₃ 27 = ?",
    "8. log₂ 32 = ?": "8. log₂ 32 = ?",
    "9. log₃ 27 = ?": "9. log₃ 27 = ?",
    "2tan x/(1−tan²x)": "2tan x/(1−tan²x)",
    
}

long_strings = {
    'Occur at x-values where denominator is zero (and not cancelled by numerator). These are "forbidden" x-values. Graph approaches these lines but never touches them.': '出现在分母为零（且未被分子约去）的x值处。这些是"禁止"的x值。图形趋近这些线但永远不触碰它们。',
    "Selection of objects where ORDER DOESN'T MATTER. C(n,r) = n!/(r!(n-r)!), also written \"n choose r\". Always C(n,r) \u2264 P(n,r). Example: choosing 3 of 5 books.": '选择对象时顺序不重要。C(n,r) = n!/(r!(n-r)!)，也写作"n选r"。始终 C(n,r) ≤ P(n,r)。例如：从5本书中选3本。',
}

# Now also handle patterns where the string has partial translation done
# by the first pass but was still marked unchanged

updated = 0
for text in list(translations.keys()):
    if text in remaining:
        translations[text] = remaining[text]
        updated += 1
    elif text in long_strings:
        translations[text] = long_strings[text]
        updated += 1

# Check for the two long summary strings by prefix
for text in list(translations.keys()):
    if text.startswith("Occur at x-values") and translations[text] == text:
        translations[text] = long_strings.get(text, translations[text])
        updated += 1
    elif text.startswith("Selection of objects where ORDER") and translations[text] == text:
        for k, v in long_strings.items():
            if k.startswith("Selection of objects"):
                translations[text] = v
                updated += 1
                break

print(f"Updated: {updated}")

# Final count
still_unchanged = [k for k,v in translations.items() if re.search(r'[a-zA-Z]{3,}', v) and k == v]
# Remove math-only from the count
math_funcs_pat = re.compile(r'\b(sin|cos|tan|sec|csc|cot|log|adj|hyp|opp|log_b|arcsin|arccos|arctan)\b', re.IGNORECASE)
truly_english = [s for s in still_unchanged if re.search(r'[a-zA-Z]{3,}', math_funcs_pat.sub('', s))]

print(f"Still unchanged: {len(still_unchanged)}")
print(f"  Math notation only: {len(still_unchanged) - len(truly_english)}")
print(f"  With English words: {len(truly_english)}")
if truly_english:
    print("\nRemaining English:")
    for s in sorted(truly_english)[:20]:
        print(f"  {repr(s)}")

# Save
with open("/workspaces/ArisEdu/algebra2_full_translations.json", "w", encoding="utf-8") as f:
    json.dump(translations, f, ensure_ascii=False, indent=2)

print(f"\nTotal translations: {len(translations)}")
