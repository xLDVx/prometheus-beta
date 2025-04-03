import pytest
from src.mall_navigation import MallMap

def test_add_connection():
    """Test adding connections between stores."""
    mall = MallMap()
    mall.add_connection("Apple Store", "Nike Store", 10.5)
    
    # Verify bidirectional connection
    assert "Nike Store" in mall.stores["Apple Store"]
    assert mall.stores["Apple Store"]["Nike Store"] == 10.5
    assert mall.stores["Nike Store"]["Apple Store"] == 10.5

def test_empty_store_names():
    """Test that empty store names are rejected."""
    mall = MallMap()
    
    with pytest.raises(ValueError, match="Store names cannot be empty"):
        mall.add_connection("", "Nike Store", 10.5)
    
    with pytest.raises(ValueError, match="Store names cannot be empty"):
        mall.add_connection("Apple Store", "", 10.5)

def test_negative_distance():
    """Test that negative distances are rejected."""
    mall = MallMap()
    
    with pytest.raises(ValueError, match="Distance cannot be negative"):
        mall.add_connection("Apple Store", "Nike Store", -5)

def test_shortest_path_same_store():
    """Test path finding when start and end are the same store."""
    mall = MallMap()
    mall.add_connection("Apple Store", "Nike Store", 10.5)
    
    path = mall.find_shortest_path("Apple Store", "Apple Store")
    assert path == ["Apple Store"]

def test_shortest_path_direct_connection():
    """Test finding a path with a direct connection."""
    mall = MallMap()
    mall.add_connection("Apple Store", "Nike Store", 10.5)
    
    path = mall.find_shortest_path("Apple Store", "Nike Store")
    assert path == ["Apple Store", "Nike Store"]

def test_shortest_path_multiple_stores():
    """Test finding a path through multiple stores."""
    mall = MallMap()
    mall.add_connection("Apple Store", "Nike Store", 10.5)
    mall.add_connection("Nike Store", "Starbucks", 7.2)
    mall.add_connection("Apple Store", "Starbucks", 15.7)
    
    path = mall.find_shortest_path("Apple Store", "Starbucks")
    assert path == ["Apple Store", "Nike Store", "Starbucks"]

def test_no_path_exists():
    """Test when no path exists between stores."""
    mall = MallMap()
    mall.add_connection("Apple Store", "Nike Store", 10.5)
    
    path = mall.find_shortest_path("Apple Store", "Starbucks")
    assert path is None

def test_nonexistent_store():
    """Test finding path with nonexistent stores."""
    mall = MallMap()
    mall.add_connection("Apple Store", "Nike Store", 10.5)
    
    with pytest.raises(ValueError, match="Start store 'Starbucks' does not exist"):
        mall.find_shortest_path("Starbucks", "Nike Store")
    
    with pytest.raises(ValueError, match="End store 'Starbucks' does not exist"):
        mall.find_shortest_path("Apple Store", "Starbucks")

def test_complex_path():
    """Test a more complex navigation scenario."""
    mall = MallMap()
    mall.add_connection("Apple Store", "Nike Store", 10.5)
    mall.add_connection("Nike Store", "Starbucks", 7.2)
    mall.add_connection("Starbucks", "Zara", 5.3)
    mall.add_connection("Apple Store", "Zara", 22.0)
    
    path = mall.find_shortest_path("Apple Store", "Zara")
    assert path == ["Apple Store", "Nike Store", "Starbucks", "Zara"]