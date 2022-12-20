
# backgrounds
image blackBg = "backgrounds/blackBackground.jpg"

image wakeUp = "backgrounds/wakeUp.jpg"

image windowView = "backgrounds/windowView.jpg"

image window = "backgrounds/window.jpg"
image windowBluered = "backgrounds/windowBluered.jpg"




# characters
define leon = Character("Леон")
image leon = "characters/leon.png"




# music
define audio.alarmRing = "audio/alarmRing.wav"

define audio.birdsong = "audio/birdsong.wav"



# variables
define volume = 0.2



# code
label start:

    jump wakeUp
    jump windowView
    jump window

    return

label wakeUp:
    
    play sound alarmRing volume(volume)
    pause 3
    play sound alarmRing volume(volume)
    pause 3

    scene blackBg

    "~Как молотом по наковальне…~"
    "~Этот звук казался мне не таким раздражающим~"
    "~Впрочем, он не так плох~"
    "~Если не просыпаться под него…~"
    "~И зачем я вообще купил этот будильник~"
    "~А может это всего лишь дело привычки. Человек ведь в ходе эволюции должен уметь приспособиться к плохим условиям~"

    "Холод"
    "Атмосферное давление"
    "Треск будильника"

    scene wakeUp with Dissolve(3)

    "~Ну, что ж, хватит философствовать, пора вставать. Интересно, что у нас там сегодня~"
    "~Ах, да, очередной день~"

label windowView:

    scene windowView with Dissolve(1)

    "~Опять зима. Отличное время года как по мне. Всё останавливается в своём хаотичном движении. Ленивые дни полные спокойствия~"
    scene windowView

    play sound birdsong volume(volume)
    pause 6

    "~Люблю их тонкие голоса, особенно в декабре. Это одно из немногих украшений в этот период, помимо снега и всяких узоров на стёклах~"

label window:

    scene window with Dissolve(1)

    scene windowBluered with Dissolve(1)
    show leon with Dissolve(1)
    
    leon "~Даже не знаю чем сегодня можно заняться...~"
