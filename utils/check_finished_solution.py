import os

def count_solutions(base_dir):
    """
    Count solved and unsolved problems in a given directory.
    Each subfolder is treated as one problem attempt.
    """
    solved_count = 0
    unsolved_count = 0
    total_folders = 0
    unsolved_list = []

    # List all subdirectories (excluding hidden folders like .template_folder)
    for folder in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder)
        if os.path.isdir(folder_path) and not folder.startswith("."):
            total_folders += 1
            readme_path = os.path.join(folder_path, "README.md")

            # Check README.md exists
            if not os.path.exists(readme_path):
                print(f"[WARN] No README found in {folder_path}")
                continue

            # Read README and check status
            with open(readme_path, "r", encoding="utf-8") as f:
                content = f.read()

            if "![Status](https://img.shields.io/badge/Status-Unsolved-red)" in content:
                unsolved_count += 1
                unsolved_list.append(folder)
            elif "![Status](https://img.shields.io/badge/Status-Solved-brightgreen)" in content:
                solved_count += 1
            else:
                print(f"[INFO] No status badge found in {folder_path}")

    return solved_count, unsolved_count, total_folders, unsolved_list


def main(show_unsolved=False):
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    hackerrank_dir = os.path.join(root_dir, "hackerrank")
    leetcode_dir = os.path.join(root_dir, "LeetCode")

    print("=========================================")
    print("Checking finished solutions summary...")
    print("=========================================\n")

    results = {}

    for category, path in [("HackerRank", hackerrank_dir), ("LeetCode", leetcode_dir)]:
        if not os.path.exists(path):
            print(f"[ERROR] {category} directory not found at {path}")
            continue

        solved, unsolved, total, unsolved_list = count_solutions(path)
        results[category] = {
            "solved": solved,
            "unsolved": unsolved,
            "total": total,
            "unsolved_list": unsolved_list
        }

    # ===== SUMMARY =====
    print("\n============= SUMMARY =============")
    for category, data in results.items():
        solved = data["solved"]
        unsolved = data["unsolved"]
        total = data["total"]
        print(f"\n📘 {category}")
        print(f"Total problems attempted : {total}")
        print(f"Solved problems          : {solved}")
        print(f"Unsolved problems        : {unsolved}")
        print(f"Completion rate          : {(solved / total * 100 if total > 0 else 0):.1f}%")

    # ===== UNSOLVED LIST =====
    if show_unsolved:
        print("\n============= UNSOLVED PROBLEMS =============")
        for category, data in results.items():
            unsolved_list = data["unsolved_list"]
            if not unsolved_list:
                print(f"\n✅ All {category} problems are solved!")
            else:
                print(f"\n❌ {category} Unsolved Problems:")
                for item in sorted(unsolved_list):
                    print(f"  • {item}")

    print("\n=========================================")
    print("Finished checking all solutions.")
    print("=========================================")


if __name__ == "__main__":
    # Change to True if you want to show the unsolved list at the end
    main(show_unsolved=True)
