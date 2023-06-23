import random


def random_phrase():
    adj = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
    noun = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']

    print(random.choice(adj) + ' ' + random.choice(noun))

random_phrase()
