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
    $ MLove = 0
    $ MTrack = 0
    $ YTrack = 0
    $ Day = 1

    jump DayStart

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

    y "Ooh a knife!"

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

        m "Wanna go get some donuts? I love donuts"

    menu:
        "Yes, I love donuts":
            jump Donuts_Win

        "No, I don't like donuts":
            jump Donuts_Loss


    label Donuts_Win:
        $ MLove = MLove + 2
        m "Hell yeah!"
        jump Donuts_Complete

    label Donuts_Loss:
        $ MLove = MLove + 1
        m "Awe, That's sad"
        jump Donuts_Complete


    label Donuts_Complete:
        m "Well I had a lot of fun today!"
        if MLove == 2:
            m "But, I think you're like, REALLY cool, we should hang out again!"
        if MLove == 1:
            m "You're cool, talk again yeah?"
        "Maiko walks off without waiting for an answer"
        hide maiko1
        with dissolve
        if MLove == 2:
            "You got the great ending"
        if MLove == 1:
            "You got the good ending"
        "Thanks for playing!"
    
    return
    
    label DayStart:
        scene club
        menu:
            "Who should I go on a date with?"

            "Maiko":
                jump MDates

            "Yuzu":
                jump YDates

        label MDates:
            label MDate1:
                if MTrack >= 1:
                    jump MDate2
                m "This is the first date!"
                m "I'm having a great time"
                if YTrack >= 3:
                    m "I do miss Yuzu though..."
                $ MTrack = 1
                jump DayEnd
                
            label MDate2:
                if MTrack >= 2:
                    jump MDate3
                m "This is the second date!"
                m "I'm having a great time again"
                $ MTrack = 2
                jump DayEnd

            label MDate3:
                if MTrack >= 3:
                    "You have finished all the dates with Maiko"
                    $ Day -= 1
                    jump DayEnd
                m "This is the third date!"
                m "Wow Yuzu absolutely hates me now"
                $ MTrack = 3
                jump DayEnd


        label YDates:
            label YDate1:
                if YTrack >= 1:
                    jump YDate3
                y "This is the first date!"
                y "I'm having a great time"
                if MTrack >= 3:
                    m "But damn do I hate that bitch Maiko"
                $ YTrack = 1
                jump DayEnd

            label YDate2:
                if YTrack >= 2:
                    jump YDate3
                y "This is the second date!"
                y "I'm having a great time again"
                $ YTrack = 2
                jump DayEnd

            label YDate3:
                if YTrack >= 3:
                    "You have finished all the dates with Yuzu"
                    $ Day -= 1
                    jump DayEnd
                y "This is the third date!"
                y "I am now dead RIP"
                $ YTrack = 3
                jump DayEnd

        label DayEnd:
            $ Day += 1
            if Day >= 5:
                return
            jump DayStart

    return

