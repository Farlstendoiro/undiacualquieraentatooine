# image movie = Movie(size=(800,800), xpos=0, ypos=0, xanchor=0, yanchor=100)

# El juego comienza aquí.

label start:

# ESTO ES PARA ARRANCAR DONDE TE CONVENGA
#    $ item1 = 0
#    $ item2 = 0
#    "Oscilador: [item1]. Estandarte: [item2]."
#    jump hangar
# BORRALO CUANDO TOQUE

# Un menú en el que una opción aparece sólo si la variable item1 es 0
#    $ item1 = 1
#    tusken "bla bla!"
#    menu:
#        "Opción A":
#            "Has dicho Opción A"
#        "Opción B":
#            "Has dicho Opción B"
#        "Opción Si Item1 Es 0" if item1 == 0:
#            "Has dicho Opción Sólo en Item1 es 0"

# inicializar variables y personajes

    # Aquí deberías declarar los personajes usados en el juego como en el ejemplo:
    call defineVariables from _call_defineVariables
    call definePersonajes from _call_definePersonajes
    
    # Aquí lo complico: you para los diálogos: you "Hola, soy [playerName]"
    define you = DynamicCharacter("playerName", color="#c8ffaa")
    
    # No sé si sigues necesitando una posición para volver...
    default posicion = "hangar"
    
# opening del juego
    
#    playerName " Reemplazar esto y los videos y todo por texto que sirva para algo."
#    $ renpy.movie_cutscene("pyke16.ogv")
#    play movie "pyke16.ogv"
#    show movie with fade
                                                                                                                                                                                                                                                      
# Este cacho de código es para que veas cómo se mete la tienda, el texto, etc.
#    scene bg tienda
#    show jawa
#    "Hola."
    
    jump alInicio


label porsiaca:
    scene bg unused celda
    with fade
    show jako
    jako "Has llegado al label porsiaca, que debería no ser usado nunca. Esto ha salido mal."

