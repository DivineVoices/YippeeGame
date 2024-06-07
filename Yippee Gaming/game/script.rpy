define y = Character("Yuzu", color="#abfcff")
define m = Character("Maiko", color="#850c0c")
define p = Character("[name]", color="#ff26ff")

transform active_char:
    zoom 1.0
transform inactive_char:
    zoom 0.75

label start:
    python:
        name = renpy.input(_("My name is"))

        name = name.strip() or __("Gamer")
        if name.lower() == "monika":
            renpy.run(OpenURL("https://www.youtube.com/watch?v=YYoOIGBcN48"))

    $ flag = False
    scene club

    show maiko1 at active_char:
        xalign 0.75
        yalign 0.5

    m "Absolutely banger game so far ngl"

    show maiko1 at inactive_char:
        xalign 0.75
        yalign 0.5

    show yuzu1 at active_char:
        xalign 0.25
        yalign 0.5
        xzoom -1.0


    y "Hi I'm here too"

    show yuzu1 at inactive_char:
        xalign 0.25
        yalign 0.5
        xzoom -1.0

    show maiko1 at active_char:
        xalign 0.75
        yalign 0.5

    m "That's pretty poggers don't you think?"

    show maiko1 at inactive_char:
        xalign 0.75
        yalign 0.5

    show yuzu1 at active_char:
        xalign 0.25
        yalign 0.5
        xzoom -1.0
  
    menu:
        y "Thoughts?"

        "It sure is":
            jump pogornog_yes

        "No I hate you":
            jump pogornog_no


    label pogornog_yes:
        y "Hell yeah it is"
        show maiko1 at active_char:
            xalign 0.75
            yalign 0.5
        show yuzu1 at inactive_char:
            xalign 0.25
            yalign 0.5
            xzoom -1.0
        m "Oh hey its the good ending would you look at that"

        jump pogornog_done

    label pogornog_no:
        $ flag = True
        y "Rude :("
        y "I'm gonna go because you're being a meanie"
        hide yuzu1
        with dissolve
        show maiko1 at active_char:
            xalign 0.75
            yalign 0.5
        m "Welp"
        m "I'm off to the park, You have no choice, come with me"
        scene park
        show maiko1 at active_char:
            xalign 0.75
            yalign 0.5
        m "This is nice"

        m "Alright, I'm bored, let's go back"
        jump pogornog_done


    label pogornog_done:
        scene club

        if flag == False: 
            show yuzu1 at inactive_char:
                xalign 0.25
                yalign 0.5
                xzoom -1.0
        show maiko1 at active_char:
                xalign 0.75
                yalign 0.5

        m "Well, what now [name]?"

        if name.lower() == "monika":
            hide yuzu1
            with dissolve
            p "I've deleted Yuzu, you're next"


            m "AHHHHHHHHHH"
            show maikodel at active_char:
                xalign 0.75
                yalign 0.5
            pause .2
            show maikodel2 at active_char:
                xalign 0.75
                yalign 0.5
            pause .2
            show maikodel3 at active_char:
                xalign 0.75
                yalign 0.5
            pause .2
            show maikodel4 at active_char:
                xalign 0.75
                yalign 0.5
            pause .5
            p "Rip Bozo"

            return

        p "Wanna go get some donuts?"

        m "Hell yeah"
            
    return
