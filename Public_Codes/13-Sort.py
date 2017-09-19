list2 = ['eat', 'ate', 'tea', 'sea', 'ease', 'see']
list3 = [43, 65, 20, 1, 79, 0.23, 102, 4]
print("list2 before sort = ",list2)
print("list3 before sort = ",list3)
list2.sort()
list3.sort()
print("list2 after sort = ",list2)
print("list3 after sort = ",list3)

print("---------------------------------------")
originalList = ["Narges", "Reza", "Saeed", "Puya", "Marjan", "Saeedeh"]
newList = originalList[:]
print("originalList before sort = ",newList)
newList.sort(reverse=True)
print("originalList after sort = ",newList)

print("\n---------------------------------------without changing original linst")
newer = sorted(originalList)
print("originalList before sort = ",originalList)
print("originalList after sort = ",newer)

print("---------------------------------------")