label findejuego:

    # Finaliza el juego:
    
    scene bg tu nave
    
    playerName "¿Jako? Todo está resuelto. Estoy en la cubierta de la nave."
    play music "music/inquietante.mp3"
    playerName "¿Jako? ¿Dónde estás?"
    show belia calamariana with dissolve
    calamariana "Tu droide no puede ayudarte, [playerName]. Nadie puede ayudarte... contra mí."
    playerName "¿Quién eres tú y cómo has subido a mi nave?"
    calamariana "Soy las sombras que se mueven en la noche. Soy el terror innombrable. Soy la muerte inesperada...{p}porque el lado oscuro es poderoso en mí."
    calamariana "Yo soy Belia Darzu, lady del sith."
    playerName "¿Belia Darzu, la shi'ido multiforme? Ella murió durante las Guerras Sith, hace más de mil años."
    calamariana "Tú nunca podrás comprender el poder del lado oscuro."
    playerName "La metamorfosis es una capacidad biológica de tu especie, no un truco de la Fuerza."
    
    if conoceClawditaA == 1:
        playerName "Además, tú no eres una shi'ido... Eres otro tipo de multiforme, ¿verdad? Eres una clawdita."
        show belia clawdita with dissolve
        belia "He usado muchos rostros y cuerpos en este tiempo. Mi favorito, sin embargo, es el aspecto humano..."
        show belia transformarse with dissolve
        show belia with dissolve
        playerName "Ésa es la mujer que intimidó al ermitaño Bellstrike, ¿verdad?{p}Tú también fuiste la rata womp gigante que hablaba. Eso explica que pudiese silbar."
        belia "Por grandes que sean mis poderes, aún es más grande mi ambición. Mis planes afectan mucho más que una mera rata."
        playerName "Sé lo que pretendías. Estabas rastreando el Desfiladero del Peñón Mellado. Buscabas los cazas ocultos de la Alianza."
        belia "No sabía que eran cazas, creí que serían cargueros. Mis planes se verían perjudicados si la República tiene presencia militar en esta zona."
        belia "Maté a los pilotos uno tras otro, obligándoles a mirar. Prometí dejar vivir a quien me dijese dónde estaban las naves escondidas; pero ninguno habló."
        playerName "Intentabas ahuyentar a todo el que pudiese acercarse demasiado. Jent Loquoy. Wassak. Los granjeros de humedad."
        playerName "Pero has fracasado. Los espías bothan han llegado antes que tú, y ahora las naves están a buen recaudo, rumbo a una base de la República."
        playerName "Para ser tan poderosa, necesitas mucha ayuda. ¿Trabajaba Thondo Qo para ti?"
        belia "Sí, le contraté para que vigilase el cañón. Eres muy perspicaz, [playerName]. Demasiado para tu propio bien."
        
    else:
        show belia transformarse with dissolve
        show belia with dissolve
        playerName "La rata womp gigante que atacó a Jent Loquoy... ¿Eras tú, verdad?"
        belia "Eres [tuUn] entrometid[tuO]. Eso te meterá en problemas."
        if conoceClawditaC == 1:
            playerName "No sólo eso: Eres el administrador zabrak del que hablaba TurJinda, ¿verdad? El que profetizaba muertes y batallas."
            belia "¿Comprendes ahora mi poder tenebroso? Puedo ver el futuro."
            playerName "Creo que puedes {i}causar{/i} el futuro. Predices que morirá el supervisor de Mimban, y después, con otra cara, viajas a Mimban y le matas."
            playerName "Pero cometes demasiados errores. Bebías siseo fotónico. Es una bebida demasiado ligera para una especie de constitución tan robusta como los zabrak. Ellos nunca piden algo así."
            playerName "Si fueses una sith con mil años de experiencia, no caerías en un desliz así."

    belia "[tuUnMayus] especialista en razas alienígenas investigando ratas womp aquí podría echar a perder todos mis planes. Por eso tuve que ponerte obstáculos y mantenerte ocupad[tuO]."

    if conoceClawditaB == 1:
        playerName "¡La investigación sobre mi nave! Tú hiciste que Terrem Jesond me incriminase."
        belia "Sí, le exigí que devolviese un favor a su socio, que por supuesto era yo con otra identidad."
        if conoceClawditaC == 1:
            playerName "No sólo eso: Eres el administrador zabrak del que hablaba TurJinda, ¿verdad? El que profetizaba muertes y batallas."
            belia "¿Comprendes ahora mi poder tenebroso? Puedo ver el futuro."
            playerName "Creo que puedes {i}causar{/i} el futuro. Predices que morirá el supervisor de Mimban, y después, con otra cara, viajas a Mimban y le matas."
            playerName "Pero cometes demasiados errores. Bebías siseo fotónico. Es una bebida demasiado ligera para una especie de constitución tan robusta como los zabrak. Ellos nunca piden algo así."
            playerName "Si fueses una sith con mil años de experiencia, no caerías en un desliz así."
        playerName "¿Por qué? ¿Quieres controlar Tatooine, el sector Arkanis?"
        belia "No. Pensaba respaldar a Jesond y ponerle de testaferro... De títere, más bien. Me habría venido bien controlar Tatooine a través de él... pero lo estropeaste."
    else:
        playerName "¡La investigación sobre mi nave! Tú hiciste que me incriminasen."
        playerName "¿Por qué? ¿Quieres controlar Tatooine, o el sector Arkanis?"
        belia "No. Me habría venido bien controlar Tatooine a través de un títere... pero lo estropeaste."
        playerName "¿Quién era tu aliado? ¿Terrem Jesond o Vykan Fenn?"
        play sound "sound/risabelia.mp3"
        belia "¡Ja! Estás más despistad[tuO] de lo que yo creía."

    belia "Mis planes son demasiado importantes para permitir que salgas de ésta con vida, [playerName]."
    belia "Que creas o no en la Fuerza, poco importa ya. Sólo uno de los dos sobrevivirá a este encuentro..."
    "Belia Darzu, si es ella realmente, echa sus brazos hacia arriba y sus manos aferran las empuñaduras de sus vibrofilos."
    play sound "sound/sable.mp3"
    with flash
    show sable:
           xalign 0.0 yalign 1.0
           linear 1.0 xalign 1.1
    $ renpy.pause(0.5)
    show belia mitad
    "La multiforme cae al suelo en dos mitades. Sus capacidades multiformes y sus supuestos poderes no la han protegido contra tu sable láser."
    hide belia
    $ renpy.pause(1)
    play music "music/ambiental.mp3"
    playerName "Jako, debes estar por aquí. Tú guardabas mi sable láser y, cuando lo llamé con telequinesis, vino de esta dirección"
    show jako
    hide sable
    playerName "Venga, viejo amigo. Déjame que te reconecte..."
    play sound "sound/activajako.mp3"
    jako "Zzzaludozzz, [playerName]. Zzziento dezzzir que la zzzizzz zzzubió a bordo y me zzzuperó con zzzuzzz poderezzz..."
    playerName "No te preocupes por eso. Hazte un autodiagnóstico, conecta el nuevo oscilador y prepara el despegue. Nos vamos de Tatooine."
    jako "¿Y la zzzizzz?"
    playerName "Supongo que el Maestro DarkSark querrá echar un vistazo a sus restos; esto es asunto de la Orden Jedi."
    scene bg findejuego

    "Una astronave como ésta no es el lugar más cómodo para relajarse o meditar, pero es mucho mejor que estar correteando bajo los soles gemelos de Tatooine y jugándose la vida a cada momento."
    "Con la burocracia en regla y todo revisado antes del despegue, nadie molesta al {i}[tuNave]{/i}. Jako lleva los mandos de forma razonablemente segura, aunque no sin alguna sacudida."
    jako "Lizzztozzz para zzzaltar al hiperezzzpazzzio..."
    play sound "sound/hiperespacio.mp3"
    with flash

    scene bg final
    $ renpy.pause(5)

    jump creditos

    return