# ISM3232 Midterm: Brightline Print Shop

- **Name:** David Leatherman
- **Version:** Python 3.14.7
- **Date:** October 25, 2026

## What This Program Does

This program calculates print job price quotes based on volume and affiliation, and flags special production requirements. It processes an inventory of pending orders, checks each job against tiered business rules, and outputs a formatted production summary for shop operations.

## Business Rules

1. **Base Print Cost:** The print cost is calculated strictly by multiplying the copy price by the number of copies ordered.
2. **Volume Discounts:** Orders between 200 and 999 copies receive an 8% discount, while orders of 1,000 or more copies receive a 15% discount. Orders under 200 copies receive no discount.
3. **Student Organization Discount:** Registered student organizations receive an extra 5 percentage points added to their volume discount, but only on jobs with 200 or more copies.
4. **Setup Fee:** A $15.00 setup fee is applied to any job whose discounted subtotal is strictly less than $40.00.
5. **Proof Approval:** Any job with a final total greater than $300.00 requires a mandatory customer proof before printing.
6. **Overnight Production Run:** Jobs exceeding 500 copies or totaling more than $400.00 require an overnight production run.

## How to Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py

## Files in This Repository

- `.gitignore`: Specifies files to keep out of Git.
- `requirements.txt`: Lists the versions including pytest and ruff.
- `business_rules.py`: Contains the eight standalone logic calculation and formatting functions.
- `main.py`: Imports the rules across sample print orders and displays the 15-line operational report.
- `commands.md`: Documents all commands, environment verification, and commit history.
- `README.md`: Provides project documentation, instructions, and testing details.
- `tests/test_business_rules.py`: Contains the unit test suite verifying pricing calculations, boundary edges, and aggregations.

## AI Use Statement

I did not use AI on this exam.