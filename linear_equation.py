import random

# ===== 設定 =====
n = 15
coef_range = [i for i in range(-9, 10) if i != 0]

# ===== LaTeX用 整形関数 =====
def linexpr(a, b):
    s = ""
    if a == 1:
        s += "x"
    elif a == -1:
        s += "-x"
    elif a != 0:
        s += f"{a}x"

    if b > 0:
        s += f"+{b}"
    elif b < 0:
        s += f"-{abs(b)}"

    if s.startswith("+"):
        s = s[1:]
    return s or "0"


def parenexpr(a, b, c):
    inner = linexpr(b, c)
    if a == 1:
        return f"({inner})"
    elif a == -1:
        return f"-({inner})"
    else:
        return f"{a}({inner})"


# ===== 問題生成 =====
problems = []
answers = []

for _ in range(n):
    x = random.randint(-10, 10)

    # 左辺： a(bx+c)
    a = random.choice(coef_range)
    b = random.choice(coef_range)
    c = random.randint(-9, 9)

    # 展開後係数
    A = a * b
    B = a * c

    # 右辺： dx+e
    d = random.choice(coef_range)
    e = A * x + B - d * x

    left = parenexpr(a, b, c)
    right = linexpr(d, e)

    problems.append(f"{left} = {right}")
    answers.append(f"x = {x}")

# ===== TeXファイル生成 =====
with open("linear_equations.tex", "w", encoding="utf-8") as f:
    f.write(r"""\documentclass[a4paper,12pt]{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{geometry}
\geometry{margin=25mm}

\begin{document}

\section*{一次方程式}
""")

    for i, p in enumerate(problems, 1):
        f.write(f"\\[{i}.\\; {p}\\]\n\n")

    f.write(r"""\newpage
\section*{解答}
""")

    for i, a in enumerate(answers, 1):
        f.write(f"\\[{i}.\\; {a}\\]\n\n")

    f.write(r"\end{document}")
