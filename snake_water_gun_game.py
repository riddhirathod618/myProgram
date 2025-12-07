import random

gm_choice = ['snake','water','gun']

comp_choice = random.choice(gm_choice)
your_choice = input("enter your choice: ")

print(f"computer choice is:{comp_choice}")
print(f"your choice is:{your_choice}")

if(comp_choice == your_choice):
    print("game draw")
else:
    if(comp_choice == 'snake' and your_choice == 'water'):
        print("You lose!")
    elif(comp_choice == 'snake' and your_choice == 'gun'):
        print("you win!")
    elif(comp_choice == 'gun' and your_choice == 'water'):
        print("you win!")
    elif(comp_choice == 'gun' and your_choice == 'snake'):
        print("you lose!")
    elif(comp_choice == 'water' and your_choice == 'snake'):
        print("you win!")
    elif(comp_choice == 'water' and your_choice == 'gun'):
        print("you lose!")
    else:
        print("something is wrong..")