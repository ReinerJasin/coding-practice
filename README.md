# Coding Practice Repository

**Last Updated:** 17 October 2025

*Number of problems solved:*

[![HackerRank Problems Solved](https://img.shields.io/badge/HackerRank-4-2EC866?style=flat-square&logo=hackerrank&logoColor=white)](https://www.hackerrank.com/profile/reinerjasin)
[![LeetCode Problems Solved](https://img.shields.io/badge/LeetCode-0-orange?style=flat-square&logo=leetcode&logoColor=white)](https://leetcode.com/u/reinerjasin/)

This repository contains solutions to programming problems from platforms like **LeetCode** and **HackerRank**.  
It is intended as a reference for learning, practice, and inspiration. Users can copy and use the solutions, but **attribution is required**.

---

## Repository Structure
```
coding-practice/
│
├── HackerRank/          # Solutions for HackerRank problems
├── LeetCode/            # Solutions for LeetCode problems
├── README.md
├── LICENSE
├── requirements.txt     # Required Python packages
└── .gitignore
```

Each problem has its own folder with a `solution.py` file and optionally a `test_cases.json` file if test cases are provided.

---

## Getting Started

Follow these steps to set up the repository locally:

### 1. Clone the Repository

```bash
git clone https://github.com/ReinerJasin/coding-practice.git
cd coding-practice
```

2. Set Up a Python Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. Install Dependencies
All required Python packages are listed in `requirements.txt`.
Install them using:

```bash
pip install -r requirements.txt
```

---

## Using the Solutions
1. Navigate to the problem folder (e.g., LeetCode/TwoSum/solution.py)
2. Copy and paste the solution into your own code file.
3. If a `test_cases.json` is included, you can run it with the provided test runner.

> Important: Please give attribution by mentioning the author in your comments:

```python
# Solution adapted from Reiner Jasin's GitHub repository (https://github.com/ReinerJasin/coding-practice/)
```

---

## Contribution Guidelines
* Feel free to submit pull requests to add new solutions or improve existing ones.
* Follow the folder structure (`HackerRank/` or `LeetCode/`).
* Include your code in a `solution.py` file with proper problem naming.

---

## License
This repository is licensed under the MIT License. You are free to use, copy, and adapt the solutions with attribution.

---

## Contact

For questions or feedback, you can open an issue or contact me personally through these links:

[![Email](https://img.shields.io/badge/reinerjasin@gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:reinerjasin@gmail.com)
&nbsp;
[![GitHub](https://img.shields.io/badge/ReinerJasin-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ReinerJasin)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/Reiner%20Jasin-0A66C2?style=flat-square&logo=data:image/png;base64,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)](https://www.linkedin.com/in/reinerjasin/)
