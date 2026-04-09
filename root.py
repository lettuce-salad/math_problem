import math
import random

def generate_root_simplification_problems(num_problems, max_value, inner_max, num_perfect_squares, filename="roots_problems.txt"):
    problems = []
    answers = []
    existing_values = set()

    # 完全な平方数の問題
    for i in range(1, int(math.sqrt(max_value)) + 1):
        square = i ** 2
        if square <= max_value:
            problems.append(f"√{square}")
            answers.append(str(i))
            existing_values.add(square)
            if len(problems) >= num_perfect_squares:
                break

    # 簡単化可能で完全平方数でない問題
    outer_values = range(2, int(math.sqrt(max_value)) + 1)
    inner_values = list(range(2, inner_max + 1))

    for outer in outer_values:
        for inner in inner_values:
            value = outer**2 * inner
            if value <= max_value and value not in existing_values:
                problems.append(f"√{value}")
                answers.append(f"{outer}√{inner}")
                existing_values.add(value)
            if len(problems) == num_problems:
                break
        if len(problems) == num_problems:
            break

    # 問題と答えをペアにしてシャッフル
    qa_pairs = list(zip(problems, answers))
    random.shuffle(qa_pairs)

    # シャッフルしたペアを分解
    problems_shuffled, answers_shuffled = zip(*qa_pairs) if qa_pairs else ([], [])

    # ファイル出力
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"【平方根を簡単にする問題（全{len(problems_shuffled)}問）】\n")
        for i, prob in enumerate(problems_shuffled):
            f.write(f"{i+1}. {prob}\n")
        f.write("\n【解答】\n")
        for i, ans in enumerate(answers_shuffled):
            f.write(f"{i+1}. {ans}\n")

    print(f"\n✅ 出力完了: {len(problems_shuffled)}問の問題を「{filename}」に保存しました。")

    if len(problems_shuffled) < num_problems:
        print(f"⚠️ 警告: 指定された {num_problems} 問すべては生成できませんでした。")


if __name__ == "__main__":
    try:
        num = int(input("作成したい問題数を入力してください（例：50）: "))
        max_val = int(input("ルートの中の最大値を入力してください（例：500）: "))
        inner_max = int(input("ルートに残る数（inner）の最大値を入力してください（例：20）: "))
        perfect_square_count = int(input("完全な平方数の問題数を入力してください（例：1）: "))

        if perfect_square_count > num:
            print("❌ 完全な平方数の問題数は、全体の問題数以下でなければなりません。")
        else:
            generate_root_simplification_problems(num, max_val, inner_max, perfect_square_count)

    except ValueError:
        print("❌ 整数を入力してください。")