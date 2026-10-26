# Terminal Record: Brightline Print Shop

## 1. Building the project
mkdir -p ism3232-midterm
touch business_rules.py main.py README.md commands.md requirements.txt .gitignore 
mkdir -p tests
touch tests/test_business_rules.py
pip install pytest ruff
pip freeze > requirements.txt
git init
git branch -M main
git remote add origin https://github.com/darealdavid1/ism3232-midterm.git

## 2. The virtual environment
/Users/darealdavid1/ism3232/.venv/bin/python3
The output shows that the virtual environment is active, it says the `.venv` folder rather than `darealdavid1`

## 3. The project structure

├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py
The file `.venv`  is present on my computer but absent from GitHub because it is excluded via `.gitignore`.

## 4. Every function and test

(.venv) darealdavid1@eduroam-Wifi-130-97-222 ism3232-midterm % rg 'def '
main.py
22:def main() -> None:

business_rules.py
16:def calculate_print_cost(copy_price: float, copies: int) -> float:
20:def get_volume_discount(copies: int, student_org: bool= False) -> float:
35:def calculate_job_total()
48:def requires_proof(total: float) -> bool:
52:def needs_overnight_run(copies: int, total: float) -> bool:
56:def total_invoiced(jobs: list) -> float:
66:def largest_job(jobs: list) -> str:
84:def format_job_line(title: str, total: float, proof: bool, overnight_run: bool) -> str:

tests/test_business_rules.py
14:def test_calculate_print_cost_standard():
18:def test_calculate_print_cost_zero_copies():
23:def test_discount_under_200_copies():
27:def test_discount_under_200_copies_student():
31:def test_discount_at_200_copies():
35:def test_discount_at_200_copies_student():
39:def test_discount_at_999_copies():
43:def test_discount_at_1000_copies():
47:def test_discount_at_1000_copies_student():
52:def test_job_total_with_setup_fee():
57:def test_job_total_at_39_99_adds_fee():
62:def test_job_total_at_exact_40_no_fee():
67:def test_job_total_above_40_no_fee():
73:def test_requires_proof_at_300():
77:def test_requires_proof_over_300():
82:def test_needs_overnight_run_copies_over_500():
86:def test_needs_overnight_run_total_over_400():
90:def test_needs_overnight_run_at_limits():
97:def test_total_invoiced():
104:def test_largest_job():
117:def test_largest_job_empty():
121:def test_largest_job_tie():
129:def test_format_job_line():
134:def test_format_job_line_yes_flags():

business_rules.py defines 8 functions, and tests/test_business_rules.py defines 24 test functions.

## 5. Which files print
rm % rg -l 'print'
main.py
business_rules.py
tests/test_business_rules.py

## 6. The commit history

(.venv) darealdavid1@eduroam-Wifi-130-97-222 ism3232-midterm % git log --oneline
9ae1f15 (HEAD -> main, origin/main) Added rules 5-8 for boundaries & formatting
b435aa7 Added rules 1-4 for discounts, pricing, and setupfees
ff1fb94 Imported functions in main.py and added a loop for the output
37445e8 Completed all business rules, loops, and constants
285e3d0 set up project structure, .gitignore, and virtualenvironment

At this point, there is 5 commits in my repository history.