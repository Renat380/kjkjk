# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
init python:
    import random

define a = Character('Безполая Детя', color="#fdfdfd")
define d = Character('Волк', color="#727072")
define z = Character('Санс', color="#6077f7")
define t = Character('Таракан', color="#a17645")


init:
    $left3 = Position(xalign=0.3, yalign=0.2)
    $left2 = Position(xalign=0.5, yalign=0.6)
    
    
# Игра начинается здесь:
label start:
    $ myRandInt = random.randint(0, 2)

    play music "zwuk.mp3"

    scene les
    show wolf at left
    show dety at right
    with dissolve 

    d "AAA что та двинолось или это мое вооброжения"

    a "Да давай решим что это твое воброжения"

    d "Ты человек если да я сделую чтоб ты вобще не смог ходить "

    a "Тогда все норм я банан"

    d "Класс хочешь дружыть"

    a "Неособа"

    d "Мы друзья"

    d "Любишь собачие печенья Бро"

    a "Не сказал бы "

    a "Как то раз я попробавал перепутав их с сухим завтроком и почуствовал себя глупа "

    d "Ты наверно почуствовал себя глупо так ты любишь собачие печенья"

    a "Ты вобще слушал мой расказ"

    d "Да но они у меня особеные"

    a "И что вних особеного"

    d "пойдем покожу"
    
    menu:
        "пойти с ним":
            jump labelq1
        "ударить и сказать что это плоха":
            jump labelq2

label labelq1: 
    "ВЫ пошли с ним и накурились собачими печеньями и вас задержала полиция "
    "ПЛОХАЯ КОНЦОВКА "
    "не курите собачие печенье это плоха"

    return
    
label labelq2: 
    "Вы ударили его"

    hide wolf at right
    show sans at left

    z "Ты шо твориш"

    a "Он хотел дать мне плохие вещи ты понимаешь что быть хорошим это сложно веть другие не хотям вести себя хорошо"

    z "Да ты прав но мне насрать чтобы получить хоршую концовку ты должен был вести себя хорошо со всеми"
    
    z "но ты не смог теперь ты умрешь"

    scene bg black

    show sans u

    play music "sanis.mp3"

    menu:
        "Ударить санса":
            jump labelq3
        "Уварачиваться":
            jump labelq4
    
label labelq3:
    "Он увернулся вы пропустили его атаку и погибли"
    "ПЛОХАЯ КОНЦОВКА"
    "Надо было увернутся"

    return

label labelq4:
    "Вы увернулись Санс не попал по вам"

    menu:
        "Ударить санса":
            jump labelq5
        "Попросить прощения у волка":
            jump label6

label labelq5:
    "Он увернулся вы пропустили его атаку и погибли"
    "ПЛОХАЯ КОНЦОВКА"
    "Надо было увернутся"

label label6:
    "Волк простил вас Санс успакоелся"

    scene les
    show sans at left
    show dety at right
    with fade
    play music "zwuk.mp3"


    z "А ну все ок братан веди сябя хорашо бро "
 

    scene bg sans
    play music "Shop.mp3"
    show sans at right
    show dety at left

    z "Хей "

    z "Ты дошол до сюда и ты вел себя хоршо со всеми"

    a "Неужели я дошол ты знаешь как это трудно"

    z "Давай отпразнуем твой сложный путь и ты получишь свою концовку"

    show dety at center
    with moveinright

    a "Ой"
    scene pol
    hide dety
    hide sans
    show tarakan


    t "О нет я умераю"

    t "УдАлиите ИстОрию браУзеРа"

    hide tarakan
    scene bg sans
    show sans at right
    show dety at left

    z "ТЫ УБИЛ ЕГО"

    a "это же просто жук"

    z "МНЕ ВСЕРОВНО ТЫ УБИЛ ЕГО"

    a "ты же толькошто паука придовил"

    z "не он жив ты же жив бро"

    'эЭээээЭээээЭ'

    z "видишь он жив теперь ты умрешь"

    hide dety
    hide sans
    scene bg black
    show sans u
    play music "sanis.mp3"

    show bazuka at left2
    show gaster blaster at left3
    z "Зацини мою МЕГАГИПЕРПУПЕРБЛАСТЕРПУШКУ"

    
    menu:
        "Ударить санса":
            jump labelq7
        "Уварачиваться":
            jump labelq8

label labelq7:
    if myRandInt == 2:
        'Вы попали под атаку Санса'
        return

    if myRandInt == 1:
        'Вы промахнулись и пропустили атаку'
        return

label labelq8:
    if myRandInt == 3:
        'Вы не смогли увернутся'
        return
    if myRandInt == 4:
        'Вы увернулись'
        
    'Вы успешно увернулись'

    menu:
        "Ударить санса":
            jump labelq9
        "Уварачиваться":
            jump labelq10

label labelq9:
    if myRandInt == 5:
        'Вы попали под атаку Санса'
        return

    if myRandInt == 6:
        'Вы промахнулись и пропустили атаку'
        return

label labelq10:
    if myRandInt == 7:
        'Вы не смогли увернутся'
        return
    if myRandInt == 8:
        'Вы увернулись'

    'Вы успешно увернулись'

    menu:
        "Ударить санса":
            jump labelq11
        "сделать таракану врот врот":
            jump labelq12

label labelq11:
    if myRandInt == 9:
        'Вы попали под атаку Санса'
        return

    if myRandInt == 10:
        'Вы промахнулись и пропустили атаку'
        return

label labelq12:
    'Он проснулся и жив'

    play music "Shop.mp3"
    scene bg sans
    show sans u at right
    show dety at left

    a "Он жив он жив"

    show sans

    z "А бро ну молодец спас таракана и подарил ему первый поцылуй"
    'ПРОДАЛЖЕНИЕ СЛЕДУЕТ'