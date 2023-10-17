dico = {
  "Alice" : ["Bob", "Dominique"],
  "Bob" : ["Alice", "Charlie", "Dominique"],
  "Charlie" : ["Bob"],
  "Dominique" : ["Alice", "Bob"]
}

def test_create_network():
    assert create_network(["Alice", "Bob", "Alice", "Charlie", "Bob", "Denis"]) == 
    {'Alice': ['Bob', 'Charlie'],'Bob': ['Alice', 'Denis'],'Charlie': ['Alice'],'Denis': ['Bob']}

    assert create_network(["Bob","Charlie","Bob","Denis","Denis","Francois"]) == {'Bob': ['Charlie', 'Denis'],'Charlie': ['Bob'],'Denis': ['Bob', 'Francois'],'Francois': ['Denis']}
    print("test Ok")

def test_are_friends():
    assert are_friends(dico, "Mahamadou", "Jelain") == False
    assert are_friends(dico, "Bob", "Dominique") == True
    assert are_friends(dico, "Alice", "Charlie") == False
    print("test Ok")

def test_all_his_friends():
    assert all_his_friends(dico, 'Alice', ["Bob", 'Dominique']) == True
    assert all_his_friends(dico, 'Bob', ["Alice", 'Dominique',"Charlie"]) == True
    assert all_his_friends(dico, 'Alice', ["Charlie", 'Dominique']) == False
    print("test Ok")

def test_is_a_community():
    assert is_a_community(dico, ['Alice','Bob','Dominique']) == True
    assert is_a_community(dico, ['Charlie','Dominique']) == False
    assert is_a_community(dico, ['Dominique','Jelian']) == False
    print("test Ok")

def test_find_community():
    assert find_community(dico,["Alice", "Bob", "Charlie", "Dominique"]) == ['Alice', 'Bob', 'Dominique']
    assert find_community(dico,["Charlie", "Alice", "Bob", "Dominique"]) == ["Charlie", "Bob"]
    assert find_community(dico,["Charlie", "Alice", "Dominique"]) == ['Charlie']
    print("test Ok")
 
def test_order_by_decreasing_popularity():
    assert order_by_decreasing_popularity(dico2, ["Alice", "Bob", "Charlie"]) == ['Bob', 'Alice', 'Charlie']
    assert order_by_decreasing_popularity(dico2, ["Bob", "Charlie","Dominique"]) == ['Bob', 'Dominique', 'Charlie']
    print("test Ok")

def test_find_community_from_person():
    find_community_from_person(dico, "Charlie") == ['Charlie', 'Bob']
    find_community_from_person(dico, "Alice") == ['Alice', 'Bob', 'Dominique']
    print("test Ok")

def test_find_max_community():
    assert find_max_community(dico) == ['Dominique', 'Bob', 'Alice']
    print("test Ok")
