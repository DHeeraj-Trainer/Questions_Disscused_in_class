# def manage_playlist(playlist, operation, song=None, another_playlist=None):

#     if operation == "add":
#         playlist.add(song)
#         return f"Song {song} added to the playlist."

#     elif operation == "remove":
#         try:
#             playlist.remove(song)
#             return f"Song {song} removed from the playlist."
#         except KeyError:
#             return f"Song {song} not found in the playlist."

#     elif operation == "discard":
#         playlist.discard(song)
#         return f"Song {song} discarded (if it existed)."

#     elif operation == "pop":
#         if playlist:
#             removed_song = playlist.pop()
#             return f"Randomly removed song: {removed_song}"
#         return "Playlist is empty."

#     elif operation == "clear":
#         playlist.clear()
#         return "Playlist cleared."

#     elif operation == "union":
#         return playlist.union(another_playlist)

#     elif operation == "intersection":
#         return playlist.intersection(another_playlist)

#     elif operation == "difference":
#         return playlist.difference(another_playlist)

#     else:
#         return "Invalid operation."


# playlist = set()

# while True:
#     print("\nOperations: add, remove, discard, pop, clear, union, intersection, difference, exit")
#     operation = input("Enter the operation you want to perform: ").lower()

#     if operation == "exit":
#         print("Exiting the playlist manager.")
#         break

#     elif operation in ["add", "remove", "discard"]:
#         song = int(input("Enter the song ID: "))
#         result = manage_playlist(playlist, operation, song)

#     elif operation in ["union", "intersection", "difference"]:
#         another_playlist = set(
#             map(int, input(
#                 "Enter another playlist as comma-separated song IDs (e.g., 101,102,103): "
#             ).split(","))
#         )
#         result = manage_playlist(
#             playlist,
#             operation,
#             another_playlist=another_playlist
#         )

#     else:
#         result = manage_playlist(playlist, operation)

#     print("\nResult:", result)
#     print("Updated Playlist:", playlist)



# def manage_catalog(catalog, operation, key=None, value=None):

#     if operation == "get":
#         return catalog.get(key, "Product ID not found.")

#     elif operation == "keys":
#         return list(catalog.keys())

#     elif operation == "values":
#         return list(catalog.values())

#     elif operation == "items":
#         return list(catalog.items())

#     elif operation == "update":
#         catalog.update({key: value})
#         return f"Product {key} updated/added successfully."

#     elif operation == "pop":
#         return catalog.pop(key, "Product ID not found.")

#     elif operation == "popitem":
#         if catalog:
#             return catalog.popitem()
#         return "Catalog is empty."

#     elif operation == "clear":
#         catalog.clear()
#         return "Catalog cleared."

#     else:
#         return "Invalid operation."


# # Initial Catalog
# catalog = {
#     101: "Laptop",
#     102: "Smartphone",
#     103: "Tablet",
#     104: "Headphones"
# }

# while True:
#     print("\nOperations: get, keys, values, items, update, pop, popitem, clear, exit")
#     operation = input("Enter the operation you want to perform: ").lower()

#     if operation == "exit":
#         print("Exiting the catalog manager.")
#         break

#     elif operation == "get":
#         key = int(input("Enter the product ID (key): "))
#         result = manage_catalog(catalog, operation, key)

#     elif operation == "update":
#         key = int(input("Enter the product ID (key): "))
#         value = input("Enter the product name (value): ")
#         result = manage_catalog(catalog, operation, key, value)

#     elif operation == "pop":
#         key = int(input("Enter the product ID (key): "))
#         result = manage_catalog(catalog, operation, key)

#     else:
#         result = manage_catalog(catalog, operation)

#     print("\nResult:", result)
#     print("Updated Catalog:", catalog)






# a = {'course': 'Python',
#       'fees':15000,
#         101: {'course': 'JavaScript',
#                'fees': 10000} 
# }
# print(a[101].get('fees',55))


lst=[]
# for i in range(1,51):
# 	lst.append(i*i)	
# print(lst)

# lst=[]
# lambda i:[lst.append(i*i) for i in range(1,51)]
# print(lst)

# sqrs=[i*i for i in range(1,51) if i%2==0]
# print(sqrs)
# sqrs={i*i for i in range(1,51) if i%2==0}
# print(sqrs)
lst=['name','age','course']
values=['Alice',30,'Python']
# sqrs={i:i*i for i in range(1,51) if i%2==0}
# print(sqrs)
# lst=['name','age','course']
# values=['Alice',30,'Python']
# dct={lst[i]:values[i] for i in range(len(values)) if len(lst)==len(values)}
# print(dct)
# # new_dict = {expression(variable):expression(variable) for variable,variable in
# # iterable_object if_statement}
# dict={k:v for k,v in zip(lst,values)}
# dct=dict(zip(lst,values))


# print("--------------------OOPS--------------------------------")
class Animal:
	pass
class Animal():
	def sound(self):
		return "Some Sound"
class Dog(Animal):
    def sound(self):
        return "Woof!"
class Cat(Animal):
    def sound(self):
        return "Meow!"
# print(Animal.sound())
# print(type(Animal),type(()))
# animal1=Animal()
# print(animal1.sound())
# classes = [Animal(), Dog(), Cat()]
# for cls in classes:
# 	print(cls.sound())

# class Car:
# 	def display(self):
# 		return f"{self.brand} {self.year} {self.model}"

# car1=Car()
# car1.brand="Benz"
# car1.year=2003
# car1.model="Classic"


# print(car1.display())

# class Car:
# 	def __init__(self,brand="NA",year=2000,model="Unknown"):
# 		self.brand=brand
# 		self.model=model		
# 		self.year=year
# 	def display(self):
# 		return f"{self.brand} {self.year} {self.model}"
# car1=Car("Benz",2003,"Classic")
# car2=Car()

# print(car1.display())
# print(car2.display())




class Car():
	def __init__(self,brand=None,year=None,model=None):
		self.brand=brand
		self.year=year
		self.model=model
	
	def get_brand(self):
		return self.brand
	def set_brand(self):
		new=input("Enter the brand:")
		self.brand=new
	def display(self):
		return f"{self.brand} {self.year} {self.model}"
c1=Car()
print(c1.get_brand())
print(c1.display())
c1.set_brand()
print(c1.get_brand())
print(c1.display())










