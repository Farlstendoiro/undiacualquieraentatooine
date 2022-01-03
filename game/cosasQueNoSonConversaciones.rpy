# En el Hangar / cuando recibas Investigación Cerrada y Oscilador y Permiso de Despegue. Lo llamaré ComprobarLosTres
# Esto se puede hacer en el Hangar o cada vez que recibas uno de estos tres.

label labeluno:
    "Estoy en label 1."
    return
    
label labeldos:
    "Estoy en label 2."
    return


label ComprobarLosTres:
    # "TBA - Comprobando si tienes los tres: %(itemOscilador)d%(itemInvestigacion)d%(itemPermisoDespegue)d"
    if itemOscilador == 1 and itemInvestigacion == 1 and itemPermisoDespegue == 1:
        "¡Has conseguido todo lo necesario para acceder a tu nave, repararla y despegar!"
        "Ahora sólo tienes que ir al hangar, subir a bordo y marcharte de este planeta...{p}A menos que haya algo más que quieras hacer aquí, claro."
    else:
        "Has conseguida una de las cosas necesarias para acceder a tu nave, repararla y despegar.{p}Pero todavía no lo tienes todo."
    return
        
label teDanPaliza:
    if apalizadoPorTropas < 1:
        show trooper at left
        show trooper2 at right
        show trooper3
        "Tres siluetas bloquean la luz de soles gemelos que viene desde la calle. Son soldados de asalto imperiales con sus armaduras blancas y sus rifles bláster en las manos."
        trooper "¡Ciudadan[tuO] [playerName]! Tenemos un asunto que discutir con usted."
        "Mientras un soldado habla, el otro ha caminado discretamente hasta ponerse a tu espalda. Rápidamente te agarra los brazos, inmovilizándote, y entonces el cabecilla te da un brutal puñetazo en el estómago."
        trooper "Éste es el asunto: No te metas en lo que no te importa. Es malo para tu salud, y la próxima vez puede ser fatal. ¿Me copias?"
        "El siguiente golpe es en tu ojo derecho. Las venas parecen estallar, y ahora apenas puedes ver de dónde vendrán los próximos ataques."
        "Entonces notas otro impacto en la cara y tu boca degusta el sabor metálico de tu propia sangre, que llega a manchar tus fosas nasales."
        "Te encorvas dolorid[tuO] y, por lo menos, te das cuenta de que ahora nadie te está agarrando. Tienes una ocasión de reaccionar. ¿Qué harás ahora?"
        menu:
            "Pelear.":
                "Intentas defenderte a puñetazos, pero los soldados bloquean fácilmente tus torpes ataques con sus antebrazos. Ellos están mucho más entrenados que tú."
                "Uno de los soldados, riendo bajo su casco, se pone a tiro para que le golpees en la placa pectoral. Él no nota nada, pero ahora tu mano duele más que casi cualquier otra parte de tu cuerpo, y ahora mismo te duele casi todo."
            "Quitar el rifle a un soldado.":
                "Intentas quitarle el rifle a uno de los soldados. Aunque no lo consigas, por lo menos estarás demasiado cerca de uno para que los otros dos te vapuleen tan fácilmente."
                "Para tu sorpresa, consigues arrebatarle el rifle. Lo sostienes, una mano en el cañón y otra en el visor, preguntándote cómo has conseguido superar al soldado."
                trooper "¡Tiene un arma! ¡Abatidl[tuO]!"
                "Un segundo demasiado tarde, comprendes que el soldado te ha dado el rifle como excusa para usar fuerza letal."
                play sound "sound/blaster.mp3"
                with flash
                "Los otros dos soldados te apuntan con sus rifles y te disparan. Los dos aciertan."
                jump HasMuerto
            "Usar el arma jawa." if itemArmaJawa == 1:
                "Desenfudas el bláster de ionización que te vendió el jawa. Sólo sirve contra droides y otras máquinas, pero quizá les sorprenda y te dé ventaja."
                trooper "¡Tiene un arma! ¡Abatidl[tuO]!"
                play sound "sound/blaster.mp3"
                with flash
                "Los soldados te apuntan con sus rifles y te disparan. Todos ellos aciertan."
                jump HasMuerto
            "Negociar con ellos.":
                playerName "Hablemos... Lleguemos a un acuerdo..."
                trooper "¿Quieres hacer un trato? ¿Qué puede tener [playerName] que nos interese?"
                menu:
                    "Ofrecer un soborno.":
                        playerName "Digamos que la paliza ya ha sucedido. Todo el mundo tiene un precio..."
                        trooper "¿Cómo te atreves a insultar a soldados del Imperio? ¡Un imperial no puede ser comprado!"
                        play sound "sound/blaster.mp3"
                        with flash
                        "Los soldados te apuntan con sus rifles y te disparan. Todos ellos aciertan."
                        jump HasMuerto
                    "Prometer no investigar su caso.":
                        playerName "Me ocuparé sólo de mis asuntos y no me meteré en lo que no me importa."
                        trooper "No lo sé. Creo que ni siquiera sabes de qué estamos hablando, así que será mejor que te sigamos pegando."
                        playerName "¡Si queréis estar seguros, sólo tenéis que decirme qué debo evitar!"
                        "Los golpes no se interrumpen mientras intentas pactar con ellos."
                        trooper2 "¿Dónde acabas de estar, listill[tuO]? ¿Qué te pasó antes de que llegásemos? ¡Ésa es la cuestión!"
                        trooper "Cállate, AF-119."
            "Escapar.":
                "Intentas correr hacia el callejón, pero uno de los soldados te placa por la cintura. Entonces otro te pisa la pierna inmovilizada, y la intensa punzada te hace pensar que la ha roto."

        "Con la pierna incapaz de sostenerte, caes al suelo, pero la paliza no se detiene."
        "Posiblemente tendrás magulladuras visibles, si sobrevives a esto. De momento, necesitas toda tu determinación para seguir respirando."
        "Entonces notas otro impacto en la cara, tan duro que debe ser un culatazo, y tu boca degusta el sabor de tu propia sangre."
        "En este momento ya casi no puedes respirar y estás a un paso de la muerte. El dolor es tan intenso que casi preferirías morir, pero ahora mismo no tienes elección."
        "Los soldados se levantan y te miran desde un picado de superioridad. Uno de ellos parece querer darte una patada final, pero otro le detiene, sacudiendo la cabeza. No hay golpe de gracia para ti."
        trooper "Espero que lo hayas entendido, [playerName]. No nos gustaría tener que pasar por esto otra vez, pero {i}a ti{/i} te gustaría aún menos. ¿De acuerdo?"

        hide trooper
        hide trooper2
        hide trooper3
        "Se han ido. Te parece que ha sido hace un par de minutos, pero puede que hayan pasado horas. Ojalá pudieses levantar la cabeza y mirar el sol para poder medir el tiempo."
        "Eres incapaz de levantarte por ti mism[tuO], por mucho que lo intentes. Hay líquido en el suelo; no quieres pensar de qué se trata."
        show ghana negro with dissolve
        "Una sombra bloquea parte de la luz que llega desde la calle principal."
        misterioso "¿Qué es esto? ¿Quién está ahí? ¿[playerName], eres tú?"
        "Este callejón es demasiado remoto para que aparezca nadie. Puede que estés alucinando."
        show ghana with dissolve
        ghana "Parece que alguien te ha dado una paliza. Deja que te ayude..."
        playerName "¿Ghana... Gleemort? Creo que... no puedo levantarme... Sostenerme en pie..."
        ghana "Eres [tuUn] exagerad[tuO]. Te han vapuleado y zarandeado un poco. Seguro que fue para asustarte. Es sólo que no tienes costumbre de meterte en peleas. En seguida te sentirás mejor."
        ghana "Claramente necesitas un trago. Déjame ver qué tengo por aquí...{p}Tengo un bláster bantha, un borrador de mentes y un whisky sacorrano. ¿Qué prefieres?"
        menu:
            "Bláster bantha.":
                pass
            "Borrador de mentes.":
                pass
            "Whisky sacorrano.":
                pass
        play sound "sound/beber.mp3"
        ghana "Menos mal que mi hocico captó el olor de tu sangre, ¿verdad?"
        playerName "Desde luego... Esta cosa que me has dado es fuertecilla, ¿eh?"
        play sound "sound/risacerdo.mp3"
        ghana "Me quedaré hasta que te encuentres algo mejor. Hoy no tengo nada que hacer."
        playerName "El trabajo de cazador sigue mal, ¿eh?"
        ghana "Mira, ya sabes lo que le pasó a la mayoría de guardias de Jabba... He salido bien librado, pero apenas han pasado unos meses y Tatooine ya no es buen terreno de caza. No sé si la situación política de la galaxia es la mejor para mi negocio."
        ghana "Ya no hay grandes bestias. Así están los tusken de violentos: Necesitan demostrar su vigor contra dragones krayt y presas enormes, pero apenas quedan unos pocos animales así y no se encuentran fácilmente."
        if dragon == 1:
            playerName "He visto un dragón krayt en el Desfiladero del Peñón Mellado. Quizá puedas ir a por él."
            ghana "No tengo el material para cazar algo así, y además los tusken se enfadarían conmigo si les quito ese animal. Deberías decírselo a {i}ellos{/i}; son más agradecidos de lo que parece."
        playerName "Tienes otras habilidades. Podrías meterte a cazarrecompensas, sobre todo si consigues un socio de fiar o un droide."
        ghana "No se me dan bien las máquinas, y en este momento es difícil saber quién es de fiar. Mucha gente tiene vínculos con los gobiernos. Lo que sé que no quiero hacer es colaborar con el Imperio, como hace Terrem Jesond."
        playerName "Espera un momento, esto me interesa: ¿Jesond colabora con el Imperio? ¿Puedes demostrarlo?"
        ghana "Yo no, pero Nengih TurJinda trabaja para Jesond, y se jacta constantemente de sus tratos con imperiales corruptos... sobre todo cuando cree que los que escuchan son unos imbéciles incapaces de hacer algo al respecto."
        playerName "¿Cómo podría yo demostrarlo?"
        ghana "¿Qué te tengo dicho? Averigua de dónde viene tu presa. Eso me lo enseñó Ephant, el traficante de armas de Jabba. Si quieres saber para quién trabaja alguien, descubre de dónde viene."
        playerName "¡El planeta de origen, claro! Gracias, Ghana Gleemort."
        ghana "Encantado de ayudar.{p}Ya se te ve mejor. Voy a seguir mi camino."
        hide ghana
        $ apalizadoPorTropas = 1
        
    jump go_Callejon

