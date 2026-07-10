from src.telecom_tax import calculate_total_with_taxes


def test_calculate_total_with_taxes_adds_correct_percentage():
    result = calculate_total_with_taxes(100)
    assert result == 127.5