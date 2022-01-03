label CallePrincipal:

    scene bg calle principal

    "Estás en la calle principal del puerto espacial de Mos Eisley. No encontrarás otro lugar como éste, tan lleno de maldad y vileza.{p}Debes tener cuidado."
    "No se puede hacer mucho en mitad de la calle, pero se puede ir a muchos sitios desde aquí."

    if itemDeclaraJent == 0:
        jump hablarJentEnLaCalle

    jump go_CallePrincipal

label Cantina:

    scene bg cantina
    show camarero
    show kabe at left

    "Ésta es la Duquesa que Ríe, la mejor cantina en esta zona, o por lo menos la mejor que hay abierta. La bebida es variada, los precios son bajos y los clientes son interesantes."

    if jugarLabria < 4:
        show labria at right
        "Un esbelto kaminoano se tambalea moviendo su cabeza como un péndulo mientras intenta apoyarse para pedir una copa."
    if informacionImplicaCrimelord2 == 1 and crimelord2Activo == 1:
        show crimelord2 at right
        "Terrem Jesond, uno de los jefes criminales, está sentado en una mesa tomándose una bebida de colores vivos."

    menu:
        "¿Quieres hablar con alguien?"
        "Hablar con la camarera.":
            jump hablarCamarero
        "Hablar con Gorlok.":
            jump hablarKabe
        "Hablar con el kaminoano." if jugarLabria < 4:
            jump hablarLabria
        "Hablar con Terrem Jesond." if informacionImplicaCrimelord2 == 1 and crimelord2Activo == 1:
            jump hablarCrimelord2EnCantina
        "No hablar con nadie":
            pass

    jump go_Cantina

label siguesEnCantina:
# La diferencia es que vienes de rebote y puede que quieras hacer más cosas. Quitar las descripciones de intro

    "Sigues en la cantina de la Duquesa que Ríe."
    scene bg cantina
    show camarero
    show kabe at left

    if jugarLabria < 4:
        show labria at right
    if informacionImplicaCrimelord2 == 1 and crimelord2Activo == 1:
        show crimelord2 at right

    menu:
        "¿Quieres hablar con alguien ahora?"
        "Hablar con la camarera.":
            jump hablarCamarero
        "Hablar con Gorlok.":
            playerName "Hola, Gorlok."
            kabe "Eh, [playerName], [tuEl] [tuEmpollon]. Siéntate. ¿Qué necesitas?"
            jump hablarKabe
        "Hablar con el kaminoano." if jugarLabria < 4:
            jump hablarLabria
        "Hablar con Terrem Jesond." if informacionImplicaCrimelord2 == 1 and crimelord2Activo == 1:
            jump hablarCrimelord2EnCantina       
        "No hablar con nadie":
            pass

    jump go_Cantina


label Hangar:

    scene bg hangar

    "Éste es el hangar donde se guarda tu nave, el {i}[tuNave]{/i}, durante tu visita a Tatooine. Puedes ver el {i}[tuNave]{/i} en el fondo, y el droide Jako debe seguir a bordo."

    if itemOscilador == 1 and itemPermisoDespegue == 1 and itemInvestigacion == 1:
        "Al fin tienes todo lo necesario. Puedes subir al {i}[tuNave]{/i}, y dejar atrás este planeta de locos."
        jump TuNave
    else:
        scene bg hangar amarillo
        if itemOscilador == 1 and itemPermisoDespegue == 1 and itemInvestigacion == 0:
            "No puedes acceder a tu nave todavía. Mientras haya una investigación abierta contra el {i}[tuNave]{/i}, no puedes irte del planeta."
        elif itemOscilador == 1 and itemPermisoDespegue == 0 and itemInvestigacion == 1:
            "No puedes acceder a tu nave todavía. Tu permiso de despegue no está autorizado."
        elif itemOscilador == 0 and itemPermisoDespegue == 1 and itemInvestigacion == 1:
            "No puedes acceder a tu nave todavía. El oscilador de cristal del {i}[tuNave]{/i} está roto y debe ser reemplazado antes de despegar."

        elif itemOscilador == 1 and itemPermisoDespegue == 0 and itemInvestigacion == 0:
            "No puedes acceder a tu nave todavía. Tu permiso de despegue no está autorizado.{p}Mientras haya una investigación abierta contra el {i}[tuNave]{/i}, no puedes irte del planeta."
        elif itemOscilador == 0 and itemPermisoDespegue == 1 and itemInvestigacion == 0:
            "No puedes acceder a tu nave todavía. El oscilador de cristal del {i}[tuNave]{/i} está roto y debe ser reemplazado antes de despegar.{p}Mientras haya una investigación abierta contra el {i}[tuNave]{/i}, no puedes irte del planeta."
        elif itemOscilador == 0 and itemPermisoDespegue == 0 and itemInvestigacion == 1:
            "No puedes acceder a tu nave todavía. El oscilador de cristal del {i}[tuNave]{/i} está roto y debe ser reemplazado antes de despegar.{p}Tu permiso de despegue no está autorizado."
        else:
            "No puedes acceder a tu nave todavía."
            "El oscilador de cristal del {i}[tuNave]{/i} está roto y debe ser reemplazado antes de despegar.{p}Tu permiso de despegue no está autorizado.{p}Mientras haya una investigación abierta contra el {i}[tuNave]{/i}, no puedes irte del planeta."

    jump go_Hangar

label OficinaImperial:

    scene bg oficina imperial
    show funcionario

    "La oficina imperial tiene un aspecto amedrentador, con sus tonos apagados y la presencia de androides en perfecta formación vigilando cada movimiento que se haga al alcance de sus sensores."
    "La máquina del fondo es un comunicador interestelar, puede que el único en el planeta, con su generador de energía incorporado. Abastece además al resto de la tecnología imperial y posiblemente pueda utilizarse también para torturar prisioneros políticos."
    "Hay un funcionario imperial con cara de pocos amigos para atender las necesidades de los ciudadanos. Ésta es la clase de sitio en la que, cuanto menos tiempo pase uno, mejor. "
    
    # "TBA preguntarKabePorCazador %(preguntarKabePorCazador)d"
    
