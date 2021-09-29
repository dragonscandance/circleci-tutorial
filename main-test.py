from main import add

def TestAdd():
    assert add(2,3) == 5
    assert add(5,5) == 11
    print("Function works!")

if __name__ == "__main__":
    TestAdd()