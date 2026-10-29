
from datetime import date

from src.recovery_rules import needs_followup


def test_overdue_lead_needs_review():
    lead = {
        "status": "Contacted",
        "next_followup_date": "2026-10-27",
        "consent_status": "Yes",
    }
    assert needs_followup(lead, date(2026, 10, 29)) is True


def test_future_followup_does_not_need_review():
    lead = {
        "status": "New",
        "next_followup_date": "2026-10-31",
        "consent_status": "Yes",
    }
    assert needs_followup(lead, date(2026, 10, 29)) is False


def test_opted_out_lead_is_excluded():
    lead = {
        "status": "No response",
        "next_followup_date": "2026-10-27",
        "consent_status": "No",
    }
    assert needs_followup(lead, date(2026, 10, 29)) is False


def test_invalid_date_is_excluded():
    lead = {
        "status": "Contacted",
        "next_followup_date": "not-a-date",
        "consent_status": "Yes",
    }
    assert needs_followup(lead, date(2026, 10, 29)) is False
