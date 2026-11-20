
# ==========================================
# QA-Mission - Grades and Absence System
# ==========================================

!pip install -q pytest ruff mypy

# 1. Create grades.py
grades_code = '''
PASS_MARK = 50

def is_pass(score: int) -> bool:
    return score >= PASS_MARK

def result(score: int) -> str:
    if is_pass(score):
        return "Pass"
    return "Fail"
'''

with open("grades.py", "w") as f:
    f.write(grades_code)


# 2. Create test_grades.py
test_grades_code = '''
import pytest
from grades import is_pass, result

@pytest.mark.parametrize(
    "score, expected",
    [(90, True), (70, True), (20, False), (50, True)]
)
def test_is_pass(score, expected):
    assert is_pass(score) == expected

def test_result_pass():
    assert result(90) == "Pass"

def test_result_fail():
    assert result(20) == "Fail"
'''

with open("test_grades.py", "w") as f:
    f.write(test_grades_code)


# 3. Create absence.py
absence_code = '''
MAX_ABSENCES = 5

def can_sit_exam(absences: int) -> bool:
    return absences <= MAX_ABSENCES

def status(absences: int) -> str:
    if can_sit_exam(absences):
        return "Allowed"
    return "Blocked"
'''

with open("absence.py", "w") as f:
    f.write(absence_code)


# 4. Create test_absence.py
test_absence_code = '''
import pytest
from absence import can_sit_exam, status

@pytest.mark.parametrize(
    "absences, expected",
    [(0, True), (5, True), (9, False)]
)
def test_can_sit_exam(absences, expected):
    assert can_sit_exam(absences) == expected

def test_status_allowed():
    assert status(3) == "Allowed"

def test_status_blocked():
    assert status(9) == "Blocked"
'''

with open("test_absence.py", "w") as f:
    f.write(test_absence_code)


# 5. Run tests
!pytest -v

# 6. Format and check code
!ruff format grades.py test_grades.py absence.py test_absence.py
!ruff check grades.py test_grades.py absence.py test_absence.py

# 7. Type checking
!mypy grades.py absence.py

# 8. Create ZIP file
import zipfile

files = [
    "grades.py",
    "test_grades.py",
    "absence.py",
    "test_absence.py"
]

with zipfile.ZipFile("QA_Mission.zip", "w") as z:
    for file in files:
        z.write(file)

# 9. Verify ZIP file
with zipfile.ZipFile("QA_Mission.zip", "r") as z:
    print("ZIP file is OK")
    print(z.namelist())

# 10. Download project
from google.colab import files
files.download("QA_Mission.zip")
