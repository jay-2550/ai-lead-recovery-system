
from datetime import date


def needs_followup(lead, today=None):
    """Return whether a lead needs a follow-up review."""

    if today is None:
        today = date.today()

    # Never contact leads who opted out.
    if lead.get("consent_status", "").strip().lower() != "yes":
        return False

    status = lead.get("status", "").strip().lower()

    if status in {"won", "lost", "closed", "do not contact"}:
        return False

    next_date = lead.get("next_followup_date", "").strip()

    if not next_date:
        return False

    try:
        due_date = date.fromisoformat(next_date)
    except ValueError:
        return False

    return due_date <= today


if __name__ == "__main__":
    sample = {
        "lead_id": "L001",
        "status": "Contacted",
        "next_followup_date": "2026-10-27",
        "consent_status": "Yes",
    }

    print("Needs follow-up review:", needs_followup(sample))
