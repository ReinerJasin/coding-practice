import json
import os
import time
import traceback
from solution import Solution       # [TEMPLATE] CHANGE CLASS NAME HERE if needed

def run_tests():
    # Get absolute path to this file's directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "test_cases.json")

    # Load test cases
    with open(json_path) as f:
        test_cases = json.load(f)

    solver = Solution()
    total_time = 0.0
    failed_cases = 0

    print("Running Tests...\n")

    for i, case in enumerate(test_cases, 1):
        start_time = time.time()

        try:
            result = solver.twoSum(**case["input"])             # [TEMPLATE] CHANGE FUNCTION NAME HERE
            elapsed = time.time() - start_time
            total_time += elapsed

            if result == case["expected"]:
                print(f"Test {i}: PASS | Time: {elapsed:.4f}s")
            else:
                failed_cases += 1
                print(f"Test {i}: FAIL | Time: {elapsed:.4f}s")
                print(f"  Input:    {case['input']}")
                print(f"  Result:   {result}")
                print(f"  Expected: {case['expected']}")
                print("-" * 50)

        except Exception as e:
            elapsed = time.time() - start_time
            total_time += elapsed
            failed_cases += 1
            print(f"Test {i}: ERROR | Time: {elapsed:.4f}s")
            print(f"  Input: {case['input']}")
            print(f"  Error: {str(e)}")
            print(f"  Traceback:\n{traceback.format_exc()}")
            print("-" * 50)

    # Print summary
    avg_time = total_time / len(test_cases) if test_cases else 0
    print("\nSummary")
    print(f"Total Tests: {len(test_cases)}")
    print(f"Passed:      {len(test_cases) - failed_cases}")
    print(f"Failed:      {failed_cases}")
    print(f"Avg Time:    {avg_time:.4f}s per test")

if __name__ == "__main__":
    run_tests()