label exploraChoza:

    scene bg choza ermitano

    if itemDiarioErmitano == 0:
        "La choza tiene apenas veinte metros cuadrados y está desordenada. Ha sido habitada por un ermitaño en el pasado, no hace demasiado tiempo, pero ahora está abandonado. Sólo quedan algunos muebles y objetos personales."
        "El ermitaño ha dejado un diario holográfico atornillado al suelo. Estos objetos se usan para grabar mensajes relativamente cortos y dejarlos disponibles para todo el que esté físicamente allí."
        $ itemDiarioErmitano = 1
    else:
        "Este sitio ha sido habitado por un ermitaño en el pasado, no hace demasiado tiempo, pero ahora está abandonado. Sólo quedan algunos muebles y objetos personales."
        "El ermitaño ha dejado un diario holográfico atornillado al suelo. Estos objetos se usan para grabar mensajes relativamente cortos y dejarlos disponibles para todo el que esté físicamente allí."

    "¿Quieres escuchar el diario del ermitaño?"
    menu:
        "Escuchar el diario ahora.":
            jump leediariodelermitano
        "No leer el diario ahora.":
            "Dejas el diario y sigues adelante."
    jump go_RutaDesierto2

label leediariodelermitano:
    show ermitano
    ermitano "Saludos, extraño. Si lees esto, seguramente yo estoy muerto. Espero que mi declaración sirva de advertencia a alguien."
    ermitano "Me llamo Ronk Bellstrike. Antes fui ranger en Antar y después cazador en el Borde. Se me daba bien, pero no tan bien. Me echaron por... múltiples pecadillos... reincidentes... Ejem"
    ermitano "Viviendo ya en Tatooine, me metí en problemas con gente de Jabba el Hutt por una deuda. Mi casa fue arrasada, mi familia murió. Yo me escondí, haciéndome el loco."
    ermitano "Desde entonces, entrené a varias manadas de ratas womp para que vigilasen mi casa y me advirtiesen si alguien se acercaba. Descubrí por las malas que nadie es de fiar."
    ermitano "Pasaron muchos años. Entonces llegó esa mujer. Me encontró."
    ermitano "Ella... tenía capacidades extraordinarias. {p=10} ¡Como los jedi de antaño!"
    ermitano "Debes estar prevenido si la ves: Era una mujer humana muy alta que no llegaba a los treinta. Esbelta, en buena forma y con cabello marrón corto."
    ermitano "Su mirada era lo peor: Era taimada, ladina y rigurosa. Era una mirada que se clavaba en tu alma como uno de los vibrofilos que ella usaba."
    ermitano "Ella me intimidó. Amenazó con matar a mis mascotas, y a personas inocentes, si yo no la ayudaba."
    ermitano "¡Ella tenía la capacidad de crear de la nada una rata womp gigantesca! Una que tenía manos en vez de dedos, hablaba y disparaba un bláster."
    ermitano "Pero no era una rata womp real, estoy seguro. Conozco el olor de las ratas, sus movimientos... No lo era."
    ermitano "Tampoco era un droide. No es posible construir un droide así: ¡Esa rata tenía la misma mirada que ella! ¡La misma esencia impía y maldita!"
    ermitano "La mujer tenía un plan. Hizo que mis ratas la acompañasen, me obligó a esconderme y hacer que las ratas siguiesen sus planes."
    ermitano "Emboscamos a varios granjeros que se acercaron a unos evaporadores. Atacamos a un jawa que buscaba chatarra en el desierto."
    ermitano "Lo peor fue cuando se estrelló el T-16 de una jovencita en el Desfiladero del Peñón Mellado. No provocamos el accidente, pero estábamos en la zona, y la mujer dijo que no quería testigos."
    ermitano "Fue a buscar a la rata monstruos y me dejó atrás, solo con mis ratas. Vi que la chica lanzaba su bengala de emergencia, pero entonces la rata gigante apareció, con un bláster en su zarpa, ante la niña."
    ermitano "Yo estaba demasiado lejos para oírles, intentando esconderme entre mis ratas. Creí que el monstruo iba a devorar a la desdichada niña, sobre todo cuando la mujer hizo un gesto para que yo enviase diez ratas allí."
    ermitano "Por suerte, llegó un speeder, avisado por la bengala de emergencia del T-16. Esa chica debe tener un ángel protegiéndola... No como yo."
    ermitano "Perdón... Me desvié... Estuve a punto de ser cómplice de un asesinato..."
    ermitano "En ocasiones, me obligó a poner falsos pulgares a algunas ratas womp para que pareciesen ser manos. De cerca se veía que eran atrezzo; pero una rata rara vez se está quieta."
    ermitano "Esa... maga está interesada en explorar la zona del Peñón Mellado. Creo que está buscando algo o a alguien por allí."
    ermitano "No sé lo que ella pretende, pero yo no puedo detenerla. Si intento huir, sé que me encontrará."
    ermitano "Mi conciencia no me permite seguir ayudándola. Sólo encuentro una salida... Si ella me necesita y no estoy, quizá eso le retrase."
    ermitano "A quien encuentre mi mensaje: Cuidáos de ella."
    hide ermitano with dissolve
    playerName "Ése es el fin del mensaje."
    playerName "Jo, qué mal rollo da..."
    $ conoceClawditaA = 1
    jump go_RutaDesierto2

