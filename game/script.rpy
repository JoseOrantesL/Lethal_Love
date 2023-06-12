# The script of the game goes in this file.

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
    scene bedroom at center:
        "bedroom.png"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    "I pull myself out of bed to the sound of my alarm and my phone buzzing."
    "I see a text on my phone from a girl, Raven, who I met through a dating app online."
    raven "I can't wait to see you today _______!"
    python:
        name = renpy.input("Enter Your Name:")

        name = name.strip() or "You"
    "I arranged a date with her at a nice restaurant."
    "I should probably get ready and find something appropriate to wear..."
    menu:
        "Formal Suit":
            "This looks nice, but might be a bit too fancy for a first meeting."
            $suit = True
            menu:
                "Semi-Formal Suit" if suit == True:
                    "This is perfect fit for the date!"
                    "I should get going to the restaurant."
                    scene restaurant
                    jump restaurantDate
                "Bright Graphic t-shirt":
                    "No way I'm wearing this to the first date, though it could be a conversation starter.."
                    menu:
                        "Semi-Formal Suit" if suit == True:
                            "This is perfect fit for the date!"
                            "I should get going to the restaurant."
                            scene restaurant
                            jump restaurantDate
        "Bright Graphic t-shirt":
            "No way I'm wearing this to the first date, though it could be a conversation starter.."
            menu:
                "Formal Suit":
                    "This looks nice, but might be a bit too fancy for a first meeting."
                    $suit = True
                    menu:
                        "Semi-Formal Suit":
                            "This is a perfect fit for the date!"
                            "I should get going to the restaurant."
                            scene restaurant
                            jump restaurantDate
                "Semi-Formal Suit" if suit == True:
                    "This is perfect fit for the date!"
                    "I should get going to the restaurant."
                    scene restaurant
                    jump restaurantDate

    label restaurantDate:
        "I arrive at the restaurant a bit early and wait a bit until I see someone who ressembles the person in Raven's profile picture."
        "Suddenly, I hear a voice -"
        raven "[you]!"
        "I turn around and see the person that I've been longing to talk to."
        show ravendefault at center:
            zoom 0.5
        raven "Have you been waiting long?"

        menu:
            "Not at all!":
                you "Not really, I just got here."
                hide ravendefault
                show ravenhappy at center:
                    zoom 0.5
                raven "Great! Shall we get going?"
                hide ravenhappy
            "I've been waiting forever.":
                you "Yeah I've been waiting for hours."
                hide ravendefault 
                show ravensurprised at center:
                    zoom 0.5
                raven "Oh really?! Sorry, I didn't realize you were coming so soon or I would've left earlier."
                you "No, that was a joke haha... I barely got here too."
                hide ravensurprised
                show ravenhappy at center:
                    zoom 0.5
                raven "Oh, sorry I haven't adjusted to your sarcasm yet haha... Let's get going! I'm hungry."
                hide ravenhappy
            "I would wait forever for you.":
                you "I'd wait forever for you."
                hide ravendefault
                show ravenblush at center:
                    zoom 0.5
                raven "Oh, stop it!"
                raven "I know you just got here too."
                hide ravenblush 
                show ravenhappy at center:
                    zoom 0.5
                raven "C'mon! Let's go in. I'm starving."
                hide ravenhappy

        "We head inside the restaurant and get seated."
        play sound "restaurantmusic.mp3"
        
        show waiter at center:
            zoom 0.5
        "I sit down with Raven at the table and start to look at the menu."
        waiter "Hi guys, welcome in."
        waiter "Can I get you started on any appetizers?"

        menu:
            "Salad":
                $appetizer = "Salad"
                hide waiter
                show ravensurprised at center:
                    zoom 0.5
                raven "Wow, what a healthy choice."
                hide ravensurprised
            "French Fries":
                $appetizer = "Fries"
                hide waiter
                show ravenhappy at center:
                    zoom 0.5
                raven "Fries... what a classic."
                raven "Maybe I'll pick a couple off of yours later."
                hide ravenhappy
            "I think I'm good.":
                hide waiter
                show ravensurprised at center:
                    zoom 0.5
                raven "Not an appetizer person, huh?"
                hide ravensurprised
        show waiter at center:
            zoom 0.5
        waiter "Alright, I'll go get that started for you guys."
        you "Thanks."
        hide waiter

        show ravendefault at center:
            zoom 0.5
        you "So what did you order?"
        raven "I ordered a Steak Tartare with some wine."
        you "Isn't that like raw steak?"
        hide ravendefault
        show ravenannoyed at center:
            zoom 0.5
        raven "Yeah, is something wrong with that?"
        you "No not at all!..."
        hide ravenannoyed
        show ravenhappy at center:
            zoom 0.5
        raven "Great, you should try it sometime! It's not that bad, but kinda pricy."
        hide ravenhappy
        show waiter at center:
            zoom 0.5
        waiter "So, I have here a Steak tartare and a glass of wine."
        if(appetizer != ""):
            waiter "I also have an order of [appetizer]"
        
        you "Thank you."

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
                raven "Yeah. You got a problem with that?"
                raven "I'll drink whenever I want to."
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
        waiter "Yes, is there a problem?"
        hide waiter
        show ravenangry at center:
            zoom 0.5
        raven "Yeah. Can I have wine that I ordered? This is champagne."
        hide ravenangry
        show waiter at center:
            zoom 0.5
        waiter "Sorry about that. I'll go get your drink right now."
        hide waiter
        show ravenannoyed at center:
            zoom 0.5
        raven "Ugh, that's annoying."
        you "You really want that wine, huh."
        hide ravenannoyed
        show ravensurprised at center:
            zoom 0.5
        raven "Sorry, that was a bit out of pocket."
        hide ravensurprised
        show ravenannoyed at center:
            zoom 0.5
        raven "Yeah, I was looking forward to it, since I only ever drink wine from my brothers' place."
        menu:
            "Brother?":
                hide ravenannoyed
                show ravensurprised at center:
                    zoom 0.5
                raven "Yeah, I have an older brother who works at a vineyard."
                raven "He's kinda wild though, like he does some crazy shit with his coworkers sometimes."
                hide ravensurprised
            "Tell me more about your brother.":
                hide ravenannoyed
                show ravenhappy at center:
                    zoom 0.5
                raven "Yeah, so my brother is older than me by a couple years and he works at a vineyard."
                raven "He comes back every once in a while to ask me do some some favors for him but thats about it. I don't see him often."
                hide ravenhappy
        show waiter at center:
            zoom 0.5
        waiter "Do you want to order any entrees?"
        hide waiter
        show ravendefault at center:
            zoom 0.5
        raven "I'll have a steak."
        hide ravendefault
        show waiter at center:
            zoom 0.5
        waiter "And for you?"
        menu:
            "Steak":
                waiter "Excellent choice, I'll be back with that shortly."
                hide waiter
            "Whatever you suggest.":
                waiter "I'd suggest the Lobster Risotto special that we have."
                you "I'll have that then."
                waiter "Great, I'll be back with those soon."
                hide waiter
            "I'm okay.":
                waiter "That's alright. Let me know if you need anything else."
                hide waiter
        "Some time passes and the waiter brings us our dishes."
        show ravenhappy at center:
            zoom 0.5
        raven "Wow, this looks so good! I can't wait to dig in!"

        "Raven starts skillfully spinning the steak knife in her hand in excitement."

        menu:
            "Careful with that...":
                hide ravenhappy
                show ravenblush at center:
                    zoom 0.5
                raven "Don't worry, I've done this enough to be good at it."
                raven "You aren't in danger unless you want to be."
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
                raven "Just kidding! Why would I do that?"
                hide ravenhappy
            "Woah, put that down.":
                hide ravenhappy
                show ravenannoyed at center:
                    zoom 0.5
                raven "What, you don't trust me enough to hold a knife?"
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
                raven "Just kidding! Why would I do that?"
                hide ravenhappy
            "Damn, thats cool.":
                hide ravenhappy
                show ravenblush at center:
                    zoom 0.5
                raven "Right?! I learned this from my brother, a while back."
                raven "Most people get scared off by this kinda stuff though."
                raven "I haven't dropped or screwed up my knife spinning since like a couple of years ago, I think."
                hide ravenblush

        "We both finish our food and clear out of the restaurant."

        show ravensad at center:
            zoom 0.5
        raven "Maaan... I am stuffed, that was way too much food."
        raven "We should probably walk it off..."
        raven "So I was thinking, there's that new carnival that opened up recently. We could head there if you want to."
        menu:
            "Sounds good!":
                hide ravensad
                show ravenhappy at center:
                    zoom 0.5
                raven "Great! Let's head over there."
                hide ravenhappy
            "Carnival?":
                hide ravensad
                show ravensurprised at center:
                    zoom 0.5
                raven "Yeah, the new one? It's apparently really cool, and the first week is free entry."
                you "Free Entry?! I'm in."
                hide ravensurprised
                show ravenhappy at center:
                    zoom 0.5
                raven "Great! Let's go then."
                hide ravenhappy

    "I arrive at the carnival with Raven."
    scene carnival at center:
        "carnivalday.jpg"
    play sound "carnival.mp3"
    show ravendefault at center:
        zoom 0.5

    raven "Yay! We're here. Happy places like these really cheer me up. It's a nice change of pace."

    menu:
        "Same! It's so bright and colorful.":
            jump carnival_route

        "Change of pace...?":
            jump suspicious_route
    
    label suspicious_route:
        $sus_points += 1
        hide ravendefault
        show ravensurprised at center:
            zoom 0.5
        raven "I don't know how to explain it."
        raven "Let's go to the Ferris wheel and enjoy the view."

        menu:
            "I'm good, ferris wheels are kinda boring.":
                hide ravensurprised
                show ravenannoyed at center:
                    zoom 0.5
                $sus_points += 1
                raven "What?! I love ferris wheels, they give us such a nice view! I'm going regardless."
                you "Okay fine, I'll go with you."
                hide ravenannoyed
                show ravenblush at center:
                    zoom 0.5
                raven "Great! Let's go!"
                jump ferris_wheel
            "Sure! Let's go check it out!":
                hide ravensurprised
                show ravenblush at center:
                    zoom 0.5
                raven "Great! I love that we're on the same page.s"
                jump ferris_wheel

        
    label carnival_route:
        hide ravenblush
        show ravenhappy at center:
            zoom 0.5
        raven "Hehe..."
        raven "Hey, let's go to the Ferris wheel! I want to see the view from the top."
        hide ravenhappy
        show ravendefault at center:
            zoom 0.5
        menu:
            "I'm good, ferris wheels are kinda boring.":
                hide ravensurprised
                show ravenannoyed at center:
                    zoom 0.5
                $sus_points += 1
                raven "What?! I love ferris wheels, they give us such a nice view! I'm going regardless."
                you "Okay fine, I'll go with you."
                hide ravenannoyed
                show ravenblush at center:
                    zoom 0.5
                raven "Great! Let's go!"
                jump ferris_wheel
            "Sure! Let's go check it out!":
                hide ravensurprised
                show ravenblush at center:
                    zoom 0.5
                raven "Great! I love that we're on the same page.s"
                jump ferris_wheel

    label ferris_wheel:

        "Raven and I get on the Ferris wheel."
        "The city lights grew smaller and smaller as we rose up into the bright sky."
        hide ravenblush
        show ravendefault at center:
            zoom 0.5

        raven "I love this view! It's so peaceful, and this breeze is to die for."

        you "I agree, it really is something else."

        "Suddenly, I remember looking through her dating profile and I didn't see anything about other social media 
        platforms online."
        "...Almost as if she is trying to hide her online presence."
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
        raven "I should show you some good shows or movies."
        hide ravensurprised
        show ravenhappy at center:
            zoom 0.5
        you "Sounds great! We can watch some at:"
        menu:
            "My place":
                you "...my place later!"
                hide ravenhappy
                show ravenblush at center:
                    zoom 0.5
                raven "Sure! I'd be glad to go to your place!"
                jump playerHouse
                return
            "Her place":
                you "...your place, if you can."
                hide ravenhappy
                show ravensurprised at center:
                    zoom 0.5
                raven "MY place!? I..."
                raven "uh..."
                hide ravensurprised
                show ravenblush at center:
                    zoom 0.5
                raven "Sure...! Let's do my place."
                jump ravenHouse
                return

    label endingChoice2:
        hide ravendefault
        show ravensurprised at center:
            zoom 0.5
        raven "Woah, you don't seem like the kind of guy to watch comedies."
        you "Yeah I have a funny bone in me..."
        hide ravensurprised
        show ravenhappy at center:
            zoom 0.5
        raven "Yeah, I guess people like what they like. I haven't seen many comedies."
        you "I can show you a couple of my favorites if you have time."
        raven "I have time right now, where do you want to go?"
        menu:
            "My place":
                you "...my place later!"
                hide ravenhappy
                show ravenblush at center:
                    zoom 0.5
                raven "Sure! I'd be glad to go to your place!"
                jump playerHouse
                return
            "Her place":
                you "...your place, if you can."
                hide ravenhappy
                show ravensurprised at center:
                    zoom 0.5
                raven "MY place!? I..."
                raven "uh..."
                hide ravensurprised
                show ravenblush at center:
                    zoom 0.5
                raven "Sure...! Let's do my place."
                jump ravenHouse
                return
    
    label wrapUpCarnival:
        hide ravensurprised
        "We had fun at the carnival for some more time."
        show ravendefault at center:
            zoom 0.5
        raven "This carnival is so much fun, but I'm getting tired, do you want to go somewhere else?"
        "Honestly, food, a good walk around the carnival, I'm feeling tired too."
        "How about..."
        menu:
            "My place":
                you "...my place later!"
                hide ravenhappy
                show ravenblush at center:
                    zoom 0.5
                raven "Sure! I'd be glad to go to your place!"
                hide ravendefault
                jump playerHouse
                return
            "Her place":
                you "...your place, if you can."
                hide ravenhappy
                show ravensurprised at center:
                    zoom 0.5
                raven "MY place!? I..."
                raven "uh..."
                hide ravensurprised
                show ravenblush at center:
                    zoom 0.5
                raven "Sure...! Let's do my place."
                jump ravenHouse
                return

    label playerHouse:
        hide ravenblush
        
        "We leave the carnival with Raven and go to my apartment."
        hide carnival
        scene playerhouse at center:
            "playerhouse.png"
        "We talked some more about what we did, and finally arrive at my place."
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
                hide ravendefault
                show ravenblush at center:
                    zoom 0.5
                jump flirt
                return
    
    label flirt:
        raven "Oh, it’s such a shame that I’m here for just a little while."
        menu: 
            "I wish you’d stay here longer.":
                you "I wish you’d stay here longer."
                jump Flirt2
                return
            "So what do you want to do?":
                you "So what do you want to do?"
                jump StopFlirt
                return

    label Flirt2:
        raven "I can stay for as long as you want me to. I live alone, and I feel lonely at times, but today feels really different for some reason."
        "Raven smiles at you"
        "I continued to flirt with Raven."

        jump stopFlirt
        return

    label stopFlirt:
        hide ravenblush
        show ravendefault at center:
            zoom 0.5
        raven "What do YOU want to do? Do you want to watch a movie or something?"
        raven "Can you play a horror movie? I love those so much!"
        "You comply and play a horror movie."

        jump movieStarts
        return


    label movieStarts:
        hide ravendefault
        show ravenhappy at center:
            zoom 0.5
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
        hide ravenhappy
        show ravenannoyed at center:
            zoom 0.5
        raven "Bro, you really need to chill. Can’t you just let me enjoy what I like?"
        raven "Seriously, it’s really annoying that people just criticize what I enjoy for no reason"
        hide ravenannoyed
        jump startScene

    label agreeSK:
        
        raven "Right?!?!?! Finally, someone who gets it. You don’t need to be a serial killer to enjoy learning what they did."
        raven "People just instantly assume that just because you enjoy the whole serial killer topic, you’re very likely to be one, but that’s just them being stupid."
        hide ravenhappy
        jump startScene

    label startScene:

        "The movie ends"
        show ravendefault at center:
            zoom 0.5
        raven "Damn, that was fun, I was so impressed when they showed his body count in such a short amount of time"
        raven "50 people in just 4 days, can you imagine? That’s a record if I’ve seen one. I’m only at two, and that’s still a lot."
        menu:

            "What do you mean by “two”?":
                jump playerKilled

            "Yeah, that movie was great!":
                
                jump avoidDeath

    label playerKilled:
        hide ravendefault
        show ravensurprised at center:
            zoom 0.5 
        raven "What? Did I say something wrong?"
        raven "Oh? You mean the two? Oh yeah, the first one was accidental, but the second one was really fun."

        menu: 

            "Fun?":
                jump playerKilled2 

    label playerKilled2:
        
        hide ravensurprised
        show ravenblush at center:
            zoom 0.5

        raven "Yeah, It’s so fun. The sheer despair that those fools showed as they were grunting in pain was like music to my ears."
        hide ravenblush
        show ravendefault at center:
            zoom 0.5
        raven "Remember my brother? He owns a wine shop. He likes to make his own wine, but long story short, while he was opening a bottle with a katana."
        raven "The katana is a weird story, but that’s not important right now. Surprise!"

        jump finishKill 

    label finishKill:

        hide ravendefault
        show ravenannoyed at center:
            zoom 0.5 
        raven "So, how do you want to die? Stabbing? Asphyxiation? Overdose? Although that one is the most painless, so it\'s way less fun"

        menu: 

            "So you’re just going to pretend like I’m not going to defend myself?":

                jump defenseAttempt


    label defenseAttempt:
        hide ravenannoyed
        show ravenhappy at center:
            zoom 0.5
        raven "Oh please, by all means, do try. It makes it more thrilling when they fight back"
        "You run to the kitchen to grab any type of weapon to defend yourself against the killer who’s revealed her true identity to you, until…"
        hide ravenhappy
        show ravenannoyed at center:
            zoom 0.5
        raven "Come on, you really didn’t think you could just run, right? "
        raven "At least, make me work a little harder for this. Seriously, it’s just good manners"
        "Just as Raven finished talking, she stabs your leg with a knife."
        menu:
            "WHY ARE YOU DOING THIS?":
                jump defenseTwo

    label defenseTwo:
        hide ravenannoyed
        show ravenhappy at center:
            zoom 0.5
        raven "Why? Because it's fun! Obviously!"
        raven "Did you know that kitchens in general are filled with so many instruments that just make my life so much easier to torture my victim?"
        raven "Oh well, it’s been nice meeting you, but I just wanted to have my fun with you a while longer. "
        hide ravenhappy
        show ravenblush at center:
            zoom 0.5
        raven "Anywhooo, nice try, sweetie!"
        "The rest of her speech is disrupted in your ears as the only thing you can hear are your own screams as she just continuously stabs you in the chest."
        hide ravenblush
        jump ending2

    label ending2:

        "Some weeks later"

        "And that concludes the report on the weather today."

        "In other news, two new serial killers have been sighted in the area these past few weeks and police have been struggling to get clues on the identities of these two."

        "If you have any clues about the identities of these maniacs, call 911."

        "We’re going through some dark times at the moment, folks."

        "Stay safe out there, and if you ever believe you could be in danger, don’t hesitate to call out for help."

        "The end."
        return


    label avoidDeath:

        raven "Hey, I had a really nice time today. It’s been really fun hanging out with you"
        
        menu: 

            "Yeah, me too. I’ll call you again sometime.":

                jump byeKiller

            "It’s been okay, I guess":

                jump byeKiller



    label byeKiller:
        
        hide ravendefault
        "Raven packs her stuff, and prepares to leave."

        "As she leaves the house, you reminisce on today’s events and decide to call it a night."

        "What did Raven mean by 'I\'m only at two'?" 

        "Oh well, I guess it doesn't matter. I got class tomorrow, so I should just hit the sack."

        "The End."
        return

    label ravenHouse:
        hide ravenblush
        "We arrive at Raven's house."
        scene ravenhouse at center:
            "ravenhouse.png"
        "As I step into the darkened room, I begin to get uneasy about the isolated location. 
        It almost seemed as if it was in the middle of nowhere. But then again, rent must be cheap."
        "When I look around and notice that Raven has multiple sharp objects around her house."
        show ravensurprised at center:
            zoom 0.5
        raven "Oh, my bad. It's kind of dark huh? let me turn on a light"
        menu: 

            "Wow, this is a pretty nice place! Thanks for having me over":

                jump nice_response

            "Oh, um… thanks for inviting me here, I won’t be long though.":

                jump evasive_response

    label nice_response:
        hide ravensurprised

        "Raven talks to you in the distance as she goes to the kitchen"

        raven "Why, thanks! Although it gets kind of lonely with just me around here… It feels better with you being here with me"

        "Raven seems pretty cool, although we may have had some weird moments during the date, I’d say it went pretty great"

        jump continueTalk

    label evasive_response:
        
        "Raven talks to you in the distance as she goes to the kitchen"
        hide ravensurprised
        raven "Are you feeling okay there? You seem kind of pale, why don’t you sit down for a minute?"
        "Something about this place seems off for some reason, but I just can\'t what it is"

        jump continueTalk

    label continueTalk:
        "Raven returns from the kitchen with wine and some popcorn."
        show ravendefault at center:
            zoom 0.5
        raven "Say, it’s still early, do you want to watch a movie with me?"

        "Raven proposes an idea that could lead this night into something else"
    
    menu:

        "Um… actually I…":
            jump twist_build_up

        "Well, y…":

            jump twist_build_up

    label twist_build_up:
        hide ravendefault
        "Even before you had a chance to respond, Raven pops a movie into the TV"
        show ravenhappy at center:
            zoom 0.5
        raven "Do you want some wine?"

        menu:

            "Yeah, that sounds great. ":

                jump gotWine

            "Thanks, but I’m good right now. We ate a lot at the restaurant.":

                jump closeToEnding

    label gotWine:

        hide ravendefault
        "Raven leaves to get the wine. After a while she comes back. "
        show ravendefault at center:
            zoom 0.5
        raven "Here you go, I hope you like it! I got it from my brother’s workplace."
        "You take a sip at the wine and the wine has an odd taste"
        "Should I say something about it?"

    menu: 

        "Oh, man. This wine is pretty great, where did you get it?":

            jump good_wine

        "Damn, this is kinda strong":

            jump bad_wine


    label good_wine:

        hide ravendefault
        show ravenhappy at center:
            zoom 0.5
        raven "There’s this store downtown where my brother works, they have some good equipment there. I even go and help him out at times."

        raven "He’s the owner and one of his favorite things to do during the process is the whole sabering the bottles and stuff"
        hide ravenhappy
        show ravensurprised at center:
            zoom 0.5
        raven "You know what that is right? It’s when they have the bottle filled up with the wine and they use a blade to pop it open. I’ve even had to do it a couple of times. It’s fun"
        menu:

            "They actually do that? What the hell?":

                jump knowMoreBlade

            "Oh, wow, I’d love to try that myself sometime":
                hide ravensurprised
                jump continueBadEnding

    label bad_wine:
        hide ravensurprised
        show ravensad at center:
            zoom 0.5
        raven "Oh really? That’s a shame."
        hide ravensad
        hide ravensad
        hide ravendefault
        hide ravenhappy
        jump continueBadEnding

    label continueBadEnding:
        "Things got awkward after that conversation"
        jump closeToEnding


    label knowMoreBlade:
        hide ravensurprised
        show ravenhappy at center:
            zoom 0.5
        raven "Yeah, sometimes they go wild though. Once, my brother used a katana to open a bottle, he completely missed and hit one of his coworkers."

        menu: 

            "Oh man, your brother does some crazy things!":

                jump playCool

            "Uh, he stabbed someone with a katana? That’s funny to you?":
                jump confrontHer


    label playCool:


        raven "I know, right? So funny. Although, the worker was kinda heavy. Last time I saw the body, my brother told me that he was going to take care of it."

        "I decided to ignore Raven’s comment and just play it cool."

        jump closeToEnding

    
    label confrontHer:
        hide ravenhappy
        show ravenangry at center:
            zoom 0.5    
        raven "Um, what’s wrong with you?"

        you "Someone got stabbed by none other than your brother, and your reaction is to laugh about it? When did this happen?"
        hide ravenangry
        show ravenhappy at center:
            zoom 0.5
        raven "Two days ago. My brother asked me to help him get rid of him later too. He just told me to help him carry it to his car and after that I don’t know what happened."

        jump killerUnmasked

    label killerUnmasked:
        hide ravenhappy
        show ravensurprised at center:
            zoom 0.5
        raven "What? Don't tell me you're afraid of me just because of something like that!"
        raven "We were having a nice time, don't you think?"
        menu:
            "Okay, but I don't feel safe being in the same room with a murderer":
                hide ravensurprised
                show ravenannoyed at center:
                    zoom 0.5
                raven "Ugh, fine. Let's just finish the damn movie and leave if you want to"
                hide ravenannoyed
                jump closeToEnding
            "Yeah, you're right let's just finish the movie":
                hide ravensurprised
                show ravenhappy at center:
                    zoom 0.5
                raven "Yay!"
                jump closeToEnding


        

    label closeToEnding:
        hide ravenhappy
        "We continued watching the movie with Raven in silence."

        "Raven starts falling asleep while watching the movie, so you decide to start preparing to leave."
        show ravendefault at center:
            zoom 0.5
        raven "Hey, I had a really nice time today. Do you mind doing me a favor before you go though?"

        menu:

            " A favor? Sure, what’s up?":

                jump trap

            "Sorry, but It’s getting kinda late, so I want to get home soon but I’ll call you.":

                jump PlayerEscapes

    label trap:

        raven "Do you mind grabbing for me a couple of pills that I have in the kitchen? I have a bad headache right now. I think I drank too much."
        hide ravendefault
        "You go into the kitchen, leaving Raven behind. You see the pills above a shelf and reach for them until you suddenly lose consciousness."

        jump SerialKiller

    label PlayerEscapes:
        hide ravendefault
        "The night continues, yet you decided to go home for the night."
        "Raven and you say to each other your goodbyes, and you start the trek back home."

    #Start from here 
        jump BackHome

    label SerialKiller:
        
        scene basement at center:
            zoom 2
            "basement.jpg"
        show ravenannoyed at center:
            zoom 0.5
        raven "Well, can you wake up?! I swear, I even tried to just knock you down with the wine, but damn you sure took a couple of blows before you lost consciousness."

        "You wake up to a yelling Raven in front of you."

    menu: 

        "What is going on here?":
            jump capturedAnswerOne

        "What happened?":
            jump capturedAnswerTwo

    label capturedAnswerOne:

        hide ravenannoyed
        show ravenangry at center:
            zoom 0.5

        raven "WhAt iS gOiNG on… if you focus for once, you’d notice that you’re trapped. DUH."

        raven "I guess picking up on clues and realizing your current situation are two things you really suck at."

        raven "or what? Did you really feel that I was interested in you? Have you watched the news recently?"

        raven "Oh, wild serial killer going on a rampage. I swear, those idiots are exaggerating. I only killed two people, and one wasn’t even me. It was my brother, I just happened to be there at the wrong time."

        jump backOnTrack


    label capturedAnswerTwo:

        raven "wHaT HapPenNed? Ugh, I can’t deal with you anymore. I kidnapped you. I thought that would be obvious with the ropes on your extremities and the basement?"

        raven "If you didn’t notice, the “weird taste” in the wine were some drugs I put in there to knock you out. "

        jump backOnTrack


    label backOnTrack:

        "raven just keeps complaining about her situation"

        menu:
            "Why are you doing this?":
                jump setUpKill

    label setUpKill:
        hide ravenangry
        show ravenhappy at center:
            zoom 0.5
        raven "Why? Well, If I’m being honest, when my brother killed that coworker, I felt a surge of adrenaline in my body. "

        raven "You see, killing is depicted as such a bad act and you shouldn’t do it, but… heh"
        hide ravenhappy
        show ravenblush at center:
            zoom 0.5
        raven "When I killed my first victim, I’m telling you, I never felt more alive. "

        raven "His screams were music to my ears, his grunts as he was falling to the floor were so damn satisfying, I just knew I had to keep going."

        raven "So I went into this dating app where I just knew it’d be easy to lure people into my house."

        raven "I just had to pretend to be interested in whatever crap they’re saying and hey, sometimes I can get away with a free meal or two. "
        
        raven "But I digress, anyway, enjoy being on the news tomorrow. Be sure to make a pretty face for them when they find you… assuming they do, of course"
        hide ravenblush
        "As soon as Raven finishes talking she grabs a knife and starts stabbing you."

        "All you can really hear is her laugh as she continues to pull that knife in and out of your body."

        jump newsFlash


    label newsFlash:
        
        "A month later"

        "The killer’s whereabouts are still unknown to this day. A body was recently found at a carnival that was taking place in town weeks ago. "

        "Several injuries were found in the body from what appear to be knife stabs. The killer is suspected to be the same one related to a worker in a wine store."

        "Be safe out there, folks. The killer is still out there, and we don’t know where, how, or when we are going to catch whoever it is."

        "The End."
    return

    #Ending 3, Raven’s House: Player escapes.

    label BackHome:
        scene playerhouse at center:
            "playerhouse.png"

        "You arrive back home. "

        "It for sure was a long day"

        "You get ready to go to bed, and as soon as your head hits the pillow, you doze off."

        "The next morning, you start your day just as any other. You get ready to go to your classes, so while making breakfast, you pick up your phone and hop into social media."

        "As you scroll down, you stumble upon a headline that says “Disturbing news in regards to the case about the two serial killers that are running rampant even today.”"

        "You continue to read"

        "“A new body was found in the killer’s car. After the killer was interrogated, he revealed that his sister helped him with the murder.”

        “The whereabouts of his accomplice are unknown, although some witnesses claim that she was seen eating at a restaurant with someone else, and later that night, another witness claims that she was seen walking around the carnival downtown.”"

        "“If you see a person with this description” * Show picture of Raven * “Beware, as she is a serial killer on the run”"

        "The End."

    # This ends the game.

    return
