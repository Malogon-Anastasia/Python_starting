# text = "Hello "
# num = 5.5
# isTrue = True
# lst = [4, 3, True, "hello world", -1]
# bts = bytes(5)

# print(bts)


# a = 5
# b = 7

# if b > a:
#     print("B is bigger")
# elif a > b:
#     print("A is bigger")
# else:
#     print("They are sharp")


# a = 0
# while a < 5:
#     if a == 3:
#         break
#     print(a)
#     a += 1


# lst = [5, 4.6, "hello world", -2, False, 7, 0]

# for item in lst:
#     print(item)

# for item in range(2, 5):
#     print(item)

# def sum(a, b):
#     print(a + b)


# sum(2, 4)

# списки:

# lst = [5, 6, "hello world", True, 0, -3.5]
# lst[1:3] = [1, 2, 3, 4, 5]
# lst.insert(2, "hello")
# lst.append(False)
# lst1 = [1, 2, 3, 4, 5]
# lst1.extend(lst)
# lst.remove("hello world")
# lst.pop(1)

# for item in lst:
#     print(item)

# print(len(lst))

# lst = [5, 6, 0, -3.5]
# lst.sort()
# lst1 = lst.copy()
# lst1[0] = "IT"
# print(lst1)

# кортеж
# tpl = ("MACOS", "LINUX", "WIN")
# (work, home, friend) = tpl
# print(work)

# зміна кортежу
# lst = list(tpl)
# lst.append("SOLARIS")
# tpl = tuple(lst)
# print(tpl)


# сет - виключаються всі дублікати:
# st = {"macos", "linux", "linux", "win", "macos", "linux"}
# st.add("solaris")
# st.remove("win")
# st.discard("win") - видаляються тільки якщо є такий ключ
# print(st)
# print("macos" in st)

# словник - це набір ключ/значення
dict = {
    "HDD": "4TB",
    "CPU": "INTEL",
    "RAM": "8G",
    "OWNER": "NASTYA"
}
dict["HDD"] = "8TB"
dict["YEAR"] = "2023"
# dict.pop("CPU") - видалення ключа

for key in dict.keys():
    print(key)
