'''   Move all Zeros present in an Array/List to the End
given_list = [7, 2, 0, 34, 56, 12, 0, 5, 6, 8, 0, 0, 9, 0, 1, 2, 4, 5]




.Find the Missing Number in an array/list
given_list = [1, 3, 2, 6, 5]
oput is :4
'''

Scenario:
You are building a product catalog system for an online store. The catalog is stored as a 
dictionary where keys are product IDs and values are product names.

Task:
Write a function manage_catalog(catalog, operation, key=None, value=None) that performs
the following operations based on the method name provided in the operation argument:

Use get() to retrieve a product name by its ID.
Use keys() to get a list of all product IDs.
Use values() to get a list of all product names.
Use items() to get all product ID-name pairs.
Use update() to add or update a product in the catalog.
Use pop() to remove a product by its ID and return its name.
Use popitem() to remove the last added product.
Use clear() to empty the catalog.
 
catalog = {
    101: "Laptop",
    102: "Smartphone",
    103: "Tablet",
    104: "Headphones"
}

operation = "get"
key = 102
print(manage_catalog(catalog, operation, key))  # Output: Smartphone


Operations: get, keys, values, items, update, pop, popitem, clear, exit
Enter the operation you want to perform: keys

Result: [101, 102, 103, 104]
Updated Catalog: {101: 'Laptop', 102: 'Smartphone', 103: 'Tablet', 104: 'Headphones'}

Operations: get, keys, values, items, update, pop, popitem, clear, exit
Enter the operation you want to perform: get
Enter the product ID (key): 102

Result: Smartphone
Updated Catalog: {101: 'Laptop', 102: 'Smartphone', 103: 'Tablet', 104: 'Headphones'}

Operations: get, keys, values, items, update, pop, popitem, clear, exit
Enter the operation you want to perform: update
Enter the product ID (key): 105
Enter the product name (value): Smartwatch

Result: Product 105 updated/added successfully.
Updated Catalog: {101: 'Laptop', 102: 'Smartphone', 103: 'Tablet', 104: 'Headphones', 105: 'Smartwatch'}

Operations: get, keys, values, items, update, pop, popitem, clear, exit
Enter the operation you want to perform: popitem

Result: (105, 'Smartwatch')
Updated Catalog: {101: 'Laptop', 102: 'Smartphone', 103: 'Tablet', 104: 'Headphones'}

Operations: get, keys, values, items, update, pop, popitem, clear, exit
Enter the operation you want to perform: exit
Exiting the catalog manager.


'''
'''



def manage_catalog(catalog, operation, key=None, value=None):
    if operation == "get":
        return catalog.get(key, "Product not found")
    elif operation == "keys":
        return list(catalog.keys())
    elif operation == "values":
        return list(catalog.values())
    elif operation == "items":
        return list(catalog.items())
    elif operation == "update":
        if key and value:
            catalog.update({key: value})
            return f"Product {key} updated/added successfully."
        else:
            return "Error: Provide both key and value for update."
    elif operation == "pop":
        if key:
            return catalog.pop(key, "Product not found")
        else:
            return "Error: Provide a key to remove a product."
    elif operation == "popitem":
        if catalog:
            return catalog.popitem()
        else:
            return "Error: Catalog is empty."
    elif operation == "clear":
        catalog.clear()
        return "Catalog cleared successfully."
    else:
        return "Error: Invalid operation."


def interactive_catalog_manager():
    catalog = {
        101: "Laptop",
        102: "Smartphone",
        103: "Tablet",
        104: "Headphones",
    }
    print("Initial Catalog:", catalog)
    
    while True:
        print("\nOperations: get, keys, values, items, update, pop, popitem, clear, exit")
        operation = input("Enter the operation you want to perform: ").strip().lower()
        
        if operation == "exit":
            print("Exiting the catalog manager.")
            break

        key = None
        value = None
        
        if operation in ["get", "pop", "update"]:
            key = input("Enter the product ID (key): ").strip()
            if key.isdigit():
                key = int(key)
            else:
                print("Invalid key! Please enter a numeric product ID.")
                continue
            
            if operation == "update":
                value = input("Enter the product name (value): ").strip()
                if not value:
                    print("Error: Product name cannot be empty!")
                    continue
        
        result = manage_catalog(catalog, operation, key, value)
        print("\nResult:", result)
        print("Updated Catalog:", catalog)


