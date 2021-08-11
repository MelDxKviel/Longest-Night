################################################################################

image placeholder = "bgs/placeholder.png"

# Объявление персонажей
define g = Character("[player_name]", image = 'geroy', color="#7B4EE0")
define b = Character("Лео", image = 'brother', color="#4E6AFF")
define f = Character("Купер", image = 'friend', color="#F1D730")
define gf = Character("Вики", image = 'girlfriend', color="#D663B1")
define s = Character("Сосед", image = 'sosed', color="#6FE9D5")
define m = Character("Маньяк", image = 'maniac', color="#EC3434")
define p = Character("Прохожие", image = 'people', color="#fff")
define music = Character("Музыкант", image = 'musician', color="#fff")
define a = Character(" ")

# Объявление музыки
define audio.main = "audio/main.mp3"
define audio.mystic = "audio/mystic.mp3"

# Начало игры
label start:

    python:
        player_name = renpy.input("Как тебя зовут?")
        player_name = player_name.strip()

        if not player_name:
            player_name = "Роуз"

    scene bg furgon
    show geroy

    play music main

    g "“Мы едем уже целую вечность, идея внезапной поездки больше не кажется такой привлекательной, особенно в этом душном фургоне. В компании этой парочки мне как-то неловко. Я даже непомню, куда мы едем...”"
    g "Напомните, куда мы, собственно, едем?"

    hide geroy
    show brother

    b "Ты едешь с нами уже 3 часа и только сейчас опомнилась?"

    hide brother
    show friend

    f "Один богатей решил воспользоваться случаем и организовал фестиваль в честь затмения, я разве не рассказывал, чудилка?"

    hide friend
    show geroy

    menu:
        "Почему я согласилась?":
            $ question = True

        "Долго еще ехать?":
            $ question = False

    if question == True:
        g question "Точно! А напомните, почему я согласилась?"

        hide geroy
        show girlfriend

        gf "Тебе было скучно, подруга, и мы взяли тебя с собой из добрых побуждений."

        hide girlfriend
        show geroy

        g "Ладно, вы правы, сама виновата…"

        $question = False

    g "Долго ещё ехать?"

    hide geroy
    show brother

    b question "Неужели тебе не нравиться поездка, [g], тебе же всегда нравилось смотреть в окно и следить за дорогой."

    hide brother
    show geroy

    g "Допустим, но в этот раз, братишка, от вас двоих пахнет ванилью. Вы флиртуете чересчур усердно."

    hide geroy
    show friend

    f "Плохая новость: они не прекратят, подруга."
    f "Хорошая новость: мы почти на месте!"

    hide friend
    show girlfriend

    gf "Жаль, что мы огорчили тебя, сестрёнка."

    hide girlfriend
    show geroy

    g "Да, забей, раз мы почти на месте. {w} Кстати, как, говоришь, фестиваль называется?"

    hide geroy
    show friend

    f "”Длиннейшая ночь”!"

    hide friend
    show geroy

    menu:
        "Задать вопрос":
            $ question = True


        "Промолчать":
            $ question = False

    if question == True:
        $ question = False
        g question "А как затмение связано с ночью?"

        hide geroy
        show brother

        b "Так совпало, что луна заслонит солнце на восходе и это продлиться почти час."

        hide brother
        show geroy

        g glum "У вас этот час уже распланирован?"

        hide geroy
        show girlfriend

        gf "Не будь такой злюкой! Ты тоже едешь на фестиваль. Встряхнись! Будет здорово!"

        hide girlfriend
        show friend

        f smile "В точку!"


    hide geroy
    show friend

    f smile "И-и-и-и-и-и-и-и-и-и-и… {w}Мы прибыли!"

    jump meeting
    return

    #конец 1 сцены

