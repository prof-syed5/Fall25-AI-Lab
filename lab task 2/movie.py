movies = [
    ("Together Forever", 29000000),
    ("Incredibles 2", 19000000),
    ("Friends with benifits", 45000000),
    ("Demon  Slayer", 37000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Beyond the Bar", 856000000),
    ("Wednesday", 200000000)
]

extra_movies = int(input("How many movies do you want to add? "))

for i in range(extra_movies):
    name = input("Enter movie name: ")
    budget = int(input("Enter movie budget: "))
    movies.append((name, budget))

# Step 1: find total budget
total = 0
for movie in movies:
    total += movie[1]

# Step 2: find average budget
average = total // len(movies)   # using // to keep it an integer

print("\nAverage movie budget is:", average)

# Step 3: find movies above average 
above_average = []
for movie in movies:
    if movie[1] > average:
        above_average.append(movie)
        diff = movie[1] - average
        print(movie[0], "cost", movie[1], "which is", diff, "over average.")

#  Step 4: count how many 
print("\nNumber of movies with above average budget:", len(above_average))