label encontrasteActivosRebeldes:
    scene bg activos rebeldes

    $ activosRebeldes  = 1
    "Entras en la cueva y lo que encuentras parece más una base militar que una guarida de contrabandistas. Ves un yate espacial, seis cazas de combate y dos bombarderos, cada uno de ellos cuidadosamente reparado y con cicatrices de combates previos."
    "No hay un solo droide en el hangar, ni tampoco orgánicos. Sólo están las naves, el equipo de mantenimiento y reparación de éstas, y varias cajas herméticamente selladas que pesan demasiado para moverlas fácilmente."
    "El equipo tiene polvo de hace aproximamente una semana: Alguien cuidaba estas naves con disciplina y cariño, hasta que le pasó algo hace sólo unos días. Pero incluso así, han tenido cuidado de dejar los cierres puestos a todo: No puedes acceder a ninguna cabina."
    "No han podido ocultar, sin embargo, las marcas exteriores: Lees claramente que las naves forman el Escuadrón Azufre, de ahí las líneas amarillas, y se identifican como veteranos de la Alianza Rebelde, ahora con el emblema de la Nueva República."
    "Encuentras restos de informes y notas garabateadas quemadas. Apenas puedes identificar estas palabras: Cpt Tem Rivten, Alderaan. Tte Agrol Nellsdan, Chandrila. Tte Sebla, Geonosis. Tte 2ª Hyanon Hyper... y se ha cortado esta palabra."
    "Está bastante claro que Thondo Qo no ha entrado en esta cueva, o habría dejado huellas."

    jump go_RutaDesierto4

