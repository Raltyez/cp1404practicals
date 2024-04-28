import wikipedia

# Tests
# search_results = wikipedia.summary("GitHub")
# print(search_results)

user_search = input("Enter a title or a phrase: ")
while user_search != "":
    try:
        search_results = wikipedia.summary(user_search)
        print(search_results)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    wikipedia.page(user_search, auto_suggest=False)
    user_search = input("Enter a title or a phrase: ")


