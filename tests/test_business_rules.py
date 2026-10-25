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
