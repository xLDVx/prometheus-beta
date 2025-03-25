import pytest
from src.dot_case import convert_to_dot_case

def test_basic_string_conversion():
    """Test basic string conversion to dot case."""
    assert convert_to_dot_case("hello world") == "hello.world"

def test_camel_case_conversion():
    """Test conversion of camel case strings."""
    assert convert_to_dot_case("helloWorld") == "hello.world"
    assert convert_to_dot_case("HelloWorld") == "hello.world"
    assert convert_to_dot_case("helloWorldTest") == "hello.world.test"

def test_snake_case_conversion():
    """Test conversion of snake case strings."""
    assert convert_to_dot_case("hello_world") == "hello.world"
    assert convert_to_dot_case("hello_world_test") == "hello.world.test"

def test_mixed_case_conversion():
    """Test conversion of mixed case strings."""
    assert convert_to_dot_case("Hello_world") == "hello.world"
    assert convert_to_dot_case("hello-World_test") == "hello.world.test"

def test_multiple_separators():
    """Test conversion with multiple different separators."""
    assert convert_to_dot_case("hello__world  test") == "hello.world.test"
    assert convert_to_dot_case("hello-world_test") == "hello.world.test"

def test_empty_string():
    """Test empty string conversion."""
    assert convert_to_dot_case("") == ""

def test_single_word():
    """Test single word conversion."""
    assert convert_to_dot_case("hello") == "hello"
    assert convert_to_dot_case("Hello") == "hello"

def test_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        convert_to_dot_case(None)
    with pytest.raises(TypeError):
        convert_to_dot_case(123)
    with pytest.raises(TypeError):
        convert_to_dot_case(["hello"])

def test_number_handling():
    """Test handling of strings with numbers."""
    assert convert_to_dot_case("hello2World") == "hello2.world"
    assert convert_to_dot_case("hello_world_2test") == "hello.world.2test"