#tuple is a collection of heterogeneous data types like list, but tuple is immutable whereas list is mutable

tuple1=(1,2,3)
print(tuple1)
print(tuple1[1])

for n in tuple1:
    print(n)
print("MAX", max(tuple1))
print("MIN", min(tuple1))
print("SUM", sum(tuple1))
print("Length", len(tuple1))