#    if preguntarKabePorCazador == 2:
#        jump puedesHablarConCazador
#    else:
        # Gorlok no te ha soplado que aquí se pregunta por el cazador (O ya has hablado con el BH).
    "¿Quieres hablar con el funcionario imperial?"
    menu:
        "Sí.":
            funcionario "Saludos, perceptor. La oficina de asuntos imperiales está a su disposición. ¿Tiene un trámite abierto?"
            jump hablarFuncionario
#       UNA CONVERSACIÓN QUE HICE CON EL FUNCIONARIO, PERO LA BUENA DEBERÍA SER LA DEL SALTO:
#                if itemInvestigacion == 0:
#                    playerName "Hay una investigación abierta sobre mi nave, {i}[tuNave]{/i}, y se trata de un malentendido que quiero resolver."
#                    "suena PITIDO ORDENADOR"
#                    funcionario "He enviado una petición a la Oficina de Seguridad Imperial para que confirmen la situación. Por favor, espere su respuesta."
#                if itemPermisoDespegue == 0:
#                    playerName "Sobre mi permiso de despegue, he solicitado que se confirme. ¿Sabemos algo?"
#                    funcionario "Se ha enviado su permiso a las oficinas de la Gobernadora y del Moff para que lo autoricen. Todavía no hay respuesta."
#                if itemPermisoDespegue == 1 and itemInvestigacion == 1:
#                    funcionario "Gracias por venir, ciudadan[tuO]. El tiempo del personal imperial es valioso. Agradecemos su presencia. Puede retirarse."
        "No.":
            pass        

    jump go_OficinaImperial

label puedesHablarConCazador:

#  HAS IDO A OFICINA IMPERIAL, ESTÁ EL CAZADOR, PUEDES HABLAR CON ÉL
    funcionario "Así que usted quiere hablar con un cazarrecompensas. Hay uno por aquí. ¿Quiere que le llame ahora?"
    menu:
        "Claro, hablaré con el cazarrecompensas.":
            funcionario "Voy a avisar al cazarrecompensas."
            hide funcionario
            playerName "Muchos cazarrecompensas son alienígenas que no han podido conseguir empleo policial por la política pro-humanos del Imperio."
            playerName "A mí se me dan bien los alienígenas porque conozco y respeto sus culturas. Seguro que me lo gano en seguida."
            show funcionario at left
            show cazador with dissolve
            cazador "Soy 4-LOM, cazarrecompensas imperial autorizado. ¿Es usted identificación: [playerName]?"
            playerName "Vaya, un droide."
            hide funcionario
            jump hablarCazador
        "Quizá más tarde.":
            playerName "Pensándolo bien, quizá sea mejor hacerlo más tarde."
            funcionario "Avíseme si cambia de opinión."
    jump go_OficinaImperial

label Trastienda:

    scene bg trastienda

    "Esto es la trastienda de la cantina Duquesa que Ríe. Posiblemente los músicos ensayan y preparan sus números en vivo aquí. No hay músicos ahora mismo."

    jump hablarCrimelords

    jump go_Trastienda

label OtroHangar:

    scene bg otro hangar
    show contrabandista

    if entrarOtroHangar == 0:
        "Mos Eisley es un puerto espacial con varios hangares a disposición de los capitanes que paguen. Éste es un hangar de más calidad que el que contrataste tú, con servicios de abastecimiento superiores."
        "La nave atracada es una lanzadera Cygnus T-5, a menudo usada por contrabandistas porque permite modificaciones para convertirla en cargueros bien armados."
        "El capitán parece ser un nativo del sistema Duro con aspecto sospechoso. Los duros tienen merecida fama de ser intrépidos pilotos, sociables y amigos de las diversiones. Más de un duro llegó a ser un infame contrabandista."
        $ entrarOtroHangar = 1
    else:
        if saludarContrabandista == 0:
            "Éste es un hangar de más calidad que el que tú contrataste. Hay una lanzadera Cygnus T-5 atracada; el duro con aspecto de contrabandista parece ser su capitán."
        else:
            "Éste es un hangar de más calidad que el que tú contrataste. Hay una lanzadera Cygnus T-5 atracada; el duro con aspecto de contrabandista es su capitán, Nengih TurJinda."

    if crimelord2Activo == 2:
        show copiloto
        "También hay otro tipo que debe ser su copiloto. Es un utai que parece estar revisando los mecanismos de la nave."

    menu:
        "¿Quieres hablar con el piloto de aspecto sospechoso?"
        "Hablar con el piloto de aspecto sospechoso.":
            jump hablarContrabandista
        "No hablar con el piloto de aspecto sospechoso.":
            pass

    jump go_OtroHangar

label Callejon:

    scene bg callejon

    "Desde la trastienda de la cantina, se puede salir al exterior por una puerta de servicio que se cierra herméticamente en cuanto estás fuera. Esto no es más que un callejón con salida a la calle principal."

    if apalizadoPorTropas == 0:
        jump teDanPaliza

    jump go_Callejon

label TuNave:

    scene bg tu nave
                                                                                                                                                                                                                      
    jump findejuego

    return

label CasaGraf:

    scene bg casa graf
    show graf

    "Según te han indicado, éste es el lugar de trabajo de Hawk Hyperhalo, rebanador."
    "Una mujer joven está tecleando en varios ordenadores en el fondo, y de vez en cuando coge un soldador y lo usa sobre una pieza de maquinaria pequeña que cabe en sus manos."

    menu:
        "¿Quieres hablar con ella?"
        "Sí, hablaré con ella.":
            if primerGraf == 0:

                playerName "¿Eres Hawk Hyperhalo? ¿La rebanadora?"
                graf "¿Quién quiere saberlo?"
                playerName "Me llamo [playerName]."
                graf "Ah, [tuEl] xenobiólog[tuO] de las ratas womp. Sí, es correcto. Eh... Mis sensores te identificaron al entrar. La pregunta era para ver si intentabas engañarme o eras de fiar."
                playerName "¿En serio? Porque los sensores parecen apagados."
                graf "Los he modificado para que no se detecte que están encendidos."
                playerName "Pues has hecho un gran trabajo porque no se nota nada. Yo diría que están todos rotos y estropeados."
                graf "Eh... ¿Qué puedo hacer por ti, [playerName]?"
                $ primerGraf = 1
            else:
                playerName "Hola, Hawk."
                graf "Hola, mundo."
            jump hablarGraf
        "No interrumpir a la mujer.":
            jump go_CasaGraf

    jump go_CasaGraf