label swoopChylerDengarRX:
    
    # "Resultado: Chyler - Dengar - RX"
    scene bg cantina piloto1
    show labria at right
    "El circuito de Telos es un túnel con suelos y paredes de transpariacero; entramados y celosías indican la ruta única. Lluvias torrenciales caen visiblemente fuera mientras el piloto prepara su vehículo."
    "Ante las cámaras, la joven humana Kimmi Chyler, vistiendo un traje acolchado, sonríe y se ajusta su casco. Un trío de luces se encienden una tras otra: Roja, amarilla y verde. Cuando la última brilla, el swoop sale disparado."
    "Chyler gana velocidad en los primeros tres segundos, y a partir de ahí procura mantenerse."
    "Ella vira hacia los lados para situarse sobre el primer cojinete de aceleración y, en cuanto lo logra, su velocidad aumenta notablemente durante varios segundos."
    "Los obstáculos parecen esferas holográficas flotantes, pero pueden dañar la electrónica de los swoops. También hay otros anaranjados que reducen el espacio en otras zonas, y que casi se pueden salvar sólo con un cojinete."
    "Chyler llega hasta el final sin haber chocado con ningún obstáculo y habiendo usado todos los cojinetes. Su tiempo total es de 40:28 segundos. Empieza a bajarse del swoop, pero la cámara no la sigue mostrando."
    scene bg cantina piloto2
    show labria at right
    "En vez de eso, vuelve mostrar a la salida, donde un piloto mucho más fornido está preparando un swoop más grande que el de Chyler. Él es Dengar."
    "La máquina de Dengar despega, encendiendo unos enormes reactores que dejan atrás llamaradas de volcán. Cuando se disipa la humareda, la velocidad de Dengar es muy superior a la de Chyler."
    "Dengar no es tan metódico como su predecesora: A veces no llega a un cojinete de aceleración. A veces está claro que {i}no se molesta{/i} en intentar alcanzar un cojinete."
    "Pero, al mismo tiempo, su swoop es mucho más rápido que el de Chyler. Con esa velocidad de crucero, quizá él ni siquiera {i}necesite{/i} la aceleración añadida."
    "En al menos una ocasión, Dengar ha chocado con un obstáculo. Su swoop ha decelerado bastante. Desde tu posición, no sabes si eso será decisivo o no."
    "Dengar alcanza la meta. Su tiempo total es de 40:32; Dengar ha perdido. La cámara vuelve al punto de partida."
    scene bg cantina piloto3
    show labria at right
    "RX-24 es tan poco humanoide que apenas merece llamarse androide. Cuando se sube a su swoop, éste desciende unos centímetros hacia abajo: El droide pesa mucho más que los pilotos humanos. Eso seguramente le perjudique."
    "La competición empieza y RX-24 se mueve visiblemente más lento que Dengar. No puedes saber realmente si va más despacio que Chyler; necesitarías ver las dos carreras a la vez."
    "RX-24 pilota literalmente como una máquina: Hace el movimiento justo para alcanzar cada cojinete y para evitar cada obstáculo. Seguramente ha visto las carreras anteriores y ha memorizado el trayecto."
    "En un momento dado, sin embargo, su swoop pierde brevemente el control durante una fracción de segundo: Un relámpago iluminaba el exterior, y los fotorreceptores del droide no lo interpretaron correctamente."
    "RX-24 tiene la meta a su alcance. En seguida será el momento decisivo en que sabrás, para bien o para mal, si has ganado la apuesta."
    "El swoop se para y se muestra el tiempo final de RX-24: 40:47."
    "El resultado final de la carrera es: ganadora Kimmi Chyler con 40:28. En segundo lugar Dengar con 40:32. Por último, RX-24 con 40:47."
    scene bg cantina
    show labria
    return

