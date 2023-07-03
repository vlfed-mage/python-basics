message = input('> ')
words = message.split(' ')

emojis = {
    ':)': '😀️',
    ':(': '🙁️'
}

output = ''

for word in words:
    output += f'{emojis.get(word, word)} '

print(output)
