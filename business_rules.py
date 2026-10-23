DISCOUNT_TIER_1_MIN_COPIES = 200
DISCOUNT_TIER_2_MIN_COPIES = 1000

DISCOUNT_RATE_TIER_1 = 0.08
DISCOUNT_RATE_TIER_2 = 0.15
STUDENT_ORG_ADDITIONAL_DISCOUNT = 0.05

SETUP_FEE_THRESHOLD = 40.0
SETUP_FEE_AMOUNT = 15.0

PROOF_THRESHOLD = 300.0
OVERNIGHT_COPIES_THRESHOLD = 500
OVERNIGHT_TOTAL_THRESHOLD = 400.0


def calculate_print_cost(copy_price: float, copies: int) -> float:
    return copy_price * copies


def get_volume_discount(copies: int, student_org: bool = False) -> float:
    if copies < DISCOUNT_TIER_1_MIN_COPIES:
        return 0.0

    if copies >= DISCOUNT_TIER_2_MIN_COPIES:
        base_rate = DISCOUNT_RATE_TIER_2
    else:
        base_rate = DISCOUNT_RATE_TIER_1

    if student_org:
        return base_rate + STUDENT_ORG_ADDITIONAL_DISCOUNT

    return base_rate


def calculate_job_total(
    copy_price: float, copies: int, student_org: bool = False
) -> float:
    raw_cost = calculate_print_cost(copy_price, copies)
    discount_rate = get_volume_discount(copies, student_org)
    discounted_cost = raw_cost * (1.0 - discount_rate)

    if discounted_cost < SETUP_FEE_THRESHOLD:
        return round(discounted_cost + SETUP_FEE_AMOUNT, 2)

    return round(discounted_cost, 2)


def requires_proof(total: float) -> bool:
    return total > PROOF_THRESHOLD


def needs_overnight_run(copies: int, total: float) -> bool:
    return copies > OVERNIGHT_COPIES_THRESHOLD or total > OVERNIGHT_TOTAL_THRESHOLD


def total_invoiced(jobs: list) -> float:
    running_total = 0.0
    for job in jobs:
        job_total = calculate_job_total(
            job["copy_price"], job["copies"], job["student_org"]
        )
        running_total += job_total
    return round(running_total, 2)


def largest_job(jobs: list) -> str:
    if not jobs:
        return ""

    highest_title = ""
    highest_total = -1.0

    for job in jobs:
        job_total = calculate_job_total(
            job["copy_price"], job["copies"], job["student_org"]
        )
        if job_total > highest_total:
            highest_total = job_total
            highest_title = job["title"]

    return highest_title


def format_job_line(title: str, total: float, proof: bool, overnight_run: bool) -> str:
    proof_str = "yes" if proof else "no"
    overnight_str = "yes" if overnight_run else "no"
    return (
        f"{title}: ${total:.2f} | proof: {proof_str} | overnight run: {overnight_str}"
    )
