from HW9 import*
import random

def main():

    goblin = Enemy('Goblin', 10, 5)
    dragon = Enemy('Dragon', 30, 10)
    ogre = Enemy('Ogre', 20, 8)
    wizard = Enemy('Wizard', 20, 10)

    enemies = {goblin, dragon, ogre, wizard}

    enemy = random.sample(sorted(enemies), 1)[0]
    print(f'You have encountered a {enemy}.')

main()