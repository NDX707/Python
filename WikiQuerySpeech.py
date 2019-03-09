import wikipedia as wiki
import sys
import os

userInput = input('Wiki Search: ')

wiki_query = wiki.summary(userInput)

print("\n","\n")

print(wiki_query)

with open('query.txt', 'w+') as f:
    sys.stdout = f
    print (wiki_query)


os.system("gtts-cli -f query.txt | play -t mp3 -")



