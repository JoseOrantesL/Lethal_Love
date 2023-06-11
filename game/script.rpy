﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define raven = Character("Raven")
define you = Character("[name]")
define waiter = Character("Waiter")

image ravendefault = "images/ravendefault.png"
image Waiter = "images/waiter.png"
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    $sus_points = 0
    $suit = False
    $appetizer = ""
    scene bedroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    "I pull myself out of bed to the sound of my alarm and my phone buzzing."
    "I see a text on my phone from a girl, Raven, who I met through a dating app online"
    raven "I can't wait to see you today _______!"
    python:
        name = renpy.input("Enter Your Name:")

        name = name.strip() or "You"
    "I arranged a date with her at a nice restaurant"
    "I should probably get ready and find something appropriate to wear..."
    menu:
        "Formal Suit":
            "This looks nice, but might be a bit too fancy for a first meeting"
            $suit = True
            menu:
                "Semi-Formal Suit" if suit == True:
                    "This is perfect fit for the date!"
                    "I should get going to the restaurant"
                    scene restaurant
                    jump restaurantDate
                "Bright Graphic t-shirt":
                    "No way I'm wearing this to the first date, though it could be a conversation starter.."
                    menu:
                        "Semi-Formal Suit" if suit == True:
                            "This is perfect fit for the date!"
                            "I should get going to the restaurant"
                            scene restaurant
                            jump restaurantDate
        "Bright Graphic t-shirt":
            "No way I'm wearing this to the first date, though it could be a conversation starter.."
            menu:
                "Formal Suit":
                    "This looks nice, but might be a bit too fancy for a first meeting"
                    $suit = True
                    menu:
                        "Semi-Formal Suit":
                            "This is a perfect fit for the date!"
                            "I should get going to the restaurant"
                            scene restaurant
                            jump restaurantDate
                "Semi-Formal Suit" if suit == True:
                    "This is perfect fit for the date!"
                    "I should get going to the restaurant"
                    scene restaurant
                    jump restaurantDate

    label restaurantDate:
        "This is the restaurant scene start"

        "I arrive at the restaurant a bit early and wait a bit until I see someone who ressembles the person in Raven's profile picture"
        "Suddenly I hear a voice -"
        raven "[you]!"
        "I turn around and see the person that I've been longing to talk to"
        show ravendefault at center:
            zoom 0.5
        raven "Have you been waiting long?"

        menu:
            "Not at all!":
                you "Not really, I just got here"
                hide ravendefault
                show ravenhappy at center:
                    zoom 0.5
                raven "Great! Shall we get going?"
                hide ravenhappy
            "I've been waiting forever":
                you "Yeah I've been waiting for hours"
                hide ravendefault 
                show ravensurprised at center:
                    zoom 0.5
                raven "Oh really?! Sorry I didn't realize you were coming so soon or I would've left earlier"
                you "No that was a joke haha... I barely got here too"
                hide ravensurprised
                show ravenhappy at center:
                    zoom 0.5
                raven "Oh sorry I haven't adjusted to your sarcasm yet haha... Lets get going! I'm hungry"
                hide ravenhappy
            "I would wait forever for you":
                you "I'd wait forever for you"
                hide ravendefault
                show ravenblush at center:
                    zoom 0.5
                raven "Oh stop it"
                raven "I know you just got here too"
                hide ravenblush 
                show ravenhappy at center:
                    zoom 0.5
                raven "Cmon! Lets go in, I'm starving"
                hide ravenhappy

        "We go inside the restaurant and get seated"

        show waiter at center:
            zoom 0.5
        "You sit down with raven at the table and start to look at the menu"
        waiter "Hi guys, welcome in."
        waiter "Can I get you started on any appetizers?"

        menu:
            "Salad":
                $appetizer = "Salad"
                hide waiter
                show ravensurprised at center:
                    zoom 0.5
                raven "Wow what a healthy choice"
                hide ravensurprised
            "French Fries":
                $appetizer = "Fries"
                hide waiter
                show ravenhappy at center:
                    zoom 0.5
                raven "Fries... what a classic"
                raven "Maybe I'll pick a couple off of yours later"
                hide ravenhappy
            "I don't want to order an appetizer":
                hide waiter
                show ravensurprised at center:
                    zoom 0.5
                raven "Not an appetizer person huh."
                hide ravensurprised
        show waiter at center:
            zoom 0.5
        waiter "Alright I'll go get that started for you guys"
        you "Thanks"
        hide waiter

        show ravendefault at center:
            zoom 0.5
        you "So what did you order?"
        raven "I ordered a Steak Tartare with some wine"
        you "Isn't that like raw steak?"
        hide ravendefault
        show ravenannoyed at center:
            zoom 0.5
        raven "Yeah is something wrong with that?"
        you "No not at all!..."
        hide ravenannoyed
        show ravenhappy at center:
            zoom 0.5
        raven "Great, you should try it sometime its not that bad, but kinda pricey"
        hide ravenhappy
        show waiter at center:
            zoom 0.5
        waiter "So I have here a Steak tartare and a glass of wine"
        if(appetizer != ""):
            waiter "I also have an order of [appetizer]"
        
        you "Thank you"

        hide waiter
        show ravendefault at center:
            zoom 0.5
        menu:
            "So... you like wine?":
                hide ravendefault
                show ravenhappy at center:
                    zoom 0.5
                raven "Yeah I love drinking wine, something about it is great..."
                hide ravenhappy
            "Drinking wine this early?":
                hide ravendefault
                show ravenannoyed at center:
                    zoom 0.5
                raven "Yeah you got a problem with that?"
                raven "I'll drink whenever I want to"
                hide ravenannoyed
        show ravensurprised at center:
            zoom 0.5
        raven "Wait a second..."
        raven "This isn't the right drink!"
        hide ravensurprised
        show ravenangry at center:
            zoom 0.5
        raven "Waiter?!"
        hide ravenangry
        show waiter at center:
            zoom 0.5
        waiter "Yes is there a problem?"
        hide waiter
        show ravenangry at center:
            zoom 0.5
        raven "Yeah can I have wine that I ordered, this is champagne"
        hide ravenangry
        show waiter at center:
            zoom 0.5
        waiter "Sorry about that, I'll go get your drink right now"
        hide waiter
        show ravenannoyed at center:
            zoom 0.5
        raven "Ugh, thats annoying."
        you "You really want that wine huh"
        hide ravenannoyed
        show ravensurprised at center:
            zoom 0.5
        raven "Sorry that was a bit out of pocket"
        hide ravensurprised
        show ravenannoyed at center:
            zoom 0.5
        raven "Yeah I was looking forwards to it, since I only ever drink wine from my brothers' place"
        menu:
            "Brother?":
                hide ravenannoyed
                show ravensurprised at center:
                    zoom 0.5
                raven "Yeah I have an older brother who works at a vineyard"
                raven "He's kinda wild though, like he does some crazy shit with his coworkers sometimes"
                hide ravensurprised
            "Tell me more about your brother":
                hide ravenannoyed
                show ravenhappy at center:
                    zoom 0.5
                raven "Yeah, so my brother is older than me by a couple years and he works at a vineyard"
                raven "He comes back every once in a while to ask me do some some favors for him but thats about it, I don't see him often"
                hide ravenhappy
        show waiter at center:
            zoom 0.5
        waiter "Do you want to order any entrees?"
        hide waiter
        show ravendefault at center:
            zoom 0.5
        raven "I'll have a steak"
        hide ravendefault
        show waiter at center:
            zoom 0.5
        waiter "And for you?"
        menu:
            "Steak":
                waiter "excellent choice, I'll be back with that shortly"
                hide waiter
            "Whatever you suggest":
                waiter "I'd suggest the Lobster risotto special that we have"
                you "I'll have that then"
                waiter "Great, I'll be back with those soon"
                hide waiter
            "I'm Ok":
                waiter "Thats ok. Let me know if you need anything else"
                hide waiter
        "Some time passes and the waiter brings us our dishes"
        show ravenhappy at center:
            zoom 0.5
        raven "Wow this looks so good I can't wait to dig in!"

        "Raven starts skillfully spinning the steak knife in her hand in excitement"

        menu:
            "Careful with that":
                hide ravenhappy
                show ravenblush at center:
                    zoom 0.5
                raven "Don't worry I've done this enough to be good at it"
                raven "You aren't in danger unless you want to be"
                hide ravenblush
                show ravendefault at center:
                    zoom 0.5
                raven "..."
                raven ".."
                hide ravendefault
                show ravenangry at center:
                    zoom 0.5
                raven "!"
                hide ravenangry
                show ravenhappy at center:
                    zoom 0.5
                raven "just kidding! Why would I do that?"
                hide ravenhappy
            "Woah put that down":
                hide ravenhappy
                show ravenannoyed at center:
                    zoom 0.5
                raven "what you don't trust me enough to hold a knife?"
                raven "You wouldn't be in danger unless you piss me off"
                hide ravenannoyed
                show ravendefault at center:
                    zoom 0.5
                raven "..."
                raven ".."
                hide ravendefault
                show ravenangry at center:
                    zoom 0.5
                raven "!"
                hide ravenangry
                show ravenhappy at center:
                    zoom 0.5
                raven "just kidding! Why would I do that?"
                hide ravenhappy
            "Damn thats cool":
                hide ravenhappy
                show ravenblush at center:
                    zoom 0.5
                raven "Right?! I learned this from my brother a while back"
                raven "Most people get scared off by this kinda stuff though"
                raven "I haven't dropped or screwed up my knife spinning since like a couple of years ago I think"
                hide ravenblush

        "A while passes and we both finish our food and clear out of the restaurant"

        show ravensad at center:
            zoom 0.5
        raven "Maaan I am stuffed, that steak was way too much food"
        raven "We should probably walk off the food..."
        raven "So I was thinking, theres that new carnival that opened up recently, we could head there if you want to"
        menu:
            "Sounds good":
                hide ravensad
                show ravenhappy at center:
                    zoom 0.5
                raven "great lets head over there"
                hide ravenhappy
            "Carnival?":
                hide ravensad
                show ravensurprised at center:
                    zoom 0.5
                raven "Yeah the new one? its apparently really cool and the first week is free entry"
                you "Free Entry?! I'm in"
                hide ravensurprised
                show ravenhappy at center:
                    zoom 0.5
                raven "great lets go then"
                hide ravenhappy
        "This is the end of restaurant scene"


    "You arrive at the carnival with Raven."
    scene carnival at center:
        zoom 7
        "carnival.png"
    play sound "carnival.mp3"

    show ravendefault at center:
        zoom 0.5

    # These display lines of dialogue.

    raven "Hey [you], glad you could make it, how was the ride here?"

    menu:
        "Hey Raven, it was alright! How about yours?":
            jump carnival_route

        "Hi... uh, it was good.":
            jump suspicious_route
    
    label suspicious_route:
        $sus_points += 1
        hide ravendefault
        show ravensurprised at center:
            zoom 0.5
        "An interesting first question to be asked. It seems normal at first but its just a bit of an odd choice..."
        raven "Good. I'm glad."
        raven "Let's go to the Ferris wheel and enjoy the view."

        menu:
            "I'm good, ferris wheels are kinda boring":
                hide ravensurprised
                show ravenannoyed at center:
                    zoom 0.5
                $sus_points += 1
                raven "What?! I love ferris wheels, they give us such a nice view! I'm going regardless."
                you "Ok fine I'll go with you"
                hide ravenannoyed
                show ravenblush at center:
                    zoom 0.5
                raven "Great! lets go!"
                jump ferris_wheel
            "Sure! lets go check it out!":
                hide ravensurprised
                show ravenblush at center:
                    zoom 0.5
                raven "Great! I love that we're on the same page"
                jump ferris_wheel

        
    label carnival_route:
        hide ravenblush
        show ravenhappy at center:
            zoom 0.5
        raven "Mine was great!"
        raven "Hey let's go to the Ferris wheel! I want to see the view from the top."
        hide ravenhappy
        show ravendefault at center:
            zoom 0.5
        menu:
            "I'm good, ferris wheels are kinda boring":
                hide ravendefault
                show ravenannoyed at center:
                    zoom 0.5
                $sus_points += 1
                raven "What?! I love ferris wheels, they give us such a nice view! I'm going regardless."
                you "Ok fine I'll go with you"
                hide ravenannoyed
                show ravenblush at center:
                    zoom 0.5
                raven "Great! lets go!"
                jump ferris_wheel
            "Sure! lets go check it out!":
                hide ravendefault
                show ravenblush at center:
                    zoom 0.5
                raven "Great! I love that we're on the same page"
                jump ferris_wheel

    label ferris_wheel:

        "Raven and I get on the Ferris wheel."
        "The city lights grew smaller and smaller as we rose up into the darkened sky."
        hide ravenblush
        show ravendefault at center:
            zoom 0.5

        raven "I love this view! It's so peaceful and this breeze is to die for."

        you "I agree, it really is something else."

        "Suddenly, I remember looking through her dating profile and I didn't see anything about other social media 
        platforms online."
        "Its almost as if she is trying to hide her online presence"
        menu:

            "So, do you have social media or anything?":
                $sus_points += 1
                jump suspicious_route2

            "What do you like to do on your free time?":
                jump carnival_route2

    
    label suspicious_route2:
        hide ravendefault
        show ravensad at center:
            zoom 0.5
        raven "Oh, I don't really like social media. I don't want everyone to be all up in my business you know."
        "that felt like a sore topic, and things got more awkward..."
        you "Yeah I can see that, it can get pretty invasive and toxic."
        hide ravensad
        show ravendefault at center:
            zoom 0.5
        jump movie
        
    label carnival_route2:
        hide ravendefault
        show ravenhappy at center:
            zoom 0.5
        raven "Hmm... lately I've been really into cooking!"
        raven "There's just something so satisfying about putting in the work to feed yourself when hungry."
        you "Wow, I wish I could cook, lately it's just been takeout for me"
        you "I buy groceries, but I don't even know what I could make. I've failed too much..."
        raven "I could come over and see what I can make for you! I'm pretty good at improvising."
        hide ravenhappy
        show ravenblush at center:
            zoom 0.5
        you "You'd do that? That would be great! A homecooked meal is a dream come true."
        jump movie

    label movie:
        raven "So what genres of shows do you like to watch?"
        menu:
            "Crime shows":
                $sus_points += 1
                jump suspicious_route3
            "Anime":
                jump normal_route3
            "I don't watch TV":
                jump endingChoice
            "Comedies":
                jump endingChoice2

    label suspicious_route3:
        hide ravendefault
        show ravensurprised at center:
            zoom 0.5
        raven "I see."
        you "... Yeah, I think it's pretty interesting, getting into the minds of all those people and seeing why they did it."
        raven "Why don't we head to my place and watch some later tonight?"
        raven "I've never seen anything like that show."
        you "Sure. I'd be happy to share my interests!"
        jump wrapUpCarnival
        return

    label normal_route3:
        hide ravendefault
        show ravensurprised at center:
            zoom 0.5
        raven "Woah you're into anime? That's sick! I've also been trying to catch up on Demon Slayer."
        raven "My roommate actually broke our TV though, so I haven't been able to watch anything on a bigger screen."
        you "Damn that sucks. If you want to, we can watch the new episode at my place after this."
        hide ravensurprised
        show ravenblush at center:
            zoom 0.5
        raven "Sounds great!"
        jump wrapUpCarnival
        return

    label endingChoice:
        hide ravendefault
        show ravensurprised at center:
            zoom 0.5
        raven "Wait you don't watch any TV!?"
        raven "I should show you some good shows or movies"
        hide ravensurprised
        show ravenhappy at center:
            zoom 0.5
        you "Sounds great! We can watch some at:"
        menu:
            "my place":
                you "my place later!"
                hide ravenhappy
                show ravenblush at center:
                    zoom 0.5
                raven "Sure! I'd be glad to go to your place!"
                jump playerHouse
                return
            "her place":
                you "your place, if you can"
                hide ravenhappy
                show ravensurprised at center:
                    zoom 0.5
                raven "MY place!? I..."
                raven "uh..."
                hide ravensurprised
                show ravenblush at center:
                    zoom 0.5
                raven "Sure...! Lets do my place"
                jump ravenHouse
                return

    label endingChoice2:
        hide ravendefault
        show ravensurprised at center:
            zoom 0.5
        raven "Woah you don't seem like the kind of guy to watch comedies"
        you "Yeah I have a funny bone in me..."
        hide ravensurprised
        show ravenhappy at center:
            zoom 0.5
        raven "Yeah I guess people like what they like, I haven't seen many comedies"
        you "I can show you a couple of my favorites if you have time"
        raven "I have time right now, where do you want to go?"
        menu:
            "my place":
                you "We can go to my place"
                hide ravenhappy
                show ravenblush at center:
                    zoom 0.5
                raven "Sure! I'd be glad to go to your place!"
                jump playerHouse
                return
            "her place":
                you "your place, if you can"
                hide ravenhappy
                show ravensurprised at center:
                    zoom 0.5
                raven "MY place!? I..."
                raven "uh..."
                hide ravensurprised
                show ravenblush at center:
                    zoom 0.5
                raven "Sure...! Lets do my place"
                jump ravenHouse
                return
    
    label wrapUpCarnival:
        hide ravensurprised
        "We had fun at the carnival for some more time"
        "After a while"
        show ravendefault at center:
            zoom 0.5
        raven "This carnival is so much fun, but I'm getting tired, do you want to go somewhere else?"
        "Honestly, food, a good walk around the carnival, I'm feeling tired too"
        "How about..."
        menu:    
            "my place":
                you "We can go to my place"
                hide ravendefault
                show ravenblush at center:
                    zoom 0.5
                raven "Sure! I'd be glad to go to your place!"
                jump playerHouse
                return
            "your place":
                you "your place, if you can"
                hide ravendefault
                show ravensurprised at center:
                    zoom 0.5
                raven "MY place!? I..."
                raven "uh..."
                hide ravensurprised
                show ravenblush at center:
                    zoom 0.5
                raven "Sure...! Lets do my place"
                jump ravenHouse
                return

    label playerHouse:
        hide ravenblush
        "We leave the carnival with Raven and go to my apartment"
        hide carnival
        "We talked some more about what we did, and finally arrive at my place"
        show ravendefault at center:
            zoom 0.5 
        raven "Oh wow, this is such a nice apartment!"
        raven "The area feels so nice and cozy too. Thanks for inviting me!"
        menu: 
            "Yeah, no problem.":
                you "Yeah, no problem."
                jump stopFlirt
                return
            "It’s all good, having you here feels nice too.":
                you "It’s all good, having you here feels nice too."
                jump flirt
                return
    
    label flirt:
        raven "Oh, it’s such a shame that I’m here for just a little while."
        menu: 
            "I wish you’d stay here longer":
                jump Flirt2
                return
            "So what do you want to do?":
                jump StopFlirt
                return

    label Flirt2:

        raven "I can stay for as long as you want me to. I live alone, and I feel lonely at times, but today feels really different for some reason."

        "Raven smiles at you"

        "You continue to flirt with Raven"

        jump stopFlirt
        return

    label stopFlirt:

        raven "What do YOU want to do? Do you want to watch a movie or something?"

        raven "Can you play a horror movie? I love those so much!"

        "You comply and play a horror movie."

        jump movieStarts
        return


    label movieStarts:

        "The movie has been playing for a while and Raven seems unusually excited."

        menu:

            "Why do you like these movies so much?":
                jump questioning
                return
            "Stay quiet and enjoy the movie.":

                jump startScene
                return

    label questioning:

        raven "I just like the serial killers topic, you know?"

        raven "I don’t know how to explain it, but they could be anywhere!"

        raven "Have you ever thought that while you’re walking across a group of people, you might’ve crossed more than one serial killer?"

        raven "It’s the mystery that I enjoy the most."

        menu:

            "Well, that’s just scary to think about.":

                jump annoySK


            "That does sound exciting!":

                jump agreeSK

    label annoySK:

        raven "Bro, you really need to chill. Can’t you just let me enjoy what I like?"

        raven "Seriously, it’s really annoying that people just criticize what I enjoy for no reason"

        jump startScene

    label agreeSK:

        raven "Right?!?!?! Finally, someone who gets it. You don’t need to be a serial killer to enjoy learning what they did."

        raven "People just instantly assume that just because you enjoy the whole serial killer topic, you’re very likely to be one, but that’s just them being stupid."

        jump startScene

    label StartScene:

        "The movie ends"

        raven "Damn that was fun, I was so impressed when they showed his body count in such a short amount of time"

        raven "50 people in just 4 days, can you imagine? That’s a record if I’ve seen one. I’m only at two, and that’s still a lot."

        menu:

            "What do you mean by “two”?":
                jump playerKilled

            "Yeah, that movie was great!":
                
                jump avoidDeath

    label playerKilled:

        raven "What? Did I say something wrong?"
        raven "Oh? You mean the two? Oh yeah, the first one was accidental, but the second one was really fun."

        menu: 

            "Fun?":
                jump playerKilled2 

    label playerKilled2:

        raven "Yeah, It’s so fun. The sheer despair that those fools showed as they were grunting in pain was like music to my ears."

        raven "Remember my brother? He owns a wine shop. He likes to make his own wine, but long story short, while he was opening a bottle with a katana."

        raven "The katana is a weird story, but that’s not important right now. Surprise!"

        jump finishKill 

    label finishKill:

        raven "So, how do you want to die? Stabbing? Asphyxiation? Overdose? Although that one is the most painless, so it’s way less fun"

        menu: 

            "So you’re just going to pretend like I’m not going to defend myself?":

                jump defenseAttempt

            "I’m going to call the cops on you":

                jump death 

    label defenseAttempt:

        raven "Oh please, by all means, do try. It makes it more thrilling when they fight back"

        "You run to the kitchen to grab any type of weapon to defend yourself against the killer who’s revealed her true identity to you, until…"

        raven "Come on, you really didn’t think you could just run, right? "

        raven "At least, make me work a little harder for this. Seriously, it’s just good manners"

        "Just as Raven finished talking, she stabs your leg with a knife."

        raven "kitchens in general are filled with so many instruments that just make my life so much easier for my prey, you know? "

        raven "Oh well, it’s been nice meeting you, but I just wanted to have my fun with you a while longer. "

        raven "Anywhooo, nice try, sweetie!"

        "The rest of her speech is disrupted in your ears as the only thing you can hear are your own screams as she just continuously stabs you in the chest."

        jump ending2

    label ending2:

        "Some weeks later"

        "And that concludes the report on the weather today."

        "In other news, two new serial killers have been sighted in the area these past few weeks and police have been struggling to get clues on the identities of these two."

        "If you have any clues about the identities of these maniacs, call 911."

        "We’re going through some dark times at the moment, folks."

        "Stay safe out there, and if you ever believe you could be in danger, don’t hesitate to call out for help."

        "The end."



    label avoidDeath:

        raven "Hey, I had a really nice time today. It’s been really fun hanging out with you"

        menu: 

            "Yeah, me too. I’ll call you again sometime.":

                jump byeKiller

            "It’s been okay, I guess":

                jump byeKiller



    label byeKiller:

    "Raven packs her stuff, and prepares to leave."

    "As she leaves the house, you reminisce on today’s events and decide to call it a night."

    "What did Raven mean by 'I\'m only at two'?" 

    "Oh well, I guess it doesn't matter. I got class tomorrow, so I should just hit the sack."

    "The End."
    

    label ravenHouse:
        "This is raven house"
        return
    # This ends the game.

    return
