import random
import timeit


def insertion_sort(arr):
    """Sort a list using the Insertion Sort algorithm."""

    sorted_arr = arr.copy()

    for i in range(1, len(sorted_arr)):

        current_value = sorted_arr[i]
        j = i - 1

        while j >= 0 and sorted_arr[j] > current_value:

            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1

        sorted_arr[j + 1] = current_value

    return sorted_arr


def merge_sort(arr):
    """Sort a list using the Merge Sort algorithm."""

    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)


def merge(left, right):
    """Merge two sorted lists into one sorted list."""

    merged = []

    left_index = 0
    right_index = 0

    while (
        left_index < len(left)
        and right_index < len(right)
    ):

        if left[left_index] <= right[right_index]:

            merged.append(left[left_index])
            left_index += 1

        else:

            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


def generate_random_data(size):
    """Generate a list of random integers."""

    return [
        random.randint(1, 1000)
        for _ in range(size)
    ]


def generate_nearly_sorted_data(size):
    """Generate a nearly sorted list."""

    data = generate_random_data(size)
    data.sort()

    swap_count = size // 10

    for _ in range(swap_count):

        first_index = random.randint(0, size - 1)
        second_index = random.randint(0, size - 1)

        data[first_index], data[second_index] = (
            data[second_index],
            data[first_index],
        )

    return data


def generate_reverse_data(size):
    """Generate a reverse sorted list."""

    return sorted(
        generate_random_data(size),
        reverse=True,
    )


def benchmark(sort_function, data):
    """Measure the execution time of a sorting algorithm."""

    return timeit.timeit(
        lambda: sort_function(data),
        number=1,
    )


def print_results(results):
    """Display benchmark results in a formatted table."""

    current_data_type = ""

    for result in results:

        if result["Data Type"] != current_data_type:

            current_data_type = result["Data Type"]

            print()
            print("=" * 70)
            print(f"Data Type: {current_data_type}")
            print("=" * 70)

            print(
                f"{'Size':<10}"
                f"{'Insertion':<15}"
                f"{'Merge':<15}"
                f"{'Timsort':<15}"
            )

            print("-" * 70)

        print(
            f"{result['Size']:<10}"
            f"{result['Insertion Sort']:<15.6f}"
            f"{result['Merge Sort']:<15.6f}"
            f"{result['Timsort']:<15.6f}"
        )


def main():
    """Run sorting benchmarks."""

    print("Sorting algorithms benchmark...")
    print("Please wait...\n")

    sizes = [100, 1000, 5000, 10000]

    data_generators = {
        "Random": generate_random_data,
        "Nearly sorted": generate_nearly_sorted_data,
        "Reverse": generate_reverse_data,
    }

    sorting_algorithms = {
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Timsort": sorted,
    }

    results = []

    for data_type, generator in data_generators.items():

        for size in sizes:

            data = generator(size)

            result = {
                "Data Type": data_type,
                "Size": size,
            }

            for algorithm_name, algorithm in sorting_algorithms.items():

                result[algorithm_name] = benchmark(
                    algorithm,
                    data,
                )

            results.append(result)

    print_results(results)

    print("\nBenchmark completed successfully.")


if __name__ == "__main__":
    main()