label SediFisk:

    scene bg sedi fisk

    "Ésta era la finca de Sedi Fisk, un nativo rico de Tatooine que un día desapareció misteriosamente. Desde entonces, su hogar se ha convertido en una ruina infestada de ratas womp."

    jump go_SediFisk

label TiendaJawa:

    scene bg tienda jawa
    show wassak

    "Esto es un reptador de las arenas de los jawas. Los jawas son nativos que sirven de quincalleros, vendiendo tecnología y chatarra que han recuperado o robado. Han dispuesto su tienda itinerante a las afueras de Mos Eisley."
    "El vendedor es Wassak, un jawa con el que has hablado en tus investigaciones pasadas."

    menu:
        "¿Quieres hablar con Wassak el jawa?"
        "Sí: Hablaré con Wassak el jawa.":
            play sound "sound/utinni.mp3"
            wassak "¡Utinni!"
            playerName "¡Utinni!"
            jump hablarWassak
        "No: Me voy a otro sitio.":
            pass

    jump go_TiendaJawa

label ZonaTusken1:

    scene bg zona tusken 1
    show tuskens
    play music "music/ambiental.mp3"

    if hablarTuskens == 0:
        jump hablarTuskens
    else:
        show tuskens
        "Entre dos montañas y cerca de un oasis, los nómadas tusken han montado un campamento con un centener de cabañas portátiles hechas de pieles de animales."
        "Es el poblado más grande que has visto nunca. Un clan grande de moradores tendría sólo unas veinte cabañas. Además, abundan las cajas de municiones y de armas."
        "Lo que curiosamente escasean son los banthas. Cada morador adulto está ligado a un bantha, y esos animales no se pueden esconder. Hay muchos menos banthas que moradores."

    jump go_ZonaTusken1

label ZonaTusken2:

    scene bg zona tusken 2

    "Has llegado a los aledaños del enclave tusken. Aquí apenas hay tiendas o pruebas de su presencia, excepto por unos túmulos erigidos para que los dioses protejan su periferia."
    
    jump hablarBob

    jump go_ZonaTusken2

label RecientesAtaques:

    scene bg recientes ataques

    if visitasteRecientesAtaques == 0:
        "Has llegado a la zona donde ha habido más ataques de moradores de las arenas contra granjeros de humedad. Está a sólo unos clics de las granjas. Posiblemente los granjeros a menudo llegaban hasta aquí, puede que incluso sus hijos jóvenes."
        "No cuesta mucho encontrar restos del ataque: Jirones ensangrentados de ropa, trozos de huesos, restos de palos gaffi y de equipo avanzado... Hay huellas de banthas y rastros de speeders. Claramente aquí ha habido una escaramuza."
        playerName "Pero eso no tiene sentido. Los moradores de las arenas rara vez se acercan tanto a zonas civilizadas, a menos que estén en pie de guerra. ¿Qué les ha llevado a atacar? Los granjeros han conseguido mantener un cierto equilibrio con ellos."
        "Estudias la arena y los despojos con el ceño fruncido. Tus ojos parpadean y tu frente sufre bajo el calor abrasador de los dos soles mientras las ruedas dentadas en tu cabeza buscan con ahínco una pista que estás segur[tuO] de poder encontrar aquí."
        "Finalmente encuentras unas huellas inusuales cerca de los restos de un bantha; el costillar de la bestia ha impedido que se borren del todo. Cuatro dedos con garras en disposición simétrica con un talón triangular, que sugieren un canino."
        playerName "No he visto ningún canino en las granjas de humedad, ni hay nada parecido extendido entre granjeros o moradores de las arenas. Pero se me ocurre que..."
        "Encuentras restos de un fluido en el cadáver del bantha. Lo frotas con tus dedos y te los llevas a la boca. Lo reconoces inmediatamente como un veneno debilitador, que en tan poca cantidad no te va a hacer efecto."
        show raquordaan at right with dissolve
        playerName "{i}Raquor'daan,{/i} el lobo oscuro de Sriluur. Es la bestia de presa domesticada por los brutales weequays. Pero no debería haber weequays aquí desde la muerte de Jabba."
        hide raquordaan
        "Una vez has encontrado las pisadas del lobo oscuro, te cuesta poco descubrir por dónde se fue. Encuentras huellas de más lobos y de los que posiblementes fuesen sus amos weequays, y finalmente das con el rastro de su speeder."
        "Fueron hacia el norte desde aquí. Entrecierras tus ojos oteando el horizonte. ¿Estás viendo una ciudad en lontananza?"
        show jako amarillo
        playerName "¿Jako, me recibes?"
        jako "Zzzz... Zzzzí perzzzzeptor."
        playerName "Triangula mi posición y después dime si hay un asentamiento al norte de donde estoy, a unos tres clics."
        jako "Zzzí, [playerName], o cazzzi."
        playerName "¿Casi hay una ciudad? Explícate."
        jako "Mozzz Gamozzz fue una ezzzcazzza poblazzzión en tiempozzz pazzzadozzz, pero fue dezzzocupada variazzz vezzzezzz. Ezzz hoy una zzziudazzz fantazzzma..."
        show mosgamos at left with dissolve
        jako "La última vezzz que ezzztuvo habitada, fue la bazzze de pizzztolerozzz clantaani, hazzzta que Jango Fett lozzz mató a todozzz en 32 ABY."
        hide mosgamos
        playerName "Parece que vuelve a ser la guarida de algún criminal. Voy a tener que echar un vistazo a ver qué descubro."
        jako "¿¡Qué!? ¿Quién te creezzz que erezzz? ¿Xim el Dézzzpota? Ezzzo ezzz peligrozzzo..."
        playerName "Corto y cierro, Jako."
        hide jako
        "Desde aquí puedes volver a las granjas de humedad o ir hasta Mos Gamos."
        $ visitasteRecientesAtaques = 1
    else:
        "Has llegado a la zona donde ha habido más ataques de moradores de las arenas contra granjeros de humedad, a sólo unos clics de sus granjas."
        "Después de estudiar la zona, has descubierto el rastro de unos weequays que iban hacia Mos Gamos, un pueblo supuestamente abandonado al norte."
        "Desde aquí puedes volver a las granjas de humedad o ir hasta Mos Gamos."

    jump go_RecientesAtaques

