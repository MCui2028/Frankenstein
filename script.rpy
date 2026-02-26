# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Ant")
define m = Character("Me")
define w = Character("William")
define j = Character("Justine")
define h = Character("Henry")
define e = Character("Elizabeth")
define f = Character("Father")
default antpoints_good = 0
default antpoints_bad = 0



# The game starts here.

label start:

    "Welcome."
    "Enter your name."

    # Prompt the player for input and store it in the 'player_name' variable
    $ player_name = renpy.input("The Protagonist's name will be:")
    
    # Use .strip() to remove any accidental leading/trailing whitespace
    $ player_name = player_name.strip() 

    # Check if the input was empty and set a default name if needed
    if player_name == "":
        $ player_name = "Victor" # or any other default name

    "Pleased to meet you, %(player_name)s."

    # add a file (named either "bg room.png" or "bg room.jpg") to show it

    show time one
    $ renpy.pause(2.0, hard=True)
    
    scene bg room
    with dissolve
    #replace with lab room

    # replace it by adding a file named "eileen happy.png" to the images directory
    show ant default

    a "Welcome back!"
    a "Did you bring back the sample?"
    m "Yeah, I have it here."
    "You take a small container out of your bag and place it gently on the table."
    m "I collected this from the river by the farm, I was planning to do some experiments with it later."
    show ant happy
    a "Great! I can't wait to finally drink fresh water. It gets tiring drinking filtered mush..."
    m "Alright. I'll get started then--let's see how this goes."
    show ant default
    a "Ok, I'll be here in the back if you have any questions!"

    hide ant

    "It's time to get started. But first..."

    menu:
        "Go to the lab.":
            jump lab
        "Talk to Ant.":
            jump talk
        "skip temporary":
            jump incubate

    label talk:
        show ant default
        a "Oh hey! Did you want to talk to me about something?"

        menu:   
            "Don't you think it's lonely here?":
                jump august_ant_1good
            "How are you liking this place?":
                jump august_ant_1bad

    label august_ant_1good:
        $ antpoints_good += 1
        show ant default
        a "What do you mean?"
        m "I mean...it's just us two here testing out the area. It must get boring sometimes."
        a "That's a good point."
        show ant consternation
        "Ant ponders the question with a furrowed brow."
        show ant default
        a "Well, I suppose it's a little lonely. But you're good company, and I'm always busy with the experiments."
        m "Oh. Yeah, I feel the same."
        m "Allllright, time to get back to the lab."
        jump lab

    label august_ant_1bad:
        $ antpoints_bad += 1
        show ant default
        a "It's not bad! There's always interesting things to explore here. Honestly, I wouldn't ask for much more."
        m "Same. It's oddly comforting, having the whole place here to ourselves."
        m "And besides, William and the others love exploring too."
        show ant consternation
        a "Pardon...?"
        m "Nevermind. Sorry, I..."
        m "I forgot. I'll be testing for a while though, so tell me if you need anything."
        m "Time to get back to the lab."
        jump lab

        label lab:
        scene lab
        hide ant
        "You open the container filled with water."
        m "Total coliform bacteria, nitrates, total dissolved solids, and pH level, that should be it."
        "Take the container. (Click)"
        call screen box
            ##image button
        screen box:
                imagebutton:
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.28
                    idle "box.png"
                    # hover "new.png"
                    # auto "box%s.avif" for idle/hover
                    # action [Hide("displayTextScreen"), Jump ("testing")]
                    action Jump ("testing")
                    # xysize(100, 100)
                    # hovered Show("displayTextScreen", displayText = "Text here")
                    # unhovered Hide("displayTextScreen")

    #         action imagebutton auto "box_%s.avif" action Skip()
    #     jump testing

        label testing:
            "You swirl the container."
            m "51 ppm. Good enough for drinking."
            "Place a pH test strip. (Click)"
        call screen bottle 
            ##image button
        screen bottle:
                imagebutton:
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.28
                    idle "bottle.png"
                    action Jump ("pH")
        
            
        label pH:
        "You place a pH test strip in the water."
        m "pH of 7. Well, not like I expected anything else."

        "Incubate the sample. (Click)"
        call screen incubate
            ##image button
        screen incubate:
                imagebutton:
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.28
                    idle "incubate.png"
                    action Jump ("incubate")
        label incubate:
        m "I need to wait a day, but otherwise all signs point to drinkable water. I'd better go tell Ant."
        scene bg room
        show ant default
        a "You're back. How did it go?"
        m "I need to wait for my coliform and bacteria testing, but otherwise my hopes are high. It's looking pretty good so far."
        m "Anyways, I'm famished. Let me grab something to eat and I'll be back."
        scene black
        "You are not alone."
        scene kitchen
        hide ant
        show william default at Position(xpos=0.25, ypos=0.8) # figure this out later!!!
        m "W-William!"
        w "[player_name]!"
        w "I'm parched. Either my throat's dry, or I'm going to catch a fever."
        m "I'll...check. Hold still."
        "You place a hand on William's forehead."
        m "Thank goodness. I doubt you're going to get a fever, but make sure to drink water."
        m "Speaking of water, I just did a test on the water near the farm, so by tomorrow we should be all right."
        w "Thank"
        w "Thank you."
        w "[player_name]."


    # This ends the game.

    return
