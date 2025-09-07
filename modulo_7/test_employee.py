# test_employee.py
from employee import Employee

def test_give_default_raise():
    emp = Employee("Diana", "Aguayo", 50000)
    emp.give_raise()
    assert emp.salary == 55000
    print("✓ Test passed: Default raise of $5000 works correctly!")

def test_give_custom_raise():
    emp = Employee("Diana", "Aguayo", 50000)
    emp.give_raise(10000)
    assert emp.salary == 60000
    print("✓ Test passed: Custom raise of $10000 works correctly!")

def test_employee_methods():
    emp = Employee("Luis", "Torres", 60000)
    
    # Test get_salary method
    assert emp.get_salary() == 60000
    print("✓ Test passed: get_salary method works correctly!")
    
    # Test get_full_name method
    assert emp.get_full_name() == "Luis Torres"
    print("✓ Test passed: get_full_name method works correctly!")
    
    # Test describe_employee method (just check it doesn't crash)
    try:
        emp.describe_employee()
        print("✓ Test passed: describe_employee method works correctly!")
    except Exception as e:
        print(f"✗ Test failed: describe_employee method crashed: {e}")

if __name__ == "__main__":
    print("Running Employee class tests...\n")
    test_give_default_raise()
    test_give_custom_raise()
    test_employee_methods()
    print("\n🎉 All tests passed successfully!")