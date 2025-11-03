movie_list=[]
ratings= []
print("Welcome to DramaList")
print("Answer a few questions (type 'done' if finish)")

while True:
    movie= input("Enter the drama/movie:").title()

    if movie == 'done'.title():
        break
    movie_list.append(movie)
    print(f"{movie} has been added to your list")

    rate= input("Whats your rate about it (out of 10):")
    ratings.append(rate)

print("\nHere are the drama you listed:")
for movie, rate in zip(movie_list, ratings):
    print(f"{movie} - {rate}")



