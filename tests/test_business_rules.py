from business_rules import (
    calculate_job_total,
    calculate_print_cost,
    format_job_line,
    get_volume_discount,
    largest_job,
    needs_overnight_run,
    requires_proof,
    total_invoiced,
)


# Rule 1: Calculate print cost
def test_calculate_print_cost_standard():
    assert calculate_print_cost(0.25, 100) == 25.0


def test_calculate_print_cost_zero_copies():
    assert calculate_print_cost(1.50, 0) == 0.0


# Rule 2 & 3: Get volume & student discount
def test_discount_under_200_copies():
    assert get_volume_discount(199, False) == 0.0


def test_discount_under_200_copies_student():
    assert get_volume_discount(199, True) == 0.0


def test_discount_at_200_copies():
    assert get_volume_discount(200, False) == 0.08


def test_discount_at_200_copies_student():
    assert get_volume_discount(200, True) == 0.13


def test_discount_at_999_copies():
    assert get_volume_discount(999, False) == 0.08


def test_discount_at_1000_copies():
    assert get_volume_discount(1000, False) == 0.15


def test_discount_at_1000_copies_student():
    assert get_volume_discount(1000, True) == 0.20


# Rule 4: Calculate job total
def test_job_total_with_setup_fee():
    # 100 * 0.25 = $25.00 -> under $40, so add $15 fee = $40.00
    assert calculate_job_total(0.25, 100, False) == 40.00


def test_job_total_at_39_99_adds_fee():
    # Under $40 by 1 cent -> 39.99 + 15 = 54.99
    assert calculate_job_total(39.99, 1, False) == 54.99


def test_job_total_at_exact_40_no_fee():
    # Exactly $40.00 does NOT get the $15 setup fee
    assert calculate_job_total(0.40, 100, False) == 40.00


def test_job_total_above_40_no_fee():
    # 150 * 0.50 = 75.00 (no discount under 200) -> $75.00
    assert calculate_job_total(0.50, 150, True) == 75.00


# Rule 5: Requires proof
def test_requires_proof_at_300():
    assert requires_proof(300.00) is False


def test_requires_proof_over_300():
    assert requires_proof(300.01) is True


# Rule 6: Needs overnight run
def test_needs_overnight_run_copies_over_500():
    assert needs_overnight_run(501, 50.00) is True


def test_needs_overnight_run_total_over_400():
    assert needs_overnight_run(100, 400.01) is True


def test_needs_overnight_run_at_limits():
    assert needs_overnight_run(500, 400.00) is False


# Rule 7 and 8: Job formatting & total invoiced


def test_total_invoiced():
    jobs = [
        {"title": "Flyers", "copy_price": 0.25, "copies": 100, "student_org": False},
        {"title": "Menus", "copy_price": 0.50, "copies": 150, "student_org": True},
    ]
    assert total_invoiced(jobs) == 115.00

    def test_largest_job():
        jobs = [
            {
                "title": "Flyers",
                "copy_price": 0.25,
                "copies": 100,
                "student_org": False,
            },
            {"title": "Menus", "copy_price": 0.50, "copies": 150, "student_org": True},
        ]
        assert largest_job(jobs) == "Menus"


def test_largest_job_empty():
    assert largest_job([]) == ""


def test_largest_job_tie():
    jobs = [
        {"title": "Flyers", "copy_price": 1.00, "copies": 100, "student_org": False},
        {"title": "Menus", "copy_price": 1.00, "copies": 100, "student_org": False},
    ]
    assert largest_job(jobs) == "Flyers"


def test_format_job_line():
    line = format_job_line("Flyers", 40.00, False, False)
    assert line == "Flyers: $40.00 | proof: no | overnight run: no"


def test_format_job_line_yes_flags():
    line = format_job_line("Catalogs", 680.00, True, True)
    assert line == "Catalogs: $680.00 | proof: yes | overnight run: yes"
