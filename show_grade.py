"""Display your Homework 1 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "42d19ebd4d8ffb56d7261cc25dd6e899"
GRADE_HASH = "e6b5d5763fbca31deb32446504cae83c1b1f90e1d4618d0d50072e555ce23446"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 1: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