label meeting:

    scene bg park with fade

    show brother

    b "Фестиваль начнется в 10 вечера, когда стемнеет."

    hide brother
    show geroy

    g "И что мы будем делать до этого времени?"
    g "До начала ещё 2 часа, если я не ошибаюсь…"

    hide geroy
    show girlfriend

    gf "Мы просто прогуляемся и посмотрим, где что находится."

    hide girlfriend
    show friend

    f "В 6 утра начнутся выступления музыкальных групп, это будет шумная ночка!"

    hide friend
    show geroy

    g "Скорее шумное утро."

    hide geroy
    show friend

    f "Да, брось, ты же не думаешь, что люди соберутся только на концерте."
    f "Движуха начнется до темноты: выпивка, новые знакомства, да и атмосфера тут, отнюдь, не будничная."

    hide friend
    show brother

    b smile "Так что у нас будет достаточно времени нагуляться, да, [gf]?"

    a "Рядом припарковался кабриолет, из-за руля поднялся мужчина в белой рубашке."

    hide brother
    show sosed

    s "Привет, народ, тоже на фестиваль? Или я слишком рано?"

    hide sosed
    show friend

    f "Нет, чувак, ты как раз вовремя."

    hide friend
    show sosed

    s smile "Тогда рад знать, что не я один такой растропный."

    hide sosed
    show brother

    b "Тебе же лучше, получилось занять удобное место."

    hide brother
    show sosed

    s smile "Верно. {w}Ну что ж, хорошего вам вечера!"

    hide sosed
    show geroy

    g "Хм..."

    menu:
        "Помолчать":
            $ question = False
        "Поинтересоваться":
            $ question = True

    if question == True:
        $ question = False
        g question "Подождите, у вас глаза разного цвета?"

        hide geroy
        show sosed

        s "Верно подмечено. Надеюсь, это никого не смущает."

        hide sosed
        show girlfriend

        gf "Это очень необычно."

        hide girlfriend
        show brother

        b "Здорово выглядишь."

        hide brother
        show sosed

        s "Я тоже так считаю. Ну что ж, до встречи на фестивале!"

    hide sosed
    hide geroy
    show friend

    f "О чем я говорил, даже часа не прошло. А народ только начал прибывать."

    hide friend
    show geroy

    g stress "Мне показалось, что он вел себя довольно странно. Какой человек начнет диалог с незнакомцами?"

    hide geroy
    show girlfriend

    gf "А мне показалось, что он достаточно приятный человек."

    hide girlfriend
    show friend

    f "Подруга, не драматизируй, просто он настроен на общение."

    hide friend
    show brother

    b "Предлагаю не обращать внимания и последовать примеру нашего нового знакомого и, наконец, осмотреться."

    jump lookaround
    return

    #Конец 2 сцены