label swoopChylerRXDengar:
    
    # "Resultado: Chyler - RX - Dengar"
    scene bg cantina piloto1
    show labria at right
    "El circuito de Telos es un túnel con suelos y paredes de transpariacero; entramados y celosías indican la ruta única. Lluvias torrenciales caen visiblemente fuera mientras el piloto prepara su vehículo."
    "Ante las cámaras, la joven humana Kimmi Chyler, vistiendo un traje acolchado, sonríe y se ajusta su casco. Un trío de luces se encienden una tras otra: Roja, amarilla y verde. Cuando la última brilla, el swoop sale disparado."
    "Chyler gana velocidad en los primeros tres segundos, y a partir de ahí procura mantenerse."
    "Ella vira hacia los lados para situarse sobre el primer cojinete de aceleración y, en cuanto lo logra, su velocidad aumenta notablemente durante varios segundos."
    "Los obstáculos parecen esferas holográficas flotantes, pero pueden dañar la electrónica de los swoops. También hay otros anaranjados que reducen el espacio en otras zonas, y que casi se pueden salvar sólo con un cojinete."
    "Chyler llega hasta el final sin haber chocado con ningún obstáculo y habiendo usado todos los cojinetes. Su tiempo total es de 40:28 segundos. Empieza a bajarse del swoop, pero la cámara no la sigue mostrando."
    scene bg cantina piloto2
    show labria at right
    "En vez de eso, vuelve mostrar a la salida, donde un piloto mucho más fornido está preparando un swoop más grande que el de Chyler. Él es Dengar."
    "La máquina de Dengar despega, encendiendo unos enormes reactores que dejan atrás llamaradas de volcán. Cuando se disipa la humareda, la velocidad de Dengar es muy superior a la de Chyler."
    "Dengar no es tan metódico como su predecesora: A veces no llega a un cojinete de aceleración. A veces está claro que {i}no se molesta{/i} en intentar alcanzar un cojinete."
    "Pero, al mismo tiempo, su swoop es mucho más rápido que el de Chyler. Con esa velocidad de crucero, quizá él ni siquiera {i}necesite{/i} la aceleración añadida."
    "En al menos una ocasión, Dengar ha chocado con un obstáculo. Su swoop ha decelerado bastante. Desde tu posición, no sabes si eso será decisivo o no."
    "Dengar alcanza la meta. Su tiempo total es de 40:47; Dengar ha perdido. La cámara vuelve al punto de partida."
    scene bg cantina piloto3
    show labria at right
    "RX-24 es tan poco humanoide que apenas merece llamarse androide. Cuando se sube a su swoop, éste desciende unos centímetros hacia abajo: El droide pesa mucho más que los pilotos humanos. Eso seguramente le perjudique."
    "La competición empieza y RX-24 se mueve visiblemente más lento que Dengar. No puedes saber realmente si va más despacio que Chyler; necesitarías ver las dos carreras a la vez."
    "RX-24 pilota literalmente como una máquina: Hace el movimiento justo para alcanzar cada cojinete y para evitar cada obstáculo. Seguramente ha visto las carreras anteriores y ha memorizado el trayecto."
    "En un momento dado, sin embargo, su swoop pierde brevemente el control durante una fracción de segundo: Un relámpago iluminaba el exterior, y los fotorreceptores del droide no lo interpretaron correctamente."
    "RX-24 tiene la meta a su alcance. En seguida será el momento decisivo en que sabrás, para bien o para mal, si has ganado la apuesta."
    "El swoop se para y se muestra el tiempo final de RX-24: 40:32."
    "El resultado final de la carrera es: ganadora Kimmi Chyler con 40:28. En segundo lugar RX-24 con 40:32. Por último, Dengar con 40:47."
    scene bg cantina
    show labria
    return

