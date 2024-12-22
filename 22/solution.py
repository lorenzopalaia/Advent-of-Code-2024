with open("22/data.txt", "r") as file:
    data = file.read().strip().replace('\r', '').splitlines()


def generate_next_secret(secret: int):
    secret = (secret ^ (secret << 6)) & 0xFF_FFFF
    secret = (secret ^ (secret >> 5)) & 0xFF_FFFF
    secret = (secret ^ (secret << 11)) & 0xFF_FFFF
    return secret


def simulate_secret_generation(seed: int, iterations: int) -> tuple[int, dict[int, int]]:
    price_changes = {}
    secret = seed
    last_digit = seed % 10

    change_history = 0

    for i in range(iterations):
        next_secret = generate_next_secret(secret)
        next_digit = next_secret % 10

        change_history = ((change_history << 8) | (
            (next_digit - last_digit) % 256)) & 0xffff_ffff

        if i >= 3:
            if change_history not in price_changes:
                price_changes[change_history] = next_digit
        secret = next_secret
        last_digit = next_digit

    return secret, price_changes


def find_best_sequence(change_data_list: list[dict[int, int]]):
    patterns = {pattern for data in change_data_list for pattern in data.keys()}
    best_pattern = max(patterns, key=lambda p: sum(
        data.get(p, 0) for data in change_data_list))
    best_score = sum(data.get(best_pattern, 0) for data in change_data_list)
    return best_score


# * Part 1

# ! IDEA : Generate the next secrets and track the changes.
# ! We sum up all the final secrets after 2000 iterations to get the total secret sum.

initial_secrets = list(map(int, data))
price_changes_list = []
res = 0
for seed in initial_secrets:
    final_secret, change_data = simulate_secret_generation(seed, 2000)
    res += final_secret
    price_changes_list.append(change_data)

print(res)


# * Part 2

# ! IDEA : Analyze the change data collected in part 1.
# ! The function identifies the pattern that appears most frequently and sums up the corresponding values.

res = find_best_sequence(price_changes_list)

print(res)