interactive_catalog_manager()
'''





'''
Question 2: Working with Set Methods
Scenario:
You are managing a music playlist where each playlist is represented as a set of song IDs.

Task:
Write a function manage_playlist(playlist, operation, song=None, another_playlist=None) 
that performs the following operations based on the method name provided in the operation argument:

Use add() to add a song to the playlist.
Use remove() to remove a specific song from the playlist.
Use discard() to remove a song only if it exists in the playlist.
Use pop() to remove and return a random song.
Use clear() to remove all songs from the playlist.
Use union() to combine the current playlist with another playlist.
Use intersection() to find common songs between two playlists.
Use difference() to find songs unique to the current playlist compared to another playlist.


Operations: add, remove, discard, pop, clear, union, intersection, difference, exit
Enter the operation you want to perform: add
Enter the song ID: 101

Result: Song 101 added to the playlist.
Updated Playlist: {101}

Operations: add, remove, discard, pop, clear, union, intersection, difference, exit
Enter the operation you want to perform: add
Enter the song ID: 102

Result: Song 102 added to the playlist.
Updated Playlist: {101, 102}

Operations: add, remove, discard, pop, clear, union, intersection, difference, exit
Enter the operation you want to perform: union
Enter another playlist as comma-separated song IDs (e.g., 101,102,103): 102,103,104

Result: {101, 102, 103, 104}
Updated Playlist: {101, 102}

Operations: add, remove, discard, pop, clear, union, intersection, difference, exit
Enter the operation you want to perform: intersection
Enter another playlist as comma-separated song IDs (e.g., 101,102,103): 102,103

Result: {102}
Updated Playlist: {101, 102}

Operations: add, remove, discard, pop, clear, union, intersection, difference, exit
Enter the operation you want to perform: pop

Result: Randomly removed song: 101
Updated Playlist: {102}

Operations: add, remove, discard, pop, clear, union, intersection, difference, exit
Enter the operation you want to perform: exit
Exiting the playlist manager.
'''


'''
def manage_playlist(playlist, operation, song=None, another_playlist=None):
    if operation == "add":
        playlist.add(song)
        return f"Song {song} added to the playlist."
    elif operation == "remove":
        if song in playlist:
            playlist.remove(song)
            return f"Song {song} removed from the playlist."
        else:
            return f"Error: Song {song} not found in the playlist."
    elif operation == "discard":
        playlist.discard(song)
        return f"Song {song} discarded (if it existed)."
    elif operation == "pop":
        if playlist:
            removed_song = playlist.pop()
            return f"Randomly removed song: {removed_song}"
        else:
            return "Error: Playlist is empty."
    elif operation == "clear":
        playlist.clear()
        return "Playlist cleared successfully."
    elif operation == "union":
        if another_playlist is not None:
            return playlist.union(another_playlist)
        else:
            return "Error: Provide another playlist for union."
    elif operation == "intersection":
        if another_playlist is not None:
            return playlist.intersection(another_playlist)
        else:
            return "Error: Provide another playlist for intersection."
    elif operation == "difference":
        if another_playlist is not None:
            return playlist.difference(another_playlist)
        else:
            return "Error: Provide another playlist for difference."
    else:
        return "Error: Invalid operation."


def interactive_playlist_manager():
    playlist = set()
    print("Welcome to the Playlist Manager!")
    print("Initial Playlist:", playlist)
    
    while True:
        print("\nOperations: add, remove, discard, pop, clear, union, intersection, difference, exit")
        operation = input("Enter the operation you want to perform: ").strip().lower()
        
        if operation == "exit":
            print("Exiting the playlist manager.")
            break

        song = None
        another_playlist = None
        
        if operation in ["add", "remove", "discard"]:
            song = input("Enter the song ID: ").strip()
            if not song.isdigit():
                print("Invalid song ID! Please enter a numeric value.")
                continue
            song = int(song)

        if operation in ["union", "intersection", "difference"]:
            another_playlist_input = input("Enter another playlist as comma-separated song IDs (e.g., 101,102,103): ").strip()
            another_playlist = set(int(s) for s in another_playlist_input.split(",") if s.isdigit())
        
        result = manage_playlist(playlist, operation, song, another_playlist)
        print("\nResult:", result)
        print("Updated Playlist:", playlist)


interactive_playlist_manager()
'''