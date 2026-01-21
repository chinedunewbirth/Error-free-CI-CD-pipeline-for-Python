"""
Example test file to demonstrate proper test structure
"""
import pytest


class TestExample:
    """Example test class"""
    
    def test_addition(self):
        """Test basic addition"""
        assert 1 + 1 == 2
    
    def test_subtraction(self):
        """Test basic subtraction"""
        assert 5 - 3 == 2
    
    def test_string_concatenation(self):
        """Test string operations"""
        result = "Hello" + " " + "World"
        assert result == "Hello World"
    
    @pytest.mark.parametrize("input,expected", [
        (2, 4),
        (3, 9),
        (4, 16),
        (5, 25),
    ])
    def test_square(self, input, expected):
        """Test squaring numbers with parameterization"""
        assert input ** 2 == expected


def test_list_operations():
    """Test list operations"""
    my_list = [1, 2, 3]
    my_list.append(4)
    assert len(my_list) == 4
    assert my_list[-1] == 4


def test_exception_handling():
    """Test that exceptions are raised properly"""
    with pytest.raises(ZeroDivisionError):
        _ = 1 / 0


@pytest.fixture
def sample_data():
    """Fixture providing sample data"""
    return {"name": "Test", "value": 42}


def test_with_fixture(sample_data):
    """Test using a fixture"""
    assert sample_data["name"] == "Test"
    assert sample_data["value"] == 42