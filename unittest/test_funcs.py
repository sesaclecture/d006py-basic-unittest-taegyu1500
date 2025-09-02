# TODO: 사용자 모듈 import
from base_funcs import even_odd, average, max_list, min_list

# TODO: 아래의 코드를 삭제하고 unittest를 작성하세요.
def test_even_odd():
    assert even_odd(4) == True
    assert even_odd(15) == False

def test_average():
    assert average([]) == 0
    assert average([1,2,3,4,5]) == 3

def test_max_list():
    assert max_list([1]) == 1
    assert max_list([1,2,3,4,5]) == 5
    assert max_list([1,1,2]) == 2

def test_min_list():
    assert min_list([0]) == 0
    assert min_list([1,3,5,6]) == 1
    assert min_list([0,1,2,3]) == 0
    
