def combine_lists(list1, list2):
    list1.reverse()
    list2.extend(list1)
    return list2


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))
print(Jamies_list)