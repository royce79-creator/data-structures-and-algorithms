from code_challenges.selection_sort.selection_sort import selection_sort

def test_import():
    assert selection_sort

def test_selection_sort():
    list = [2,7,4,6,1]
    selection_sort(list)
    assert list == [1,2,4,6,7]

def test_selection_sort2():
    list = [10,8,6,4,2,0]
    selection_sort(list)
    assert list == [0,2,4,6,8,10]

def test_selection_sort3():
    list = [1,1,1,1,0,0,0,0,3,3,3,3,2,2,2,2]
    selection_sort(list)
    assert list == [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3]
