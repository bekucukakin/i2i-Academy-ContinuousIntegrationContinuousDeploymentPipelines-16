SPECIAL_COMMUNICATION_TAX_RATE = 0.075
VALUE_ADDED_TAX_RATE = 0.20


def calculate_total_with_taxes(amount: float) -> float:
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    total_rate = 1 + SPECIAL_COMMUNICATION_TAX_RATE + VALUE_ADDED_TAX_RATE
    return round(amount * total_rate, 2)