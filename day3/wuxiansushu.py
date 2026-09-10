def is_prime(n):
    """判断 n 是否为素数"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes():
    """无限生成素数的生成器"""
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# 打印素数（按下 Ctrl + C 可终止程序）
try:
    for prime in generate_primes():
        print(prime, end=" ")
except KeyboardInterrupt:
    print("\n程序已被手动停止。")