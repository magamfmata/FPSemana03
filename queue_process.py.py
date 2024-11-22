import collections

palavras = input("Escreve um grupo de palavras: ")
words = palavras.split()
queue= collections.deque()

for i in words: 
    queue.appendleft(i)
print("Initial Queue:",queue)

print("words with 'o':")

for word in queue:
    if 'o' in word:
        print(word)