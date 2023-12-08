"""
test module to test get texts and questions
"""
import pytest
from texts import get_texts
from questions import get_quetions


def test_get_texts():
    """
    test method get texts
    """
    result = get_texts()
    assert result != {}

@pytest.mark.parametrize("name", [
    "questions_cs.json",
    "questions_en.json"
])

def test_get_questions(name):
    """
    test method get questions
    """
    result = get_quetions(name)
    assert result != {}
