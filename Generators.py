# def gen_odd(n):
#     for num in range(1, n + 1, 2):
#         yield num
#
# odd = gen_odd(10)
# # print(next(odd))
# # print(next(odd))
# # print(next(odd))
# # print(next(odd))
# # # print(next(odd))
# # # print(next(odd))
# for i in odd:
#     print(i)


# print('input N')
# n = int(input())
# gen_odd = (num for num in range(1, n + 1, 2))
# for i in gen_odd:
#     print(i)

# from itertools import zip_longest
# tutors = ['Иван,Ivan,Ivan', 'Анастасия,Nastya, Nastya', 'Петр,Petr,Petr', 'Сергей,Sergey,Sergey',
#     'Дмитрий,Dima,Dima', 'Борис.Borya,Borya', 'Елена,Lena,Lena']
# klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
# tu_kl = ((tu, kl) for tu, kl in zip_longest(tutors, klasses) if tu is not None)
# for i in tu_kl:
#     print(i)

# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [i for i in src[1:] if i > src[src.index(i) - 1]]
# print(result)

# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [i for i in src if src.count(i) == 1]
# print(result)

from itertools import zip_longest
tutors = ['Иван,Ivan,Ivan', 'Анастасия,Nastya, Nastya', 'Петр,Petr,Petr', 'Сергей,Sergey,Sergey',
    'Дмитрий,Dima,Dima', 'Борис.Borya,Borya', 'Елена,Lena,Lena']
klasses = ['9А', '7В', '9Б', 'вязание,охота', '8Б', '10А']
if len(tutors) >= len(klasses):
    t_k = {}
    for tu, kl in zip_longest(tutors, klasses):
        t_k[tu] = kl
    print(t_k)