label lookaround:
    
    scene bg road with fade

    show friend

    f "Стоит отдать должное организации, территория обставлена очень даже неплохо."

    hide friend
    show brother

    b question "Полность согласен. А кстати, куда ты нас ведешь?"

    hide brother
    show friend

    f question "На смотровую площадку. Это, типо, главная фишка этого фестиваля, разве я не говорил?" 

    hide friend
    show geroy

    g smile "Видишь, не только у меня проблемы с памятью." 

    hide geroy
    show girlfriend

    gf happy "Это здорово! Виды дикой природы завораживают, жду не дождусь!" 

    hide girlfriend
    show brother

    b smile "Вижу, ты полна энтузиазма, малыш. Мы пришли." 

    #конец сцены, переход на смотровую площадку
    scene bg viewpoint with fade

    a "Герои подошли к смотровой площадке. Все осматривают открывшийся пейзаж леса."

    show geroy

    g "В чем прикол этих смотровых? Здесь нет ничего, кроме леса."

    hide geroy
    show girlfriend

    gf "В этом и суть: небо и лес во время затмения, разве не здорово?"

    hide girlfriend
    show brother

    b "Что насчет защиты? На затмение нельзя смотреть невооруженным глазом."

    hide brother
    show friend

    f "По периметру расположены пункты выдачи солнечных фильтров, так что за глаза можете не боятсья."

    hide friend
    show geroy

    g "А если фильтров не хватит?"

    hide geroy
    show friend

    f smile "Надень пакет на голову." 

    hide friend
    show geroy

    g "Замётано"

    hide geroy
    show brother

    b "Вот мы и решили.."

    hide brother
    show friend

    f "Ладно, пойдем осмотрим ресторанный дворик в ряду павильонов, я уже хочу есть."

    hide friend
    show girlfriend

    gf "Заодно выясним, где тут туалет."

    hide girlfriend
    show brother

    b "И бар!"

    hide brother
    show friend

    f smile "Зачёт!"

    #конец сценки, переход на ряд павильонов

    scene bg crowded place with fade

    a "Прошло 3 часа. Герои проводят время в ряду павильонов."

    show geroy

    g "Не думала, что будет столько народу..."

    hide geroy
    show friend

    f "Это ещё не много, подруга. Ближе к утру ещё больше народу привалит."

    hide friend
    show brother

    b "Хорошо, ребят, мы с Вики пойдём на смотровую."

    hide brother
    show girlfriend

    gf "Смотреть на звёздное небо!"

    hide girlfriend
    show brother

    b "С собой не зовём."

    hide brother
    show geroy

    g "Развлекайтесь. Только не забудь потом мне брата вернуть."

    hide geroy
    show brother

    b "Эй, я ещё здесь!"

    hide brother
    show girlfriend

    gf "Не переживай, подруга. Верну в целости и сохранности."

    hide girlfriend
    show friend

    f "О-кей, ребят, а я к фургону, вздремну часок."

    hide friend
    show geroy

    g "Я с тобой!"

    hide geroy
    show friend

    f question "Не хочешь позависать здесь? Познакомиться с кем-нибудь?"

    hide friend
    show geroy

    g stress "Хочешь бросить меня одну среди толпы незнакомцев? Да ни за что!"

    hide geroy
    show friend

    f "Как скажешь, трусишка. Тогда погнали!"

    jump darkness
    return
    #конец сцены

label darkness:
    scene bg park dark with fade
    play music mystic
    show friend

    f "Ладно, я спать. Ты, конечно, можешь лечь со мной, но брату сама объяснять будешь."

    hide friend
    show geroy

    g "Неважно, я не хочу спать."

    hide geroy
    show friend

    f "Как скажешь."
    f "*уходит*"

    hide friend
    show geroy

    g "Наконец-то тишина.."

    hide geroy
    show sosed

    s "Решила отдохнуть от суеты?"

    hide sosed
    show geroy

    g surprise "А!? Да, верно."

    hide geroy
    show sosed

    s "Прости, если застал врасплох."

    hide sosed
    show geroy

    g "Ничего, переживу… {w}Как долго вы здесь? Пока мы шли, вас не было видно"

    hide geroy
    show sosed

    s smile "Я сам только что пришел. {w} Логично, что вы с другом меня не видели"

    hide sosed
    show geroy

    g "Тоже устали от шума?"

    hide geroy
    show sosed

    s "А ты проницательная. Да, я не очень люблю большие скопления людей"

    hide sosed
    show geroy

    g "Хах! Я тоже."
    g question "Но зачем вы тогда приехали на фестиваль?"

    hide geroy
    show sosed

    s smile "Давай так, мы оба перейдём на “ты” и я тебе отвечу."

    hide sosed
    show geroy

    g "Хорошо."

    hide geroy
    show sosed

    s "Мне было интересно, как организуют фестиваль по такому поводу. {w}Но, в первую очередь, я здесь из-за затмения"

    hide sosed
    show geroy

    g "А что вам… то есть тебе помешало приехать ближе к началу самого затмения?"

    hide geroy
    show sosed

    s "Я боялся, что мне не хватит места на стоянке, да и искать потом второпях что и где находится как-то не хотелось."

    hide sosed
    show geroy

    g "Ммм... Понятно"

    hide geroy
    show sosed

    s "Ваша компания разделилась?"

    hide sosed
    show geroy

    g glum "Да, голубкам нужно время, чтобы побыть вдвоем."

    hide geroy
    show sosed

    s smile "Нельзя винить парочку за их желание побыть наедине в такой атмосфере."

    hide sosed
    show geroy

    g "Тебе повезло, что ты не ездил с ними в одной машине."

    hide geroy
    show sosed

    s "Всё слишком приторно?"

    hide sosed
    show geroy

    g bit smile "Читаешь мои мысли. {w}Мой брат уделяет своей девушке слишком много внимания."

    hide geroy
    show sosed

    s question "Разве это плохо? Может быть у них всё серьёзно, а ты напрягаешься понапрасну."

    hide sosed
    show geroy

    g "Неприятно, когда единственный родной человек почти игнорирует моё присутствие."

    hide geroy
    show sosed

    s smile "Да, это грубовато."

    hide sosed
    show geroy

    g glum "..."

    hide geroy
    show sosed

    s question "Эй, ты в порядке?"

    hide sosed
    show geroy

    g "Да забей... Просто вырвалось."

    hide geroy
    show sosed

    s "Послушай, жизнь же не стоит на месте. Всё постоянно меняется к лучшему или не очень, но это не повод заранее вешать нос, особенно, когда тебе есть к чему стремиться."
    s "Только принимая удары судьбы мы по-настоящему учимся крепко стоять на ногах."

    hide sosed
    show geroy

    g question "Это звучало... старомодно. Ты точно из нашего времени?"

    hide geroy
    show sosed

    s smile "Хах, в точку! Современным меня не назовёшь."
    s "На самом деле, мне кажется, что ты драматизируешь, в конце концов это не ставит крест на твоей жизни."

    hide sosed
    show geroy

    g glum "Может ты и прав..."

    hide geroy
    show sosed

    s "Знаешь, ты напоминаешь мне кое-кого... Что ж, до встречи!"

    hide sosed
    show geroy

    g "Ладно, пока."
    g "*провожает незнакомца взглядом*"
    g stress "Это было странно. Думаю, я достаточно времени пробыла на стоянке. Вернусь к людям, заодно поищу этих двоих."

    jump strangethings
    return

    #конец 4 сцены