label MosGamos:

    scene bg mos gamos

    if visitasteMosGamos == 0:
        "Mos Gamos debería ser un pueblo vacío, sin más movimiento que el que traiga el viento. Al principio te parece ver personas en trajes aislantes, pero en seguida compruebas que son espantajos para ahuyentar a los animales."
        "Los edificios están sucios y, a simple vista, sí que parecerían abandonados. No es la primera vez que los habitantes de un sitio huyen dejando toda la tecnología activada. Pero hay muchas cosas que no cuadran."
        "Desde luego, está esa pequeña nave azul. Los carroñeros deberían haberse ocupado de ella en las varias décadas desde la visita de Jango Fett."
        "También hay huellas recientes de pies y patas, posiblemente los weequays y sus lobos. Las sigues intentando no hacer ruido, y encuentras un edificio con la puerta abierta."
        playerName "La seguridad de aquí se basa en que nadie sospeche que aquí hay algo. Nadie husmea dentro de una choza que se va a caer a trozos. Bueno, nadie inteligente. Pero no contaban conmigo."
        scene bg interior mos gamos
        "El interior del rancho está mejor abastecido. Hay muestras de tecnología avanzada, pero no demasiadas. Ves aparatos como el bastón aturdidor, orientados a mantener prisioneros. ¿Qué está pasando aquí?"
        show weequay with dissolve
        "Un guardia weequay gira una esquina y te intercepta. Lleva un arma en cada una de sus manos, y su olor es intensísimo."
        menu:
            "Atacarle.":
                "Intentas pelear con el weequay, pero él es mucho más rápido que tú. Su pica de fuerza te golpea y una descarga aturdidora te inmoviliza."
                "Un instante después, el weequay te pone su cuchillo en el cuello y te ejecuta."
                jump HasMuerto
                return
            "Hablarle.":
                playerName "¡Alabado sea el dios Raquor, que camina por las llanuras en forma de lobo oscuro!"
                "El guardia había alzado su pica de fuerza para golpearte, pero de pronto se detiene y te escucha."
                playerName "Traigo una bestia que he cazado para ofrendarla a Raquor. ¿Puedes guiarme a su santuario?"
                "El weequay te mira suspicaz. No ha visto muchos seguidores de su religión que no fuesen weequays (quizá porque no existen), pero quiere darte el beneficio de la duda."
                "Con un gesto de sus manos, te pide que enseñes el sacrificio."
                if itemRataMuerta == 1:
                    show ratamuerta at left
                    "Sacas la rata womp muerta que te dio Jent Loquoy y se la enseñas al weequay."
                    play sound "sound/risaweequay.mp3"
                    "El weequay parece reír al ver tu exigua ofrenda."
                    playerName "Hubo otras doce como ésta, pero las quemé tras vencerlas. ¿Quizá no sabes que su mordisco transmite enfermedades? Fue una buena caza."
                    "El weequay se encoge de hombros. Su cara es demasiado inexpresiva para saber si está satisfecho.{p}Sin embargo, se echa a un lado y con los brazos te deja paso."
                    hide ratamuerta
                elif itemArmaJawa == 1:
                    "Sacas la pistola iónica que te vendió Wassak. El weequay la mira confuso, porque no es lo que él esperaba; pero no hace nada. Quizá sólo estás moviendo el arma porque tu sacrificio está debajo."
                    "El arma iónica no puede dañar a un orgánico, pero sí a la tecnología: Disparas a la barra brillante que ilumina la habitación y de pronto la dejas a oscuras."
                    scene bg interior mos gamos
                    show weequay
                    "Tú estás preparado para esto, pero él no. Eso te permite empujarle y escapar a otra sala. Cierras la puerta a tu espalda."
                else:
                    "Rebuscas en tu inventario algo que mostrar, pero no encuentras nada útil. El weequay empieza a impacientarse, taconeando el suelo varias veces."
                    "Finalmente, comprendes que estás en un aprieto e intentas huir por donde has venido, pero el guardia no había dejado de vigilarte. Te lanza el cuchillo y lo clava en tu pierna."
                    "Un instante después, tienes al weequay encima con su pica preparada. Lo último que ves es que ha puesto el control de la pica en posición letal antes de bajarla."
                    jump HasMuerto
                    return
        hide weequay
        "Has llegado a un pasillo. Con un control de la puerta, bloqueas el acceso para que el weequay no pueda seguirte, y sigues explorando."
        scene bg habitacion mos gamos
        show droidemalo
        show weequay at right
        "Has encontrado una sala con monitores desde donde puedes observar otras salas sin ser visto. Sólo hay actividad en una, en la que un droide RA-7 está dando instrucciones a un weequay."
        droidemalo "Espero que estéis satisfechos. Habéis podido cazar los banthas de los moradores de las arenas para sacrificarlos a vuestros dioses."
        "El weequay no responde."
        droidemalo "Las tribus tusken os habrían aplastado si yo no hubiese ocultado vuestra implicación. En vez de eso, yo hice que los guiaseis a una trampa para capturarles. ¿Están bien retenidos en el sótano?"
        "El weequay asiente discretamente con la cabeza."
        droidemalo "Ahora los moradores se enfrentarán a los granjeros de humedad y a los jawas, y Vykan Fenn les venderá armas a todos ellos. La guerra es buen negocio."
        droidemalo "Mientras tanto, llevarás a los prisioneros tusken a la Nébula Fantasma, hasta que encontremos alguien que compre tropas {i}berserker{/i}, y los soltaremos en el planeta que nos diga."
        "El weequay no dice nada. No es un gran conversador; por sus abalorios, ves que ha hecho voto de silencio en honor al dios Quay."
        droidemalo "Ve al borde del sistema y consígueme un carguero, discretamente. Necesitamos bodegas resistentes pero con suministro de aire."
        hide weequay
        "El weequay se va; el droide queda inmóvil como si fuese un objeto inanimado. Cuando oyes los motores de su nave despegando, tienes una ocasión de entrar en esa sala."
        droidemalo "¿Quién eres tú?"
        menu:
            "Atacarle.":
                if itemArmaJawa == 1:
                    "Llevas preparada el arma iónica de Wassak y le disparas a quemarropa. El perno de sujección queda enganchado en su vientre."
                else:
                    "En cuanto intentas atacar, el droide se pone en guardia. Te dispara un láser a quemarropa desde su dedo, con precisión letal."
                    droidemalo "No había ningún código de confirmación, espía."
                    jump HasMuerto
                    return
            "Farolear.":
                playerName "Soy [tuUn] agente de Umbara. Tengo nuevas instrucciones. Debemos cancelar esta operación, se ha vuelto demasiado peligrosa."
                droidemalo "¿Cuál es el código de confirmación?"
                playerName "Bueno, eh... ¿Vy...?"
                "El droide te dispara un láser a quemarropa desde su dedo, con precisión letal."
                droidemalo "No había ningún código de confirmación, espía."
                jump HasMuerto
                return
        play sound "sound/droidefalla.mp3"
        "El droide queda envuelto en destellos azules que queman sus circuitos. Chirriando de dolor, cae al suelo."
        hide droidemalo with dissolve
        show cabezadroide with dissolve
        playerName "Aunque el droide ya no se pueda mover, su memoria sigue intacta y se puede reproducir. Esta cabeza es exactamente la prueba que necesitas de lo que está pasando."
        $ itemCabezaDroide = 1
        $ visitasteMosGamos = 1
    else:
        "Desde la última vez que estuviste aquí, Mos Gamos ha pasado a ser una auténtica ciudad fantasma. Los weequays se han marchado. Los moradores de las arenas han sido liberados."
        "Se podría reconstruir la ciudad, pero de momento no parece haber suficiente interés. Después de todo, desde aquí sólo se puede ir a un sitio..."

    jump go_MosGamos

