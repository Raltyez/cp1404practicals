
text = input("Text: ")
words = text.split()
texts_to_count = {}
for word in words:
    # LBYL method (which works)
    # if word not in texts_to_count:
    #     texts_to_count[word] = 1
    # elif word in texts_to_count:
    #     texts_to_count[word] += 1
    try:
        texts_to_count[word] += 1
    except KeyError:
        texts_to_count[word] = 1
text_counts = texts_to_count.items()
sorted_text_counts = sorted(text_counts)
for piece in sorted_text_counts:
    print(f"{piece[0]:10} : {piece[1]}")

