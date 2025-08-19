import os

def create_problem_folder(number, difficulty, topics, title):
    slug = title.lower().replace(" ", "_")
    folder_name = f"{str(number).zfill(3)}_{slug}"
    folder_path = os.path.join("../problems", folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")
    else:
        print(f"Folder already exists: {folder_path}")

    # Create solution.py stub
    solution_file = os.path.join(folder_path, "solution.py")
    with open(solution_file, "w") as f:
        f.write(f"class Solution(object):\n    def {slug}(self, *args):\n        pass\n")

    # Create approach.md stub
    approach_file = os.path.join(folder_path, "approach.md")
    with open(approach_file, "w") as f:
        f.write(
            f"# {number}. {title}\n\n**Difficulty:** {difficulty}\n**Topics:** {topics}\n\n## Intuition\n\n## Algorithm\n\n## Complexity\n\n## Notes / Pitfalls\n")

    print(f"Created solution.py and approach.md for {title}!\n")


# -------------------------------
# Batch list of all 27 problems
problems = [
    (1, "Easy", "Array, Hash Map", "Two Sum"),
    (3, "Medium", "Hash Map, Sliding Window", "Longest Substring Without Repeating Characters"),
    (4, "Hard", "Array, Binary Search", "Median of Two Sorted Arrays"),
    (5, "Medium", "String, Dynamic Programming", "Longest Palindromic Substring"),
    (6, "Medium", "String", "Zigzag Conversion"),
    (7, "Medium", "Math", "Reverse Integer"),
    (8, "Medium", "String, Math", "String to Integer (atoi)"),
    (9, "Easy", "Math", "Palindrome Number"),
    (11, "Medium", "Array, Two Pointers", "Container With Most Water"),
    (12, "Medium", "Math, String", "Integer to Roman"),
    (13, "Easy", "Math, String", "Roman to Integer"),
    (14, "Easy", "String", "Longest Common Prefix"),
    (15, "Medium", "Array, Two Pointers", "3Sum"),
    (17, "Medium", "Backtracking", "Letter Combinations of a Phone Number"),
    (20, "Easy", "Stack, String", "Valid Parentheses"),
    (22, "Medium", "Backtracking", "Generate Parentheses"),
    (26, "Easy", "Array", "Remove Duplicates from Sorted Array"),
    (28, "Easy", "String, Sliding Window", "Find the Index of the First Occurrence in a String"),
    (32, "Hard", "Stack, Dynamic Programming", "Longest Valid Parentheses"),
    (33, "Medium", "Binary Search", "Search in Rotated Sorted Array"),
    (34, "Medium", "Binary Search", "Find First and Last Position of Element in Sorted Array"),
    (35, "Easy", "Binary Search", "Search Insert Position"),
    (36, "Medium", "Hash Table, Backtracking", "Valid Sudoku"),
    (58, "Easy", "String", "Length of Last Word"),
    (175, "Easy", "SQL", "Combine Two Tables"),
    (217, "Easy", "Hash Table", "Contains Duplicate"),
    (242, "Easy", "Hash Table, Sorting", "Valid Anagram"),
    (347, "Medium", "Hash Table, Heap", "Top K Frequent Elements")
]

# -------------------------------
# Create all problem folders
if __name__ == "__main__":
    for p in problems:
        create_problem_folder(*p)