label PalacioJabbaExt:

    scene bg palacio jabba ext

    "La construcción ante tus ojos es famosa por haber sido el Palacio del gánster Jabba el Hutt, aunque más bien parece una fundición. Empezó como monasterio de la religiosa Orden de [bomarr]."
    "Un siglo atrás, los monjes dieron cobijo a un criminal precursor de Jabba, y desde entonces no faltaron bandidos en su hogar. Tras la muerte de Jabba, sin embargo, se dice que sólo los monjes siguen dentro de esas paredes."

    jump go_PalacioJabbaExt

label PalacioJabbaInt:

    scene bg palacio jabba int
    show monje1 at left
    show monje2 at right

    "El acceso más fácil al interior del palacio es a través del garaje de barcazas, que está abierto. No está desocupado, sin embargo: Entre los vehículos hay dos monjes [bomarr]."
                                                               
    
    if asustasteBandido == 1 and bandidoCapturado == 0:
        "Los monjes se apartan de tu camino, dejándote paso libre para perseguir a Thondo Qo."
        jump go_PalacioJabbaInt
    else:
        "¿Quieres hablar con los monjes?"
        menu:
            "Hablar con monjes.":
                jump hablarMonjes
            "No hablar con monjes.":
                pass

    jump go_PalacioJabbaInt

label RutaDesierto1:

    scene bg ruta desierto 1

    if visitasteCamino1 == 0:
        "Arena hasta donde alcanza la vista, con los soles gemelos de Tatooine repartiendo un calor abrasador. Si pasas mucho tiempo por aquí, sin duda te deshidratarás."
        "Según has leído en los mapas, un poco más adelante está el Desfiladero del Peñón Mellado, donde seguramente haya algo de sombra."
        $VisitasteCamino1 = 1
    elif visitasteCamino1 == 1 and bandidoCapturado == 0:
        "Ésta es una zona del Mar de Dunas que lleva hacia el Desfiladero del Peñón Mellado. Aquí hace mucho más calor que en la mayoría de otros lugares."
    elif visitasteCamino1 == 1 and bandidoCapturado == 1:
        "Ésta es una zona del Mar de Dunas que lleva hacia el Desfiladero del Peñón Mellado. Pasaste por aquí cuando capturaste a Thondo Qo."

    jump go_RutaDesierto1

