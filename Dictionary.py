# """Перевод чисел"""
# numer = {'one': 'один', 'two': 'два', 'three':'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь','nine': 'девять', 'ten': 'десять' }
# def num_translate (x):
#     result = numer.get(x)
#     return result
# num_en = input()
# print(num_translate(num_en))


# """ Перевод чисел с учетом регистра"""
# numer = {'one': 'один', 'two': 'два', 'three':'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь','nine': 'девять', 'ten': 'десять' }
# def num_translate (x):
#     result = numer.get(x.lower())
#     if x[0].isupper():
#         result = result.title()
#     return result
# num_en = input()
# print(num_translate(num_en))
#
# """
# Написать функцию, принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы
# """
# names = (input().split())
# def thesaurus(nm):
#     thes = {}
#     thes_ = {}
#     for i in nm:
#         i0 = str(i[0])
#         name_ = []
#         if i0 in thes:
#             name_.extend(thes[i0])
#             name_.append(i)
#         else:
#             name_ = i.split()
#         thes_ = {i0:name_}
#         thes.update(thes_)
#     return thes
# a = thesaurus(names)
# print('thes=', a)
#
# """
# Написать функцию, принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь,
# в котором ключи — первые буквы фамилий, а значения — словари,
# реализованные по схеме предыдущего задания и содержащие записи,
# в которых фамилия начинается с соответствующей буквы
# """
# names = ['Inan Sergeev', 'Inna Serova', 'Petr Alekseev', 'Ilya Ivanov', 'Anna Saveleva']
# def thesaurus_adv(nm):
#     global_thes = {}
#     for i in nm:
#         thes = {}
#         thes_ = {}
#         i0 = str(i[0][0])
#         i1 = str(i.split()[1][0])
#         name_ = []
#         if i1 in global_thes:
#             thes = global_thes[i1]
#             if i0 in thes:
#                 name_.extend(thes[i0])
#                 name_.append(i)
#             else:
#                 name_ = i.split(',')
#             thes_ = {i0:name_}
#             thes.update(thes_)
#             thes_ = {i1:thes}
#             global_thes.update(thes_)
#         else:
#             name_ = i.split(',')
#             thes = {i0:name_}
#             thes_ = {i1:thes}
#             global_thes.update(thes_)
#     return global_thes
#
# a = thesaurus_adv(names)
# print('thes=', a)

# """
# Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого)
# """
# n = int(input())
# nouns = ['auto', 'fors', 'fire', 'sity', 'home']
# adverbs = ['today', 'yesteray','tomorrow', 'day', 'night']
# adjectives = ['green', 'red', 'hot', 'yellow', 'blue']
# def shut(n):
#     hoho = []
#     for i in range(n):
#         word_=[]
#         import random
#         a = random.choice(nouns)
#         b = random.choice(adverbs)
#         c = random.choice(adjectives)
#         word_.append(a)
#         word_.append(b)
#         word_.append(c)
#         hoho.append(' '.join(word_))
#     return hoho
# joke = shut(n)
# print(joke)

"""
Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого),
но без повторного использования слов, если стоит такой флажок (y)
"""
n = int(input())
rul = str(input())
nouns = ['auto', 'fors', 'fire', 'sity', 'home']
adverbs = ['today', 'yesteray','tomorrow', 'day', 'night']
adjectives = ['green', 'red', 'hot', 'yellow', 'blue']
def shut(n,rul):
    import random
    hoho = []
    for i in range(n):
        word_=[]
        a = random.choice(nouns)
        if rul == 'y':
            nouns.remove(a)
        b = random.choice(adverbs)
        c = random.choice(adjectives)
        word_.append(a)
        word_.append(b)
        word_.append(c)
        hoho.append(' '.join(word_))
    return hoho
joke = shut(n,rul)
print(joke)
