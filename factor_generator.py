import random
from collections import Counter

def sieve(n):
    """エラトステネスの篩：n以下の素数を返す"""
    is_prime = [True] * (n + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i, val in enumerate(is_prime) if val]

def generate_number(primes, max_value):
    """指定された素数から max_value 以下の数を作る"""
    for _ in range(1000):
        count = random.randint(2, 6)
        chosen = random.choices(primes, k=count)
        n = 1
        for p in chosen:
            n *= p
        if n <= max_value:
            return n
    raise ValueError("条件を満たす数が見つかりません。最大値を上げてください。")

def prime_factors(n):
    """n の素因数分解を Counter で返す"""
    i = 2
    factors = Counter()
    while i * i <= n:
        while n % i == 0:
            factors[i] += 1
            n //= i
        i += 1
    if n > 1:
        factors[n] += 1
    return factors

def to_superscript(num):
    """整数を上付き文字に変換（例: 12 -> ¹²）"""
    sup_map = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")
    return str(num).translate(sup_map)

def format_factors(factors):
    """例: 2³ × 3 × 5²"""
    parts = []
    for base in sorted(factors):
        exp = factors[base]
        if exp == 1:
            parts.append(f"{base}")
        else:
            parts.append(f"{base}{to_superscript(exp)}")
    return " × ".join(parts)

def main():
    try:
        num_problems = int(input("何問出題しますか？: "))
        max_prime = int(input("素因数に使う最大の素数はいくつですか？: "))
        max_value = int(input("問題に使う数の最大値はいくつですか？: "))
    except ValueError:
        print("整数で入力してください。")
        return

    primes = sieve(max_prime)
    if not primes:
        print(f"{max_prime} 以下に素数がありません。")
        return

    with open("questions.txt", "w", encoding="utf-8") as qf, open("answers.txt", "w", encoding="utf-8") as af:
        qf.write(f"次の数を素因数分解せよ（素因数は最大 {max_prime} 以下、値は最大 {max_value}）：\n")
        af.write("解答：\n")

        for i in range(1, num_problems + 1):
            try:
                number = generate_number(primes, max_value)
            except ValueError as e:
                print(f"問題{i}：{e}")
                break

            factors = prime_factors(number)
            qf.write(f"{i}. {number}\n")
            af.write(f"{i}. {format_factors(factors)}\n")

    print("出題と解答を questions.txt / answers.txt に出力しました。")

if __name__ == "__main__":
    main()
