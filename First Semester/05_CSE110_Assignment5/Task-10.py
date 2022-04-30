given = {'sci fi': 5, 'mystery': 3, 'horror': 14, 'young_adult': 2, 'adventure': 9}
position = str
highest = int()
for key, val in given.items():
    if val > highest:
        highest = val
        position = key
print("The highest selling book genre is", "'"+position+"'", "and the number of books sold are", highest, end=".")

