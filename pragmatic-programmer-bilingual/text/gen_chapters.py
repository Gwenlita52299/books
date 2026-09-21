#!/usr/bin/env python3
"""Generate chapter placeholder .tex files and the tip-index appendix."""
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent  # project root
CONTENT = HERE / "content"
CONTENT.mkdir(exist_ok=True)

ESC = {"&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_",
       "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}",
       "^": r"\textasciicircum{}", "\\": r"\textbackslash{}"}


def esc(s: str) -> str:
    out = []
    for ch in s:
        out.append(ESC.get(ch, ch))
    return "".join(out).replace('"', "``").replace("''", "''")


CHAPTERS = [
    (1, "A Pragmatic Philosophy", "务实的哲学", "01-a-pragmatic-philosophy",
     "本部分讨论态度与思维方式：承担责任、对抗软件腐化、做变革的催化剂、持续投资自己的知识资产，以及如何沟通。"),
    (2, "A Pragmatic Approach", "务实的方法", "02-a-pragmatic-approach",
     "本部分给出可操作的设计原则：DRY、正交性、可逆性、曳光弹开发、原型、领域语言与估算。"),
    (3, "The Basic Tools", "基础工具", "03-the-basic-tools",
     "本部分聚焦日常工具：纯文本、命令行、编辑器、版本控制、调试、文本处理与代码生成。"),
    (4, "Pragmatic Paranoia", "务实的偏执", "04-pragmatic-paranoia",
     "本部分讲防御性实践：契约式设计、尽早崩溃、断言、异常与资源的正确释放。"),
    (5, "Bend, or Break", "弯曲，或折断", "05-bend-or-break",
     "本部分关注灵活性与解耦：迪米特法则、元编程、时间耦合、视图分离与黑板系统。"),
    (6, "While You Are Coding", "编码之时", "06-while-you-are-coding",
     "本部分讲编码当下的自律：不要靠巧合编程、估算算法量级、重构与可测试性。"),
    (7, "Before the Project", "项目之前", "07-before-the-project",
     "本部分讲动手前的事：挖掘需求、解决无解难题、需求规约陷阱与打破思维定式。"),
    (8, "Pragmatic Projects", "务实项目", "08-pragmatic-projects",
     "本部分讲团队与工程化：务实团队、无处不在的自动化、无情测试、文档与签名。"),
]

TIPS = {
    1: ("Care About Your Craft", "关心你的手艺"),
    2: ("Think! About Your Work", "思考！关于你的工作"),
    3: ("Provide Options, Don't Make Lame Excuses", "提供选项，别找蹩脚的借口"),
    4: ("Don't Live with Broken Windows", "不要容忍破窗"),
    5: ("Be a Catalyst for Change", "做变革的催化剂"),
    6: ("Remember the Big Picture", "记住大局"),
    7: ("Make Quality a Requirements Issue", "把质量当作需求问题"),
    8: ("Invest Regularly in Your Knowledge Portfolio", "定期投资你的知识资产"),
    9: ("Critically Analyze What You Read and Hear", "批判性地分析你所读所闻"),
    10: ("It's Both What You Say and the Way You Say It", "说什么与怎么说同样重要"),
    11: ("DRY - Don't Repeat Yourself", "DRY——不要重复自己"),
    12: ("Make It Easy to Reuse", "让复用变得容易"),
    13: ("Eliminate Effects Between Unrelated Things", "消除不相关事物之间的影响"),
    14: ("There Are No Final Decisions", "没有最终决定"),
    15: ("Use Tracer Bullets to Find the Target", "用曳光弹寻找目标"),
    16: ("Prototype to Learn", "用原型学习"),
    17: ("Program Close to the Problem Domain", "贴近问题领域编程"),
    18: ("Estimate to Avoid Surprises", "估算以避免意外"),
    19: ("Iterate the Schedule with the Code", "让进度表随代码迭代"),
    20: ("Keep Knowledge in Plain Text", "让知识保存在纯文本中"),
    21: ("Use the Power of Command Shells", "善用命令行的力量"),
    22: ("Use a Single Editor Well", "熟练使用一个编辑器"),
    23: ("Always Use Source Code Control", "始终使用源码版本控制"),
    24: ("Fix the Problem, Not the Blame", "解决问题，而不是归咎于人"),
    25: ("Don't Panic", "不要惊慌"),
    26: ('"select" Isn\'t Broken', "``select'' 没有坏"),
    27: ("Don't Assume It - Prove It", "别假设——去证明"),
    28: ("Learn a Text Manipulation Language", "学一门文本处理语言"),
    29: ("Write Code That Writes Code", "写能生成代码的代码"),
    30: ("You Can't Write Perfect Software", "你写不出完美的软件"),
    31: ("Design with Contracts", "用契约来设计"),
    32: ("Crash Early", "尽早崩溃"),
    33: ("If It Can't Happen, Use Assertions to Ensure That It Won't",
         "若不可能发生，就用断言确保它不会"),
    34: ("Use Exceptions for Exceptional Problems", "用异常处理异常问题"),
    35: ("Finish What You Start", "有始有终"),
    36: ("Minimize Coupling Between Modules", "最小化模块间的耦合"),
    37: ("Configure, Don't Integrate", "配置，而非集成"),
    38: ("Put Abstractions in Code, Details in Metadata", "抽象进代码，细节进元数据"),
    39: ("Analyze Workflow to Improve Concurrency", "分析工作流以改善并发"),
    40: ("Design Using Services", "用服务来设计"),
    41: ("Always Design for Concurrency", "始终为并发而设计"),
    42: ("Separate Views from Models", "让视图与模型分离"),
    43: ("Use Blackboards to Coordinate Workflow", "用黑板协调工作流"),
    44: ("Don't Program by Coincidence", "不要靠巧合编程"),
    45: ("Estimate the Order of Your Algorithms", "估算算法的量级"),
    46: ("Test Your Estimates", "检验你的估算"),
    47: ("Refactor Early, Refactor Often", "尽早重构，经常重构"),
    48: ("Design to Test", "为测试而设计"),
    49: ("Test Your Software, or Your Users Will", "你不测试，用户就会替你测试"),
    50: ("Don't Use Wizard Code You Don't Understand", "不要用你不理解的向导代码"),
    51: ("Don't Gather Requirements - Dig for Them", "不要收集需求——去挖掘需求"),
    52: ("Work with a User to Think Like a User", "与用户共事，像用户一样思考"),
    53: ("Abstractions Live Longer than Details", "抽象比细节活得更久"),
    54: ("Use a Project Glossary", "使用项目术语表"),
    55: ("Don't Think Outside the Box - Find the Box", "别跳出框框想——先找到框框"),
    56: ("Listen to Nagging Doubts - Start When You're Ready", "倾听内心的疑虑——准备好了就开始"),
    57: ("Some Things Are Better Done than Described", "有些事做胜过说"),
    58: ("Don't Be a Slave to Formal Methods", "不要做形式化方法的奴隶"),
    59: ("Expensive Tools Do Not Produce Better Designs", "昂贵的工具不产生更好的设计"),
    60: ("Organize Around Functionality, Not Job Functions", "围绕功能组织，而非职务"),
    61: ("Don't Use Manual Procedures", "不要用手工流程"),
    62: ("Test Early. Test Often. Test Automatically.", "早测试，常测试，自动化测试"),
    63: ("Coding Ain't Done 'Til All the Tests Run", "所有测试都跑通，编码才算完"),
    64: ("Use Saboteurs to Test Your Testing", "用“破坏者”来测试你的测试"),
    65: ("Test State Coverage, Not Code Coverage", "测试状态覆盖，而非代码覆盖"),
    66: ("Find Bugs Once", "同一个 bug 只找一次"),
    67: ("Treat English as Just Another Programming Language", "把英语当成另一种编程语言"),
    68: ("Build Documentation In, Don't Bolt It On", "把文档做进去，而不是补上去"),
    69: ("Gently Exceed Your Users' Expectations", "温和地超越用户的期望"),
    70: ("Sign Your Work", "为你的作品署名"),
}

