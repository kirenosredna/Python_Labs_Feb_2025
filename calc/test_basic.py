from calc import basic

def test_add():
    assert basic.add(4, 3) == 7, "Should be 7"
    assert basic.add(4, 3, 2) == 9, "Should be 9"

def test_mul():
    assert basic.mul(4, 3) == 7, "Should be 7"
    assert basic.mul(4, 3, 2) == 24, "Should be 24"

def main():
    print("Starting tests")
    test_add()
    test_mul()
    print("All success")

if __name__ == "__main__":
    main()