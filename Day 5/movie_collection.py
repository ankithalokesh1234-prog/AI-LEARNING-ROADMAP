movies = {
    "KGF": 9,
    "Kantara": 10,
    "Charlie": 8
}

movie = input("Enter movie name: ")

if movie in movies:
    print("Rating:", movies[movie])
else:
    print("Movie not found")
