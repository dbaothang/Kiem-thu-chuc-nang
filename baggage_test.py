from main import baggage_fee

# Bảng quyết định
def test_decision_table():
    # Trọng lượng < 0, chiều dài khác nhau
    assert baggage_fee(-5, -10) == "Invalid" 
    assert baggage_fee(-5, 0) == "Invalid"   
    assert baggage_fee(-5, 50) == "Invalid" 
    assert baggage_fee(-5, 150) == "Invalid"  
    assert baggage_fee(-5, 250) == "Invalid"  

    # Trọng lượng = 0, chiều dài khác nhau
    assert baggage_fee(0, -10) == "Invalid"  
    assert baggage_fee(0, 0) == 0    
    assert baggage_fee(0, 50) == 0   
    assert baggage_fee(0, 150) == 0  
    assert baggage_fee(0, 250) == "Invalid"  

    # Trọng lượng 0 < weight <= 20, chiều dài khác nhau
    assert baggage_fee(15, -10) == "Invalid"  
    assert baggage_fee(15, 0) == 0   
    assert baggage_fee(15, 50) == 0  
    assert baggage_fee(15, 150) == 10  
    assert baggage_fee(15, 250) == "Invalid"  

    # Trọng lượng 20 < weight <= 50, chiều dài khác nhau
    assert baggage_fee(40, -10) == "Invalid" 
    assert baggage_fee(40, 0) == 0   
    assert baggage_fee(40, 50) == 20  
    assert baggage_fee(40, 150) == 30  
    assert baggage_fee(40, 250) == "Invalid"  

    # Trọng lượng > 50, chiều dài khác nhau
    assert baggage_fee(55, -10) == "Invalid"  
    assert baggage_fee(55, 0) == "Invalid"  
    assert baggage_fee(55, 50) == "Invalid"  
    assert baggage_fee(55, 150) == "Invalid" 
    assert baggage_fee(55, 250) == "Invalid"  


# Kiểm thử biên mạnh
def test_boundary_values():
    # hai giá tri normal
    assert baggage_fee(25, 100) == 20

    # giữ nguyên normal length
    assert baggage_fee(-1, 100) == "Invalid"
    assert baggage_fee(0, 100) == 0
    assert baggage_fee(1, 100) == 0
    assert baggage_fee(49, 100) == 20
    assert baggage_fee(50, 100) == 20
    assert baggage_fee(51, 100) == "Invalid"

    # giữ nguyên normal weight
    assert baggage_fee(25, -1) == "Invalid"
    assert baggage_fee(25, 0) == 0
    assert baggage_fee(25, 1) == 20
    assert baggage_fee(25, 199) == 30
    assert baggage_fee(25, 200) == 30
    assert baggage_fee(25, 201) == "Invalid"

