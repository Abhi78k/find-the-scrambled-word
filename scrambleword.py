import random
words = ['alphabet','astronaut','headphones']
w = words[random.randint(0,2)]
l = len(w)
def shuffler():
    play = 0
    shuffled = random.sample(w,l)
    shuffledword = ''.join(shuffled)
    while play<10:
        print(f"Find the word! {''.join(shuffledword)}")
        g = input("Enter your guess! ")
        if g==w:
            print("You win!")
            return
        else:
            print("Wrong guess! Try again")
            print(f"{9-play} chances left!")
            play+=1
            if play==10:
                print(f"You lose! The word was {w}")
            continue

shuffler()