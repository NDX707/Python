import wikipedia as wiki

userInput = input('Wiki Search: ')

wiki_query = wiki.summary(userInput)

print("\n","\n")

print(wiki_query)