label swoopDengarChylerRX:
    
    # "Resultado: Dengar - Chyler - RX"
    scene bg cantina piloto1
    show labria at right
    "El circuito de Telos es un túnel con suelos y paredes de transpariacero; entramados y celosías indican la ruta única. Lluvias torrenciales caen visiblemente fuera mientras el piloto prepara su vehículo."
    "Ante las cámaras, la joven humana Kimmi Chyler, vistiendo un traje acolchado, sonríe y se ajusta su casco. Un trío de luces se encienden una tras otra: Roja, amarilla y verde. Cuando la última brilla, el swoop sale disparado."
    "Chyler gana velocidad en los primeros tres segundos, y a partir de ahí procura mantenerse."
    "Ella vira hacia los lados para situarse sobre el primer cojinete de aceleración y, en cuanto lo logra, su velocidad aumenta notablemente durante varios segundos."
    "Los obstáculos parecen esferas holográficas flotantes, pero pueden dañar la electrónica de los swoops. También hay otros anaranjados que reducen el espacio en otras zonas, y que casi se pueden salvar sólo con un cojinete."
    "Chyler llega hasta el final sin haber chocado con ningún obstáculo y habiendo usado todos los cojinetes. Su tiempo total es de 40:28 segundos. Empieza a bajarse del swoop, pero la cámara no la sigue mostrando."
    scene bg cantina piloto2
    show labria at right
    "En vez de eso, vuelve mostrar a la salida, donde un piloto mucho más fornido está preparando un swoop más grande que el de Chyler. Él es Dengar."
    "La máquina de Dengar despega, encendiendo unos enormes reactores que dejan atrás llamaradas de volcán. Cuando se disipa la humareda, la velocidad de Dengar es muy superior a la de Chyler."
    "Dengar no es tan metódico como su predecesora: A veces no llega a un cojinete de aceleración. A veces está claro que {i}no se molesta{/i} en intentar alcanzar un cojinete."
    "Pero, al mismo tiempo, su swoop es mucho más rápido que el de Chyler. Con esa velocidad de crucero, quizá él ni siquiera {i}necesite{/i} la aceleración añadida."
    "En al menos una ocasión, Dengar ha chocado con un obstáculo. Su swoop ha decelerado bastante. Desde tu posición, no sabes si eso será decisivo o no."
    "Dengar alcanza la meta. Su tiempo total es de 40:09; Dengar va en cabeza. La cámara vuelve al punto de partida."
    scene bg cantina piloto3
    show labria at right
    "RX-24 es tan poco humanoide que apenas merece llamarse androide. Cuando se sube a su swoop, éste desciende unos centímetros hacia abajo: El droide pesa mucho más que los pilotos humanos. Eso seguramente le perjudique."
    "La competición empieza y RX-24 se mueve visiblemente más lento que Dengar. No puedes saber realmente si va más despacio que Chyler; necesitarías ver las dos carreras a la vez."
    "RX-24 pilota literalmente como una máquina: Hace el movimiento justo para alcanzar cada cojinete y para evitar cada obstáculo. Seguramente ha visto las carreras anteriores y ha memorizado el trayecto."
    "En un momento dado, sin embargo, su swoop pierde brevemente el control durante una fracción de segundo: Un relámpago iluminaba el exterior, y los fotorreceptores del droide no lo interpretaron correctamente."
    "RX-24 tiene la meta a su alcance. En seguida será el momento decisivo en que sabrás, para bien o para mal, si has ganado la apuesta."
    "El swoop se para y se muestra el tiempo final de RX-24: 40:32."
    "El resultado final de la carrera es: ganador Dengar con 40:09. En segundo lugar Kimmi Chyler con 40:28. Por último, RX-24 con 40:32"
    scene bg cantina
    show labria
    return
        
label swoopDengarRXChyler:
    
    # "Resultado: Dengar - RX - Chyler"
    scene bg cantina piloto1
    show labria at right
    "El circuito de Telos es un túnel con suelos y paredes de transpariacero; entramados y celosías indican la ruta única. Lluvias torrenciales caen visiblemente fuera mientras el piloto prepara su vehículo."
    "Ante las cámaras, la joven humana Kimmi Chyler, vistiendo un traje acolchado, sonríe y se ajusta su casco. Un trío de luces se encienden una tras otra: Roja, amarilla y verde. Cuando la última brilla, el swoop sale disparado."
    "Chyler gana velocidad en los primeros tres segundos, y a partir de ahí procura mantenerse."
    "Ella vira hacia los lados para situarse sobre el primer cojinete de aceleración y, en cuanto lo logra, su velocidad aumenta notablemente durante varios segundos."
    "Los obstáculos parecen esferas holográficas flotantes, pero pueden dañar la electrónica de los swoops. También hay otros anaranjados que reducen el espacio en otras zonas, y que casi se pueden salvar sólo con un cojinete."
    "Chyler llega hasta el final sin haber chocado con ningún obstáculo y habiendo usado todos los cojinetes. Su tiempo total es de 40:32 segundos. Empieza a bajarse del swoop, pero la cámara no la sigue mostrando."
    scene bg cantina piloto2
    show labria at right
    "En vez de eso, vuelve mostrar a la salida, donde un piloto mucho más fornido está preparando un swoop más grande que el de Chyler. Él es Dengar."
    "La máquina de Dengar despega, encendiendo unos enormes reactores que dejan atrás llamaradas de volcán. Cuando se disipa la humareda, la velocidad de Dengar es muy superior a la de Chyler."
    "Dengar no es tan metódico como su predecesora: A veces no llega a un cojinete de aceleración. A veces está claro que {i}no se molesta{/i} en intentar alcanzar un cojinete."
    "Pero, al mismo tiempo, su swoop es mucho más rápido que el de Chyler. Con esa velocidad de crucero, quizá él ni siquiera {i}necesite{/i} la aceleración añadida."
    "En al menos una ocasión, Dengar ha chocado con un obstáculo. Su swoop ha decelerado bastante. Desde tu posición, no sabes si eso será decisivo o no."
    "Dengar alcanza la meta. Su tiempo total es de 40:09; Dengar va en cabeza. La cámara vuelve al punto de partida."
    scene bg cantina piloto3
    show labria at right
    "RX-24 es tan poco humanoide que apenas merece llamarse androide. Cuando se sube a su swoop, éste desciende unos centímetros hacia abajo: El droide pesa mucho más que los pilotos humanos. Eso seguramente le perjudique."
    "La competición empieza y RX-24 se mueve visiblemente más lento que Dengar. No puedes saber realmente si va más despacio que Chyler; necesitarías ver las dos carreras a la vez."
    "RX-24 pilota literalmente como una máquina: Hace el movimiento justo para alcanzar cada cojinete y para evitar cada obstáculo. Seguramente ha visto las carreras anteriores y ha memorizado el trayecto."
    "En un momento dado, sin embargo, su swoop pierde brevemente el control durante una fracción de segundo: Un relámpago iluminaba el exterior, y los fotorreceptores del droide no lo interpretaron correctamente."
    "RX-24 tiene la meta a su alcance. En seguida será el momento decisivo en que sabrás, para bien o para mal, si has ganado la apuesta."
    "El swoop se para y se muestra el tiempo final de RX-24: 40:28."
    "El resultado final de la carrera es: ganador Dengar con 40:09. En segundo lugar RX-24 con 40:28. Por último, Kimmi Chyler con 40:32"
    scene bg cantina
    show labria
    return

