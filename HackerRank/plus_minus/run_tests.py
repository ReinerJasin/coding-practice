import json
import os
import time
import traceback
import tracemalloc
import io
import sys
from solution import plusMinus  # [TEMPLATE] CHANGE FUNCTION NAME HERE

def run_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "test_cases.json")

    with open(json_path) as f:
        test_cases = json.load(f)

    total_time = 0.0
    total_memory = 0.0
    failed_cases = 0

    print("Running HackerRank Tests...\n")

    for i, case in enumerate(test_cases, 1):
        start_time = time.time()
        tracemalloc.start()

        try:
            # Capture print output
            buffer = io.StringIO()
            sys.stdout = buffer

            plusMinus(case["input"])        # [TEMPLATE] CHANGE FUNCTION NAME HERE
            printed_output = buffer.getvalue().strip()

            sys.stdout = sys.__stdout__  # Restore stdout

            elapsed = time.time() - start_time
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            total_time += elapsed
            total_memory += peak

            if str(printed_output) == str(case["expected"]):
                print(f"Test {i}: PASS | Time: {elapsed:.4f}s | Peak Memory: {peak / 1024:.2f} KB")
            else:
                failed_cases += 1
                print(f"Test {i}: FAIL | Time: {elapsed:.4f}s | Peak Memory: {peak / 1024:.2f} KB")
                print(f"  Input: {case['input']}")
                print(f"  Output (printed): {printed_output}")
                print(f"  Expected: {case['expected']}")
                print("-" * 50)

        except Exception as e:
            sys.stdout = sys.__stdout__  # Ensure it's restored if error happens
            elapsed = time.time() - start_time

            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            total_time += elapsed
            total_memory += peak
            failed_cases += 1
            
            print(f"Test {i}: ERROR | Time: {elapsed:.4f}s | Peak Memory: {peak / 1024:.2f} KB")
            print(f"  Input: {case['input']}")
            print(f"  Error: {str(e)}")
            print(f"  Traceback:\n{traceback.format_exc()}")
            print("-" * 50)

    avg_time = total_time / len(test_cases) if test_cases else 0
    avg_memory = total_memory / len(test_cases) if test_cases else 0

    print("\nSummary")
    print(f"Total Tests: {len(test_cases)}")
    print(f"Passed:      {len(test_cases) - failed_cases}")
    print(f"Failed:      {failed_cases}")
    print(f"Avg Time:    {avg_time:.4f}s per test")
    print(f"Avg Memory:  {avg_memory / 1024:.2f} KB per test")

if __name__ == "__main__":
    run_tests()
