# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Ant")
define m = Character("Me")


# The game starts here.

label start:

    # add a file (named either "bg room.png" or "bg room.jpg") to show it

    scene time one
    # it shows August for like 5secs
    
    scene bg room
    #replace with lab room

    # replace it by adding a file named "eileen happy.png" to the images directory
    show ant default

    a "Welcome back,"
    a "Did you bring back the sample?"
    m "Yeah, I have it here."
    "*You take a small container out of your bag and place it gently on the table.*"
    m "I collected this from the river by the farm, I was planning to do some experiments with it later."
    a "I see. The lab in the back is currently open, but don't mess with my vials."
    "Ant pauses, seemingly wanting to add something but eventually decides not to."
    m "Alright, I'll make sure to clean up as well."
    a "Ok. I'll leave it to you then."


    # This ends the game.

    return

