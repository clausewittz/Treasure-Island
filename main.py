print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

first_choice = input("You found yourself unconscious on the shore of an island.There are 2 roads leading to the center of the island. Left or right?\n").lower()

first_choice.lower()
if first_choice == "left":
  print("You entered the forest area and attacked by wild animals!")
  print(""""
       ^  ^  ^   ^      ^  ^   ^  ^  ^   ^  ^
      /|\/|\/|\ /|\    /|\/|\ /|\/|\/|\ /|\/|\
      /|\/|\/|\ /|\    /|\/|\ /|\/|\/|\ /|\/|\
ejm96 /|\/|\/|\ /|\    /|\/|\/|\ /|\/|\
""")
  run_or_dead = input("Run or climb. (Tree)\n").lower()
  if run_or_dead == "run":
    print("You get exhausted and catched by the animals. You're dead!")

  elif run_or_dead == "climb":
    print("You climbed on a tree safely and waited till the animals are gone. You fell asleep and woke up in the morning.")

    print("""
    _{\ _{\{\/}/}/}__
             {/{/\}{/{/\}(\}{/\} _
            {/{/\}{/{/\}(_)\}{/{/\}  _
         {\{/(\}\}{/{/\}\}{/){/\}\} /\}
        {/{/(_)/}{\{/)\}{\(_){/}/}/}/}
       _{\{/{/{\{/{/(_)/}/}/}{\(/}/}/}
      {/{/{\{\{\(/}{\{\/}/}{\}(_){\/}\}
      _{\{/{\{/(_)\}/}{/{/{/\}\})\}{/\}
     {/{/{\{\(/}{/{\{\{\/})/}{\(_)/}/}\}
      {\{\/}(_){\{\{\/}/}(_){\/}{\/}/})/}
       {/{\{\/}{/{\{\{\/}/}{\{\/}/}\}(_)
      {/{\{\/}{/){\{\{\/}/}{\{\(/}/}\}/}
       {/{\{\/}(_){\{\{\(/}/}{\(_)/}/}\}
         {/({/{\{/{\{\/}(_){\/}/}\}/}(\}
          (_){/{\/}{\{\/}/}{\{\)/}/}(_)
            {/{/{\{\/}{/{\{\{\(_)/}
             {/{\{\{\/}/}{\{\}/}
              {){/ {\/}{\/} \}\}
              (_)  \.-'.-/
          __...--- |'-.-'| --...__
   _...--"   .-'   |'-.-'|  ' -.  ""--..__
 -"    ' .  . '    |.'-._| '  . .  '   jro
 .  '-  '    .--'  | '-.'|    .  '  . '
          ' ..     |'-_.-|
  .  '  .       _.-|-._ -|-._  .  '  .
              .'   |'- .-|   '.
  ..-'   ' .  '.   `-._.-�   .'  '  - .
   .-' '        '-._______.-'     
    
    """)

    found_cave=input("The adventure is just begun. You found a cave. Enter or walk?\n").lower()
    if found_cave == "enter":
      print("Its a bear cave. You can't run. You're dead.")
      print("""

       .'"'.        ___,,,___        .'``.
: (\  `."'"```         ```"'"-'  /) ;
 :  \                         `./  .'
  `.                            :.'
    /        _         _        \
   |         0}       {0         |
   |         /         \         |
   |        /           \        |
   |       /             \       |
    \     |      .-.      |     /
     `.   | . . /   \ . . |   .'
 jgs   `-._\.'.(     ).'./_.-'
           `'  `._.'  '/'
             `. --'-- .'
               `-...-'
      
      """"")
    
    elif found_cave=="walk":
      swim_or_boat=input("You kept walking and found a river. Swim or wait for a boat?\n").lower()
      if swim_or_boat == "swim":
        print("Something in the sea ate you. You're dead!")
        print("""

                 .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
          snd                         (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-'

        """)
      elif swim_or_boat == "wait":
        print("You waited for a boat and safely passed the river. You found a big castle.")
        print("""
                               ,.=,,==. ,,_
                      _ ,====, _    |I|`` ||  `|I `|
                     |`I|    || `==,|``   ^^   ``  |
                     | ``    ^^    ||_,===TT`==,,_ |
                     |,==Y``Y==,,__| \L=_-`'   +J/`
                      \|=_  ' -=#J/..-|=_-     =|
                       |=_   -;-='`. .|=_-     =|----T--,
                       |=/\  -|=_-. . |=_-/^\  =||-|-|::|____
                       |=||  -|=_-. . |=_-| |  =|-|-||::\____
                       |=LJ  -|=_-. . |=_-|_| =||-|-|:::::::
                       |=_   -|=_-_.  |=_-     =|-|-||:::::::
                       |=_   -|=//^\. |=_-     =||-|-|:::::::
                   ,   |/&_,_-|=||  | |=_-     =|-|-||:::::::
                ,--``8%,/    ',%||  | |=_-     =||-|-|%::::::
            ,---`_,888`  ,.'''''`-.,|,|/!,--,.&\|&\-,|&#:::::
           |;:;K`__,...;=\_____,=``           %%%&     %#,---
           |;::::::::::::|       `'.________+-------\   ``
          /8M%;:::;;:::::|                  |        `-------
        """)
        enter_the_castle = input("Enter the castle or find another ship to leave.\n").lower()
        if enter_the_castle == "enter":
          print("You found out that the castle is abandoned. A big treasure awaits you!! You won!")
        elif enter_the_castle == "find":
          print("You left the island without the treasure. Game over.")
          print("""   _____|\
                  _.--| SSt |:
                 <____|.----||
                        .---''---,
                         ;..__..'    _...
                       ,'/  ;|/..--''    \
                     ,'_/.-/':            :
                _..-'''/  /  |  \    \   _|/|
               \      /-./_ \;   \    \,;'   \
               ,\    / \:  `:\    \   //    `:`.
             ,'  \  /-._;   | :    : ::    ,.   .
           ,'     ::   /`-._| |    | || ' :  `.`.)
        _,'       |;._:: |  | |    | `|   :    `'
      ,'   `.     /   |`-:_ ; |    |  |  : \
      `--.   )   /|-._:    :          |   \ \
         /  /   :_|   ;`-._;   __..--';    : :
        /  (    ;|;-./_  _/.-:'o |   /     ' |
       /  , \._/_/_./--''/_|:|___|_,'        |
      :  /   `'-'--'----'---------'          |
      | :     O ._O   O_. O ._O   O_.      ; ;
      : `.      //    //    //    //     ,' /
    ~~~`.______//____//____//____//_______,'~
              //    //~   //    //
       ~~   _//   _//   _// ~ _//     ~
     ~     / /   / /   / /   / /  ~      ~~
          ~~~   ~~~   ~~~   ~~~
        
          """)
        else:
          print("you can only pick enter or find")

      else:
        print("you can only pick swim or wait")


  
  else:
    print("You can only pick run or climb.")

elif first_choice == "right":
  print("You realize that there is a path made of stones that leads to the center of the island and you follow this path.")

  local_of_island = print("Locals of the island found you and you found out they are cannibals! Your hands are tied and you're going to get eaten soon.")
  question = input("Tell them you're god to trick them or let them do their thing.\n").lower()
  if question == "tell":
    print("They started to respect you and killed the man who tied your hands. But they found out you're not a god. Their wise man got you busted. You got killed and they ate you.")

  elif question == "let":
    print("They're singing songs and made a fire, they're dancing around this fire and they painted your face with blood. You lose. Game over.")
    print("""
       (                 ,&&&.
             )                .,.&&
            (  (              \=__/
                )             ,'-'.
          (    (  ,,      _.__|/ /|
           ) /\ -((------((_|___/ |
         (  // | (`'      ((  `'--|
       _ -.;_/ \--._      \ \-._/.
      (_;-// | \ \-'.\    <_,\_\`--'|
      ( `.__ _  ___,')      <_,-'__,'
 jrei  `'(_ )_)(_)_)'
    """)

  else:
    print("you can only pick tell or let")
else:
  print("you can only pick left or right.")
