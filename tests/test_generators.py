from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from typing import List, Dict, Any
import pytest


@pytest.fixture()
def test_filter_by_currency(transactions: Any) -> None:
    filter_by_currency(transactions) == currency