label strangethings:
    scene bg crowded place with fade

    show geroy

    g "Кажется стало немного свободнее."
    g "Даже если так, нашей парочки все равно не видать."
    g "Осмотрюсь немного, может замечу."
    g "..."
    g stress "Что-то мне не нравится, что их до сих пор не видно"

    menu:
        "Искать дальше":
            $ question = False
        "Спросить у прохожих":
            $ question = True

    if question == True:
        $ question = False

        g "Здравствуйте, вам не встречался парень среднего роста в черной кожанке или рыжая девушка в зеленом платье?"

        hide geroy
        show people

        p "Не помню."
        p "Я не видел."
        p "Кажется, я видел, как парень в кожанке двигался к смотровой площадке."

        hide people
        show geroy

    g "Ладно. Поищу на смотровой площадке."

    #сценка 2
    scene bg viewpoint with fade
    show geroy


    g "Итак, я на месте, где же они?"
    g "*осматривает площадку*"
    g "Не вижу их, может, они ушли.."
    g "Стоп, мне показалось или..."
    g "*видит на краю два лепестка багрового цвета*"
    g stress "Странно, не видела, чтобы где-то здесь были цветы."
    g "Очевидно, что Лео и Вики здесь нет. Может мы разминулись среди павильонов."

    #сценка 3
    scene bg crowded place with fade

    show geroy

    g stress "Где же они? {w}Секунду, вижу знакомое платье.."
    g "Эй, Вики"

    hide geroy
    show girlfriend

    gf scary "*оборачивается*"
    gf scary "А?!"

    hide girlfriend
    show geroy

    g "Фух, я вас уже обыскалась. {w}А где Лео?"

    hide geroy
    show girlfriend

    gf "Если бы я сама знала."

    hide girlfriend
    show geroy

    g "Как это? Вы же друг от друга не отходите!"

    hide geroy
    show girlfriend

    gf "Мы с Лео были на смотровой площадке, но мне надо было отлучится, а когда я вернулась, его уже там не было."
    gf sad "Я думала, что он пошел сюда, но, по всей видимости, ошиблась."

    hide girlfriend
    show geroy

    menu:
        "Промолчать":
            $ question = False
        "Спросить про лепестки":
            $ question = True

    if question == True:
        $ question = False

        g "Ты не видела красных цветов, пока вы были на смотровой площадке?"

        hide geroy
        show girlfriend

        gf "Нет, не видела. Вокруг вообще нет никаких цветов."

        hide girlfriend
        show geroy

        g stress "Так, теперь мне это вообще не нравится."

    g "Может пойдем на стоянку? Вдруг он решил вернуться в фургон."

    hide geroy
    show girlfriend

    gf "Думаешь, он мог уйти, не сказав об этом?"

    hide girlfriend
    show geroy

    g "В любом случае, на смотровой площадке я его не видела."
    g glum "И здесь его тоже нет. {w}Лучше сходить и проверить"

    hide geroy
    show girlfriend

    gf happy "Может мы зря переживаем, и он решил приготовить сюрприз?"

    hide girlfriend
    show geroy

    g "Послушай, подруга, я не оставлю тебя одну, пока мы его не найдем. {w}А искать мы пойдем прямо сейчас, возражения не принимаются."

    hide geroy
    show girlfriend

    gf angry "Э-э-эх, ладно!"

    #сценка 4
    scene bg park dark with fade

    show girlfriend

    gf angry "Мы пришли, но здесь никого нет."

    hide girlfriend
    show geroy

    g stress "А куда пропал Купер?!"

    hide geroy
    show friend

    f "Эй, я никуда не пропадал?"

    hide friend
    show geroy

    g "Ты же пошел спать!"

    hide geroy
    show friend

    f "Спал, но у ребят сигналка сработала и не выключалась.."

    hide friend
    show people dark

    p "Привет."
    p "Хей!"
    p "Чё как?"

    hide people
    show friend

    f "..пришлось вмешаться. А ребята оказались клёвыми."

    hide friend
    show girlfriend

    gf "Купер, ты не видел Лео?"

    hide girlfriend
    show friend

    f "Как раз у вас хотел спросить, ведь сладкая парочка обычно всегда вместе."

    hide friend
    show geroy

    g glum "Я тоже удивилась, когда обнаружила Вики одну."

    hide geroy
    show friend

    f "Не думаю, что Лео мог просто потеряться, скорее он что-то задумал."

    hide friend
    show girlfriend

    gf "Спасибо, что успокоил, Куп."

    hide girlfriend
    show geroy

    g stress "Но мы его нигде не видели."

    hide geroy
    show friend

    f "Эй, мы с твоим братом сто лет знакомы, подруга, он не даст себя в обиду на фестивале хипстеров."

    hide friend
    show girlfriend

    gf angry "Да, [g], ты зря паникуешь, ещё меня на уши подняла даже толком не подумав. Есть масса причин, по которым он мог задержаться."
    gf angry "Должно быть, он прямо сейчас меня ищет."

    hide girlfriend
    show geroy

    g "Может подождем его здесь?"

    hide geroy
    show girlfriend

    gf very angry "Да успокойся уже, пожалуйста!"
    gf "*уходит*"

    hide girlfriend
    show friend

    f "Ты заставила её понервничать. Но не думаю, что она обиделась."

    hide friend
    show geroy

    g stress "Всё это меня настораживает."

    hide geroy
    show friend

    f question "Останешься у фургона или еще дров наломаешь?"

    hide friend
    show geroy

    g "Я хочу поговорить с кое-кем.. {w}Эй, старомодный парень!"
    g glum"Куда же он запропастился? Ох…"

    a "[g] обнаруживает возле машины несколько багровых лепестков на земле."

    g question "Снова эти лепестки? У него ведь не было цветов."
    g stress "Всё это не просто так… {w}Я должна догнать Вики!"

    return

################################################################################