# tip ranges per chapter (inclusive)
RANGES = {1: (1, 10), 2: (11, 19), 3: (20, 29), 4: (30, 35),
          5: (36, 43), 6: (44, 50), 7: (51, 59), 8: (60, 70)}

for num, en, zh, fname, note in CHAPTERS:
    lo, hi = RANGES[num]
    lines = [
        f"% Chapter {num}: {en} / {zh}",
        f"\\chapter{{{esc(en)}}}",
        "",
        "\\begin{center}",
        "\\begin{minipage}{0.86\\textwidth}",
        "\\itshape\\small\\color{ppgray}",
        esc(zh) + "。" + note,
        "",
        "\\vspace{0.5em}",
        f"本部分对应原书 TIP {lo}--{hi}。完整译文待补。",
        "\\end{minipage}",
        "\\end{center}",
        "",
        "\\begin{bitext}",
        "\\src{This chapter has not been translated yet.}",
        f"\\tgt{{本章尚未翻译（原书 Chapter {num}: {esc(en)}）。}}",
        "\\end{bitext}",
        "",
        "\\section*{Tips in this chapter\\quad 本章 Tips}",
        "\\begin{longtable}{@{}r p{0.44\\textwidth} p{0.40\\textwidth}@{}}",
        "\\toprule",
        "\\textbf{\\#} & \\textbf{English} & \\textbf{中文} \\\\",
        "\\midrule",
        "\\endhead",
    ]
    for t in range(lo, hi + 1):
        en_t, zh_t = TIPS[t]
        lines.append(f"{t} & {esc(en_t)} & {zh_t} \\\\")
    lines += ["\\bottomrule", "\\end{longtable}", ""]
    (CONTENT / f"{fname}.tex").write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {fname}.tex")

# ---- appendix: full tip index ----
app = [
    "% Appendix: full tip index",
    "\\chapter{Tips Index\\quad TIP 总索引}",
    "",
    "\\begin{longtable}{@{}r p{0.44\\textwidth} p{0.40\\textwidth}@{}}",
    "\\toprule",
    "\\textbf{\\#} & \\textbf{English} & \\textbf{中文} \\\\",
    "\\midrule",
    "\\endhead",
]
for t in sorted(TIPS):
    en_t, zh_t = TIPS[t]
    app.append(f"{t} & {esc(en_t)} & {zh_t} \\\\")
app += ["\\bottomrule", "\\end{longtable}", ""]
(CONTENT / "99-appendix-tips.tex").write_text("\n".join(app), encoding="utf-8")
print("wrote 99-appendix-tips.tex")