label RutaDesierto2:

    scene bg ruta desierto 2

    if visitasteCamino2 == 0:
        "Estás en una zona del desierto menos ardua que otras; aquí uno puede refugiarse contra parte del calor yendo cerca de una pared del Desfiladero."
        "Eso debió decidir la persona que construyó una especie de hábitat o choza prefabricada en uno de los laterales. No tiene puerta, y sin duda ha sido usada como escondite en el pasado."
        $VisitasteCamino2 = 1
        menu:
            "Ir a otro sitio.":
                jump go_RutaDesierto2
            "Explorar la choza.":
                jump exploraChoza

    elif visitasteCamino2 == 1 and itemDiarioErmitano == 0 and bandidoCapturado == 0:
        "En esta zona del desierto empieza el Desfiladero. Hace calor, pero menos que en otros lugares."
        "Ves la entrada a una choza. Puedes buscar en su interior si quieres, pero tienes pruebas de que Thondo Qo siguió adelante, no se ocultó allí."
        menu:
            "Ir a otro sitio (Seguir persiguiendo al Bandido).":
                jump go_RutaDesierto2
            "Explorar la choza.":
                jump exploraChoza

    elif visitasteCamino2 == 1 and itemDiarioErmitano == 0 and bandidoCapturado == 1:
        "En esta zona del desierto empieza el Desfiladero. Hace calor, pero menos que en otros lugares."
        "Ves la entrada a una choza. Puedes buscar en su interior si quieres, ahora que ya no hay que preocuparse por Thondo Qo."
        menu:
            "Explorar la choza.":
                jump exploraChoza
            "Seguir tu camino.":
                jump go_RutaDesierto2


    elif visitasteCamino2 == 1 and itemDiarioErmitano == 1 and bandidoCapturado == 0:
        "En esta zona del desierto empieza el Desfiladero. Hace calor, pero menos que en otros lugares.{p}Sabes con certeza que Thondo Qo siguió adelante hacia el interior del Desfiladero."
        "Ves también la entrada a una choza. Puedes buscar en su interior si quieres, pero Thondo Qo está suelto y no está dentro."
        menu:
            "Explorar la choza.":
                "Este sitio ha sido habitado por un ermitaño en el pasado, no hace demasiado tiempo, pero ahora está abandonado. Sólo quedan algunos muebles y objetos personales."
                "El ermitaño ha dejado un diario holográfico atornillado al suelo. Estos objetos se usan para grabar mensajes relativamente cortos y dejarlos disponibles para todo el que esté físicamente allí."
                "¿Quieres leer el diario del ermitaño?"
                menu:
                    "Sí.":
                        jump leediariodelermitano
                    "No.":
                        pass
                jump go_RutaDesierto2
            "Seguir tu camino.":
                jump go_RutaDesierto2

    elif visitasteCamino2 == 1 and itemDiarioErmitano == 1 and bandidoCapturado == 1:
        "En esta zona del desierto empieza el Desfiladero. Hace calor, pero menos que en otros lugares."
        "Pasaste por aquí cuando perseguías a Thondo Qo, y también revisaste el interior de la choza que hay abierta en la pared del Desfiladero."
        menu:
            "Explorar la choza.":
                "Este sitio ha sido habitado por un ermitaño en el pasado, no hace demasiado tiempo, pero ahora está abandonado. Sólo quedan algunos muebles y objetos personales."
                "El ermitaño ha dejado un diario holográfico atornillado al suelo. Estos objetos se usan para grabar mensajes relativamente cortos y dejarlos disponibles para todo el que esté físicamente allí."
                "¿Quieres leer el diario del ermitaño?"
                menu:
                    "Sí.":
                        jump leediariodelermitano
                    "No.":
                        pass
            "Seguir tu camino.":
                jump go_RutaDesierto2

    jump go_RutaDesierto2

label RutaDesierto3:

    if dragon == 1:
        scene bg ruta desierto 3
        play sound "sound/krayt.ogg"
        "El dragón sigue aquí, las garras de sus cuatro patas clavadas en el suelo. Está enfurecido por el estrépito causado por Qo, y no permitirá que nadie pase por aquí."
    elif dragon == 0:
        scene bg ruta desierto 3
        play sound "sound/krayt.ogg"
        "El ruido de la moto ha despertado a un habitante del cañón: Un colosal reptil con cuernos, púas y unos dientes que pueden pulverizar piedras. Aunque es una forma de vida fascinante, es demasiado peligroso para que te acerques a él."
        "Es la variante pequeña del dragón krayt, el dragón de cañones, que sólo mide treinta metros de largo. Come banthas, eopies, ratas womp, y a algunos tuskens que lo persiguen como rito de madurez. Es el animal más grande que puede matar un solo cazador en este mundo."
        "Las garras de sus cuatro patas están clavadas en el suelo. El dragón está enfurecido por el estrépito causado por Qo, y no permitirá que nadie pase por aquí."
        $ dragon = 1
    else:
        scene bg ruta desierto 3 sin dragon
        "El dragón ha desaparecido, pero quedan restos de sangre verdosa, huesos y fragmentos de armas primitivas. Parece que [UOuuuhrRr] ha pasado por aquí, y ha vivido para contarlo."

    jump go_RutaDesierto3

label RutaDesierto4:

    scene bg ruta desierto 4

