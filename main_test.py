
def test_time_until_function_exists():
    from main import time_until
    assert callable(time_until), "The 'time_until' function is not implemented."