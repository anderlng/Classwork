# Directions:
# You will use set.intersection(set2), set.union(set2), and/or set.difference(set2) to answer the following:
# 1. What is the print out of the union of Sergio and Anderling?
# 2. What is the print out of the difference between Jessellyz and Samaya?
# 3. What is the print out of the intersection of DruKiel and Santiago?
# 4. Who has the first name that matches the most of the letters in your name?
# 5. Who has the first name that matches the least of the letters in your name?
# HINT for 4 and 5. You can write 14 lines of code or 2 to answer 4 and 5.
# You may use your notes and vocabulary web page. Nothing else from the web.

def main():
    Abdullahi = {'A', 'b', 'd', 'u', 'l', 'l', 'a', 'h', 'i'}
    Mustafa = {'M', 'u', 's', 't', 'a', 'f', 'a'}
    Sergio = {'S', 'e', 'r', 'g', 'i', 'o'}
    Robert = {'R', 'o', 'b', 'e', 'r', 't'}
    Yonatan = {'Y', 'o', 'n', 'a', 't', 'a', 'n'}
    Santiago = {'S', 'a', 'n', 't', 'i', 'a', 'g', 'o'}
    Jose_Gabriel = {'J', 'o', 's', 'e', ' ', 'G', 'a', 'b', 'r', 'i', 'e', 'l'}
    Yofreilin = {'Y', 'o', 'f', 'r', 'e', 'i', 'l', 'i', 'n'}
    Jessellyz = {'J', 'e', 's', 's', 'e', 'l', 'l', 'y', 'z'}
    Ismael = {'I', 's', 'm', 'a', 'e', 'l'}
    Anderling = {'A', 'n', 'd', 'e', 'r', 'l', 'i', 'n', 'g'}
    Juan = {'J', 'u', 'a', 'n'}
    Jonatan = {'J', 'o', 'n', 'a', 't', 'a', 'n'}
    Samayah = {'S', 'a', 'm', 'a', 'y', 'a', 'h'}
    DruKiel = {'D', 'r', 'u', 'K', 'i', 'e', 'l'}
    names = [Abdullahi, Mustafa, Sergio, Robert, Yonatan, Santiago, Jose_Gabriel, Yofreilin ,Jessellyz, Ismael, Anderling, Juan, Jonatan, Samayah, DruKiel]
    print(Sergio.union(Anderling))
    print(Jessellyz.difference(Samayah))
    print(DruKiel.intersection(Santiago))
    print(Anderling.intersection(Abdullahi))
    print(Anderling.intersection(Mustafa))
    print(Anderling.intersection(Sergio))
    print(Anderling.intersection(Robert))
    print(Anderling.intersection(Yonatan))
    print(Anderling.intersection(Santiago))
    print(Anderling.intersection(Jose_Gabriel))
    print(Anderling.intersection(Yofreilin))
    print(Anderling.intersection(Jessellyz))
    print(Anderling.intersection(Ismael))
    print(Anderling.intersection(Juan))
    print(Anderling.intersection(Jonatan))
    print(Anderling.intersection(Samayah))
    print(Anderling.intersection(DruKiel))


if __name__ == "__main__":
    main()
