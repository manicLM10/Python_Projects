print("Welcome to Treasure Island.Your Misson is to find the treasure.")
total_life = 3
n = total_life
while(n!=0):
    print("Choose left or right ?")
    c_1 = input()
    if c_1.lower() == 'right':
        print("Game Over")
        n-=1
        print(f"Life Remaining {n}")
        print("want To play(press Enter) or Quit the Game (press q)")
        r = input()
        if r == 'q':
            break

    else:
        print("If you need to wait for boat or you are gonna swim")
        print("Swim or Wait")
        c_2 = input()
        if c_2.lower() == 'swim':
            print("Game Over")
            n-=1
            print(f"Life Remaining {n}")
            print("want To play(press Enter) or Quit the Game (press q)")
            r = input()
            if r == 'q':
                break

        else:
            print("Choose the Coorect Door!!")
            print("Red or Blue or Yellow")
            c3 = input()
            if c3.lower() == 'red' or c3.lower() == 'blue' :
                print("Game Over")
                n-=1
                print(f"Life Remaining {n}")
                print("want To play(press Enter) or Quit the Game (press q)")
                r = input()
                if r == 'q':
                    break

            else:
                print("You Win !!")
                print("want To play(press Enter) or Quit the Game (press q)")
                r = input()
                if r == 'q':
                    break
  