# Activos Rebeldes: No lo has visto 0; encontrado 1. Cuando hables con Graf, 2.

    # "TBA: VisitasteCamino4: %(visitasteCamino4)d."
    # "TBA: activosRebeldes: %(activosRebeldes)d. bandidoCapturado: %(bandidoCapturado)d."

    "En esta zona del desierto, un cañón ancho, el Desfiladero del Peñón Mellado, te protege de las inclemencias de los soles gemelos. Por otro lado, también protege a los animales nativos, muchos de los cuales son peligrosos."
    "Los contrabandistas y otros fugitivos a menudo eligen cuevas en estos muros para atracar sus naves y esconderse de las autoridades. De hecho ves una gran cueva con restos de tecnología a la vista."

    if visitasteCamino4 == 0 and bandidoCapturado == 0:
        "En este momento, estás persiguiendo a Thondo Qo. Quizá él se ha intentado esconder en esa cueva, así que podrías investigarla. O quizá él te ha tendido una trampa allí."
        "No ves movimiento dentro de la cueva, pero sí indicios de actividad reciente en los últimos días, quizá una semana."
        "¿Será mejor seguir adelante por el desierto, o explorar la cueva llena de tecnología?"
        $visitasteCamino4 = 1
        menu:
            "Seguir por el desierto.":
                jump go_RutaDesierto4
            "Explorar la cueva.":
                jump encontrasteActivosRebeldes

    elif visitasteCamino4 == 1 and activosRebeldes == 0 and bandidoCapturado == 0:
        "Thondo Qo sigue fugado y le has visto en el desierto. Quizá él se ha intentado esconder en esa cueva, así que podrías investigarla. O quizá él te ha tendido una trampa allí."
        "No ves movimiento dentro de la cueva, pero sí indicios de actividad reciente en los últimos días, quizá una semana."
        "¿Será mejor seguir adelante por el desierto, o explorar la cueva llena de tecnología?"
        $visitasteCamino4 = 1
        menu:
            "Seguir por el desierto.":
                jump go_RutaDesierto4
            "Explorar la cueva.":
                jump encontrasteActivosRebeldes

    elif visitasteCamino4 == 1 and activosRebeldes == 0 and bandidoCapturado > 0:
        "La cueva tiene indicios de actividad reciente en los últimos días, quizá semanas, pero no notas movimiento dentro de ella."
        "Ahora que Thondo Qo está entre rejas, quizá puedas tomarte unos minutos para investigarla."
        menu:
            "Seguir por el desierto.":
                jump go_RutaDesierto4
            "Explorar la cueva.":
                jump encontrasteActivosRebeldes

    elif visitasteCamino4 == 1 and activosRebeldes == 1 and bandidoCapturado == 0:
        "Ya has explorado el interior de la cueva, y sabes que Thondo Qo no ha estado allí. Lo más probable es que haya escapado hacia el otro extremo del cañón."

    elif visitasteCamino4 == 1 and activosRebeldes == 1 and bandidoCapturado == 1:
        "Ya has explorado el interior de la cueva y sabes que las naves están dentro, pero no puedes hacer nada con ellas."
        "Al fondo está la zona del cañón donde capturaste al fugitivo Thondo Qo."

    elif visitasteCamino4 == 1 and activosRebeldes == 2 and bandidoCapturado == 0:
        "Ya has explorado el interior de la cueva y sabes que las naves están dentro, pero no puedes hacer nada con ellas. Thondo Qo no estuvo allí."
        "Es importante apresar a Thondo Qo, que posiblemente escapó hacia el final del cañón."

    elif visitasteCamino4 == 1 and activosRebeldes == 2 and bandidoCapturado == 1:
        "Ya has explorado el interior de la cueva y sabes que las naves están dentro, pero no puedes hacer nada con ellas. Ahora son problema de Hawk."
        "Al fondo está la zona del cañón donde capturaste al fugitivo Thondo Qo."

    jump go_RutaDesierto4

label RutaDesierto5:

    scene bg ruta desierto 5

    if visitasteCamino5 == 0:
        "Has llegado al final del Desfiladero del Peñón Mellado, posiblemente donde Jent Loquoy estrelló su T-16. Parece una zona difícil de recorrer a altas velocidades, y no lo digo por nada."
        "También ves los restos estrellados de una moto-jet, aún llameantes y expulsando una columna de humo negro que se eleva hasta el cielo. Alguien ruge en el siniestro."
        show bandido
        "Al acercarte, ves que es Thondo Qo. El accidente le ha dejado inmovilizado, con los restos metálicos de la moto-jet apresándolo. Un cilindro de balanceo mantiene sus brazos inmovilizados, y el array sensor se le ha clavado en el pecho."
        bandido "Ayúdame... Cuando el fuego llegue al combustible, explotará y me matará..."
        menu:
            "Ayudarle a salir.":
                "Coges las piezas rotas de la moto-jet e intentas levantarlas. Pesan más de lo que parece, así que necesitas las dos manos y un esfuerzo visible."
                "En cuanto Qo tiene las dos manos libres, desenfunda una pistola bláster y te dispara a quemarropa en el vientre."
                play sound "sound/blasterpesado.mp3"
                "Sueltas los pedazos de la moto, pero ahora que él puede usar los brazos, los sostiene y los levanta."
                "Riendo, Qo se sube a tu eopie y te deja atrás para que mueras. No tardarás, porque no puedes moverte y el fuego ha llegado al depósito de combustible"
                play sound "sound/explosion.mp3"
                jump HasMuerto
                return
            "Negociar su rendición.":
                playerName "No me fío de ti, Qo. Ríndete primero y deja que te espose, o no te soltaré."
                bandido "¿Estás loc[tuO]? ¡No hay tiempo de esposarme! Esto puede explotar en cualquier momento."
                bandido "Me rindo, lo prometo. Dejaré que me esposes cuando me hayas salvado la vida, ¡te deberé la vida! Ya ves que estoy herido, no voy a escapar."
                menu:
                    "Liberarle.":
                        playerName "De acuerdo, confiaré en ti."
                        "Coges las piezas rotas de la moto-jet e intentas levantarlas. Pesan más de lo que parece, así que necesitas las dos manos y un esfuerzo visible."
                        "En cuanto Qo tiene las dos manos libres, desenfunda una pistola bláster y te dispara a quemarropa en el vientre."
                        play sound "sound/blasterpesado.mp3"
                        "Sueltas los pedazos de la moto, pero ahora que él puede usar los brazos, los sostiene y los levanta."
                        "Riendo, Qo se sube a tu eopie y te deja atrás para que mueras. No tardarás, porque no puedes moverte y el fuego ha llegado al depósito de combustible"
                        play sound "sound/explosion.mp3"
                        jump HasMuerto
                        return
                    "Exigir las esposas.":
                        playerName "No confío en ti. Acepta mis condiciones, o no hay rescate."
                        bandido "¡Oh, de acuerdo!"
                        "Qo extiende sus hirsutas manos para que le encadenes, gruñendo enojado durante todo el proceso. También le quitas una pistola blaster, que tiras al suelo."
                        "Coges las piezas rotas de la moto-jet e intentas levantarlas. Pesan más de lo que parece, así que necesitas las dos manos y un esfuerzo visible."
                        "En cuanto Qo tiene las dos manos libres, intenta atacarte, pero sus grilletes le impiden moverse diestramente. Te echas atrás y eso basta para esquivarle."
                        play sound "sound/explosion.mp3"
                        "Empujas a Qo unos metros más adelante; él solo se cae al suelo. La moto-jet explota inofensivamente, aunque asusta levemente a tu eopie. Activas tu comunicador."
                        show jako amarillo at right
                        playerName "Jako, ¿puedes enviar mis coordenadas a un cazarrecompensas llamado 4-LOM para que se pase a recoger un prisionero?"
                        jako "Zzzí, perzzzeptor... Zzziempre ezzz zzzatizzzfactorio zzzozzziabilizzzar con otro droide..."
                        hide jako with dissolve
                        play sound "sound/motojet.mp3"
                        show cazador at right
                        "4-LOM apenas tarda unos minutos en aparecer, montando en una plataforma flotante."
                        cazador "Thondo Qo, estás arrestado por la autoridad del Imperio Galáctico. Saludos, [playerName]. Has cumplido tu palabra. No me opongo a colaborar contigo en el futuro."
                        playerName "Esto va a ser lo más agradable que me digas... ¿Puedes darme alguna prueba de que Qo ha sido apresado?"
                        cazador "He subido a los registros oficiales el informe de la captura, indicando tu colaboración. Todos pueden saber que has apresado a Thondo Qo."
                        "4-LOM se lleva a Thondo Qo en su plataforma, elevándose por encima de los acantilados. Más vale que Tho no intente escaparse o se caerá docenas de metros."
                        $ visitasteCamino5 = 1
                        $ bandidoCapturado = 1
                        $ hablarCazador = 2
    else:
        "Éste es el extremo final del Desfiladero del Peñón Mellado, donde capturaste a Thondo Qo, y donde Jent Loquoy estrelló su T-16."
        "El desierto se extiende durante kilómetros inacabables hacia el horizonte. No hay nada interesante en esa dirección."

    jump go_RutaDesierto5

