
# def remove_duplicates():
#     names = ["lenin", "arun", "kumar", "lenin","arun", "suresh", "kumar", "lenin", "arun", "kumar"]
#     unique =[]
#     for i in names:
#      if i not in unique:
#          unique.append(i)
#     return unique

# def main():
#      result=remove_duplicates()
#      print("the unique names are:",result)
# main()

names = ["lenin", "arun", "kumar", "lenin","arun", "suresh", "kumar", "lenin", "arun", "kumar"]

length_names = len(names)
print(length_names)

def remove_duplicates():
    unique_names = []
    for name in names:
        print("\n")
        print("Unique names:", unique_names)
        if name  in unique_names:
             print(f"The name {name} is already in the list")
        else:
            unique_names.append(name)
           
    print("\n")
    print(unique_names)

remove_duplicates()


def remove_duplicates_using_set():
    unique_names = set(names)
    print(unique_names)


remove_duplicates_using_set()