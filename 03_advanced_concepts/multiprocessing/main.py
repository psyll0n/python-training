import time
import os
from typing import Any, Callable
from multiprocessing import Pool


def expensive_func(n: int) -> int:
    """A function that simulates an expensive computation"""
    for _ in range(100_000):
        n *= 2
    return n


def single_process(numbers: list[int]) -> list[int]:
    """Run the expensive function in a single process."""
    return [expensive_func(n) for n in numbers]


def multi_process(numbers: list[int]) -> list[int]:
    """Run the expensive function using multiple processes."""
    with Pool(processes=os.cpu_count()) as pool:
        results = pool.map(expensive_func, numbers)
    return results


def get_time(func: Callable[..., Any], *args: Any) -> float:
    """Measure the time taken by a function to execute."""
    start_time = time.perf_counter()
    func(*args)
    total_time = time.perf_counter() - start_time

    print(f"Time taken by {func.__name__}: {total_time:.4f} seconds")
    return total_time


def main() -> None:
    print("CPU Count:", os.cpu_count())
    numbers: list[int] = list(range(1, 21))
    assert single_process(numbers) == multi_process(numbers)

    # -- Single Process Benchmark --
    single_time: float = get_time(single_process, numbers)

    # -- Multi Process Benchmark --
    multi_time: float = get_time(multi_process, numbers)

    print(
        f"Multi-processing is {single_time / multi_time:.2f} times faster than single processing."
    )


if __name__ == "__main__":
    main()
