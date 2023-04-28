from search import search_binary

def test_binary_search():
    # тест на пустой
    assert search_binary([], 0) == None

    # тест на один элемент
    assert search_binary([1], 1) == 0
    assert search_binary([1], 0) == None

    # тест на несколько элементов
    assert search_binary([1, 2, 3, 4, 5], 3) == 2
    assert search_binary([1, 2, 3, 4, 5], 6) == None
    assert search_binary([1, 2, 3, 4, 5], 0) == None
