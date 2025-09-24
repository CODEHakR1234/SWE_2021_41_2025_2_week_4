# ishappy.py

def isHappy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total_sum += digit ** 2
        n = total_sum
    return n == 1


if __name__ == "__main__":
    sample0_output = isHappy(19)  # True
    sample1_output = isHappy(2)   # False

    # 절대경로로 수정
    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19:{sample0_output}\n")
        f.write(f"2:{sample1_output}\n")

    print("Results saved to /app/bind_mount/output.txt")
