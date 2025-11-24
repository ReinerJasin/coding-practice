import json
import os
import time
import traceback
import tracemalloc
import subprocess

def run_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "test_cases.json")
    solution_path = os.path.join(base_dir, "solution.py")

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
            # Run solution.py as a subprocess
            process = subprocess.run(
                ["python3", solution_path],
                input=str(case["input"]).encode(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=5,
                cwd=base_dir
            )

            output_text = process.stdout.decode().strip()
            error_text = process.stderr.decode().strip()

            if output_text == "" and error_text != "":
                print(f"  STDERR: {error_text}")
    
            elapsed = time.time() - start_time
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            total_time += elapsed
            total_memory += peak

            output_text = process.stdout.decode().strip()

            # Convert printed output to float
            try:
                output_value = float(output_text)
            except:
                output_value = output_text  # fallback

            expected = case["expected"]

            is_pass = False

            # Float comparison with tolerance
            if isinstance(output_value, (int, float)) and isinstance(expected, (int, float)):
                if abs(output_value - expected) < 1e-6:
                    is_pass = True
            else:
                if output_value == expected:
                    is_pass = True

            if is_pass:
                print(f"Test {i}: PASS | Time: {elapsed:.4f}s | Peak Memory: {peak/1024:.2f} KB")
            else:
                failed_cases += 1
                print(f"Test {i}: FAIL | Time: {elapsed:.4f}s | Peak Memory: {peak/1024:.2f} KB")
                print(f"  Input:    {case['input']}")
                print(f"  Output:   {output_value}")
                print(f"  Expected: {case['expected']}")
                print("-" * 50)

        except Exception as e:
            elapsed = time.time() - start_time
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            total_time += elapsed
            total_memory += peak
            failed_cases += 1

            print(f"Test {i}: ERROR | Time: {elapsed:.4f}s | Peak Memory: {peak/1024:.2f} KB")
            print(f"  Input: {case['input']}")
            print(f"  Error: {e}")
            print(f"  Traceback:\n{traceback.format_exc()}")
            print("-" * 50)

    avg_time = total_time / len(test_cases)
    avg_memory = total_memory / len(test_cases)

    print("\nSummary")
    print(f"Total Tests: {len(test_cases)}")
    print(f"Passed:      {len(test_cases) - failed_cases}")
    print(f"Failed:      {failed_cases}")
    print(f"Avg Time:    {avg_time:.4f}s per test")
    print(f"Avg Memory:  {avg_memory / 1024:.2f} KB per test")

if __name__ == "__main__":
    run_tests()
