from logic_utils import check_guess


def _normalize_result(result):
    if isinstance(result, tuple):
        return result
    return result, None


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = _normalize_result(check_guess(50, 50))
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = _normalize_result(check_guess(60, 50))
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = _normalize_result(check_guess(40, 50))
    assert outcome == "Too Low"


def test_high_guess_is_classified_correctly_after_hint_fix():
    outcome, _ = _normalize_result(check_guess(75, 50))
    assert outcome == "Too High"


def test_low_guess_is_classified_correctly_after_hint_fix():
    outcome, _ = _normalize_result(check_guess(25, 50))
    assert outcome == "Too Low"


def test_adjacent_high_guess_still_returns_too_high():
    outcome, _ = _normalize_result(check_guess(51, 50))
    assert outcome == "Too High"


def test_adjacent_low_guess_still_returns_too_low():
    outcome, _ = _normalize_result(check_guess(49, 50))
    assert outcome == "Too Low"


def test_too_high_returns_lower_hint_when_message_exists():
    outcome, message = _normalize_result(check_guess(60, 50))
    assert outcome == "Too High"
    if message is not None:
        assert message == "📉 Go LOWER!"


def test_too_low_returns_higher_hint_when_message_exists():
    outcome, message = _normalize_result(check_guess(40, 50))
    assert outcome == "Too Low"
    if message is not None:
        assert message == "📈 Go HIGHER!"