label swoopRXChylerDengar:
    
    # "Resultado: RX - Chyler - Dengar"
    scene bg cantina piloto1
    show labria at right
    "El circuito de Telos es un túnel con suelos y paredes de transpariacero; entramados y celosías indican la ruta única. Lluvias torrenciales caen visiblemente fuera mientras el piloto prepara su vehículo."
    "Ante las cámaras, la joven humana Kimmi Chyler, vistiendo un traje acolchado, sonríe y se ajusta su casco. Un trío de luces se encienden una tras otra: Roja, amarilla y verde. Cuando la última brilla, el swoop sale disparado."
    "Chyler gana velocidad en los primeros tres segundos, y a partir de ahí procura mantenerse."
    "Ella vira hacia los lados para situarse sobre el primer cojinete de aceleración y, en cuanto lo logra, su velocidad aumenta notablemente durante varios segundos."
    "Los obstáculos parecen esferas holográficas flotantes, pero pueden dañar la electrónica de los swoops. También hay otros anaranjados que reducen el espacio en otras zonas, y que casi se pueden salvar sólo con un cojinete."
    "Chyler llega hasta el final sin haber chocado con ningún obstáculo y habiendo usado todos los cojinetes. Su tiempo total es de 40:28 segundos. Empieza a bajarse del swoop, pero la cámara no la sigue mostrando."
    scene bg cantina piloto2
    show labria at right
    "En vez de eso, vuelve mostrar a la salida, donde un piloto mucho más fornido está preparando un swoop más grande que el de Chyler. Él es Dengar."
    "La máquina de Dengar despega, encendiendo unos enormes reactores que dejan atrás llamaradas de volcán. Cuando se disipa la humareda, la velocidad de Dengar es muy superior a la de Chyler."
    "Dengar no es tan metódico como su predecesora: A veces no llega a un cojinete de aceleración. A veces está claro que {i}no se molesta{/i} en intentar alcanzar un cojinete."
    "Pero, al mismo tiempo, su swoop es mucho más rápido que el de Chyler. Con esa velocidad de crucero, quizá él ni siquiera {i}necesite{/i} la aceleración añadida."
    "En al menos una ocasión, Dengar ha chocado con un obstáculo. Su swoop ha decelerado bastante. Desde tu posición, no sabes si eso será decisivo o no."
    "Dengar alcanza la meta. Su tiempo total es de 40:32; Dengar ha perdido. La cámara vuelve al punto de partida."
    scene bg cantina piloto3
    show labria at right
    "RX-24 es tan poco humanoide que apenas merece llamarse androide. Cuando se sube a su swoop, éste desciende unos centímetros hacia abajo: El droide pesa mucho más que los pilotos humanos. Eso seguramente le perjudique."
    "La competición empieza y RX-24 se mueve visiblemente más lento que Dengar. No puedes saber realmente si va más despacio que Chyler; necesitarías ver las dos carreras a la vez."
    "RX-24 pilota literalmente como una máquina: Hace el movimiento justo para alcanzar cada cojinete y para evitar cada obstáculo. Seguramente ha visto las carreras anteriores y ha memorizado el trayecto."
    "En un momento dado, sin embargo, su swoop pierde brevemente el control durante una fracción de segundo: Un relámpago iluminaba el exterior, y los fotorreceptores del droide no lo interpretaron correctamente."
    "RX-24 tiene la meta a su alcance. En seguida será el momento decisivo en que sabrás, para bien o para mal, si has ganado la apuesta."
    "El swoop se para y se muestra el tiempo final de RX-24: 40:09."
    "El resultado final de la carrera es: ganador RX-24 con 40:09. En segundo lugar Kimmi Chyler con 40:28. Por último, Dengar con 40:32."
    scene bg cantina
    show labria
    return

