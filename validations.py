# validations.py
# Input cleaning and validation for NexoTech Solutions tickets (rule BR0),
# plus the check for yes/no answers typed by the user.
#
# AI disclosure (PUCPR Resolution 274/2024): During the preparation of this code,
# the author(s) used Claude (Anthropic, model claude-opus-5) to draft the cleaning
# and validation functions from the team's business rule BR0, and the yes/no
# input check added for the keyboard ticket entry (AI log Entry 020). After using
# this tool, the author(s) reviewed and edited the content as needed and take
# full responsibility for the content.


def clean_text(value):
    """Return the value in lowercase, without surrounding spaces (BR0).

    A missing value (None) becomes empty text, so the business rules
    never receive None and can always compare text with text.
    """
    if value is None:
        return ""
    # str() protects against a number typed into a text field
    return str(value).strip().lower()


def is_missing(value):
    """Return True when a field has no usable content (None, empty or only spaces)."""
    return clean_text(value) == ""


def ask_yes_or_no(question):
    """Ask a yes/no question until the answer is valid. Return True for "yes".

    The answer is cleaned first, so "YES", "Yes " and "yes" are all accepted.
    """
    answer = clean_text(input(question))
    # Keep asking until the user types yes or no, so the program never guesses
    while answer != "yes" and answer != "no":
        print("Please answer yes or no.")
        answer = clean_text(input(question))
    return answer == "yes"
