

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
en = enumerate(seasons)

# for x in dir(en):
#     print x
'''
def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
'''
        
# print enumerate(seasons).next()
print en.next()