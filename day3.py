print('''
              __   
           .-'  '-.       [Jamie]
          /        )                                 
          |  C   o( 
           \       >      
            )  \  /      ..`'
         .-._ / `'      /////     
        / _    \       ( | /
        |/ )    \\     / _,
        / /      |\   / /
       / /       | \ / /
      (  )       /\ ' /
       \ \      (  `-'
        \ \      Y 
        /\ `-.   |
        |(   ^'  |
        \ \\\\  /
         `-    f|
           |   ||
           |   f/
           j   /
           |   )
           |  |
           /  |
           f  |
           \  |
            | |&
           (   `-._,
            -^-----'
      ''' )
print("Welcome to Jamie's life")
print("Your mission is to make Jamie happy") 
print("Let get start")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

activity = (input("What would you like Jamie to do? games or gym? "))

if activity == "games":
    print("Jamie feels happy to start play video game!")

elif activity == "gym":
    print("Jamie feels healiter and stronger!")

food = (input("What would you like to eat? pizza or chicken? "))

if food == "pizza":
    print("Jamie is full and notice some weight gain")
elif food == "chicken":
    print("Jamie is start getting muscle and stronger!")
        
bed = input("What would you like Jamie to do before bed? book or phone? ")

if bed == "book":
    print("Jamie learning new things!")
elif bed == "phone":
    print("Jamie is getting satisfaction")

if activity == "gym" and food == "chicken" and bed == "book":
    print("Jamie feels stronger and happier")
elif activity == "games" and food =="pizza" and bed == "phone":
    print("Jamie got the satisfaction but he feels depressed.")