label swoopRXDengarChyler:
    
    # "Resultado: RX - Dengar - Chyler"
    scene bg cantina piloto1
    show labria at right
    "El circuito de Telos es un túnel con suelos y paredes de transpariacero; entramados y celosías indican la ruta única. Lluvias torrenciales caen visiblemente fuera mientras el piloto prepara su vehículo."
    "Ante las cámaras, la joven humana Kimmi Chyler, vistiendo un traje acolchado, sonríe y se ajusta su casco. Un trío de luces se encienden una tras otra: Roja, amarilla y verde. Cuando la última brilla, el swoop sale disparado."
    "Chyler gana velocidad en los primeros tres segundos, y a partir de ahí procura mantenerse."
    "Ella vira hacia los lados para situarse sobre el primer cojinete de aceleración y, en cuanto lo logra, su velocidad aumenta notablemente durante varios segundos."
    "Los obstáculos parecen esferas holográficas flotantes, pero pueden dañar la electrónica de los swoops. También hay otros anaranjados que reducen el espacio en otras zonas, y que casi se pueden salvar sólo con un cojinete."
    "Chyler llega hasta el final sin haber chocado con ningún obstáculo y habiendo usado todos los cojinetes. Su tiempo total es de 40:32 segundos. Empieza a bajarse del swoop, pero la cámara no la sigue mostrando."
    scene bg cantina piloto2
    show labria at right
    "En vez de eso, vuelve mostrar a la salida, donde un piloto mucho más fornido está preparando un swoop más grande que el de Chyler. Él es Dengar."
    "La máquina de Dengar despega, encendiendo unos enormes reactores que dejan atrás llamaradas de volcán. Cuando se disipa la humareda, la velocidad de Dengar es muy superior a la de Chyler."
    "Dengar no es tan metódico como su predecesora: A veces no llega a un cojinete de aceleración. A veces está claro que {i}no se molesta{/i} en intentar alcanzar un cojinete."
    "Pero, al mismo tiempo, su swoop es mucho más rápido que el de Chyler. Con esa velocidad de crucero, quizá él ni siquiera {i}necesite{/i} la aceleración añadida."
    "En al menos una ocasión, Dengar ha chocado con un obstáculo. Su swoop ha decelerado bastante. Desde tu posición, no sabes si eso será decisivo o no."
    "Dengar alcanza la meta. Su tiempo total es de 40:28; Dengar va en cabeza. La cámara vuelve al punto de partida."
    scene bg cantina piloto3
    show labria at right
    "RX-24 es tan poco humanoide que apenas merece llamarse androide. Cuando se sube a su swoop, éste desciende unos centímetros hacia abajo: El droide pesa mucho más que los pilotos humanos. Eso seguramente le perjudique."
    "La competición empieza y RX-24 se mueve visiblemente más lento que Dengar. No puedes saber realmente si va más despacio que Chyler; necesitarías ver las dos carreras a la vez."
    "RX-24 pilota literalmente como una máquina: Hace el movimiento justo para alcanzar cada cojinete y para evitar cada obstáculo. Seguramente ha visto las carreras anteriores y ha memorizado el trayecto."
    "En un momento dado, sin embargo, su swoop pierde brevemente el control durante una fracción de segundo: Un relámpago iluminaba el exterior, y los fotorreceptores del droide no lo interpretaron correctamente."
    "RX-24 tiene la meta a su alcance. En seguida será el momento decisivo en que sabrás, para bien o para mal, si has ganado la apuesta."
    "El swoop se para y se muestra el tiempo final de RX-24: 40:09."
    "El resultado final de la carrera es: ganador RX-24 con 40:09. En segundo lugar Dengar con 40:28. Por último, Kimmi Chyler con 40:32." 
    scene bg cantina
    show labria
    return

label HasMuerto:
    play music "music/muerte.mp3"
    scene bg muerte
    $ ui.saybehavior()
    $ ui.interact()
    jako "¿[playerName]? ¿Ezzztázzz ahí? ¿Me rezzzibezzz? ¿Cómo vamozzz a zzzalir de ézzzta?"
    return


# UNUSED:

label mapa:
 
   # scene bg mapa ground

   window hide None

   $ result = renpy.imagemap("bg mapa ground.png","bg mapa hover.png",[(31, 232, 136, 291, "hangar"),(158, 135, 262, 195, "tienda"),(281, 38, 386, 98, "desierto")])

   if result == "hangar":
      "Has elegido hangar."
      if posicion in ["hangar", "tienda"]:
         jump hangar
      else:
         "...pero no puedes ir desde [posicion]."
   elif result == "tienda":
      "Has elegido tienda."
      if posicion in ["hangar", "tienda", "desierto"]:
# (que en este caso sí que son todas las posiciones pero da igual)
         jump TiendaJawa
      else:
         "...pero no puedes ir desde [posicion]."
   elif result == "desierto":
      "Has elegido desierto."
      if posicion in ["tienda", "desierto"]:
         jump ZonaTusken1
      else:
         "...pero no puedes ir desde [posicion]."
   else:
      "¿Cómo hemos llegado hasta aquí?"
      jump mapa

   jump mapa

label hangar:

    scene bg hangar
    with fade
    $ posicion = "hangar"

# INTENTANDO QUE FUNCIONE INVENTARIO, NO VEO NADA
    screen pantallainventario():
        button:
            xpos 1.0
            ypos 0
            text "Inventario"
            action Jump(inventario)
# QUIZÁ ESTO: https://www.youtube.com/watch?v=SDXG17W0cBA
# FIN DE INVENTARIO

    "Estás en el hangar."

label inventario:

#   TBA PENDIENTE HACER; AL MENOS QUE EXISTA
    you "Veamos qué llevas encima... Esto es tu inventario..."

    jump expression posicion

label porsiaca_cosasquenosonconversaciones:
    scene bg unused celda
    with fade
    show jako
    jako "Has llegado al label porsiaca_cosasquenosonconversaciones, que debería no ser usado nunca. Esto ha salido mal."