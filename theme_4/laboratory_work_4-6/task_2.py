# На вход программе подается список кортежей. Программа выводит новый список, содержащий только непустые кортежи.

tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = [t for t in tuples if len(t) > 0]

print(non_empty_tuples)