label Granjas:

    scene bg granjas
    show granjero
    
    "Las granjas de humedad son una necesidad en mundos con escasa agua: Los granjeros trabajan duro con sus evaporadores para obtener del entorno agua con la que regar sus cosechas subterráneas en jardines hidropónicos y, si sobra, para venderla a otros habitantes a altos precios. Rara vez sobra."
    menu:
        "¿Quieres hablar con un granjero genérico?"
        "Hablaré con un granjero.":
            playerName "Hola, pintoresco figurante genérico. ¿Qué puedes contarme de interés?"
            jump hablarGranjero
        "No hablaré con granjeros.":
            pass

    jump go_Granjas

label GranjaDarklighter:

    scene bg granja darklighter
    if hablarDarklighter == 0:
        show darklighter
        "El barón Huff Darklighter es conocido en todo el sistema por ser el granjero de humedad de más éxito, dueño de una docena de granjas. Su ostentosa villa, que incluye muchos de sus activos, se extiende ante ti. Has visto gobernadores planetarios con menos dinero que Darklighter."
        menu:
            "Darklighter en persona está ante ti. ¿Quieres hablar con Darklighter?"
            "Hablar con Darklighter.":
                darklighter "¡Hola, viajer[tuO] espacial! Dime por favor tu nombre; el mío, que sin duda has oído ya, es Barón Huff Darklighter. Soy el potentado de las granjas de humedad."
                playerName "Me llamo [playerName] y soy xenobiólog[tuO]. He venido a estudiar las formas de vida locales."
                darklighter "La vida tiende a abrirse paso incluso en estos inhóspitos parajes. Encontrarás formas de vida fascinantes: Los jerbas, los skettos y los banthas de los moradores de las arenas."
                playerName "He oído precisamente que los moradores están causando muchos problemas a los granjeros, y que aparecen con menos banthas que lo habitual."
                darklighter "Ah, quizá has oído también que nadie sabe mejor que el Barón lo que sucede en las granjas, ¿verdad? ¿Es eso lo que quieres averiguar?"
                darklighter "¿Qué quieres saber, [playerName]?"
                jump hablarDarklighter
            "No hablar con Darklighter.":
                pass
    else:
        "Huff Darklighter está reunido y no puede atenderte en este momento."

    jump go_GranjaDarklighter

label GranjaLoquoy:

    scene bg granja loquoy

    if hablarLoquoy == 0:
        show loquoy at right
    if questReclutarPiloto < 2:
        show jent

    "La granja de la familia Loquoy tiene varios evaporadores y droides dispersos por un territorio que parece mayor que el de la mayoría de otras granjas. Sólo hay un hábitat, dominado por un edificio de planta circular con dos pisos; casi ninguna otra granja alcanza esas alturas."
    
    if primeraVezEnGranjaLoquoy == 0:
        jent "Hola, [playerName]. Ésta es mi madre, Lorna."
        $ primeraVezEnGranjaLoquoy = 1

    if hablarLoquoy == 0 and questReclutarPiloto < 2:
        menu:
            "¿Quieres hablar con alguno de ellos?"
            "Con Jent.":
                jent "Hola, [playerName]. Me alegra que hayas venido y aceptado mi oferta."
                jump hablarJentGranja
            "Con Lorna.":
                if saludarLoquoy == 0:
                    loquoy "Hola. Soy Lorna Loquoy, granjera de humedad. Llámame Lorna la Larga. Creo que has conocido a mi hija Jent."
                    playerName "¿Siempre ha sido usted granjera de humedad, Lorna la Larga?"
                    loquoy "No, yo antes era tripulante en una cañonera pira... quiero decir, en un carguero mercante. Lo dejé porque, eh, quería sentar cabeza. Me enamoré del padre de Jent, eh..."
                    $ saludarLoquoy = 1
                else:
                    loquoy "¿Puedo hacer algo más por ti, [playerName]?"
                    playerName "Tengo alguna pregunta más, Lorna la Larga..."
                jump hablarLoquoy
            "Con ninguno.":
                pass
    elif hablarLoquoy > 0 and questReclutarPiloto < 2:
        menu:
            "¿Quieres hablar con Jent?"
            "Veeenga.":
                jent "Hola, [playerName]. Me alegra que hayas venido."
                jump hablarJentGranja
            "No.":
                pass        

    jump go_GranjaLoquoy