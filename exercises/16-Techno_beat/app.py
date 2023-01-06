def lyrics_generator(song):
    beats = ''
    drops = 0
    for i in song:
        if i == 0:
            beats += 'Boom '
        else:
            beats += 'Drop the base '
            drops += 1
            if drops == 3:
                beats += '!!!Break the base!!! '
    return beats


# Your code go above, nothing to change after this line:
print(lyrics_generator([0, 0, 1, 1, 0, 0, 0]))
print(lyrics_generator([0, 0, 1, 1, 1, 0, 0, 0]))
print(lyrics_generator([0, 0, 0]))
print(lyrics_generator([1, 0, 1]))
print(lyrics_generator([1, 1, 1]))
