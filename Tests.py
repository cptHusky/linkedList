import pytest
from LinkedList import LinkedList, GreatLinkedList

def test_init():
    ll = LinkedList()
    assert ll.head == None
    assert ll.length == 0

def test_len():
    ll = LinkedList()
    assert len(ll) == 0
    ll.append(1)
    assert len(ll) == 1
    ll.append(2)
    assert len(ll) == 2
    ll.append(3)
    assert len(ll) == 3
    ll.prepend(0)
    assert len(ll) == 4
    ll.delete_node(2)
    assert len(ll) == 3

def test_append():
    ll = LinkedList()
    ll.append(1)
    assert ll.head.data == 1
    ll.append(2)
    assert ll.head.next.data == 2
    ll.append(3, after=2)
    assert ll.head.next.next.data == 3
    with pytest.raises(ValueError):
        ll.append(4, after=5)

def test_prepend():
    ll = LinkedList()
    ll.prepend(1)
    assert ll.head.data == 1
    ll.prepend(2)
    assert ll.head.data == 2
    assert ll.head.next.data == 1
    ll.prepend(3)
    assert ll.head.data == 3
    assert ll.head.next.data == 2
    assert ll.head.next.next.data == 1

def test_delete_node():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.delete_node(1)
    assert ll.head.next.data == 3
    ll.delete_node(0)
    assert ll.head.data == 3
    ll.delete_node(0)
    assert ll.head == None
    with pytest.raises(IndexError):
        ll.delete_node(0)

def test_getitem():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll[0] == 1
    assert ll[1] == 2
    assert ll[2] == 3
    with pytest.raises(IndexError):
        ll[3]

def test_iter():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert list(iter(ll)) == [1, 2, 3]

def test_comparison():
    gll1 = GreatLinkedList()
    gll2 = GreatLinkedList()
    assert gll1 == gll2
    assert not gll1 != gll2
    assert gll1 >= gll2
    assert gll1 <= gll2

    gll1.append(1)
    assert gll1 >= gll2
    assert not gll2 >= gll1
    assert gll2 <= gll1
    assert not gll1 <= gll2
    assert gll1 > gll2
    assert gll2 < gll1
    assert gll1 != gll2
    assert gll2 != gll1 

    gll2.append(2)
    assert gll1 == gll2 #1-2
    assert not gll1 > gll2
    assert not gll2 > gll1
    assert gll1 >= gll2
    assert gll2 >= gll1

    gll1.append(3)
    assert gll1 != gll2
    assert gll1 > gll2
    assert gll2 < gll1
    assert gll1 >= gll2
    assert gll2 <= gll1

def test_is_the_same_type():
    assert LinkedList.is_the_same_type(LinkedList())
    assert GreatLinkedList.is_the_same_type(GreatLinkedList())
    assert LinkedList().is_the_same_type(GreatLinkedList())
    assert not GreatLinkedList().is_the_same_type(LinkedList())

def test_find():
    gll = GreatLinkedList()
    assert gll.find() == None
    with pytest.raises(ValueError):
        gll.find(1)
    gll.append(1)
    gll.append(2)
    gll.append(3)
    assert gll.find(1) == 0
    assert gll.find(2) == 1
    assert gll.find(3) == 2
    with pytest.raises(ValueError):
        gll.find(4)
    gll.append(1)
    assert gll.find(1) == 0
