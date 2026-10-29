# AI Lead Recovery System

An automation project that identifies overdue customer follow-ups, prioritizes leads that need attention, and prepares personalized recovery messages using n8n and Python.

## Features

- Detect overdue follow-ups
- Validate lead records
- Identify duplicate and incomplete entries
- Respect contact preferences and opt-outs
- Prepare personalized follow-up drafts
- Track lead recovery status

## Technology Stack

- n8n — workflow automation
- Python — validation and business rules
- Google Sheets — lead data storage
- Ollama — optional local AI message generation

## Workflow

1. Import lead records.
2. Validate the data.
3. Identify leads requiring follow-up.
4. Generate a draft message for review.
5. Update the lead's recovery status.

## Safety

This project uses fictional sample data. Messages require human review before sending. Leads that have opted out must not receive further marketing outreach.

## Project Status

Initial development — prototype in progress.
