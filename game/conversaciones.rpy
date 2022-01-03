# ¿PUEDO HACER UNA VARIABLE QUE SE LLAME IGUAL QUE UNA LABEL, Y NO PASE NADA? hablarDarklighter, hablarGranjero
#     SÍ SE PUEDE
# ¿PUEDO HACER UNA SUBRUTINA QUE VUELVA A DONDE ESTABAS CON RETURN?
#     Sí, pero es CALL
#     call subroutine
#     (...)
#     label subroutine:
#     "Hola"
#     return
# ¿ESTO FUNCIONA? SÍ, FUNCIONA
#     if jugarLabria < 2:
#         show labria

#  -------

#     $ item1 = 1
#     menu:
#         tusken "bla bla!"
#         "XXX" if XXX == 0:
#             wassak "Bla bla, elige una opción."
#         "Opción A":
#             "Has dicho Opción A"
#         "Opción B":
#             "Has dicho Opción B"
#         "Opción Si Item1 Es 0" if item1 == 0:
#             "Has dicho Opción Sólo en Item1 es 0"
# 
#     if item2 == 0 and chat1 == True:
#         show tusken

# ----------

# Hablar Jent en la calle
# SI itemDeclaraJent = 0 entonces Jent está delante de la calle
# Se accede desde la calle principal

label hablarJentEnLaCalle:
    show jent
    "Te aborda una joven twi'lek vestida con ropas raídas de granjero, pero que intenta imitar los andares de un piloto espacial. Hay docenas así en este planeta."
    muchacha "Eh, tú eres [tuEl] científic[tuO] de otro planeta, ¿verdad? ¿[playerName] o algo así? ¡Tengo que hablar que contigo! Es sobre ratas womp."
    playerName "No sé, muchacha, tengo bastantes cosas que hacer, y ya he hablado con muchos granjeros y cazadores que me cuentan sus locuras sobre ratas womp extrañas a cambio de que les pague una copa."
    muchacha "Eh... No. ¡No es así! Bueno, {i}soy{/i} granjera, y {i}es{/i} una historia sobre una rata womp extraña... ¡Pero es real! Yo no soy como Gor Kolomo."
    muchacha "Yo no puedo pedirte una copa. ¡Ni siquiera tengo edad para beber! Sólo quiero que escuches mi historia. ¿No demuestra eso que soy de fiar?"
    menu:
        "Venga, cuéntame lo que sea y acabemos con esto.":
            pass
        "No, no quiero hablar contigo.":
            muchacha "¡Oh, vamos, será sólo un momento!"
            playerName "Te pondrás así de pesada hasta que te escuche, ¿no?"
#            show jent smile
            muchacha "{i}sonriendo{/i} Ésa es mi idea."
            playerName "Bueno, adelante."
            show jent
    jent "Me llamo Jent Loquoy. Tengo 17 de Dunas siempre que puedo, para mejorar mis habilidades de pilotaje. ¿Sabes lo que es un T-16?"
    playerName "El saltador de Incom de alto rendimiento, con motor iónico y lásers. Los controles son similares a los de las naves Incom y responde de forma parecida, así que se usa para entrenamientos."
    jent "Eeeso es. Es lo mejor que tengo para probarlo. Soy buena piloto. Voy al simulador imperial siempre que puedo, a probar en Sienars, Incoms, Koensayr..."
    playerName "TIEs, alas-X y alas-Y. ¿Tienen de eso en los simuladores imperiales?"
    jent "Sí, claro, si vas allí, podrás ver mis resultados en esas naves. Tengo casi quinientas horas de vuelo en simulador. Bueno, unas cuatrocientas. Pero eso da para el permiso de copiloto."
    playerName "Es fascinante, ¿pero hay ratas womp extrañas en alguna parte de tu historia? ¿Me vas a hablar de ratas womp espaciales en un simulador?"
    jent "Ah, sí, perdona. Quería dejarte claro que soy buena piloto, para que no creas que el accidente fue porque yo sea torpe. Oye, podría pilotar en el espacio en condiciones reales y... Vale."
    jent "El mes pasado, yo estaba pilotando mi T-16 por el Desfiladero del Peñón Mellado, en el Mar de Dunas. Lo he hecho un gúgol de veces, me sé cada {i}revoqueco{/i}, y a veces disparo a las ratas womp mientras corro. Hago piruetas, pero sólo porque sé que van a salir bien."
    jent "Nunca choco en el Desfiladero, pero ese día caí en una emboscada y estrellé mi máquina. Apenas me dio tiempo a eyectar antes de que mi máquina se estrellara en la pared del cañón."
    jent "Entonces pude ver que alguien había colgado un cable en el cañón y eso había cortado mi ala superior. Si revisas los escombros, verás el corte. ¡Demasiado limpio!"
    jent "Tuve {b}mucha{/b} suerte porque aterricé en la parte superior del Desfiladero, y entonces pude mirar abajo."
    jent "En el vado había docenas de ratas womp, ¡cientos! Se movían como un ejército organizado."
    playerName "Las ratas womp nunca hacen grupos tan grandes."
    jent "No, porque se pelean entre ellas, ¡pero éstas tenían líderes! Había una o dos ratas que sostenían trozo de metal como si fueran palos. Estaban al mando, y conducían a las otras para escalar las paredes y venir a por mí."
    jent "Disparé mi bengala de rescate y las ratas de los palos se escaparon, pero las otras seguían trepando hacia mí. Si Pa no hubiese venido en su speeder, yo no estaría aquí ahora."
    "Jent deja de hablar y te mira, con cara de confusión."
    jent "¿Eran ratas womp inteligentes, verdad? La gente dice que no existen, pero: ¿Ratas sosteniendo palos? ¿Liderando manadas? ¿Cuándo has visto algo parecido?"
    playerName "Háblame antes de tu saltador. ¿Qué modelo era?"
    jent "Un T-16 Skyhopper de Incom, del '34. Speeder aéreo de alto rendimiento, de segunda mano y muy modificado."
    playerName "¿Motores iónicos E-16/x y generadores repulsores DCJ-45?"
    jent "No, el motor es un Shocsar de SoroSuub, una de las modificaciones, pero alcanza los 1.200 clics por hora sin problemas."
    playerName "¿Ibas a velocidad transónica cuando chocaste? Estabas a punto de romper la barrera del sonido en atmósfera, en tierra. No es fácil controlar una máquina y a la vez fijarse en el entorno. Es por eso que el Imperio prohibió las carreras de vainas."
    jent "¡Ja! El Imperio prohibe porque le gusta prohibir todo lo divertido. ¿Crees que no soy capaz de llevar un chisme así? Hace un par de años, yo misma piloté una vaina restaurada en Boonta. Vale, se deshizo antes de acabar la carrera, pero puedo llevar esos chismes."
    jent "Soy una gran piloto. Pregunta a mis amigos, Hawk y Wassak. Ellos te lo confirmarán."
    playerName "¿Wassak, el jawa? He hablado con él y tampoco me parece la fuente más fiable."
    jent "Es mi mecánico para las reparaciones y mantenimiento. ¡Que te diga cómo tengo mi T-16!{p}¿No me crees, verdad?"
    show anzati at left with dissolve
    show r5d4 at right  with dissolve
    playerName "No descarto nada a la ligera. En esta galaxia he visto cosas muy raras. Desde los anzati hasta Waru... pasando por ese droide R5 con capacidades jedi..."
    jent "Hay tauntauns con escamas, worrts espaciales y leviatanes sith. ¿Por qué dudar de una rata womp inteligente?"
    hide anzati
    hide r5d4
    playerName "Nunca se ha podido confirmar un avistamiento de rata womp inteligente. Ha habido informes durante siglos, pero son criptoxenozoología."
    jent "Si consiguieses pruebas, serías, como, alguien importante en lo tuyo, ¿no? Tengo una rata muerta de ese encuentro, creo que no era una de las inteligentes. Me la llevé a casa. Quiero que te la quedes. Quizá le puedas hacer una {i}atorsia{/i} y descubrir algo en ella."
    jent "No soy la única. Varios granjeros han sido emboscados por ratas womp. ¡Pregunta entre las granjas!"
    jent "Pásate también por la granja de mi familia y te daré la rata."
    playerName "Sospecho que acabaré pasándome, sí..."
    jent "Y pásate por las granjas a por la rata. Estás invitad[tuO]."
    playerName "Lo tendré en cuenta. Gracias por tu declaración, Jent Loquoy. Me quedo con tu nombre."
    hide jent with dissolve

    $ itemDeclaraJent = 1
    $ preguntarWassakPorJent = 1
    $ preguntarGrafPorJent = 1 
    
    jump go_CallePrincipal

# Hablar Wassak

label hablarWassak:
    menu:
        "¿Puedes venderme un oscilador?" if primerWassak == 0:
            playerName "Necesito un oscilador de cristal. ¿Puedes venderme uno?"
            wassak "¿Para qué necesitas un oscilador de cristal? Eso sólo sirve para regular la potencia de una nave estelar y... Si necesitas uno, es que tienes una nave varada."
            playerName "¿Has usado la Fuerza o eres así de perspicaz tú solo?"
            wassak "Comprendo que tienes un problema. No tengo un oscilador ahora, pero puedo conseguirlo. Se lo canjearé a otro jawa. Me llevará tiempo."
            playerName "¿Cuánto me va a costar?"
            wassak "Sobre eso: Tú tienes un problema grave. Lo resolveré, si {i}tú{/i} resuelves {i}mi{/i} problema grave."
            playerName "Esto me da mala espina."
            wassak "Habrás oido que los moradores de las arenas nos han declarado la guerra. Están atacando nuestros reptadores de arena. Donde ven un jawa, lo matan."
            wassak "No podemos defendernos de un enemigo así. ¡Es un xenocidio! ¡Ayúdame, [playerName], eres mi única esperanza!"
            playerName "(¿Dónde he oido esa frase antes?){p}¿Qué esperas que haga, Wassak? ¿Derrotar a una tribu de moradores de las arenas yo sol[tuO]?"
            wassak "No es una tribu. ¡Son todos! No se había visto nada igual desde los tiempos de Gardulla la Hutt."
            wassak "Consigue una tregua. Nuestros clanes están dispuestos a negociar un alto el blaster; pero ahora ni siquiera sabemos porqué nos atacan. A ti no te atacarán nada más verte. Tú hablas jawaés y tusken. Puedes convencerles."
            playerName "Oh, sí. Revan consiguió eso mismo hace casi cuatro mil años. Si él pudo, ¿por qué yo no?"
            wassak "¿Quién es Revan? ¿Podemos llamarle?"
            playerName "Mejor no. Veré lo que puedo hacer, Wassak... ¡pero consigue mi oscilador!{p}¿Cómo hago para meterme en estos líos?"
            $ primerWassak = 1
        "¿Puedes venderme un arma?" if itemArmaJawa == 0:
            playerName "¿Puedes venderme un arma, Wassak?"
            wassak "¿Keeza? ¡Shootogawa!"
            playerName "Wassak, sé perfectamente que hablas Básico. No finjas ser un salvaje."
            wassak "Hkeek nkulla... Por no dejarme jugar, te venderé la pistola por... 300."
            playerName "Si es una pistola bláster, es barata. Si es un arma jawa, es cara."
            wassak "Es un bláster de ionización. Un diseño magnífico. Lo hice yo mismo, con piezas que encontré por ahí."
            wassak "Dispara un perno de sujección a cualquier máquina y, cuando impacta, causa un estallido iónico que la inutiliza. Apaga lo que sea durante un periodo limitado. Muy útil para cazar droides."
            playerName "¿Cuánto tiempo queda apagada la tecnología?"
            wassak "Ehh... Depende de la tecnología, pero suele ser tiempo suficiente para... lo que necesites hacer. Eso sí: Cuidado si lo intentas con máquinas que tengan varios sistemas independientes."
            playerName "Venga, dame el bláster, ten algo de dinero."
            wassak "{i}Taa baa.{/i} (Gracias)."
            $ itemArmaJawa = 1
            $ dinero = 2
        "¿Sabes si Jent es buena piloto?" if preguntarWassakPorJent == 1:
            playerName "He oído que conoces a Jent. ¿Es ella buena piloto?"
            wassak "¿Jent Loquoy? ¿La hija de la pirata espacial?"
            wassak "¡De las mejores que he visto! Nunca me trae restos de speeders que haya estrellado; ni tampoco los encuentro tirados por el desierto."
            wassak "Y sin embargo, ella siempre intenta comprar nueva tecnología, más avanzada. Motores más rápidos. Presurización más hermética. Es una chica que conoce su máquina."
            wassak "Pero también es un pelín fantasmona. Ella se cree mejor de lo que realmente es. Quiere pilotar cazas espaciales."
            wassak "Yo le vendo motores y otras piezas de vehículos, así que sé muy bien lo que pilota. A veces incluso tengo que instalarle yo algunos componentes. Si consigue no matarse con eso, es que es buena."
            wassak "Mira, te lo puedo contar: Ella nunca, {i}nunca{/i} me trae restos de algo que haya estrellado. Menos dos veces: Una fue la vaina de carreras, pero esos componentes eran de la época del padre de mi padre."
            wassak "Y está el T-16 del mes pasado, claro. Lo he visto y alguien ha cortado el ala superior. Eso no fue un accidente, fue un alambre. Seguramente usaron un lanzador de cables."
            $ preguntarWassakPorJent = 2
        "¿Me vuelves a contar tu historia de la rata?" if conoceClawditaA == 0:
            playerName "Vuelve a contarme tu encuentro con las ratas womp."
            playerName "¿Podemos hablar de tu encuentro con ratas womp inteligentes?"
            "Wassak se ajusta su hábito, se yergue en toda su altura (93 centímetros) y te mira fijamente."
            wassak "Soy Wassak, del clan Nkik."
            wassak "Paso mucho tiempo en el desierto, buscando tesoros. He visto muchas ratas womp. Tengo incluso..."
            playerName "Esa parte ya la tengo grabada."
            playerName "Devolviste el droide a las autoridades imperiales, ¿verdad?"
            wassak "Sí, claro."
            playerName "Esas piezas que tienes a la venta se parecen mucho al sensor de movimiento y a la antena de transmisión de un droide Arakyd."
            wassak "¿A ver? Sí, son otro droide Arakyd comprado legalmente a un granjero hace muchas lunas. Un granjero... muy viejo."
            playerName "¿Y las autoridades imperiales no te pidieron tu permiso para disparar un bláster? ¿Me lo enseñarías?"
            wassak "No tengo que enseñarte mi licencia de armas. Tú no eres un imperial."
            playerName "Estás seguro de haber visto que esas ratas tenían dedos y pulgares."
            wassak "Vi claramente a las dos que se acercaron a mí. Tenían una mirada de inteligencia. Las que intentaban llevarse el droide, no lo sé."
            wassak "Si intentaban llevarse el droide, supongo que tendrían capacidad manipuladora."
            wassak "Quizá las ratas inteligentes lideran clanes de ratas normales. Con los jawas también pasa."
            playerName "¿El poder va a quienes tienen pulgares?"
            wassak "El poder va a quienes tienen inteligencia, listill[tuO]."
            if itemRataMuerta == 1 and ensenarRataWassak == 0:
                playerName "Tu amiga Jent Loquoy habla de un encuentro similar con ratas womp inteligentes."
                show ratamuerta at right
                playerName "Me dio este cadáver de rata. Dice que es una de las ratas inteligentes que le atacaron."
                playerName "Tiene zarpas normales. No puede mover dedos independientemente, y desde luego no tiene pulgares."
                wassak "."
                wassak ". ."
                wassak ". . ."
                wassak ". {p}. {p}¿Y?"
                wassak "[playerName], Jent es un encanto para ser humana, no dudo de su palabra, pero a veces exagera sus relatos para impresionar."
                wassak "Bueno, sí que dudo de su palabra. Ella puede haberse equivocado. Quizá ella se imaginó que las ratas de su historia eran inteligentes. Yo sólo puedo hablar de {i}mi{/i} historia."
        "El diario del ermitaño demuestra que tu historia es falsa." if conoceClawditaA == 1 and visteDeclaracionWassak == 1:
            playerName "Tengo algo que enseñarte."
            show ermitano at left
            "Wassak escucha con atención el diario del ermitaño."
            playerName "Las ratas que te atacaron estaban amaestradas y controladas por este tipo. Cualquiera con experiencia en trato de animales puede conseguir algo así; y sospecho que su cómplice tenía capacidades de la Fuerza que le ayudaban."
            wassak "Vaya, qué se le va a hacer."
            playerName "La rata que silba debe ser la rata gigante e inteligente que, según el ermitaño, podía hablar."
            wassak "Supongo que me engañaron. Te pagaré las bebidas a las que me invitaste a cambio de mi declaración."
            playerName "¿No te preocupa esto?"
            "Wassak se encoge de hombros."
            wassak "No especialmente. No hay dinero ni tecnología por medio."
            # NO ACTUALIZA NADA, TE PUEDE VOLVER A SALIR

        "¿Tienes un ordenador de navegación?" if ordenadorNav == 1:
            playerName "¿Tienes un ordenador de navegación que yo pueda usar?"
            wassak "¡Pero si no tienes una nave! ¿Para qué quieres un ordenador de navegación?"
            playerName "Porque soy [tuUn] [tuEmpollon] y me gusta estudiar las estrellas y las rutas. ¿Tienes o no tienes?"
            wassak "Eso suena muy aburrido. Ah, qué más da. Al fondo lo tienes. Cuidado con el galoomp."
            playerName "¿Es tu mascota o tu cena?"
            wassak "¿No puede ser las dos cosas?"
            "Decides ir al ordenador de navegación y no debatir más con Wassak."
            hide wassak
            $ ordenadorNav = 2
            jump usandoOrdenadorNav
        "¿Puedo volver a usar tu ordenador de navegación?" if ordenadorNav == 2:
            playerName "¿Puedo volver a usar tu ordenador de navegación, por favor?"
            wassak "Mira que eres rar[tuO]. Está al fondo, donde siempre."
            jump usandoOrdenadorNav
        "¿Qué tal está tu comunidad jawa?":
            if itemEstandarte == 0:
                wassak "Los moradores de las arenas atacan sin parar. Esto es un desastre. Varios clanes han sido diezmados. Los reptadores han sufrido daños. Necesitamos una solución."
            elif itemEstandarte > 0:
                wassak "Es estupendo. Los bandidos tusken han dejado de atacarnos, ¡y hasta quieren comerciar! Los tusken quieren armas avanzadas para alejar a la gente de Vykan Fenn de sus territorios. El clan Kkuui y el cacique UOu'uu'h'rRr se reunirán en busca de formas de colaborar."
                wassak "Algunos jawas hablan del comienzo de una nueva era... y después intentan venderte algo."

        "Dame el oscilador; los tusken no os atacarán." if itemEstandarte == 1 and primerWassak == 1:
            playerName "Tengo buenas noticias, Wassak. Espero que tú también."
            playerName "Una jefa del crimen estaba matando a moradores y banthas y dejando pruebas falsas que os implicaban. He revelado sus tejemanejes y los moradores de las arenas no volverán a atacaros. Su cacique, UOu'uu'h'rRr', simpatiza con vosotros."
            wassak "Es un bonito cuento, [playerName], pero no he llegado a setenta ciclos siendo confiado.{p}¿Puedes demostrar lo que dices?"
            show estandarte at right
            playerName "Esperaba que me lo pideses. ¿Qué te parece el estandarte de Fuerte Tusken?"
            wassak "Nunca creí que vería eso en manos de un [tuEspecie]. Si los moradores te lo han dado, es que confían en ti. Los jawas también lo harán."
            playerName "La confianza está bien, pero yo buscaba otra cosa..."
            wassak "Con mucho gusto te doy el oscilador. Gracias, [playerName]."
            hide estandarte
            $ itemEstandarte = 2
            $ itemOscilador = 1
            call ComprobarLosTres from _call_ComprobarLosTres
        "Eso es todo por ahora.":
            playerName "Eso será todo por ahora."
            wassak "Hasta más ver."
            jump go_TiendaJawa   

    jump hablarWassak


label usandoOrdenadorNav:
#    "itemRuta: %(itemRutaMelocoton)d. itemRutaReal: %(itemRutaRealMelocoton)d."
    playerName "Con un ordenador de navegación y la ruta que me ha dado TurJinda, puedo averiguar algo sobre dónde ha estado..."
    # Tienes la ruta falsa
    if itemRutaMelocoton == 1 and itemRutaRealMelocoton == 0:
        show rutamala
        playerName "Vamos a ver en qué sistemas has estado. Quizá descubra algo útil comparando tus manifiestos y tus rutas."
        show tecnologia at right with dissolve
        playerName "Sector Portmoak, planeta Reuss VIII. Muy desagradable. Es una pesadilla sobreindustrializada. Según esto, el {i}Tormenta de Melocotón{/i} compró tecnología media allí."
        playerName "Es sospechoso que TurJinda no llenase toda su bodega. Quizá simplemente metió algo de contrabando en el resto del espacio. No es para echarse las manos a la cabeza."
        playerName "Desde ahí, cogió la Carrera de Especia de Llanic en dirección al sector Katharkk."
        hide tecnologia with dissolve
        show pirata at left with dissolve
        playerName "Menciona un incidente con piratas en el sistema Socorro. Eso es predecible. Yo mism[tuO] nunca he podido pasar por Socorro sin toparme con piratas."
        playerName "Sufrió daños menores en el casco por... baterías turboláser. A mí siempre me atacan con cañones iónicos, para intentar inmovilizarme sin dañar la nave."
        hide pirata with dissolve
        show trooper at right with dissolve
        playerName "Consigue aterrizar en Llanic, el intercambiador con la Ruta de Comercio Triellus y famoso puerto ilegal de especia."
        playerName "Últimamente Llanic ha sido un territorio candente. El Imperio quería afianzar su poder allí, pero hay demasiado comercio ilegal. "
        playerName "Allí vende la tecnología media y compran especia por cauces legales, pero no a los hutts. Supongo que puede ser cierto."
        hide trooper
        show kerkoiden at left with dissolve
        playerName "Desde ahí vuela hasta Arkanis, se pasa a la Carrera Coreliana y se detiene en Christophsis para comprar...{p}¿droides?."
        playerName "Eso no tiene sentido. Christophsis no fabrica droides. Sólo exporta minerales, productos industriales y arte. ¡Nadie llena su bodega de droides en Christophsis!"
        playerName "No hay más detalles. Ni siquiera veo una lista de modelos o fabricantes de su cargamento. Hay facturas con fecha y sello de Christophsis, pero nada más."
        playerName "Este dato es extraño: El {i}Tormenta de Melocotón{/i} pasó doce días en dique seco en Christophsis sin motivo aparente. No estaba de reparaciones, la tripulación no estaba de vacaciones..."
        hide kerkoiden
        show joe at right with dissolve
        playerName "Desde Christophsis vuelve a la ruta Triellus y acaba en Tatooine.{p}Algo huele a podrido en todo esto..."
        hide joe
        playerName "Sobre el monitor, esto es técnicamente viable, pero es poco práctico. Una nave así perdería dinero en un transporte tan ineficiente."
        playerName "Parece una historia contada para que tenga sentido... Todo es {i}demasiado{/i} normal. Incluso los piratas socorranos."
        playerName "Estoy segur[tuO] de que, si yo pudiese contactar con los puertos de Christophsis, Llanic y Reuss VIII, no tendrían registros de esta nave ni de ninguna parecida."
        playerName "Alguien se está tomando muchas molestias para que no se descubra algo."
        $ itemRutaMelocoton = 2
        jump go_TiendaJawa
    # Tienes la Ruta Falsa y ya la has mirado
    elif itemRutaMelocoton == 2 and itemRutaRealMelocoton == 0:
        playerName "Esto no me dará más información. Ya sé lo que necesito."
        show tecnologia at left with dissolve
        show rutamala with dissolve
        show especia at right with dissolve
        playerName "Supuestamente, TurJinda compró tecnología media en Reuss VIII y después especia en Llanic y, de algún modo, droides en un mundo como Christophsis que no fabrica droides."
        playerName "Ataque pirata en Socorro con turbolásers... Todo es posible, pero son muchas improbabilidades seguidas."
        playerName "Todo parece normal, y por eso apesta a falso."
        hide tecnologia
        hide rutamala
        hide especia
        jump go_TiendaJawa
    # Tienes la Ruta Buena y la Falsa. No has mirado ninguna - o sólo tienes la Buena
    elif (itemRutaMelocoton == 1 or itemRutaMelocoton == 0) and itemRutaRealMelocoton == 1:
        show rutabuena
        show svivren at left with dissolve
        playerName "Echemos un vistazo. Reparaciones masivas en Svivren que llevaron semanas. Es el mayor tiempo en dique seco recientemente. Empezaremos por ahí."
        playerName "En Svivren compraron un cargamento de media tecnología, y de ahí fueron a Ryloth a venderlo, con escala técnica en Bahalian, cerca de Qiaxx."
        playerName "De momento tiene sentido: Svivren exporta tecnología, Ryloth la importa. Se saca beneficio en la ruta."
        hide svivren with dissolve
        show especia at right with dissolve
        playerName "¿Qué compraste en Ryloth, pillín? ¿Esclavos o droga? Ryloth no exporta mucho más...{p=10}Especia bruta para fabricar medicina. ¿En serio?"
        playerName "Desde Ryloth coges una ruta no registrada... ¿hasta el sector Ferra? Hypori. ¿Qué hay en Hypori?"
        hide especia with dissolve
        show droide at left with dissolve
        playerName "Recoges droides... Espera, ¿no llenaste la bodega sólo con especia en Ryloth? Si tu cliente necesita droides y especia, ¿por qué no encargó dos naves? Recibiría dos cargamentos llenos... Esto no es eficiente."
        playerName "...a menos que la discrecion sea muy importante. ¿Quién está interesado en tanta discreción?"
        hide droide
        show kaminoano at right with dissolve
        playerName "Has llegado al... Espacio Salvaje, más allá de Rishi... Conozco estas coordenadas: ¡Es Kamino! ¡El mundo de los clonadores!"
        show ororo at left with dissolve
        playerName "Un momento, espera. Se rumorea Transportes Ororo desafió a Transporte Xizor, de Sol Negro; Xizor mató a sus dueños... ¿y quizá los reemplazó por directivos afines a él?"
        hide kaminoano with dissolve
        show xizor at right with dissolve
        playerName "Xizor fue Príncipe del sindicato criminal Sol Negro. Svivren y Qiaxx están asociados a Sol Negro; he oído que el Príncipe Dequc controla esos mundos, y que intentó escindirse para crear su propia organización, Nébula Negra."
        playerName "Ryloth, Hypori e incluso Kamino formaban parte de otro grupo criminal, el Consorcio Zann, pero se dice que Sol Negro también los ha absorbido."
        playerName "Sin embargo, los hutts y los señores de la guerra no van a permitir semejante cosa. Van a pelear por esos sistemas."
        hide ororo with dissolve
        show blacksun at left with dissolve
        playerName "Conclusión: El poder de Terrem Jesond viene de que Sol Negro controla estos sistemas. Pero su control es inestable. Sus mundos cambiarán de manos en un mes."
        hide xizor
        playerName "Jesond y Transportes Ororo tienen sobornado al Imperio en este sector, Arkanis, para poder volar por aquí. Pero si el Imperio pierde el sector, que es probable, Ororo está perdido."
        playerName "El koorivar Jesond es agente de Sol Negro, y está perdiendo puntos rápidamente."
        playerName "Tengo suficiente información para que Jesond se retire de la competición."
        hide blacksun
        $ informacionImplicaCrimelord2 = 1
        $ itemRutaRealMelocoton = 2
        $ ordenadorNav = 3
        jump go_TiendaJawa
    # Tienes la Ruta Buena y la Falsa. Miraste antes la falsa
    elif itemRutaMelocoton == 2 and itemRutaRealMelocoton == 1:
        # La RUTA BUENA es: Svivren (O19) > Qiaxx (P18) > Ryloth (R17) > Hypori (S16) > Kamino (S15) > Tatooine
        hide wassak with dissolve
        show rutamala at left with dissolve
        show rutabuena at right with dissolve
        playerName "De un golpe de vista, esto no tiene nada que ver con lo que TurJinda me dio antes."
        hide rutamala with dissolve
        hide rutabuena with dissolve
        show rutabuena
        show svivren at left with dissolve
        playerName "Echemos un vistazo. Reparaciones masivas en Svivren que llevaron semanas. Es el mayor tiempo en dique seco recientemente. Empezaremos por ahí."
        playerName "En Svivren compraron un cargamento de media tecnología, y de ahí fueron a Ryloth a venderlo, con escala técnica en Bahalian, cerca de Qiaxx."
        playerName "De momento tiene sentido: Svivren exporta tecnología, Ryloth la importa. Se saca beneficio en la ruta. Parece algo normal."
        hide svivren with dissolve
        show especia at right with dissolve
        playerName "¿Qué compraste en Ryloth, pillín? ¿Esclavos o droga? Ryloth no exporta mucho más...{p=10}Especia bruta para fabricar medicina. ¿En serio?"
        if itemRutaMelocoton > 0:
            playerName "De momento casi todo parece legal. ¿Por qué me ocultaste la ruta antes, TurJinda? ¿Qué tienes que ocultar?"
        else:
            playerName "De momento casi todo parece legal, pero algo huele mal. ¿Qué tienes que ocultar, TurJinda?"
        playerName "Desde Ryloth coges una ruta no registrada... ¿hasta el sector Ferra? Hypori. ¿Qué hay en Hypori?"
        hide especia with dissolve
        show droide at left with dissolve
        playerName "Recoges droides... Espera, ¿no llenaste la bodega sólo con especia en Ryloth? Si tu cliente necesita droides y especia, ¿por qué no encargó dos naves? Recibiría dos cargamentos llenos... Esto no es eficiente."
        playerName "...a menos que la discrecion sea muy importante. ¿Quién está interesado en tanta discreción?"
        hide droide with dissolve
        show kaminoano at right with dissolve
        playerName "Has llegado al... Espacio Salvaje, más allá de Rishi... Conozco estas coordenadas: ¡Es Kamino! ¡El mundo de los clonadores!"
        show ororo at left with dissolve
        playerName "Un momento, espera. Se rumorea Transportes Ororo desafió a Transporte Xizor, de Sol Negro; Xizor mató a sus dueños... ¿y quizá los reemplazó por directivos afines a él?"
        hide kaminoano with dissolve
        show xizor at right with dissolve
        playerName "Xizor fue Príncipe del sindicato criminal Sol Negro. Svivren y Qiaxx están asociados a Sol Negro; he oído que el Príncipe Dequc controla esos mundos, y que intentó escindirse para crear su propia organización, Nébula Negra."
        playerName "Ryloth, Hypori e incluso Kamino formaban parte de otro grupo criminal, el Consorcio Zann, pero se dice que Sol Negro también los ha absorbido."
        playerName "Sin embargo, los hutts y los señores de la guerra no van a permitir semejante cosa. Van a pelear por esos sistemas."
        hide ororo with dissolve
        show blacksun at left with dissolve
        playerName "Conclusión: El poder de Terrem Jesond viene de que Sol Negro controla estos sistemas. Pero su control es inestable. Sus mundos cambiarán de manos en un mes."
        hide xizor
        playerName "Jesond y Transportes Ororo tienen sobornado al Imperio en este sector, Arkanis, para poder volar por aquí. Pero si el Imperio pierde el sector, que es probable, Ororo está perdido."
        playerName "El koorivar Jesond es agente de Sol Negro, y está perdiendo puntos rápidamente."
        playerName "Tengo suficiente información para que Jesond se retire de la competición."
        hide blacksun
        $ informacionImplicaCrimelord2 = 1
        $ itemRutaRealMelocoton = 2
        $ ordenadorNav = 3
        jump go_TiendaJawa
    # Ya tienes toda la información que necesitas
    elif itemRutaRealMelocoton == 2:
        show rutabuena with dissolve
        playerName "Ya he averiguado lo que necesitaba saber. No necesito mirar nada más aquí."
        hide rutabuena with dissolve
        jump go_TiendaJawa
    playerName "Bueno, ya he mirado el ordenador de navegación."
    jump go_TiendaJawa

label hablarGraf:

    menu:
        "Necesito un permiso de despegue." if preguntarPermisoEnCantina == 2 and itemWantedPoster == 0:
            playerName "Tengo un problema con mi permiso de despegue. Parece que se haya borrado de las bases de datos imperiales."
            graf "Vamos a empezar por algo fácil: ¿Tú tenías un permiso de despegue válido de verdad? No me mientas."
            playerName "Sí, lo tenía. No sé qué ha pasado."
            graf "Ha pasado que el software imperial falla como el superláser de la Estrella de la Muerte. Bugs, glitches, y la mitad del tiempo no encuentran su propio pico con ocho tentáculos."
            graf "Software contratado a una consultora poblada de trabajadores clónicos, que subcontrata a un desarrollador droide... Ah, pero para qué aburrirte con la historia de mi vida."
            graf "Puedo resolver tu problema. Es tan simple como que yo me meto en su base de datos, encuentro tu permiso, le pongo una marca de que hay que procesarlo y llega a la oficina de la gobernadora. Incluso puedo homologarlo allí."
            graf "Lo que haré es entrar en un sistema imperial y {i}hacer el trabajo{/i} que tendrían que hacer ellos, pero mejor. Porque yo soy la número uno."
            graf "Me puedo hacer pasar por un Moff o algo. Si alguien investiga, el Moff dirá que hizo ese trámite porque, si no, reconocería ineficiencia en su propia gente."
            graf "Pero eso tiene un coste, [playerName]. Ahora mismo el teniente Harburik quiere impresionar al Moff, y con tres amos del crimen peleando por el control de Tatooine, necesita cazar a alguien. No quiero atraer a los de blanco sobre mí."
            playerName "Lo comprendo, corres un riesgo. Dime cuánto quieres."
            graf "No quiero dinero. Quiero que me hagas un favor."
            show bandido amarillo at left with dissolve
            graf "Éste es Thondo Qo. Es un bandido que ha destrozado muchas vidas. Antiguo mercenario, asesino a sueldo, mala persona en general. Hay mil créditos de recompensa por él."
            playerName "Suena peligroso. ¿Por qué me estás hablando de él?"
            graf "Quiero que le captures y le entregues a las autoridades."
            playerName "¿Qué?"
            menu:
                "Tú necesitas más bien un cazarrecompensas.":
                    playerName "Tú no necesitas un xenobiólogo, ¡tú necesitas un cazarrecompensas!"
                    graf "No. {i}Tú{/i} necesitas un cazarrecompensas."
                "¿No prefieres algo de dinero?":
                    playerName "¿No prefieres que te pague en efectivo?"
                    graf "Esto no se resuelve con dinero."
                "¿Yo te doy dinero y tú contratas un cazarrecompensas?":
                    playerName "¿Y si te doy dinero y tú contratas un cazarrecompensas?"
                    graf "No puedo buscar un cazarrecompensas directamente. Mi cabeza tiene un precio. Debería saltar del sector lo antes posible."
            playerName "¿Qué problemas tienes con Qo?"
            graf "¡Es un monstruo que ha matado gente inocente en mi propia ciudad! No puedo permitir en buena conciencia que siga suelto. Encuéntralo y elimínalo."
            playerName "¿Es personal? ¿Buscas venganza?"
            graf "Si le paras a tiempo, no."
            playerName "No sé si podré con eso..."
            graf "Quédate el holograma. Incluye los detalles de la recompensa. Por supuesto, no puedes cobrarla sin una licencia de cazarrecompensas."
            playerName "¿Por qué los cazarrecompensas no van a por él?"
            graf "La recompensa es demasiado baja. No les cubre los costes de investigar dónde está Qo."
            playerName "Voy a arrepentirme de esto, pero necesito mi permiso de despegue."
            hide bandido
            $ itemWantedPoster = 1
            $ preguntarKabePorCazador = 1
        "¿Podrías retirar una investigación abierta sobre mi nave?" if preguntarGrafInvestigacion == 0 and itemInvestigacion == 0:
            playerName "Hay una acusación de contrabando sobre mi nave."
            graf "Eso es un asco. Hasta que la sobresean o resuelvan, no te dejarán salir del sistema."
            playerName "¿Tú podrías hacer que... desapareciese?"
            play sound "sound/gasp.mp3"
            graf "No. No. Ni hablar."
            graf "Eso es entrar en bases de datos imperiales bien protegidas. Si me pillan, me mandarán a Kessel o algo peor."
            menu:
                "Seguro que eres lo bastante buena, y será un logro memorable.":
                    playerName "Vamos, eres la gran rebanadora, la alumna aventajada de Shenir Rix."
                    graf "Nunca vi a Rix, sólo chateamos por la red. Tal vez ni siquiera era Rix."
                    playerName "Si lo consigues, te forjarás una reputación."
                    graf "Sí, entre los Rangers y Seguridad Imperial. Ni hablar."
                "Pídeme a cambio lo que quieras.":
                    playerName "Ponle precio. Conseguiré lo que necesites."
                    graf "No hay recompensa que compense esto. No podría gastármela en el Averno."
                    playerName "¿El Averno? Hacía mucho que no oía esa palabra."
            playerName "Bueno, si estás segura..."
            graf "Mi vida ya es bastante complicada."
            $ preguntarGrafInvestigacion = 1
        "¿Es Jent una buena piloto?" if preguntarGrafPorJent == 1:
            playerName "Tú eres Hawk, la amiga de Jent Loquoy, ¿verdad? Ella me ha hablado de ti."
            graf "Vaya, ¿me menciona a otras personas?"
            playerName "Dijo que me dirías si ella es buena piloto."
            graf "¿Buena? Es excelente. Nos conocemos de toda la vida y he seguido su resultados desde que ella apenas llegaba a los controles."
            show cifras jent at left with dissolve
            graf "Éstos son sus resultados del simulador. Conozco pilotos de combate que se quedan en bastante menos."
            playerName "¿Conoces muchos pilotos de combate?"
            graf "Bueno, antiguos pilotos de combate. Las cantinas de un puerto espacial están llenas de ex-militares metidos a pilotos comerciales, y la mitad de ellos son mucho peores que Jent."
            graf "Ella se presentó a las pruebas de la Academia Imperial para ser piloto de caza, en {i}todos{/i} los cazas."
            graf "Siempre superó la nota de corte para entrar. Pero no llegó al nivel excelente, por muy poco."
            graf "Si hubiese sacado excelencia, el Imperio habría pagado sus estudios con una beca."
            hide cifras jent with dissolve
            playerName "¿Y tú no tuviste nada que ver con sus notas?"
            graf "¡Ja! Ella me mataría si me atreviese a rebanar sus resultados."
            graf "Jent llegará a ser piloto, sólo espero que civil. Ojalá ella no fuese una {i}fangirl{/i} del Imperio."
            playerName "¿Cuál es el problema?"
            graf "¿Crees que el Imperio aprecia a los rebanadores?"
            playerName "¿No te gusta el Imperio?"
            graf "Soy rebanadora. Me meto en sistemas donde no debería entrar. 7 de cada 10 veces, son sistemas imperiales. ¿Qué crees que piensa el Imperio sobre mi carrera?"
            $ preguntarGrafPorJent = 2
        "¿Me prestas un ordenador de navegación?" if ordenadorNav == 1:
            playerName "¿Puedes prestarme un ordenador de navegación?"
            graf "¿Qué?"
            graf "¡No {i}tengo{/i} un ordenador de navegación! ¿Qué crees que es esto, una nave espacial?"
            playerName "Vale, perdona."
            # No cambias variables, así que esto puede volver a salir
        "He capturado a Thondo Qo." if bandidoCapturado == 1 and itemPermisoDespegue == 0:
            playerName "He capturado a Thondo Qo como me pediste."
            graf "Sí, tengo un {i}feed{/i} que me ha avisado. Ha sido muy inteligente recurrir a 4-LOM, que tiene enlace permanente con las redes."
            playerName "Eso está muy bien. ¿Cumplirás tu parte del trato, o eres tan traicionera como Qo?"
            graf "¡Me ofendes! Soy una rebanadora de palabra. Déjame teclear un momento y tu permiso de despegue estará restaurado..."
            play sound "sound/teclear.mp3"
            if activosRebeldes == 1:
                graf "Mientras esperas, ¿te apetece hacerme otro favor? No me ofenderé si lo rechazas, y no puedo ofrecerte nada a cambio."
                playerName "¿De qué se trata?"
                graf "Necesito un piloto..."
                playerName "¿En Tatooine? Entra en la cantina y encontrarás dos pilotos por cada vaso que veas."
                graf "Necesito a alguien de fiar, no a un mercenario borracho. No me vale cualquier piloto de carguero medio o pesado. Quiero un piloto de... de caza de combate. Incom. Z-95 y {i}(murmurando){/i} T-65."
                playerName "¿Alas-X? ¿En qué estás metida, Hawk?"
                graf "¿En qué {b}no{/b} estoy metida, [playerName]? Soy una rebanadora. ¿Puedes ayudarme?"
                playerName "Yo no sé pilotar ni un carguero. Necesito a mi droide para eso. Como mucho soy [tuUn] copilot[tuO] mediocre."
                graf "¿Me ayudarías a encontrar un piloto? Por favor, estoy desesperada."
                menu:
                    "Te ayudaré.":
                        playerName "Te ayudaré. Eres más agradable que la mayoría de gente por aquí."
                        graf "No lo lamentarás. Si conoces a alguien, traémelo."
                        $ questReclutarPiloto = 1
                    "No puedo ayudarte.":
                        playerName "No puedo ayudarte. No conozco a ningún piloto que cumpla esas condiciones."
                        play sound "sound/sigh.mp3"
                        graf "{i}suspiro{/i} No puedo culparte. Gracias por escucharme, y no lo cuentes por ahí."
                        $ questReclutarPiloto = 2
                        pass
                graf "Tu permiso de despegue estará listo en cuestión de unos minutos..."
                $ activosRebeldes = 2
            else:
                graf "Tu permiso de despegue estará listo en cuestión de unos minutos..."
            "Hawk se sienta ante un ordenador y empieza a teclear furiosamente."
            "La pantalla se llena de caracteres y cambia demasiado rápido para que puedas seguir sus acciones."
            "De vez en cuando hay algún mensaje en letras rojas grandes, pero Hyperhalo lo ignora."
            "Ella ha terminado en un cuarto de kilosegundo. Se gira y te mira sonriendo."
            show permisodedespegue at left
            graf "Un permiso de despegue para mi amig[tuO] [playerName], firmado por el Moff Alexander Julstan IV."
            graf "¿Puedo hacer algo más por ti?"
            hide permisodedespegue
            $ bandidoCapturado = 2            
            $ itemPermisoDespegue = 1
            call ComprobarLosTres from _call_ComprobarLosTres_1

                                                                                           
        "Te he descubierto: He encontrado las naves rebeldes." if activosRebeldes == 1 and questReclutarPiloto == 0:
            playerName "Teniente Hyanon Hyperhalo, ¿Fuerzas Especiales de la Alianza?"
            "Hyperhalo suda y desvía la mirada."
            graf "En realidad, trabajo para la Red de Espías Bothan."
            graf "Y no sé si soy teniente o qué. Todo el resto de la unidad ha muerto."
            playerName "¿Fue Qo?"
            graf "No, pero corría el riesgo de que él descubriese el hangar secreto."
            graf "¡Yo no podía permitir que un bandido se hiciese con esos cazas!"
            playerName "Con uno de ésos, podrías salir del planeta sin problemas. Esclavizas los motores de los otros cazas, y te los llevas. Desde lo de Endor, hay una docena de mundos que son refugio seguro para ti."
            graf "¡¡¡Pero yo no sé pilotar un caza!!!{p}¿Supongo que tú no podrías hacerlo por mí?"
            playerName "¿Qué? Yo ni siquiera sé pilotar mi propia nave. Necesito a mi droide para que la lleve."
            playerName "Además, no vamos en la misma dirección. Tengo mi propia misión que cumplir."
            graf "Voy a arrepentirme de esto, pero:"
            graf "¿Podrías conseguirme un piloto para esto? Uno de fiar, no un canalla como TurJinda."
            graf "No sé si me queda algo que ofrecerte a cambio. Ayúdame, por favor. Estoy desesperada."
            menu:
                "Acepto, haré una buena obra por ti.":
                    playerName "Te ayudaré. Eres más agradable que la mayoría de gente por aquí. Puedo hacer una buena obra por ti."
                    graf "No lo lamentarás. Si conoces a un buen piloto, traémelo."
                    $ questReclutarPiloto = 1
                "No puedo ayudarte.":
                    playerName "No puedo ayudarte. No conozco a ningún piloto que cumpla esas condiciones."
                    play sound "sound/sigh.mp3"
                    graf "No puedo culparte. Gracias por escucharme, y no lo cuentes por ahí."
                    $ questReclutarPiloto = 2
                    pass
            graf "Tu permiso de despegue estará listo en cuestión de unos minutos..."
            $ activosRebeldes = 2
            "Hawk se sienta ante un ordenador y empieza a teclear furiosamente."
            "La pantalla se llena de caracteres y cambia demasiado rápido para que puedas seguir sus acciones."
            "De vez en cuando hay algún mensaje en letras rojas grandes, pero Hyperhalo lo ignora."
            "Ella ha terminado en un cuarto de kilosegundo. Se gira y te mira sonriendo."
            graf "Un permiso de despegue para mi amig[tuO] [playerName], firmado por el Moff Alexander Julstan IV."
            show permisodedespegue at right
            "Hawk te da el permiso de despegue."
            hide permisodedespegue
            graf "¿Puedo hacer algo más por ti?"
            $ bandidoCapturado = 2            
            $ itemPermisoDespegue = 1
            call ComprobarLosTres from _call_ComprobarLosTres_2

        "¿Qué hay entre Jent y tú?" if hablarGrafDeJent == 0:
            playerName "¿Qué hay entre Jent Loquoy y tú?"
            graf "¿Jent? Eh - Somos amigas desde niñas. Crecimos juntas."
            "Hyperhalo balbucea, desvía la mirada y tiembla visiblemente."
            graf "Ya sabes, otra chica de tu misma edad, en una colonia pequeña, os conocéis desde crías... Haces migas por necesidad."
            playerName "Ya..."
            $ hablarGrafDeJent = 1
        "Hasta luego.":
            playerName "Me voy, Hawk. Hasta luego."
            "Hawk está totalmente concentrada en un monitor, tecleando ocasionalmente. Es posible que haya murmurado una despedida."
            jump go_CasaGraf

    jump hablarGraf


label hablarJentGranja:
    menu:
        "Enséñame las pruebas de tu aventura." if itemRataMuerta == 0 and conoceClawditaA == 0:
            jent "Sí, claro. Como recordarás, las ratas womp me tendieron una trampa y estrellaron mi T-16. Las ratas womp no son lo bastante inteligentes para eso, ni para perseguirme en un grupo tan grande."
            jent "Pero éstas estaban juntas, y tenían líderes claros. Al día siguiente, volví por allí, esta vez con el speeder. Ya no tenía el T-16."
            "Jent baja la cabeza y suspira un momento."
            play sound "sound/sigh.mp3"
            jent "Encontré una rata muerta justo en ese sitio. Creo que fue atropellada por las otras cuando huyeron. Piénsalo: Todo el grupo era... raro. Ratas inteligentes. Tenemos una rata muerta."
            show ratamuerta at left
            "Recibes rata womp muerta."
            playerName "Esto es... Parece una rata womp normal. Sus zarpas son normales..."
            jent "Tú eres una lumbrera. Creo esta rata tiene algo en su cerebro. Si le abres la cabeza, descubrirás algo extraordinario."
            playerName "¿Una autopsia?"
            playerName "Así, a simple vista, sospecho que no murió pisoteada por ratas sino por un vehículo repulsor."
            hide ratamuerta
            if visteDeclaracionWassak == 1:
                playerName "¿Sabes? He hablado con Wassak, el jawa. Tú me dijiste que erais amigos."
                jent "Sí."
                playerName "Él ha tenido otro encuentro con ratas inteligentes y vio que tenían pulgares. Si tus ratas inteligentes sostenían palos, también deberían tenerlos, para poder manipular herramientas."
                jent "Tiene sentido, ¿no?"
                playerName "Esta rata tiene zarpas normales. Es un plantígrado. No tiene dedos que pueda mover independientemente."
                jent "Quizá... ¿dos ratas inteligentes lideraban una manada de ratas normales?"
                playerName "¿Y ésta es una de las soldados, mientras las otras son reinas? Me parece pillado por los pelos."
            playerName "Pero oye, me llevo la rata. Si descubro algo importante, me aseguraré de mencionar tu nombre."
            $ itemRataMuerta = 1

        "Así que te consideras piloto..." if hablarJentPiloto == 0:
            playerName "Así que vas por ahí diciendo que eres piloto."
            jent "Vaya, gracias. Me encanta hablar de eso y poca gente aquí me deja."
            playerName "(Sospecho que se saben todas tus anécdotas)."
            jent "Llevo poniéndome a los mandos de un speeder desde antes de sostenerme en pie sola. He pilotado todo lo que he encontrado a mano, siempre puliendo mis capacidades."
            jent "Ma me compró el T-16 hace tres años, de segunda mano y me hizo prometer que no volaría sin supervisión en un año. Dediqué ese tiempo a mejorar la máquina con piezas compradas a los jawas. Aprendí un montón."
            playerName "¿Qué vehículos sabes pilotar?"
            jent "Cazas espaciales, saltadores, vainas, lanzaderas, cañoneras, cargueros, cápsulas, yates. ¡Me atrevo con todo!"
            jent "Tengo 630 horas de vuelo, la mitad en simulador de caza. Quería entrar en la Academia Imperial. ¿Has visto mis resultados en la oficina imperial?"
            if preguntarGrafPorJent == 2:
                playerName "No ha sido fácil, pero sí: Eres segunda teniente en simulación. Te han derribado más veces de las que has ganado, pero has ganado más de la mitad de tus batallas."
                jent "A veces sacrifico mi nave embistiendo el puente enemigo. A veces me destruyen cuando nuestro bando ya ha ganado la batalla. Yo podría ser una piloto decente."
            else:
                playerName "No he podido. Pero si eres tan buena, ¿por qué no te dan la beca que quieres?"
                jent "No sé si llego a tanto... Seguramente no soy tan buena como para ser as de la aviación espacial, pero puedo ser piloto."
            jent "El año pasado superé la nota de corte para entrar, pero no para que me financiasen los estudios. Pretendía volver a intentarlo el año que viene, pero ahora ya no lo sé."
            playerName "¿Qué ha pasado?"
            jent "La batalla de Endor. El Imperio está {i}musido{/i} en el caos. Ni siquiera sé si seguirán con la Academia."
            playerName "Precisamente ahora están bajando los requisitos de acceso porque necesitan muchos oficiales rápido."
            jent "Además, el Imperio hace escaneos muy estrictos de lealtad y... La verdad es que no me simpatizan. No me gustaría ser piloto de combate en un TIE."
            playerName "¿Ah, no? Es el sueño de casi cualquier niño."
            jent "¡Ya no soy ninguna niña! Pero en realidad, el Imperio es {i}orsepivo{/i} y malvado. Yo me apuntaría a la Rebelión si pudiese, como hizo el hijo de Darklighter. Él sí que molaba. Ahora quiero estar en la Nueva Alianza Rebelde, que siempre han iod de buenos."
            jent "Pero para entrar en la Nueva Cosa Ésa sí que hay que tener contactos. Alguien que haya luchado contra el Imperio en la guerra. Yo ni siquiera conocí al hijo de Darklighter."
            jent "Daría un ojo y un brazo por pilotar para ellos. Bueno, no, porque entonces no podría pilotar. Pero tú me entiendes, ¿no?"
            $ hablarJentPiloto = 1
        "Este diario explica lo de las ratas inteligentes" if conoceClawditaA == 1 and itemDiarioErmitano < 2:
            playerName "He encontrado este diario en el Mar de Dunas."
            playerName "Parece bastante claro: Un ermitaño entrenó a varias ratas para hacer trucos y colaboró con alguien que podía simular una rata gigante."
            playerName "Diría que te han engañado con lo de las ratas... o más bien que tú me intentas engañar a mí... porque, según el ermitaño, las ratas te atraparon, y tu historia olvida sospechosamente esa parte."
            jent "Ups.{p}Esto no es lo que parece, [playerName]... Puedo explicarlo todo..."
            playerName "Adelante. Te escucho."
            show loquoy at right
            loquoy "Sí, yo también estoy interesada."
            jent "Oh, {i}poodoo{/i}..."
            jent "Vi el cable, pero me acerqué aposta. Quería ponerme a prueba y saber si podía girar a tiempo. No podía. Fui demasiado rápida."
            jent "El asiento eyectable cayó sobre el barranco; pero el cinturón se rompió y yo me caí al fondo. Entonces vi a la rata gigante, que me apuntaba con un bláster. Es extraño, porque no creí que hubiese ratas allí."
            jent "Creí haber visto una persona mientras caía. Debió ser el hombre del mensaje."
            jent "La rata vino a por mí y me pilló. ¿Te imaginas lo que es ver algo así de feo, así de grande, y así de {b}cerca?{/b} Empezaron a aparecer las otras ratas a mi alrededor. Pero quizá fuesen unas diez, no tantas como dije."
            jent "El monstruo me echó su fétido aliento a la cara y me preguntó qué había visto yo. ¿Puedes creerlo? ¿Que una rata te pregunte algo así? Le dije la verdad. Yo estaba demasiado asustada para mentir."
            jent "Me siguió interrogando y entonces oímos llegar el speeder de Pa. La rata se giró, pero no me soltó."
            jent "Me hizo prometer que no le contaría a nadie nuestra conversación, o iría a por mi familia. Ella había memorizado el código del speeder de Pa."
            loquoy "Jent, tu padre y yo sabemos defendernos. Los moradores de las arenas no han podido con nosotros. ¡Que vengan las ratas!"
            playerName "Has llamado {i}ella{/i} a la rata. ¿Por qué?"
            jent "Tenía voz de mujer. Humanoide, al menos."
            playerName "¿Qué más te preguntó?"
            jent "Quería saber si yo había encontrado alguna nave espacial en la zona. Un yate o algo así, en alguna de las cuevas. Le dije que no, ¡y era cierto! ¡No sé qué buscaba, pero yo no lo tenía!"
            playerName "Tranquila, Jent."
            loquoy "(Esta niña necesita una aventura de verdad pronto... Algo realmente épico)."
            $ itemDiarioErmitano = 2
        "Hawk necesita una piloto, ven conmigo." if questReclutarPiloto == 1 and hablarJentPiloto == 1:
            playerName "Tengo un trabajo para ti, necesitamos una piloto."
            jent "¿Qué? Bueno, pero..."
            show loquoy at right
            loquoy "¡Un momento, forastero! ¿No irás a meter a mi niña a contrabandista o algo así?"
            playerName "No, Lorna la Larga. En este planeta, si quisiera un contrabandista, sé dónde conseguirlos."
            loquoy "¿Pirata espacial, entonces?"
            playerName "Tampoco. Sólo necesito que lleve unas naves hasta su propietario."
            loquoy "Lástima. La piratería es una profesión honorable."
            jent "¿Yo no tengo nada que opinar?"
            loquoy "Llevas toda la vida queriendo ser piloto. Ve y consigue unas horas de vuelo hiperespacial en condiciones."
            jent "Yo confío en [playerName], Ma, ¿pero tú estás segura con [tuPronombre]...?"
            loquoy "[tuPronombreMayus] sabe que, si te hace algo, no descansaré hasta sacarle los redaños."
            playerName "Quede tranquila, Lorna la Larga. Venga, Jent, vamos hacia la finca de Sedi Fisk, a convencer a tu nuevo jefe."
            jent "Pero... ¿Quién es? Por esa zona, sólo vive..."
            $ questReclutarPiloto = 2
            hide jent
            hide loquoy
            scene bg casa graf
            show jent at left
            show graf
            jent "Hola, Hawk. ¿A ti también te están contratando?"
            graf "¿Qué estás haciendo, [playerName]? ¿Qué hace ella aquí?"
            playerName "Necesitas un piloto, Hyperhalo. Ella es piloto."
            graf "¡Ya sabes porqué no puedo implicarla! No me obligues a decirlo con ella delante."
            playerName "Jent, ¿qué dirías si te ofrezco pilotar para la Nueva República?"
            jent "¡Hey, estupendo! Sus cazas son una delicia y ellos son los buenos. ¿Piensan liberar Tatooine del Imperio? ¿Puedo ayudar?"
            graf "¿Qué?"
            jent "Espera: ¿Tú trabajas para la Nueva República? [playerName], nunca lo habría imaginado. Pensé que eras [tuUn] [tuEmpollon], sin más. ¿Puedes recomendarme a tus jefes?"
            playerName "Yo, no. Habla con tu amiga."
            jent "¿Para qué voy a hablar con Hawk? Ella no está en la Nueva República."
            graf "Ah... Esto..."
            graf "Verás, Jent... Llevo casi tres años colaborando con la Alianza Rebelde. A tiempo parcial; me infiltro en agencias imperiales y de los hutts..."
            "Jent se queda con la boca abierta y parpadea lentamente tres veces. Su voz sube dos agudos.***¿SE DICE ASÍ? TBA"
            jent "{b}¿¡¿QUÉ?!?{/b}"
            jent "¿Eres una agente secreta rebelde y nunca me dijiste nada?"
            graf "Era un secreto. Aún lo es. Por eso se llama agente {i}secreta{/i}..."
            jent "Te conozco desde los tres años y sabes que pilotar para la Alianza es mi sueño."
            graf "No, tú querías pilotar para el Imperio..."
            jent "Serías mi ídolo, mi heroína, y tú te lo callas. No sé si pegarte o besarte."
            playerName "Jent, escucha: Hyperhalo tiene que sacar del planeta un escuadrón de cazas. Alguien debe pilotar la nave maestra. Es peligroso."
            graf "Es muy importante, Jent. Esas naves tienen que llegar a espacio republicano. No va a ser fácil. Tendrás que volar hasta Kothlis, en el sector Bothan."
            graf "Eres mi única esperanza, Jent. ¿Estarías dispuesta ayudarme con esto? ¿Pilotarás las naves en esta misión para la República?"
            "Jent medita un instante, mirando al techo y acariciándose el mentón, pero no se molesta en tapar su sonrisa. Está encantada con esto."
            jent "No sin ti. Ahora te pregunto yo: ¿Te apetece subirte a una nave y vivir aventuras espaciales conmigo?"
            "El brillo en los ojos de Hawk no se debe, por una vez, al reflejo de los monitores, sino a lágrimas de alegría que rezuman al oír esas palabras."
            playerName "¡Por favor! Buscáos una pequeña luna."
            play sound "sound/chicasrien.ogg"
            "Ambas te miran y se echan a reír."
            playerName "Veo que vuestro problema está resuelto. Con permiso (de despegue), voy a seguir con mi vida."
            graf "Gracias, [playerName]. Nunca podremos pagarte por tu ayuda."
            jent "Hawk, ¿te parece que invitemos a Wassak? ¿Como mecánico de a bordo? Quizá consigamos droides copilotos..."
            graf "Como si yo fuese a negarte algo..."
            "Sales de la casa de Hyperhalo."
            jump go_CasaGraf
        "Eso es todo.":
            playerName "Eso es todo."
            jent "Eh, mantén el contacto."
            jump go_GranjaLoquoy

    jump hablarJentGranja

label hablarLoquoy:
    menu:
        "¿Han tenido problemas con moradores de las arenas?" if hablarLornaMoradores == 0:
            playerName "Los moradores de las arenas están especialmente agresivos. He oído que atacan granjas de humedad. ¿Ha peleado con ellos, Lorna la Larga?"
            loquoy "¿Por qué lo dices, muchachito? ¿Crees que soy de las que buscan problemas y se lanzan al abordaje, espada en mano, a la primera oportunidad?"
            playerName "Bueno, usted tiene una espada en la mano en este momento..."
            loquoy "Ah, sí. A ver, sé defenderme mejor que el granjero medio. Ha habido que hacer milicias de voluntarios ocasionales. La verdad es que esta estación está siendo brutal."
            loquoy "Pero yo no soy más que un tripulante con un arma, y disparo donde me dice el capi. No tengo la visión global."
            playerName "¿Con quién debería hablar?"
            loquoy "Con Darklighter. Huff Darklighter es el granjero más rico de la zona, quizá del planeta. Es el que más se juega, y el que mejor se informa."
            playerName "Gracias, Lorna la Larga."
            $ hablarLornaMoradores = 1
        "¿Es Jent tan buena piloto como dice?" if hablarLornaJent == 0:
            playerName "Usted ha visto a pilotos espaciales haciendo su trabajo, ¿no?"
            loquoy "Sí, yo no soy piloto. Yo era artillera, especialidad en torpedos. Pero serví con varios pilotos y capitanes."
            playerName "¿Torpedos en un carguero mercante?"
            loquoy "El sistema Socorro es un lugar, eh, divertido. A veces hay que defenderse de, eh, cinturones de asteroides. Destruir asteroides con torpedos, sí, eso tiene sentido, ¿verdad?"
            playerName "Lorna la Larga, siendo sinceros: ¿Es Jent tan buena piloto como ella dice ser?"
            loquoy "A ver...{p}No es tan buena como los pilotos que estaban en mis naves. Pero ellos tenían más muertes en su haber, digo, más tablas. Además, Jent es más cauta."
            loquoy "Lo que no me creo es que chocase su T-16 por torpeza. Eso no tiene maldito sentido. Si yo creyese que ella puede hacer eso, ¡no le habría dejado el T-16!"
            $ hablarLornaJent = 1
        "Hábleme del accidente de Jent." if hablarLornaAccidente == 0:
            playerName "Dígame, Lorna la Larga, su hija me ha mencionado un encuentro con ratas womp en el que se rompió su T-16, y dice que usted estuvo allí. ¿Puede hablarme de esas ratas?"
            loquoy "Cuando yo llegué, había una horda de esas bestezuelas. Más ratas juntas de las que yo había visto nunca, quizá unas tres o cuatro docenas, todas con un único objetivo. ¿Alguna vez habías visto tantas ratas juntas, [playerName]?"
            playerName "Trabajando juntas, no; pero Jent a mí me habló de cientos de ratas."
            loquoy "Jent exagera. Sin duda estaba asustada."
            loquoy "Ella decía que había dos ratas sosteniendo palos, pero si estaban allí, se fueron antes de que yo llegase."
            playerName "Se asustaron por la bengala. Al menos los eventos están en orden."
            loquoy "Disparé a una de las ratas que se acercó demasiado. Jent se empeñó en llevársela como recuerdo. Le parecía un momento significativo."
            loquoy "Mira, [playerName], tú has viajado por el espacio, igual que yo. Hemos visto cosas que creíamos imposibles. Yo no lo descarto a la ligera."
            $ hablarLornaAccidente = 1
        "Eso todo.":
            playerName "Eso es todo por ahora."
            loquoy "Aaarrrr! Quiero decir, hasta luego."
            jump go_GranjaLoquoy
            
#       ESTO HACE QUE LORNA NO VUELVA A SALIR. ¿POR QUÉ QUERRÍA YO ALGO ASÍ?
#    $ hablarLoquoy = 1

    jump hablarLoquoy

label hablarDarklighter:

    menu:
        "¿Cómo es la relación con los moradores?" if hablarDarklighter1 == 0:
            playerName "¿Es el trato entre moradores y granjeros tan duro como se cuenta?"
            darklighter "Ah, muchach[tuO], será difícil tenernos a todos contentos. Los moradores vivían en Tatooine antes que nosotros y bebían la escasa agua en las plantas y en el desierto."
            darklighter "Entonces llegamos nosotros y construimos los evaporadores de humedad. El agua que había pasó a ser para nuestras cosechas. Los moradores vieron sus fuentes secarse. Se enfadaron, claro."
            darklighter "Llevo años intentando convencer a los moradores de que el agua es suficiente para todos, {i}si{/i} usamos nuestra tecnología; pero desconfían."
            darklighter "Las escaramuzas son frecuentes. Esto está llegando a ser una guerra."
            $ hablarDarklighter1 = 1
        "¿Dónde atacan con más fiereza los moradores?" if hablarDarklighter2 == 0:
            playerName "¿Hay alguna zona que los moradores ataquen con más ahínco?"
            darklighter "Hay una zona hacia el noroeste de aquí. Está dentro del territorio de las granjas, pero los moradores no respetan las fronteras del Imperio."
            darklighter "Es un camino en desuso para los civilizados. No hay nada de nuestro interés en esa dirección."
            darklighter "Ahora hemos tenido que poner sensores y defensas en esa zona, o se convertirá en un campo de batalla."
            "Con esa información, ahora puedes visitar la zona de los recientes ataques."
            $ hablarDarklighter = 1
            $ descubrirDondeAtaques = 1
            $ hablarDarklighter2 = 1
        "¿Es usted el padre de Biggs Darklighter?" if hablarDarklighter3 == 0:
            playerName "Darklighter... Como Biggs Darklighter, ¿verdad? ¿El héroe de Yavin?"
            "Huff Darklighter sonríe e hincha su pecho."
            darklighter "Así es. Biggs era mi hijo, y le transmití mis ideales de libertad y democracia. Por eso luchó tan duramente contra el Imperio."
            darklighter "Gracias a él, la Alianza destruyó la Estrella de la Muerte, y ése fue el primer paso hasta llegar a la victoria final en Endor."
            darklighter "Yo no podría estar más orgulloso. Mi sobrino Gavin seguirá los pasos de Biggs cuando sea lo bastante mayor."
            $ hablarDarklighter3 = 1
        "Hasta luego.":
            playerName "Eso es todo, hasta luego."
            darklighter "Discúlpame que me retire, [playerName] pero hay muchos asuntos que requieren mi atención. El trabajo de un Barón potentado nunca termina."
            jump go_GranjaDarklighter
    jump hablarDarklighter

label hablarGranjero:
    
    # Hecho: Aquí hay que meter un randomizador que elija al azar una de las frases que digan.
    $ randomrumor = renpy.random.randint(1, 7)
    if randomrumor == 1:
        granjero "Los moradores de las arenas atacan muy a menudo las granjas. Son muchas tribus, están organizados y por algún motivo tienen pocos banthas."
    elif randomrumor == 2:
        granjero "He oído que algunos moradores han atacado también a los jawas."
    elif randomrumor == 3:
        granjero "Desde la muerte de Jabba el Hutt, varios jefes criminales luchan por controlar el contrabando en Tatooine."
    elif randomrumor == 4:
        granjero "La muerte del emperador es mentira, pura propaganda de la Rebelión."
    elif randomrumor == 5:
        granjero "Si quieres saber algo, con quien tienes que hablar es con Huff Darklighter. Es el granjero más rico y mejor informado de la zona."
    elif randomrumor == 6:
        granjero "Wenny Boggs es un gruñón, celoso del éxito de Darklighter. Está a un paso de ser un anarquista. Pero él se conoce el Mar de Dunas mejor que ninguno de nosotros."
    else:
        granjero "Cada vez veo ratas womp más raras. Ratas inteligentes. Ratas inteligentes, ratas acorazadas, ratas rabiosas... Sólo faltan ratas voladoras, y espero no haberlo gafado."
    playerName "Oh, qué interesante. Gracias."
    hide granjero

#    if hablarGranjero == 0:
#        "random a elegir novedades: Jawas atacados. Asentamientos atacados. Combate de jfes criminales."
#        "Sí saben sobre ataques."
#        "Sí han oído las historias de ratas womp friquis."
#        $ hablarGranjero = 1
#    else:
#    "Frases genéricas sobre ataques tusken."

    jump go_Granjas


label hablarCrimelord2EnCantina:

    hide kabe with dissolve
    hide camarero with dissolve
    hide crimelord2
    show crimelord2
    playerName "Quiero hablar contigo, Jesond. O más bien, {i}tú{/i} quieres hablar {i}conmigo{/i}."
    crimelord2 "El trabajo de un directivo nunca termina. No puede uno tomarse una copa en paz."
    menu:
        "Enseñarle la ruta real del {i}Tormenta de Melocotón{/i}.":
            playerName "He investigado una de tus naves, {i}Tormenta de Melocotón{/i}."
            crimelord2 "Una de las de Transportes Ororo, ¿no? ¿Y qué has descubierto, algo de contrabando?"
            play sound "sound/beber.mp3"
            "Jesond se lleva su cóctel a la boca."
            playerName "Tengo su auténtica ruta."
            "Jesond escupe la bebida, baja el vaso y te mira sin parpadear con sus ojos reptilianos y su completa atención."
            if crimelord1 < 2:
                playerName "Sé lo que significa. He descubierto tu plan. Si se lo cuento a Fenn y Radon, me imagino que te harán pedazos."
            else:
                playerName "Sé lo que significa. He descubierto tu plan. Si se lo cuento a Radon, me imagino que te hará pedazos."
            playerName "Lo siento, no tengo práctica con metáforas para muertes violentas. No suelo hacer amenazas. Pero me recibes, ¿verdad?"
            crimelord2 "¿Qué crees que sabes?"
            playerName "Tu nave, bien armada, visita mundos de la Nébula Negra, una escisión de Sol Negro. Después va a mundos del Consorcio Zann, un grupo criminal absorbido por Sol Negro. Si no coges mercancía, es que la misión es otra. Destruir."
            playerName "No sacas tajada con el comercio. TurJinda no es un contrabandista, sino un sicario. Intentas acallar a los mundos que te desafían, porque no controlas esos mundos. ¿Qué tal voy?"
            crimelord2 "Sigue."
            playerName "Si consigues Tatooine, puedes afianzar tu poder. Tus aliados te apoyarán, y con eso conseguirás que los mundos de Zann se calmen. Pero necesitas un imperio estable para hacerte con Tatooine."
            playerName "Si te hacías con Tatooine sin que nadie supiese el problema del Consorcio Zann, todo iría bien. Ahora es demasiado tarde."
            crimelord2 "Le-nore, ven un momento."
            show mayordomo at left
            "Un droide mayordomo camina a su lado. La mayoría de cantinas hacen que los droides se queden fuera porque ocupan espacio pero no consumen; parece que la Duquesa no."
            crimelord2 "Nos vamos de Tatooine, Le-nore. Completamente. Organiza los detalles, vete avisando a todo el mundo. Y quiero hablar con el capitán del {i}Tormenta de Melocotón{/i} en cuanto estemos a salvo."
            "El droide asiente con la cabeza y se retira."
            hide mayordomo
            menu:
                "Hablarle de la investigación del {i}[tuNave]{/i}.":
                    playerName "No es la única nave con la que tienes que hacer algo, Jesond. Hablemos del {i}[tuNave]{/i}."
                    playerName "Te jactas de controlar todo el tráfico de entrada y de salida. Claramente tienes contactos en la oficina de investigación imperial. Una palabra tuya, y la investigación sobre mi nave se desintegrará."
                    crimelord2 "No sabes lo que estás pidiendo, [playerName]."
                    playerName "Un momento, ahora lo entiendo: La investigación no ha sido casualidad. ¡Fuiste tú! Me incriminaste. ¿Pero por qué?"
                    crimelord2 "Tienes enemigos, [playerName]. Enemigos formidables. No sé qué has hecho para enfadarles, pero ahora estás perdid[tuO]. ¡Nadie puede con gente así!"
                    crimelord2 "Esa mujer es invencible. Puede llegar a todas partes. Puede nublar tu mente para que olvides haberles visto. ¡Puede matar con un pensamiento! ¡Lo he visto con mis propios ojos!"
                    playerName "¿Si ella es tan poderosa, por qué te necesita?"
                    crimelord2 "¡Tú no lo comprendes! Si alguien así te dice que perjudiques a otro incautando su nave, ¡no haces preguntas! ¡Obedeces!"
                    playerName "¿A quién tienes más miedo, Jesond? ¿A la mujer misteriosa, o a los dos jefes del crimen que querrán saber esto?"
                    crimelord2 "Está bien. Tú ganas. Haré que retiren la investigación. ¿Desde cuándo eres tan dur[tuO]?"
                    playerName "Tú sólo eres un señor del crimen. No te imaginas lo que es trabajar en una universidad. En mi día a día, la gente es implacable de verdad."
                    $ conoceClawditaB = 1
                    $ itemInvestigacion = 1
                    $ crimelord2Activo = 2
                    $ crimelord2EliminadoEnCantina = 1
                    call ComprobarLosTres from _call_ComprobarLosTres_3
                    jump siguesEnCantina
                "Interrogarle sobre sus amigos.":
                    playerName "Así que tus amigos son gente poderosa. ¿Quiénes son? ¿El moff sectorial? ¿El gobernador de Reuss?"
                    crimelord2 "No podrías ir más desencaminad[tuO]. Te hablo de gente verdadero poder. ¡Gente contra la que nadie puede!"
                    crimelord2 "Esa mujer es invencible. Puede llegar a todas partes. Puede nublar tu mente para que olvides haberles visto. ¡Puede matar con un pensamiento! ¡Lo he visto con mis propios ojos!"
                    playerName "¿Si ella es tan poderosa, por qué te necesita?"
                    playerName "No eres tan duro como quieres aparentar, Jesond. Cualquier ilusionista puede convencerte de que tiene poderes del lado oscuro."
                    $ crimelord2Activo = 2
                    $ crimelord2EliminadoEnCantina = 1
                    call ComprobarLosTres from _call_ComprobarLosTres_4
                    jump siguesEnCantina
        "Interrogarle sobre sus amigos.":
            pass
            playerName "Así que tus amigos son gente poderosa. ¿Quiénes son? ¿El moff sectorial? ¿El gobernador de Reuss?"
            crimelord2 "No podrías ir más desencaminad[tuO]. Te hablo de gente verdadero poder. ¡Gente contra la que nadie puede!"
            crimelord2 "Esa mujer es invencible. Puede llegar a todas partes. Puede nublar tu mente para que olvides haberles visto. ¡Puede matar con un pensamiento! ¡Lo he visto con mis propios ojos!"
            playerName "¿Si ella es tan poderosa, por qué te necesita?"
            playerName "No eres tan duro como quieres aparentar, Jesond. Cualquier ilusionista puede convencerte de que tiene poderes del lado oscuro."
    jump siguesEnCantina


label hablarCamarero:
    
    playerName "Duquesa, sírveme otra."
    camarero "Marchando jugo jawa y algo de conversación."

    menu:
        "¿Sabes cómo conseguir un permiso de despegue?" if preguntarPermisoEnCantina == 0:
            playerName "¿Sabes cómo puedo conseguir un permiso de despegue?"
            camarero "Creí que tenías un permiso de despegue. ¿No ibas a irte del planeta hoy mismo?"
            playerName "Ha habido un imprevisto. Han traspapelado mi permiso de despegue."
            camarero "Qué desastre... Te recomiendo hablar con Gorlok, aquí mismo, en la cantina. Sabe de bastantes cosas, te podrá orientar."
            $ preguntarPermisoEnCantina = 1
        "Si quisiera un cazarrecompensas..." if preguntarKabePorCazador == 1:
            playerName "Si yo quisiera contratar a un cazarrecompensas... ¿Qué tendría que hacer?"
            camarero "¿Ahora quieres contratar un cazarrecompensas? Qué vida más interesante llevas."
            playerName "Duquesa, ¿puedes ayudarme?"
            camarero "Creo que te he hablado de Gorlok. Es el listillo del bar. Sabe de todo, o eso dice. Habla con él."
        "Hay una investigación abierta sobre mi nave." if jugarLabria < 2:
            playerName "Hay una investigación abierta sobre mi nave, y no dejarán que despegue hasta que se resuelva. ¿Qué se te ocurre que puedo hacer?"
            camarero "Ni idea. Yo sólo sé sobre bebidas."
            "El kaminoano alto con aspecto de borracho se fija en ti y se une a la conversación."
            show labria at right
            labria "Creo que yo podría ayudarte con ese problema. Me llamo Vasail Tai."
            "¿Quieres hablar con Vasail?"
            menu:
                "Sí, hablar con Vasail.":
                    jump hablarLabria
                "Ahora mismo no.":
                    labria "Claro, esperaré... Pero no sé cuánta gente por aquí puede ayudarte con ese problema."
        "¿Quién es el nuevo cliente?" if jugarLabria < 2:
            playerName "No he visto antes a este cliente. ¿Quién es?"
            camarero "¿Quién? Ah, es un fracasado. Le dejamos quedarse porque no pide dinero a los clientes. Hace apuestas extrañas pero, cuando gana, se niega a cobrarlas."
            camarero "Se llama Vasail Tai y dice que está intentando asentarse en la zona. Otro que llega a colonizar, con ganas del comerse la galaxia."
            playerName "No es una especie habitual en este sector."
            camarero "La mía tampoco."
        "Conversación ociosa.":
            playerName "¿Nunca has pensado en volver a Polis Massa?"
            camarero "Mi familia sigue allí. Eso me anima a vivir en otro sector."
            playerName "Quizá conozcas a una arqueóloga de Polis Massa de la que oí hablar. Hace veinte años, ella encontró pruebas de que el Imperio Infinito de los rakata había llegado a la Brecha de Kathol."
            playerName "Después, ella tuvo problemas cuando intentó transportar sus descubrimientos y la acusaron de contrabando; y más problemas aún cuando la acusaron de falsificar sus evidencias. Escapó al sector Arkanis. {b}Este{/b} sector."
            playerName "Nogugny Kriill era su nombre. Una de las pocas kallidahin, o polis massanas, con cuerdas vocales lo bastante fuertes para hablar en idioma Básico."
            camarero "No tengo ni idea de lo que me estás contando...{p}Pero me alegra que el fisgón de Gorlok esté durmiendo en su mesa ahora mismo."
        "Hasta luego.":
            playerName "Hasta luego, Duquesa."
            camarero "Cielos despejados, [playerName]."

    jump siguesEnCantina


label hablarCazador:
    menu:
        "Busco a Thondo Qo.":
            jump hablarCazadorSobreBandido
        "¿Por qué un droide es cazarrecompensas?":
            playerName "¿Por qué un droide se mete a cazarrecompensas?"
            cazador "Por amor o dinero."
            playerName "¿O por amor al dinero?"
            cazador "Si tienes algo relevante que decirme, hazlo."
        "¿Qué ha sido de tu socio Zuckuss?":
            playerName "Tu reputación te precede, 4-LOM. Tú y tu socio Zuckuss reclamasteis varias recompensas muy altas para el Cártel Hutt."
            playerName "¿Dónde está Zuckuss ahora? ¿Sigue trabajando contigo?"
            cazador "Las actividades de identificación: Zuckuss no son asunto tuyo a menos que me pagues para encontrar a identificación: Zuckuss."
            playerName "No quieres hablar del tema, vale."
            cazador "Si tienes algo relevante que decirme, hazlo."
    jump hablarCazador

label hablarCazadorSobreBandido:
    show bandido amarillo at left with dissolve
    playerName "Estoy buscando a un criminal fugitivo, Thondo Qo."
    cazador "¿Por qué? No está condenado a muerte en varios sistemas. Su recompensa es de sólo mil créditos, y eso no cubre los gastos de la captura."
    cazador "Si Qo es capturado, le juzgarán. Hay 7 posibilidades entre 29 de que quede libre. Si le encierran, hay 19 posibilidades entre 47 de que escape en menos de 3 ciclos. En ambos casos, tu problema no queda resuelto por su captura."
    playerName "Mis razones son mías, 4-LOM. ¿Sabes algo sobre Qo?"
    cazador "La información pública sobre Qo está disponible en otras fuentes. La información deducida sobre Qo es irrelevante si nadie va a capturarle."
    cazador "Qo es un conocido asociado de otro criminal, Banndarr Bo. Me interesa su recompensa, así que persigo a ambos. Sé dónde se esconde, pero no le he perseguido todavía. Estoy implicado en otras 54 cazas con más prioridad."
    cazador "He consultado las bases de datos. La recompensa por Qo es imperial. Tú, [playerName], no tienes licencia imperial de cazarrecompensas. Si le capturas, no podrás cobrar la recompensa por él."
    playerName "¿Y si me dijeses a mí dónde está? ¿Perjudicaría eso a tus otros trabajos?"
    cazador "Tú podrías capturarle. No estás registrado como cazador, pero podrías estar asociado a uno de mis competidores."
    menu:
        "Nos repartiremos la recompensa.":
            playerName "Te ofrezco el 50[porcien] de la recompensa, y no tendrás que hacer nada. Sólo darme esa información."
            cazador "Pido el 72[porcien] de la recompensa, y sólo si está vivo."
            playerName "¡Oh, vamos!"
            cazador "..."
            playerName "..."
            cazador "..."
            playerName "El 66."
            cazador "..."
            playerName "Bueno, acepto."
            cazador "Thondo Qo ha sido identificado pilotando una moto-jet en los alrededores del antiguo palacio de Jabba, seis veces en los últimos nueve días. Su escondite tiene que estar en esa zona. El palacio es la única estructura relevante en el área."
            cazador "Un intento de captura en el palacio exigiría registrar el palacio, lo cual llevaría tiempo, o sacarle del palacio y posiblemente perseguirle en el cercano Mar de Dunas. Mil créditos no compensan ese tiempo."
            playerName "Gracias, 4-LOM. Esta pequeña conversación te ha hecho ganar mil créditos. Seguro que eso sí que compensa, ¿verdad?"
            cazador "Tus posibilidades de capturar a Qo son de 13 entre 36. El beneficio teórico obtenido por seguir esta política es de aproximadamente 260 créditos."
            playerName "Realmente lo tuyo es por amor al dinero, 4-LOM."
        "Renuncio a la recompensa.":
            playerName "Te quedarás toda la recompensa."
            cazador "Trato hecho."
            cazador "Thondo Qo ha sido identificado pilotando una moto-jet en los alrededores del antiguo palacio de Jabba, seis veces en los últimos nueve días. Su escondite tiene que estar en esa zona. El palacio es la única estructura relevante en el área."
            cazador "Un intento de captura en el palacio exigiría registrar el palacio, lo cual llevaría tiempo, o sacarle del palacio y posiblemente perseguirle en el cercano Mar de Dunas. Mil créditos no compensan ese tiempo."
            playerName "Gracias, 4-LOM. Esta pequeña conversación te ha hecho ganar mil créditos. Seguro que eso sí que compensa, ¿verdad?"
            cazador "Tus posibilidades de capturar a Qo son de 13 entre 36. El beneficio teórico obtenido por seguir esta política es de aproximadamente 361,11 créditos."
            playerName "Realmente lo tuyo es por amor al dinero, 4-LOM."
        "Tú dijiste que era una recompensa baja.":
            playerName "Tú dijiste que era una recompensa baja y poco prioritaria."
            cazador "Eres un duro negociador."
            cazador "Thondo Qo ha sido identificado pilotando una moto-jet en los alrededores del antiguo palacio de Jabba, seis veces en los últimos nueve días. Su escondite tiene que estar en esa zona. El palacio es la única estructura relevante en el área."
            cazador "Un intento de captura en el palacio exigiría registrar el palacio, lo cual llevaría tiempo, o sacarle del palacio y posiblemente perseguirle en el cercano Mar de Dunas. Mil créditos no compensan ese tiempo."
            playerName "Gracias, 4-LOM."
    cazador "Cuando le hayas capturado, dame una señal y yo me ocuparé de entregarle. Pero recuerda: Si intentas traicionarme, todos los cazarrecompensas del sector irán a por ti."
    playerName "Tranquilo, 4-LOM, confía en mí."
    $ hablarCazador = 1
    $ preguntarKabePorCazador = 3

    jump go_OficinaImperial

label hablarContrabandista:
    if crimelord2Activo == 3:
        contrabandista "¡Tú! ¿Esperabas esconder la verdad? ¡Has liquidado a Terrem Jesond! No sabes lo que eso significa."
    
    if saludarContrabandista == 0:
        contrabandista "¡Hola, viajer[tuO]! Está claro que tú, como yo, no eres de por aquí, ¿eh? Soy Nengih TurJinda, capitán del carguero mercante TBA {i}Tormenta de Melocotón{/i}. ¿Eres pilot[tuO] espacial?"
        playerName "No, no. Me llamo [playerName] y soy xenobiólog[tuO]. He venido a estudiar las ratas womp."
        contrabandista "¡Estupendo! Mi negocio es difícil, y desconfío de la competencia."
        $ saludarContrabandista = 1

    menu:
        "Háblame de tu trabajo" if turjindaHablaTrabajo == 0:
            playerName "¿Cómo es la vida de un contrabandista?"
            contrabandista "¿Crees que soy un contrabandista? ¡Oh, qué afrenta! Yo soy un importador legítimo en la nómina de una empresa como Transportes Ororo. Todo es legal en cada sistema que visito."
            contrabandista "Es decir, digamos que compro especia en Llanic y la vendo en Andalasa. La especia es legal en ambos mundos, no he hecho nada malo."
            contrabandista "Después en Andalasa me voy a Svivren, donde esa especie no es legal. Pero yo ya no llevo especia."
            playerName "¿Entonces para ti es moral comerciar con esclavos y otras mercancías... controvertidas?"
            contrabandista "Buena pregunta. Me caes bien. Transportes Ororo decide el cargamento del {i}Tormenta de Melocotón{/i}; la sede está en el sector Astal y hay que cumplir siempre las leyes de allí."
            contrabandista "Trabajo con comida, metales, productos químicos, tecnología, especia para fines médicos y de vez en cuando droides. Cosas así."
            playerName "¿Y no corres riesgos? Las modificaciones de tu nave me sugieren una tripulación de tres como mucho, y no mucha potencia. Tendrás encuentros con piratas o zygerranos..."
            contrabandista "O peor: Con aduaneros. No es que tenga nada que esconder, claro, pero esos trámites hacen perder mucho tiempo, y mi tiempo es valioso."
            contrabandista "Sí, ha habido... aventuras. Tiroteos. Pero esta nave no es sólo un casco bonito (que también); tiene armas pesadas añadidas. Mis problemas no suelen ser las personas."
            contrabandista "Mynocks. Cinturones de asteroides. Rutas mal cartografiadas; a veces, si puedo, actualizo los servidores corrigiendo esto. Atmósferas exóticas, ¿sabías que aquí no hay helio? ¿Cómo se les ocurre?"
            $ turjindaHablaTrabajo = 1
        "Estoy buscando un cazarrecompensas." if itemWantedPoster == 1 and hablarCazador == 0:
            contrabandista "No, esto no funciona así: Es el cazarrecompensas el que te busca a ti."
            play sound "sound/risacontrabandista.mp3"
        "¿Es Tatooine un buen puerto?" if crimelord1Activo == 0 and turjindaHablaPuerto == 0:
            playerName "¿Es Tatooine un buen puerto comercial?"
            contrabandista "Antes era mejor. Jabba el Hutt tenía sus defectos, pero sabía imponer el orden, y todos sabían quién estaba al mando."
            playerName "¿O sea, que pagabas sus sobornos?"
            contrabandista "Él era el gobernador de Tatooine. He estado en mundos en los que el mandatario tenía menos legitimidad."
            contrabandista "Desde la muerte de Jabba, varias potencias intentan hacerse con el control de Tatooine. Es un premio demasiado jugoso para dejarlo escapar."
            contrabandista "Pero hasta que alguno se imponga claramente, será complicado aterrizar en este planeta."
            playerName "¿Tienes algún favorito en esa competición?"
            contrabandista "¡Ni siquiera podría decirte quiénes participan! Pero algo tengo claro: Tendrá que ser alguien con influencia, con contactos que le respalden."
            $ turjindaHablaPuerto = 1
        "Quiero ver tu bitácora." if apalizadoPorTropas == 1 and ordenadorNav == 0:
            contrabandista "Hola, [playerName]. ¿Qué haces por aquí? ¿Quieres volver a quedar impresionad[tuO] ante la belleza del {i}Tormenta de Melocotón{/i}?"
            playerName "De hecho, sí. Hay una parte de tu nave que quiero ver en detalle."
            contrabandista "No te imaginas lo bien que está todo. ¿Qué te interesa? ¿Los motores? ¿Las torretas? ¿La cápsula de escape?"
            playerName "El cuaderno de bitácora."
            contrabandista "¿Qué?"
            playerName "El diario de navegación. El registro automático de las coordenadas que has visitado en tiempo real y las rutas seguidas entre ellas. Es información pública."
            contrabandista "Pero... ¿Por qué quieres ver eso? Será mucho más ameno si te cuento yo, en la cantina, sobre los puertos donde he estado y las damas que allí he amado bajo los soles dorados..."
            playerName "Podrías olvidarte de algo importante; y tu ordenador de a bordo no olvida nada. Es mejor que eche un vistazo a la ruta que has seguido."
            contrabandista "Mira, trabajo para Transportes Ororo, éstos son mis permisos."
            menu:
                "Ir de farol.":
                    playerName "Vamos, TurJinda, he hablado con tus superiores en Transportes Ororo. Son ellos los que quieren que alguien de fuera revise tu ruta."
                    contrabandista "No sé si creer que hayas hablado con ellos..."
                    playerName "Si quieres, les llamamos ahora mismo para preguntarles. Es decir, si no te importa molestarles para un asunto tan rutinario como enseñar algo público."
                    contrabandista "¡Oh, de acuerdo! Tú ganas. Toma este holodisco. Lo puedes ver en cualquier ordenador de navegación."
                    $ itemRutaMelocoton = 1
                    $ ordenadorNav = 1
                "Intentar confundirle.":
                    playerName "¿Has leído estas políticas? Sé que son largas y complejas, y con referencias a otros sitios; pero eso es importante."
                    playerName "Dicen que las rutas que sigues son públicas, por supuesto, y también que puedo verificarlas con tus logs de los otros sistemas. Por ejemplo, chequeando que el impacto ambiental de los mundos en tu casco se corresponde con los mundos que dices haber visitado."
                    contrabandista "¿En serio dice esto?"
                    playerName "Míralo tú mismo. Es el Decreto Imperial A-SL-7554.706.232. Me lo conozco bien, he trabajado con ellos."
                    contrabandista "No puedo creer que... Mira, si son las políticas de Transportes Ororo, no voy a discutir con ellos. Toma este holodisco. Lo puedes ver en cualquier ordenador de navegación."
                    $ itemRutaRealMelocoton = 1
                    $ ordenadorNav = 1
                "Intentar amenazarle.":
                    playerName "No me enseñes esas tonterías. Lo que quiero saber es dónde ha estado tu nave. Si no me lo enseñas a mí, quizá deba llamar a las autoridades planetarias."
                    contrabandista "Eso no me intimida. El Imperio está bastante debilitado en el Borde Exterior, [playerName]."
                    playerName "No estoy hablando del Imperio. Sabes tan bien como yo que en Tatooine gobierna el crimen organizado, y he hablado con los que dirigen el cotarro."
                    contrabandista "Me vas a meter en un lío..."
                    playerName "¿Con Transportes Ororo? Tienen pinta de ser aterradores."
                    contrabandista "Toma este holodisco. Lo puedes ver en cualquier ordenador de navegación."
                    $ itemRutaMelocoton = 1
                    $ ordenadorNav = 1
        "Dame tu bitácora real." if itemRutaMelocoton == 2 and itemRutaRealMelocoton == 0:
            playerName "Quiero ver la {i}auténtica{/i} bitácora de tu nave."
            contrabandista "No sé a qué te refieres. Ya te he dado mi bitácora."
            playerName "Me has dado un relato de ciencia-ficción, una fantasía que posiblemente escribió tu droide de a bordo."
            contrabandista "Eso me ofende: Fue mi copiloto, que es orgánico."
            playerName "¡Entonces lo admites! Quiero saber dónde ha estado realmente el {i}Tormenta de Melocotón{/i}. Quiero ver los puertos donde has atracado, ¡y hasta los nombres de los aduaneros que pisaron tu bodega!"
            contrabandista "Quizá pueda disuadirte con un poco de contrabando. Tengo una caja de peluches de Ackbar Cosquillas, muy populares..."
            playerName "En este momento, estoy tentad[tuO] a traer aquí al Imperio, a los hutts y a los moradores de las arenas para convencerte de que me digas la verdad."
            contrabandista "No pierdas los nervios, [playerName]. No te servirá de nada tener la ruta de mi nave. ¿Qué esperas averiguar?"
            playerName "De momento, he averiguado que no falsificas bien. Si intentas colarme otra mentira, lo lamentarás."
            contrabandista "*suspiro*. Toma este holodisco. Aquí está la ruta real. Pero dime, ¿cómo descubriste que la ruta era falsa?"
            playerName "Precisamente porque te esforzaste demasiado para que nada llamase la atención. Eso es demasiada casualidad."
            $ itemRutaRealMelocoton = 1
        "¿Y qué si he liquidado a Jesond?" if crimelord2Activo == 3 and conoceClawditaC < 1:
            playerName "Sí, he acabado con Terrem Jesond. ¿Y qué? ¿Tienes algún problema?"
            contrabandista "Oh, claro que lo tengo: Jesond era mi jefe. Me has metido en un buen lío. ¡Pero ni te imaginas el lío en que {i}tú{/i} estás metid[tuO]!"
            contrabandista "¿Realmente crees que has vencido a un simple señor del crimen? Jesond era mucho más que eso. Si no, no habría sobrevivido hasta ahora."
            contrabandista "¿Por qué crees que te incriminó? Él estaba devolviendo un favor a alguien realmente poderoso...{p}Más poderoso de lo que tú puedas imaginar."
            playerName "¿De qué estás hablando, TurJinda?"
            contrabandista "Los amigos de Jesond... Son gente temible. He visto lo que pueden hacer. Ellos acaban con bandas enteras, destruyen civilizaciones, asesinan a Moffs..."
            contrabandista "Mi tripulación y yo nos reunimos varias veces con su administrador, un enorme zabrak que siempre bebía siseo fotónico. Cada pronóstico que hizo... Se cumplía."
            contrabandista "Predijo la muerte del supervisor de Mimban. Me advirtió que me alejase de Anoat justo antes de la batalla de Hoth. Hasta me recomendó dejar de tratar con SoroSuub..."
            playerName "Pero... Los zabraks son de constitución muy robusta, y el siseo es una soda suave. ¡Para su organismo, eso es como beber agua!"
            contrabandista "¿Eso es lo que te parece importante? La gente que ve el futuro va a por ti, [playerName]. ¡Son los lores del sith!"
            playerName "¿Quién? ¿Darth Desolous? ¿Belia Darzu? No me hagas reír. ¡Los sith se extinguieron hace más de mil años!"
            contrabandista "¡Eso es lo que quieren que creamos! Recuerda a Darth Vader."
            $ conoceClawditaC = 1
        "Hasta luego.":
            playerName "Cielos despejados, TurJinda"
            contrabandista "No intentes usar nuestro argot, [playerName]. No te sale bien."
            jump go_OtroHangar
            pass

    jump hablarContrabandista


label hablarCrimelords:

# RECUERDA: Tenemos Vykan Fenn Crimelord 1, que captura tuskens y tiene weequays;
# Terrem Jesond Crimelord 2, que te ha liado para la investigación, y está mezclado con Clawdita, y es Sol Negro;
# y Radon el Hutt Crimelord 3 que es un hutt, y va a ser 3 la mejor opción; pretende hacer contrabando de agua.

    # "TBA: primeraVezTrastienda: %(primeraVezTrastienda)d. crimelord1Activo: %(crimelord1Activo)d. crimelord2Activo: %(crimelord2Activo)d. itemCabezaDroide: %(itemCabezaDroide)d. itemInvestigacion: %(itemInvestigacion)d."

    if crimelord1Activo < 3 and primeraVezTrastienda > 0:
        show crimelord1 at left
    if crimelord2Activo < 2 and primeraVezTrastienda > 0:
        show crimelord2
    if primeraVezTrastienda > 0:
        show crimelord3 at right


    # HAS VENCIDO A CRIMELORD 1; VARIAS OPCIONES:
    # TIENES PRUEBAS CONTRA ÉL, pero no has puesto a los tusken en su contra; NO MENCIONO A CRIMELORD2 para simplificar
    if primeraVezTrastienda == 1 and crimelord1Activo == 1 and itemCabezaDroide == 1:
        # "TBA (Tienes pruebas comprometidas contra crimelord1; pero no has puesto a los tusken en su contra)"
        crimelord3 "Hola, [playerName]. ¿Tienes algo interesante para nosotros?"
        playerName "En realidad, sí. Tengo algo que interesará a Vykan Fenn."
        "Les enseñas a todos la cabeza del droide RA-7. Fenn hace un mohín, intentando disimular que la reconoce."
        playerName "Los bancos de memoria de este droide demostrarán lo que voy a contaros. Se trata del plan de Vykan Fenn, y está grabado."
        playerName "Fenn ha estado secuestrando moradores de las arenas para venderlos como guerreros esclavos en otros planetas. Los suelta en la superficie y ellos, confusos, causan estragos."
        playerName "Mientras tanto, los weequays han seguido los rituales de su cultura matando enormes bestias, concretamente banthas. Eso ha enfurecido a los moradores, que tratan a los banthas como hermanos."
        playerName "Por eso los moradores se ha reunido para ir a la guerra contra los granjeros de humedad y posiblemente contra los jawas. Fenn aprovechará esto para vender armas a todos los bandos."
        "Mientras explica estos detalles, Fenn te lanza un pequeño objeto desde su mano."
        crimelord1 "¡Coge esto!"
        play sound "sound/explosion.mp3"
        "Instintivamente intentaste cogerlo, pero explotó cuando te tenía a quemarropa. Era una pequeña granada, ideada para matar a sólo una persona."
        "Mientras tu visión se nubla, ves a Fenn jactándose de su triunfo y oyes las palabras de Radon el Hutt:"
        crimelord3 "¿Por qué has venido a revelarnos su plan, [playerName]? Podrías habérselo contado a los moradores de las arenas, y {i}ellos{/i} habrían atacado a Fenn."
        jump HasMuerto
        return

    # LE DISTE LA CABEZA DE DROIDE A TUSKEN BOB. Crimelord1Activo = 2 porque ha muerto a manos de los tusken            
    if primeraVezTrastienda == 1 and crimelord1Activo == 2 and crimelord2Activo == 1:
        hide crimelord1
        # "TBA - LE DISTE LA CABEZA DE DROIDE A TUSKEN BOB. Crimelord1Activo = 2 ; PASA A = 3"
        crimelord2 "¡Vaya, mira quién ha venido! Supongo que debemos darte las gracias, [playerName]."
        playerName "¿A mí? ¿Por qué?"
        crimelord3 "Sabemos lo que has hecho. Has movilizado a los moradores de las arenas contra Vykan Fenn y les has mandado a su guarida secreta de Mos Gamos."
        crimelord2 "Sólo que la guarida ya no es tan secreta, claro."
        crimelord3 "Los moradores han rescatado a sus prisioneros e incluso han enviado un diplomático a las granjas de humedad a explicarles que la guerra ha terminado."
        crimelord2 "El diplomático tusken atacó a los granjeros, pero un segundo embajador les ha convencido de que todo es un malentendido."
        crimelord3 "Pareces decidid[tuO] a traer la paz a Tatooine. En cuanto lo hayas conseguido, yo traeré la prosperidad."
        crimelord2 "Eso será si te libras de mí antes, claro."
        crimelord3 "No lo dudes, Jesond: Lo haré."
        $ crimelord1Activo = 3
        jump go_Trastienda

    # ÍDEM PERO YA ESTÁ MUERTO CRIMELORD2.
    if primeraVezTrastienda == 1 and crimelord1Activo == 2 and crimelord2Activo > 1:
        hide crimelord1
        # "TBA - con Jesond muerto, LE DISTE LA CABEZA DE DROIDE A TUSKEN BOB. Crimelord1Activo = 2 ; PASA A = 3 Y TÚ A FINAL"
        crimelord2 "Bienvenid[tuO], [playerName]. Sé lo que has hecho. Has movilizado a los moradores de las arenas contra Vykan Fenn y les has mandado a su guarida secreta de Mos Gamos."
        crimelord3 "Sólo que la guarida ya no es tan secreta, claro."
        crimelord3 "Los moradores han rescatado a sus prisioneros e incluso han enviado un diplomático a las granjas de humedad a explicarles que la guerra ha terminado."
        crimelord3 "El diplomático tusken atacó a los granjeros, pero un segundo embajador les ha convencido de que todo es un malentendido."
        crimelord3 "Pareces decidid[tuO] a traer la paz a Tatooine. En cuanto lo hayas conseguido, yo traeré la prosperidad."
        $ crimelord1Activo = 3
        jump hasVencidoAAmbosCrimelords

    # HAS VENCIDO A CRIMELORD 2; DOS OPCIONES
    # Has convencido a CRIMELORD 2 en la cantina y ahora entras en la trastienda
    if primeraVezTrastienda == 1 and informacionImplicaCrimelord2 == 1 and crimelord2Activo == 2:
        if crimelord1Activo < 3:
            # "TBA: 1-?-2 Has convencido a CRIMELORD 2 en la cantina y ahora entras en la trastienda (PASA DE 2 A 3). Fenn está ACTIVA."
            show crimelord1 at left
            hide crimelord2
            show crimelord3 at right
            crimelord3 "Ah, mira quién ha venido. Tu trabajo empieza a funcionar."
            crimelord1 "Terrem Jesond nos ha enviado un mensaje. Dice que renuncia a Tatooine según lo acordado; mañana no quedará ni una de sus naves aquí. No ha dicho porqué se va."
            crimelord3 "Lee entre líneas, Vykan Fenn. Nuestr[tuO] fiel [playerName] ha descubierto algo vergonzoso sobre Jesond, y él ha decidido que prefiere huir antes que permitir que lo sepamos."
            crimelord1 "No me quejo, Hutt. Ahora sólo quedamos tú y yo... y pronto, sólo quedaré yo."
            crimelord3 "Tú nunca vencerás, Fenn. Pero, cuando caigas, quizá [playerName] quiera extender su tiempo de servicio a los hutts..."
        else:
            # "TBA: 1-?-2 Has convencido a CRIMELORD 2 en la cantina y ahora entras en la trastienda (PASA DE 2 A 3). Fenn está MUERTA."
            crimelord3 "Ah, mira quién ha venido. Tu trabajo ha sido un éxito."
            crimelord3 "Terrem Jesond nos ha enviado un mensaje. Dice que renuncia a Tatooine según lo acordado; mañana no quedará ni una de sus naves aquí. No ha dicho porqué se va."
            crimelord3 "Claramente has descubierto algo vergonzoso sobre Jesond, y él ha decidido que prefiere huir antes que enfrentarse a mi ira."
            hide crimelord1
            hide crimelord2
            show crimelord3
        $ crimelord2Activo = 3
        if crimelord1Activo == 3:
            jump hasVencidoAAmbosCrimelords
        jump go_Trastienda
 
    # Si estás en la TRASTIENDA, y AÚN NO HAS DELATADO AL CRIMELORD 2, Y LE HABLAS EN TRASTIENDA
    if primeraVezTrastienda == 1 and informacionImplicaCrimelord2 == 1 and crimelord2Activo == 1:
        "TBA 1-x-1 InfoImplicaCrimelord2 1 - AÚN NO HAS DELATADO AL CRIMELORD 2, Y LE HABLAS EN TRASTIENDA. ÉL ESTÁ A 1; INFOIMPLICA 1"
        crimelord2 "Bienvenido, [playerName]. He sabido que me has estado investigando. Por supuesto, estoy tranquilo."
        if crimelord1Activo < 3:
            crimelord1 "¿Qué ha pasado, Jesond?"
        else:
            crimelord3 "¿Qué ha pasado, Jesond?"
        crimelord2 "[playerName] ha investigado las rutas que siguen mis naves, las naves de Transportes Ororo. Sin duda habrá visto que todo es muy razonable."
        playerName "Bueno, la ruta pública es... mundana. Una nave no puede ganar dinero con ese comercio, ni siquiera con contrabando."
        crimelord2 "Quizá haya un interés estratégico en hacer esos movimientos. Por supuesto, no sé nada sobre el contrabando que puedan hacer mis capitanes."
        playerName "Por el contrario, la ruta {b}real{/b} es mucho más interesante. Tiene relación con muchos de tus amigos, Jesond, e incluso me dice quiénes son."
        crimelord2 "¿Qué?{p}¿De qué hablas? Las rutas que tengo son..."
        crimelord3 "Déjale hablar, Jesond. Quiero saber eso."
        if crimelord1Activo < 3:
            crimelord1 "Sí, Jesond. Yo también estoy interesada."
        playerName "Sospecho que he descubierto incluso qué le pasó al grupo de Vasail Tai. Tu carguero con armamento pesado se pasó por Kamino antes de venir, y no parece que haya cambiado su carga allí. Más bien creo que sirvió de cañonera contra sus instalaciones."
        crimelord3 "¿Es eso cierto, Jesond?"
        playerName "No sólo eso. La nave pasó además por Ryloth y Hypori. Todos esos sistemas pertenecieron al Consorcio Zann hasta su disolución."
        if crimelord1Activo < 3:
            crimelord1 "Yo había oído que Sol Negro absorbió al Consorcio Zann."
        else:
            crimelord3 "Yo había oído que Sol Negro absorbió al Consorcio Zann."
        playerName "Creo que todavía hay resistencia entre los antiguos Zann. Después de todo, Sol Negro lleva tambaleándose desde la muerte de Xizor el año pasado, ¿no?"
        crimelord2 "¡Sol Negro es una leyenda! Un cuento de hadas. Soy un empresario legítimo con intereses..."
        playerName "...en Svivren y Qiaxx, dos mundos controlados por uno de los herederos de Xizor: Dequc, de la Nébula Negra."
        crimelord3 "Ésa es una apuesta audaz, Jesond. Mantienes el control de las rutas mientras tus amigos sean poderosos. Pero tus amigos son Sol Negro, y su poder se ha debilitado."
        if crimelord1Activo < 3:
            crimelord1 "Ese poder se está debilitando por momentos. Los señores de la guerra imperiales van a intentar hacerse con esos sistemas. Si Sol Negro los tiene que defender, no podrá ayudarte."
        else:
            crimelord3 "Ese poder se está debilitando por momentos. Los señores de la guerra imperiales van a intentar hacerse con esos sistemas. Si Sol Negro los tiene que defender, no podrá ayudarte."
        crimelord2 "Si afianzo el control sobre Tatooine, entonces formaré una cabeza de puente estable. Ellos podrán apoyarme y yo les apoyaré a ellos..."
        crimelord3 "¿Qué opinas tú, [playerName]?"
        menu:
            "Muerte a Jesond.":
                if crimelord1Activo < 3:
                    playerName "Jesond se ha pasado de listo. Unos jefes del cri... Quiero decir, unos empresarios respetables como vosotros no podéis permitir que ese insulto quede impune. Os haría parecer débiles."
                    crimelord3 "Desde luego, eso no es algo que deseemos."
                else:
                    playerName "Jesond se ha pasado de listo. Un jefe del cri... Quiero decir, un respetable empresario hutt no puede permitir que ese insulto quede impune. Te haría parecer débil."
                    crimelord3 "Desde luego, eso no es algo que yo desee."
                playerName "Si le dejais ir y logra salir adelante, quizá vuelva en unos años, buscando venganza. Es demasiado peligroso para dejarle vivir."
                crimelord2 "¿Qué? Espera... No..."

                if crimelord1Activo < 3:
                    crimelord1 "Tienes razón, [playerName]. Es mejor que nos ocupemos de este asunto aquí y ahora."
                    "De entre los pliegues de su capa, Fenn extrae una pistola bláster de bolsillo, cromada, elegante y discreta. Con un gesto perfectamente practicado, eleva su brazo y apunta a la cabeza de Jesond..."
                else:
                    crimelord3 "Tienes razón, [playerName]. Es mejor que me ocupe de este asunto aquí y ahora."
                    "Radon el Hutt mete su mano entre los pliegues de su piel y de su interior saca una enorme pistola blaster pesada, tan sucia y viscosa como lo está él. Alza su pequeño brazo y dispara a Jesond."
                    play sound "sound/blaster.mp3"
                    with flash
                    "El disparo chamusca la pared, pasando inofensivamente a treinta centímetros de la cabeza de Jesond. El koorivar respira aliviado, pero entonces Radon vuelve a disparar y le da en el estómago."
                play sound "sound/blaster.mp3"
                with flash
                hide crimelord2
                crimelord3 "Buen trabajo, [playerName]. Estoy contento contigo."
                $ crimelord2Activo = 3
            "Exilio para Jesond.":
                if crimelord1Activo < 3:
                    playerName "Jesond se ha pasado de listo. Unos jefes del cri... Quiero decir, unos empresarios respetables como vosotros no podéis permitir que ese insulto quede impune. Os haría parecer débiles."
                    crimelord3 "Desde luego, eso no es algo que deseemos."
                else:
                    playerName "Jesond se ha pasado de listo. Un jefe del cri... Quiero decir, un respetable empresario hutt no puede permitir que ese insulto quede impune. Te haría parecer débil."
                    crimelord3 "Desde luego, eso no es algo que yo desee."
                playerName "Pero, si sus supuestos amigos son tan poderosos como él dice, ellos se podrían enfadar si Jesond tiene un... {i}accidente{/i}."
                if crimelord1Activo < 3:
                    "Fenn ya estaba metiendo una mano dentro de su capa, posiblemente para desenfundar un arma. Se detiene cuando dices esto."
                playerName "Si Jesond acepta retirarse de Tatooine definitivamente, para siempre, creo que todos podemos darnos por satisfechos, ¿verdad?"
                if crimelord1Activo < 3:
                    playerName "Vosotros os librais de un competidor por el control del planeta, y Jesond sale de aquí con vida."
                else:
                    playerName "Radon se libra del último competidor por el control del planeta, y Jesond sale de aquí con vida."
                crimelord3 "Me parece...{p}aceptable. Quizá algún día Jesond pueda hacer algo por los hutts. Lo permito."
                if crimelord1Activo < 3:
                    crimelord1 "Es menos que perfecto, pero me parece bien."
                hide crimelord1
                hide crimelord3
                crimelord2 "¡Gracias, [playerName]! Podrías haber acabado conmigo, pero no lo has hecho. Te recompensaré."
                crimelord2 "Yo lancé la investigación abierta sobre el {i}[tuNave]{/i}. Una mujer muy peligrosa me pidió que lo hiciese para perjudicarte."
                crimelord2 "Tienes enemigos, [playerName]. Enemigos formidables. No sé qué has hecho para enfadarles, pero ahora estás perdid[tuO]. ¡Nadie puede con gente así!"
                crimelord2 "Esa mujer es invencible. Puede llegar a todas partes. Puede nublar tu mente para que olvides haberles visto. ¡Puede matar con un pensamiento! ¡Lo he visto con mis propios ojos!"
                playerName "¿Si ella es tan poderosa, por qué te necesita?"
                crimelord2 "¡Tú no lo comprendes! Si alguien así te dice que perjudiques a otro incautando su nave, ¡no haces preguntas! ¡Obedeces!"
                crimelord2 "Pero: Tú ganas. Haré que retiren la investigación en seguida. Lamento las molestias causadas y: Que nuestros caminos nunca vuelvan a cruzarse."
                hide crimelord2
                if crimelord1Activo < 3:
                    show crimelord1 at left
                show crimelord3 at right
                $ itemInvestigacion = 1
                $ crimelord2Activo = 3
            "Colaboración con Jesond.":
                playerName "Creo que es posible... colaborar con Jesond."
                crimelord3 "¿Cómo?"
                playerName "Jesond ya se ha caido fuera de la competición. No puede ser el amo de Tatooine. Pero puede asociarse con el amo de Tatooine."
                playerName "Nadie se beneficia con las guerras de bandas. Si Jesond muere, el territorio de la Nébula Negra arderá, será un caos. Pero: Si Jesond tiene un acuerdo con el amo de Tatooine, quizá todos salgan ganando."
                if crimelord1Activo < 2:
                    crimelord3 "Escucha, [playerName]: Jesond se ha pasado de listo. Si Fenn y yo permitimos que ese insulto quede impune, entonces pareceremos débiles, y eso no nos lo podemos permitir."
                    crimelord1 "Es una lástima. Yo propuse que [playerName] nos ayudase. Está claro que me equivoqué. [tuPronombreMayus] no está a la altura de lo que necesitamos."
                    crimelord3 "Está claro lo que tenemos que hacer, Fenn."
                    "De entre los pliegues de su capa, Fenn extrae una pistola bláster de bolsillo, cromada, elegante y discreta. Con un gesto perfectamente practicado, eleva su brazo y apunta a la cabeza de Jesond."
                    play sound "sound/blaster.mp3"
                    with flash
                    hide crimelord2
                    "El cuerpo sin vida de Jesond cae al suelo, pero Fenn no le dedica una segunda mirada. Apenas ha pasado una fracción de segundo y ella ha movido su arma hacia ti. Su rostro es una máscara estoica que ni dice ni permite unas últimas palabras. Te dispara directamente a la cabeza."
                    play sound "sound/blaster.mp3"
                    with flash
                    jump HasMuerto
                    return
                else:
                    crimelord3 "Escucha, [playerName]: Jesond se ha pasado de listo. Si permito que ese insulto quede impune, entonces pareceré débil, y eso no me lo puedo permitir."
                    "Mientras habla, Radon el Hutt mete su mano entre los pliegues de su piel y de su interior saca una enorme pistola blaster pesada, tan sucia y viscosa como lo está él. Alza su pequeño brazo y dispara."
                    play sound "sound/blaster.mp3"
                    with flash
                    "El plasma chamusca la pared, pasando inofensivamente entre Jesond y tú. El koorivar respira aliviado, pero entonces Radon vuelve a disparar y te da en el estómago."
                    play sound "sound/blaster.mp3"
                    with flash
                    "Caes al suelo agonizante. Tu visión se nubla y tus oídos dejan de funcionar. No llegas a oír el siguiente disparo de Radon, pero sospechas que le ha dado a Jesond. Para entonces, el dolor es tan intenso que ya no importa..."
                    play sound "sound/nada.mp3"
                    with flash
                    jump HasMuerto
                    return
        if crimelord1Activo == 3:
                jump hasVencidoAAmbosCrimelords
        jump go_Trastienda

    # HAS ESTADO AQUÍ, VUELVES PERO AÚN NO TIENES NADA; ME DA LO MISMO QUE TE HAYAS CARGADO O NO AL 2
    if primeraVezTrastienda == 1 and crimelord1Activo < 3:
        "TBA: 1-1-1 HAS ESTADO AQUÍ, VUELVES PERO AÚN NO TIENES NADA"
        crimelord3 "Hola, [playerName]. ¿Tienes algo interesante para nosotros?"
        playerName "Todavía no."
        crimelord1 "Vuelve a vernos cuando tengas algo que contar."
        jump go_Trastienda
        
    # HAS ESTADO AQUÍ, VUELVES PERO AÚN NO TIENES NADA; TE HAS CARGADO YA AL CRIMELORD 1        
    if primeraVezTrastienda == 1 and crimelord1Activo == 3 and crimelord2Activo < 3:
        "TBA 1-2-1 HAS ESTADO AQUÍ, VUELVES PERO AÚN NO TIENES NADA; TE HAS CARGADO YA AL CRIMELORD 1"
        crimelord3 "Hola, [playerName]. ¿Tienes algo interesante para nosotros?"
        playerName "Todavía no."
        crimelord2 "Vuelve a vernos cuando tengas algo que contar."
        jump go_Trastienda



    # CONVERSACIÓN INICIAL    
    # Ésta es la conversación inicial - que tiene que ir al final
    if primeraVezTrastienda == 0 and crimelord1Activo < 2:
        "0-<1-?"  
        # Crimelord 1 activo; Crimelord 2 activo. 0 no los conoces; 1 les conoces y están activos. 2 has eliminado a ese.
        # (Así que en el primer diálogo pasan a Crimelord1 Activo = 1)
        # "TBA: CONVERSACIÓN INICIAL"
        scene bg trastienda humo3
        with dissolve
        $ renpy.pause(1)
        scene bg trastienda humo2
        with dissolve
        $ renpy.pause(1)
        scene bg trastienda humo1
        with dissolve
        $ renpy.pause(1)
        "Al entrar en la trastienda, sientes en la cara un golpe de humedad como no habías sentido desde que aterrizaste en este planeta desértico."
        "La sorpresa continúa cuando observas que la atmósfera está perfumada. Quienquiera que esté aquí dentro no repara en gastos para su comodidad. Con dificultad vislumbras que hay varias personas..."
        show crimelord2 with dissolve
        "En el centro de la habitación ves a un reptiliano de Kooriva, el mundo corporatocrático. Los comerciantes koorivars son astutos, oportunistas e implacables que negociaron con el Senado Galáctico hasta que se les concedió un nuevo mundo."
        "Se han ganado un nicho en la sociedad a base de comprar barato en un mundo y vender caro en otro, sin preocuparse de si su mercancía es moralmente aceptable. Ahora mismo este koorivar parece estar negociando con alguien..."
        koorivar "No es sólo porque yo controle las rutas hiperespaciales. No sólo tengo las naves, las empresas navieras y los armadores. Tengo los contactos que me protegen."
        show crimelord1 at left with dissolve
        "El koorivar está hablando con una humanoide calva, demacradamente pálida. Reconoces su origen: Es del oscuro planeta Umbara, en la Nébula Fantasma. ¿Qué puede haberla traído al soleado Tatooine, cuando los umbaranos rehúyen la luz?"
        "Ambición, quizá: Muchos umbaranos ansían el poder, como Darth Ruin. Él no fue el único caso en que estos manipuladores inescrutables apoyaron a los sith."
        umbarana "¿Estás buscando una guerra de bandas, mercader? Porque yo estoy preparada para eso si hace falta. Tatooine es un territorio demasiado valioso para que me retire."
        show crimelord3 at right with dissolve
        "No habías visto hasta ahora, sorprendentemente, al tercer ocupante de la sala. Debía estar oculto tras el vapor, porque es una babosa verde de cuatro metros, con una boca que podría devorar las cabezas de los otros dos, y un vozarrón que hace temblar edificios."
        "Tu mente automáticamente repasa lo que sabes de la especie: Gastrópodos hermafroditas, poderosos y expansionistas, megalómanos que se ven más allá de la moral... pero en este caso, no es un mero estudio abstracto. La fama de la raza les precede: Es un hutt."
        hutt "Nadie quiere un conflicto abierto, Fenn. Así nos arriesgaríamos a destruir el botín que queremos robar: Las instalaciones en ruinas, los agentes dispersos huyendo..."
        "La mujer umbarana escucha al hutt con el ceño fruncido, pero sus pupilas rápidamente se desvían lateralmente hasta enfocarte a ti."
        umbarana "¡Un momento! ¿Quién es [tuEse]?"
        "Los otros dos te miran y se acercan un paso hacia ti."
        hutt "Sí. ¿Quién eres tú, y cómo has entrado?"
        playerName "No se preocupen ustedes, ya me iba..."
        play sound "sound/clicpuerta.ogg"
        "Ese sonido es la puerta cerrándose automáticamente a tu espalda antes de que puedas salir."
        koorivar "Tú no te vas a ninguna parte hasta que respondas."
        playerName "Yo... Soy [playerName], [tuUn] xenobiólog[tuO] de paso. Acabo de ganar un juego de azar a Vasail Tai y me dijo que entrase..."
        umbarana "¿Qué?"
        hutt "¡Ese imbécil de Tai! Ha creído que [tuEste] viajer[tuO] espacial es una cuarta potencia y le ha dejado pasar."
        umbarana "Su historia no tiene sentido. Lo mejor es matarl[tuO] y olvidarnos del tema."
        koorivar "Oh, yo doy fe. Sé de una Universidad que organizó un viaje a Tatooine para estudiar las ratas womp."
        playerName "¿Cómo sabes eso?"
        koorivar "Nada vuela por las rutas hiperespaciales de Tatooine sin que Terrem Jesond se entere. {i}Nada.{/i}"
        umbarana "Si no [tuLe] vamos a matar, tenemos que encontrar[tuLe] uso, y se me ocurre una idea."
        umbarana "Estamos en un punto muerto. Necesitamos a alguien de fuera que tome la decisión final."
        crimelord2 "Ah. ¿Sugieres que intentemos intimidar[tuLe] y que nos diga cuál de los tres le da más miedo?"
        umbarana "No seas necio. [tuPronombreMayus] es [tuUn] [tuEmpollon], ¿no? Le daremos nuestros argumentos, [tuPronombre] investigará y demostrará quién de nosotros está mejor preparado para el... puesto."
        crimelord2 "Es una idea... peculiar."
        hutt "Es una opción, Jesond. Ninguno de nosotros renunciará a Tatooine por sí mismo. Ninguno aceptará una alianza con otro. Ninguno puede vencer a los otros dos fácilmente."
        crimelord2 "Esto sólo funcionará si los tres aceptamos la decisión final de [playerName]. Los dos que pierdan, deben renunciar al control de Tatooine."
        umbarana "Acepto."
        hutt "Yo también."
        playerName "¿Me podríais explicar dónde me he metido?"
        umbarana "Posiblemente acabas de aceptar el trabajo más peligroso de tu vida, [playerName]."
        hutt "Desde la muerte del llorado Jabba, su imperio comercial ha quedado en el aire. Nadie controla el mercado de Tatooine. Eso perjudica a todos, especialmente a la gente de Tatooine."
        hutt "Esos pobres desdichados necesitan un líder que les controle, que controle todo lo que Tatooine puede ofrecer. Alguien con poder, para que todos le obedezcan."
        umbarana "Cuanto más tardemos, peor será. Su palacio ya ha caído en manos de los monjes. Algunos tenientes de Jabba intentan hacerse con piezas de su dominio; pero eso será peor. Esto exige oligarquía."
        crimelord2 "Nosotros tres somos los más preparados para ese puesto, los únicos que hemos llegado con vida a la fase final. Pero sólo uno puede tomar este premio."
        umbarana "Y finalmente seré yo: Soy Vykan Fenn de la Nébula Fantasma. Sólo yo tengo la fuerza para traer estabilidad a Tatooine."
        crimelord2 "Pero soy yo, Terrem Jesond, quien controla el transporte, tanto las rutas como las aduanas. La fuerza no mantendrá el control."
        hutt "Jesond ni siquiera imagina las rutas al alcance de los hutts. Radon el Hutt traerá al fin la prosperidad a este desdichado planeta."
        $ crimelord1Activo = 1
        $ crimelord2Activo = 1
        jump primeraCharlaCrimelords
    
    elif primeraVezTrastienda == 0 and crimelord1Activo == 2:
        "0-<1-2"  
        # HAS VENCIDO A Crimelord 1 antes de entrar en la trastienda
        # "TBA: CONVERSACIÓN INICIAL PERO SIN CRIMELORD 1"
        scene bg trastienda humo3
        with dissolve
        $ renpy.pause(1)
        scene bg trastienda humo2
        with dissolve
        $ renpy.pause(1)
        scene bg trastienda humo1
        with dissolve
        $ renpy.pause(1)
        "Al entrar en la trastienda, sientes en la cara un golpe de humedad como no habías sentido desde que aterrizaste en este planeta desértico."
        "La sorpresa continúa cuando observas que la atmósfera está perfumada. Quienquiera que esté aquí dentro no repara en gastos para su comodidad."
        show crimelord2 with dissolve
        "En el centro de la habitación ves a un reptiliano de Kooriva, el mundo corporatocrático. Los comerciantes koorivars son astutos, oportunistas e implacables que negociaron con el Senado Galáctico hasta que se les concedió un nuevo mundo."
        "Se han ganado un nicho en la sociedad a base de comprar barato en un mundo y vender caro en otro, sin preocuparse de si su mercancía es moralmente aceptable. Ahora mismo este koorivar parece estar negociando con alguien..."
        koorivar "No es sólo porque yo controle las rutas hiperespaciales. No sólo tengo las naves, las empresas navieras y los armadores. Tengo los contactos que me protegen."
        show crimelord3 at right with dissolve
        "No habías visto hasta ahora, sorprendentemente, al tercer ocupante de la sala. Debía estar oculto tras el vapor, porque es una babosa verde de cuatro metros, con una boca que podría devorar las cabezas de los otros dos, y un vozarrón que hace temblar edificios."
        "Tu mente automáticamente repasa lo que sabes de la especie: Gastrópodos hermafroditas, poderosos y expansionistas, megalómanos que se ven más allá de la moral... pero en este caso, no es un mero estudio abstracto. La fama de la raza les precede: Es un hutt."
        hutt "Tatooine es un territorio demasiado valioso para que me retire, mercader. Si intentamos forzar la situación, nos arriesgaríamos a destruir el botín que queremos robar: Las instalaciones en ruinas, los agentes dispersos huyendo..."
        "El koorivar escucha al hutt frunciendo su frente escamosa, pero sus pupilas amarillas rápidamente se desvían hasta enfocarte a ti."
        koorivar "¡Un momento! ¿Quién es [tuEse]?"
        "El hutt también te mira y repta un paso hacia ti."
        hutt "Sí. ¿Quién eres tú, y cómo has entrado?"
        playerName "No se preocupen ustedes, ya me iba..."
        play sound "sound/clicpuerta.ogg"
        "Ese sonido es la puerta cerrándose automáticamente a tu espalda antes de que puedas salir."
        koorivar "Tú no te vas a ninguna parte hasta que respondas a las preguntas."
        playerName "Yo... Soy [playerName], [tuUn] xenobiólog[tuO] de paso. Acabo de ganar un juego de azar a Vasail Tai y me dijeron que entrase..."
        koorivar "¿Qué?"
        hutt "¡Ese imbécil de Tai! Ha creído que [tuEste] viajer[tuO] espacial es una cuarta potencia y le ha dejado pasar."
        koorivar "Oh, yo doy fe. Sé de una Universidad que organizó un viaje a Tatooine para estudiar las ratas womp."
        playerName "¿Cómo sabes eso?"
        koorivar "Nada vuela por las rutas hiperespaciales de Tatooine sin que Terrem Jesond se entere. {i}Nada.{/i}"
        hutt "Si no [tuLe] vamos a matar, tenemos que encontrar[tuLe] uso, y se me ocurre una idea."
        hutt "Estamos en un punto muerto. Necesitamos a alguien de fuera que tome la decisión final."
        crimelord2 "Ah. ¿Sugieres que intentemos intimidar[tuLe] y que nos diga cuál de los dos le da más miedo?"
        hutt "No seas necio. [tuPronombreMayus] es [tuUn] [tuEmpollon], ¿no? Le daremos nuestros argumentos, [tuPronombre] investigará y demostrará quién de nosotros está mejor preparado para el... puesto."
        crimelord2 "Es una opción. Ninguno de nosotros renunciará a Tatooine por sí mismo. Ninguno aceptará una alianza con el otro. Ninguno puede vencer al otro fácilmente."
        crimelord2 "Pero esto sólo funcionará si ambos aceptamos la decisión final de [playerName]. El que pierda debe renunciar al control de Tatooine."
        hutt "Acepto."
        playerName "¿Me podríais explicar dónde me he metido?"
        crimelord2 "Posiblemente acabas de aceptar el trabajo más peligroso de tu vida, [playerName]."
        hutt "Desde la muerte del llorado Jabba, su imperio comerfcial ha quedado en el aire. Nadie controla el mercado de Tatooine. Eso perjudica a todos, especialmente a la gente de Tatooine."
        hutt "Esos pobres desdichados necesitan un líder que les controle, que controle todo lo que Tatooine puede ofrecer. Alguien con poder, para que todos le obedezcan."
        crimelord2 "Cuanto más tardemos, peor será. Su palacio ya ha caído en manos de los monjes. Algunos tenientes de Jabba intentan hacerse con piezas de su dominio; pero eso será peor. Esto exige oligarquía."
        hutt "Nosotros dos somos los más preparados para ese puesto, los únicos que hemos llegado con vida a la fase final. Pero sólo uno puede tomar este premio."
        crimelord2 "Pero soy yo, Terrem Jesond, quien controla el transporte, tanto las rutas como las aduanas. La fuerza no mantendrá el control."
        hutt "Jesond ni siquiera imagina las rutas al alcance de los hutts. Radon el Hutt traerá al fin la prosperidad a este desdichado planeta."
        $ primeraVezTrastienda = 1
        $ crimelord2Activo = 1
        jump primeraCharlaCrimelords

    if primeraVezTrastienda == 1 and crimelord1Activo == 3 and crimelord2Activo == 3:
        "1-2-2 ItemInvestigacion = 1"  
        hide crimelord1
        hide crimelord2
        show crimelord3
        crimelord3 "Ah, [playerName]. ¿Has venido a deleitarte contemplando la grandeza de Radon el Hutt?"
        if conoceClawditaB == 0:
            playerName "Hay una cosa que me reconcome. ¿Quién tenía interés en dejarme varad[tuO] aquí? ¿Quién abrió esa investigación contra mi nave?"
            crimelord3 "La abrió Terrem Jesond moviendo sus hilos, pero alguien más movía los hilos de Jesond en ese momento."
            crimelord3 "Uno de los contactos de Jesond le pidió que lo hiciera. Jesond la describía como una mujer humanoide invencible con poderes sobrenaturales del lado oscuro."
            playerName "¿El lado oscuro... de la Fuerza?"
            crimelord3 "Los hutts somos más poderosos que esa vanagloriada Fuerza. Fuimos anteriores a los jedi y a los sith, y vimos el final de ambos. No nos intimida esa mujer."
            crimelord3 "Si lo que cuentan de ella es cierto, no me imagino qué pretendía hacer una persona con esos poderes asociándose con un don nadie como Jesond."
            playerName "¿Qué cuentan de ella? ¿Algo que pueda revelar porqué va a por mí?"
            crimelord3 "Dicen que puede ver el futuro, hacer que las personas la olviden y matar con la mente como Darth Vader. Pero no sé qué busca de ti. Quizá debas tener cuidado con los amigos que haces, [playerName]."
            playerName "Gracias, Radon. Seguiré mi camino."
            $ conoceClawditaB = 1

    jump go_Trastienda
    
label hasVencidoAAmbosCrimelords:
    if primeraVezTrastienda > 0:
        "1-3-3 ItemInvestigacion = 0"  
    hide crimelord1
    hide crimelord2
    # con esto Radon aparece en el centro
    hide crimelord3
    show crimelord3
    playerName "Bueno, hasta aquí hemos llegado, Radon. Ahora eres el indiscutible amo de Tatooine."
    crimelord3 "Yo soy un humilde importador de especia que representa a los poderosos hutts. Sus intereses legítimos cuidarán de Tatooine. Eso es lo mejor para todos."
    if itemInvestigacion == 1:
        playerName "No voy a discutírtelo, Radon. Fenn y Jesond tenían demasiados trapos sucios."
        jump go_Trastienda
    else:
        playerName "No voy a discutírtelo, Radon. Fenn y Jesond tenían demasiados trapos sucios.{p}Pero me gustaría pedirte algo."
        crimelord3 "La magnificencia de los hutts es casi tan grande como su ira. Habla, [playerName]."
        playerName "El Imperio mantiene una investigación abierta sobre mi nave, el [tuNave]. Sospecho que es cosa de uno de tus competidores, porque soy inocente."
        play sound "sound/risahutt.mp3"
        crimelord3 "¡Claro que lo eres!"
        playerName "Quizá podrías usar tu influencia para... agilizar el asunto y que retiren la investigación... En pago por los servicios que he prestado a los hutts."
        crimelord3 "¿Por qué deberían los hutts malgastar sus riquezas y su tiempo en ayudar a un insignificante mamífero como tú?"
        menu:
            "Te resultará barato.":
                playerName "Lo que pido es algo sencillo, costará poco a los poderosos hutts."
                crimelord3 "Quizá, pero esto costará aún menos."
                "Mientras habla, Radon el Hutt mete su mano entre los pliegues de su piel y de su interior saca una enorme pistola blaster pesada, tan sucia y viscosa como lo está él. Alza su pequeño brazo y dispara."
                play sound "sound/blaster.mp3"
                with flash
                "Caes al suelo agonizante. Tu visión se nubla y tus oídos dejan de funcionar. Radon se asegura de tu muerte con un segundo disparo."
                play sound "sound/nada.mp3"
                with flash
                jump HasMuerto
                return
            "Glorificará el poder de los hutt.":
                playerName "Cuando se sepa que he servido a los hutts y he recibido lo que yo buscaba, mejorará vuestra reputación y animará a otros a servir a los hutts."
                playerName "Todos sabrán que los hutts cumplen su palabra cuando dicen a un sirviente 'Serás recompensado'."
                crimelord3 "Tienes... razón.{p}Me ocuparé de que se retire la investigación del [tuNave], [playerName]. Quizá el [tuNave] deba servir también a los hutts."
                $ itemInvestigacion = 1
                # No te ha matado
                jump go_Trastienda


label primeraCharlaCrimelords:
    if crimelord1Activo < 2 and primeraVezTrastienda > 0:
        show crimelord1 at left
    if crimelord2Activo < 2 and primeraVezTrastienda > 0:
        show crimelord2
    if primeraVezTrastienda > 0:
        show crimelord3 at right
    menu:
        "Hablar con Vykan Fenn." if crimelord1Activo <2 and saludarFenn == 0:
            hide crimelord1
            hide crimelord2
            hide crimelord3
            show crimelord1 at center
            playerName "¿Por qué debería apoyar a la Nébula Fantasma?"
            crimelord1 "¿Por qué, me preguntas? ¿Acaso no hay prosperidad en Umbara, con todos los conflictos en que hemos participado? ¿No somos un mundo rico?"
            playerName "Lo sois, a base de arrimaros al sol que más calienta. Vuestros Asesinos Sombra apoyaron a los sith, pero se pasaron a la República cuando los jedi vencieron. Fuisteis separatistas en las Guerras Clon, y cuando vuestro bando perdió, os faltó tiempo para apoyar al Imperio."
            crimelord1 "¡Exacto! Eso demuestra que siempre comprendemos dónde está el poder. Las facciones vienen y van, la supremacía cambia, pero Umbara siempre obtiene beneficio. Por eso Umbara es el amigo que necesita Tatooine."
            playerName "{i}(Hasta que dejes de necesitar a Tatooine...){/i}"
            crimelord1 "¿Qué has dicho?"
            playerName "He dicho... He dicho que la Nébula está muy lejos. ¿Cuál es esa fuerza que dices tener para controlar Tatooine? Quiero decir, para {i}defender{/i} Tatooine."
            crimelord1 "Los Clanes. Tengo a mi disposición tropas mercenarias de las más brutales especies alienígenas, dispuestas a derramar su sangre, y la de otros, por mi causa."
            playerName "¿Los Clanes? Klatooinianos, niktos, vodranos, weequays, whífidos... Son poderosos, pero sus culturas son muy distintas al estándar. Suele ser complicado controlarles sin un buen liderazgo."
            crimelord1 "Mis oficiales droides no me han fallado hasta ahora. ¡Han dirigido a los Clanes en victorias contra los Rifleros de Churhee en Sarin, contra los Irregulares de Láramus en Parmic y contra los piratas de Urias Xhaxin en el Borde Medio!"
            playerName "¿Son todos tus enemigos son agentes de la Alianza Rebelde como esos tres? ¿Qué podrán hacer tus mercenarios contra el Imperio?"
            crimelord1 "¿Qué Imperio? Palpatine está muerto, y ahora sus carroñeros se repartirán sus restos. Prepárate para ver a los Moffs y Almirantes como señores de la guerra guerreando entre sí por un par de sistemas prioritarios."
            crimelord1 "El Imperio no sabe actuar cuando falla la disciplina, ¡y yo controlo a las fuerzas del caos!"
            "Desde luego, Vykan Fenn tiene confianza en sus capacidades, y sus gestos amedrentan."
            $ saludarFenn = 1
            hide crimelord1
            if crimelord1Activo < 2:
                show crimelord1 at left
            if crimelord2Activo < 2:
                show crimelord2
            show crimelord3 at right
            jump primeraCharlaCrimelords
        "Hablar con Terrem Jesond." if saludarJesond == 0:
            hide crimelord1
            hide crimelord2
            hide crimelord3
            show crimelord2 at center
            playerName "Terrem Jesond: Dime porqué crees que puedes controlar Tatooine."
            crimelord2 "Ah, muchach[tuO]. ¡Yo ya controlo Tatooine! Decido qué entra y qué sale. El comercio lo es todo, y más en un mundo que no sea autosuficiente."
            crimelord2 "Soy un magnate, [playerName]. Tengo participaciones en múltiples empresas menores de modo que, sin que se me pueda acusar de monopolio, controlo casi todo el tráfico del Borde Exterior."
            crimelord2 "Extraigo minerales en Modirin. Fabrico tecnología en Reuss. Construyo naves en astilleros de Bahalianos y de Bengel. Las muevo con Transportes Ororo. Llego al mercado con Exportaciones Galindas. Incluso alcanzo a las clases altas con los Casinos Kendamari."
            crimelord2 "De Christophsis a Svivren, de Ryloth a Qiaxx, e incluso en las Regiones Desconocidas, mis naves siempre están recorriendo las rutas y haciéndome ganar más dinero."
            playerName "¿Cómo proteges tu inversión? ¿Seguridad mercenaria?"
            crimelord2 "Cuando eres tan poderoso como yo, la inversión se protege sola. Los primeros interesados en que yo triunfe son los que pueden ayudarme, porque eso les beneficia."
            playerName "''(Eso suena a exhaustiva red de sobornos: Oficiales imperiales, gobiernos planetarios y seguramente incluso piratas. Si es cierto, reconozco que lo tiene bien montado).''"
            crimelord2 "Eso no quita que yo posea también empresas de cobros. Tengo más empresas que las que puedo recordar, y también más amigos influyentes. Sin ir más lejos, hago esquí flotante con el rector de tu universidad. ¿Quieres que le hable bien de ti?"
            playerName "Ese tipo de amigos no son fáciles de mantener, Jesond. Si les pides favores, ellos te pedirán favores a cambio. ¿Qué haces si te piden algo que no estás dispuesto a dar?"
            crimelord2 "Somos amigos es que nos ayudamos unos a otros. Buscamos la forma en que nuestros intereses sean compatibles. Cuando yo posea Tatooine (y lo poseeré), mis amigos no me pedirán este mundo. Si necesitan algo de aquí, lo tendrán a través de mí."
            crimelord2 "No puedes imaginarte el poder que llegan a tener algunas de estas personas, [playerName]. Los holodramas de conspiraciones se quedan cortos. Xim el Déspota era un aficionado comparado con mis amigos."
            playerName "Si no supiera que es absurdo, creería que tus amigos son los Lores del Sith."
            crimelord2 "No lo descartes."
            $ saludarJesond = 1
            hide crimelord2
            if crimelord1Activo < 2:
                show crimelord1 at left
            if crimelord2Activo < 2:
                show crimelord2
            show crimelord3 at right
            jump primeraCharlaCrimelords
        "Hablar con Radon el Hutt." if saludarRadon == 0:
            hide crimelord1
            hide crimelord2
            hide crimelord3
            show crimelord3 at center
            "Aunque no simpatizas con los hutts, te diriges a Radon con respeto, usando su idioma para intentar ganártelo."
            play sound "sound/boshuda.mp3"
            play sound "sound/risahutt.mp3"
            crimelord3 "Buen intento, [playerName], pero no vuelvas a hacerlo. Tu patética garganta simplemente no puede emular los matices de una lengua tan elegante como el huttés."
            crimelord3 "Somos un pueblo antiguo. Nuestro imperio era una potencia galáctica cuando tu civilización aún se preguntaba si las rocas son comestibles. Nosotros llevamos la paz, el progreso y la prosperidad a tioneses, gamorreanos y niktos, y acabamos con amenazas como los evocii, el Imperio Infinito y Xim el Déspota."
            playerName "Es... una forma de verlo. "
            crimelord3 "Sólo los hutts podemos mantener el actual estado del bienestar en Tatooine. El éxito de Jabba lo prueba. Los gobiernos caen; nosotros, longevos y poderosos, nos mantenemos. Todas las potencias triunfantes han sabido apoyarnos, desde antes de la República. Quienes no lo hicieron, fueron aplastados."
            playerName "Tatooine pertenecerá a alguien. Si no es a los hutts, será a otros. ¿No es eso?"
            crimelord3 "¡Que se maravillen de nuestro esplendor! ¡Que se estremezcan ante nuestro poder! ¡Que sientan el peso de nuestras cadenas para servir a sus legítimos amos!"
            playerName "Oh Vuestra... Hutticidad. No te discuto, pero no me has dicho todavía qué ofreces a Tatooine que tus rivales no puedan."
            crimelord3 "Nuestro poder es mucho mayor que el de Vykan Fenn. Nuestras armas son más poderosas. Nosotros hemos asesinado impunemente a Moffs mientras los umbaranos simplemente les esquivaban. Prevaleceremos."
            crimelord3 "Terrem Jesond te hablará de sus rutas de comercio. ¡Ja! Los hutts conocemos rutas hiperespaciales secretas con las que abasteceremos a Tatooine de recursos valiosos, desde agua hasta especia. ¿Has oído hablar del Guión de Tatooine, que lo conecta con Nal Hutta a través del Borde Medio?"
            playerName "Sí, pero nadie ha podido demostrar su existencia. Es un mito, como el Salto Coreliano."
            play sound "sound/risahutt.mp3"
            crimelord3 "Son dos mitos muy lucrativos, [playerName]. Son leyendas que mis naves recorren constantemente."
            playerName "No se puede decir que te intimiden tus adversarios o que dudes de tus posibilidades."
            crimelord3 "Estoy seguro de que puedo conseguir algo que tú necesites. Si aprendiste nuestro idioma, sabes que quien ayuda a los hutts... es recompensado."
            $ saludarRadon = 1
            hide crimelord3
            if crimelord1Activo < 2:
                show crimelord1 at left
            if crimelord2Activo < 2:
                show crimelord2
            show crimelord3 at right
            jump primeraCharlaCrimelords
        "Acusarles de crimen organizado." if saludarTresCrimelords == 0:
            if crimelord1Activo < 2:
                show crimelord1 at left
            if crimelord2Activo < 2:
                show crimelord2
            show crimelord3 at right
            playerName "Creo que sois unos delincuentes, líderes de grupos de bandidos, disputándoos el territorio de Tatooine para el contrabando."
            crimelord1 "¿Qué? ¿Cómo te atreves a hablarme así?"
            "Fenn mete una mano en su manto, tanteando en un gesto de desenfunde; pero Jesond detiene su brazo con una mano escamosa."
            crimelord3 "Te equivocas, [playerName]. Somos empresarios respetables intentando evitar una competencia perjudicial. Me atrevo a decir: somos {i}más{/i} éticos que la mayoría de empresarios."
            crimelord3 "Empresas como TaggeCo o Minerales Borde Exterior simplemente se asentarían aquí y causarían la bancarrota de cualquiera que se opusiera a ellos."
            playerName "¿Justamente TaggeCo y MBE? Ambas son empresas tapadera para el crimen organizado."
            crimelord2 "Entonces tú no nos acusarás sin pruebas, ¿verdad?"
            crimelord1 "Desde luego, muchos de nosotros llevamos el estigma de nuestras especies. Como hemos triunfado, nos acusan de haberlo hecho con malas artes. Sobre todo al hutt."
            crimelord2 "Hubo empresas koorivar entre los Separatistas durante las Guerras Clon, pero no creo que me culpes a {i}mí{/i} de sus delitos. ¡Por entonces yo no era ni un huevo!"
            playerName "Bueno... De acuerdo."
            $ saludarTresCrimelords = 1
            jump primeraCharlaCrimelords
        "Preguntarles quién es Vasail Tai." if explicaTai == 0:
            if crimelord1Activo < 2:
                show crimelord1 at left
            if crimelord2Activo < 2:
                show crimelord2
            show crimelord3 at right
            crimelord3 "Ah, sí, Vasail Tai. Valiente inútil."
            crimelord2 "Tai participaba en esta... amistosa competencia. Su grupo decidió... retirarse cuando se demostró que no estaban preparados para controlar Tatooine."
            crimelord3 "Sí, eso sucedió. Tai estuvo entre los supervivientes."
            playerName "¿Supervivientes? Creí que simplemente su empresa había dejado el sistema."
            crimelord3 "Los supervivientes dejaron el sistema."
            if crimelord1Activo < 2:
                crimelord1 "No creas que llegaron muy lejos."
            crimelord2 "En todo caso, Tai quedó varado en el planeta y nos ofreció sus servicios. Decidimos que podría ayudar a, eh, llevar el día a día de la competición."
            crimelord3 "Le pedimos que estuviese alerta para ver si llegaba algún otro aspirante y que le pusiese a prueba para ver si estaba a la altura."
            crimelord2 "Parece que te tomó por alguien importante."
            if crimelord1Activo < 2:
                crimelord1 "No se me ocurre porqué."
            $ explicaTai = 1
            jump primeraCharlaCrimelords
        "Ayudarles.":
            if crimelord1Activo < 2:
                show crimelord1 at left
            if crimelord2Activo < 2:
                show crimelord2
            show crimelord3 at right
            playerName "Está bien, os ayudaré. Me voy a investigar."
            if crimelord1Activo < 2 and crimelord1Activo < 2:
                crimelord1 "Si intentas traicionarnos, [playerName], acabaré contigo de una forma especialmente truculenta."
                crimelord2 "Fenn habla metafóricamente. No está amenazando con matarte."
                crimelord1 "¿Ah, no? Quiero decir... Por supuesto que no."
                playerName "Qué bien..."
            else:
                crimelord3 "Que tu búsqueda sea fructífera, y que tomes la decisión correcta."
                crimelord2 "Todos sabemos cuál será la decisión correcta."
                crimelord3 "{i}Mee jewz ku. Bargon u noa-a-uyat.{/i}{p}(Adiós. Tus servicios serán recompensados, o gracias)."
            $ primeraVezTrastienda = 1
            $ crimelord1Activo = 1  
            $ crimelord2Activo = 1
            $ jugarLabria = 4
            jump go_Trastienda

label hablarFuncionario:

    menu:
        "Hay un problema con mi permiso de despegue." if intentarPermisoEnOficina == 0:
            playerName "Hay un problema con mi permiso de despegue. Yo tenía autorización para dejar Tatooine, pero sus soldados me dicen que no aparece en sus bases de datos."
            funcionario "No son {i}mis{/i} soldados, son soldados del Imperio. Vamos a ver. Enséñeme su copia del permiso de despegue."
            playerName "Claro."
            funcionario "Efectivamente, este código no aparece en el sistema informático. Es posible que exista, pero que se haya perdido el acceso a ella. La solución es sencilla."
            funcionario "Se notifica a la central de Arkanis. En cuanto encuentren pruebas de que su permiso existía, lo notifican a la oficina de la Gobernadora Aryon o del Moff Julstan para que lo sellen, y su permiso vuelve a ser válido."
            playerName "¿Cuánto puede llevar esto?"
            funcionario "La Gobernadora y el Moff están muy ocupados con la guerra ahora mismo. Esto antes se resolvía en cuestión de minutos, pero ahora el trámite es más lento y lleva tiempo."
            funcionario "¿Es usted uno de los pilotos de Transportes Ororo? Esa empresa tiene acuerdos especiales con la oficina del Moff Julstan y pueden acelerar el proceso."
            playerName "No, no trabajo para Ororo..."
            funcionario "Esto funciona así: Con un permiso de despegue, usted puede dejar el planeta; pero como hay una investigación abierta sobre su nave, entonces la nave y todo lo que esté a bordo se quedan aquí."
            funcionario "Si se retira la investigación, pero usted no tiene permiso de despegue, entonces la nave puede irse, pero usted se queda."
            playerName "Esto es más complicado de lo que creía. Creo que necesito el consejo de un experto en administración local."
            $ intentarPermisoEnOficina = 1
        "Quiero hablar con un cazarrecompensas." if preguntarKabePorCazador == 2:
            playerName "Quiero hablar con un cazarrecompensas autorizado. Me han dicho que venga aquí."
            $ itemWantedPoster = 2
            jump puedesHablarConCazador
        "¿Qué sabemos de mi permiso de despegue?" if intentarPermisoEnOficina == 1 and itemPermisoDespegue == 0:
            playerName "¿Qué sabemos de mi permiso de despegue?"
            funcionario "He informado a la central de Arkanis. Lo último que me han dicho es que buscarán su permiso en sus archivos, pero aún no lo han encontrado."
            funcionario "Cuando encuentren su permiso y lo envíen a la Gobernadora y al Moff para que lo selle uno de ellos, yo recibo copia. De momento, no hay nada."
            playerName "Gracias. Comprendo que usted no puede hacer más."
            funcionario "Gracias por confiar en el Imperio."
        "Hay una investigación abierta sobre mi nave" if itemInvestigacion == 0:
            playerName "Hay una investigación abierta sobre mi nave, {i}[tuNave]{/i}, y se trata de un malentendido que quiero resolver."
            play sound "sound/pitido.mp3"
            funcionario "He enviado una petición a la Oficina de Seguridad Imperial para que confirmen la situación. Por favor, espere su respuesta."
            playerName "¿No puede hacer nada más desde aquí?"
            funcionario "Lo siento, esto es jurisdicción de otro departamento del Imperio."
        "Quiero ver los resultados del simulador.":
            playerName "Quisiera acceder al simulador de naves espaciales para ver los resultados de uno de los pilotos en entrenamiento."
            funcionario "Por supuesto. ¿Tiene usted licencia de vuelo?"
            playerName "Bueno... No. Yo no sé pilotar."
            funcionario "¿Cómo ha llegado usted a Tatooine entonces?"
            playerName "Mi nave tiene un droide piloto."
            funcionario "Admiro su valor, [playerName]. Pilotar por este sistema no es para nada pan comido. Yo no sería capaz de confiar en un droide para ese trabajo."
            funcionario "En todo caso, el simulador sólo está disponible para pilotos espaciales. Lo siento."
        "No, no tengo un trámite abierto.":
            playerName "No, no tengo ningún trámite abierto en este momento."
            funcionario "Cuando necesite algo del Imperio, abra un trámite y estaremos encantados de ayudar. Hasta la próxima."
            jump go_OficinaImperial

    jump hablarFuncionario


label hablarKabe:
    
    menu:
        "¿Sabes cómo puedo conseguir un permiso de despegue?" if preguntarPermisoEnCantina == 1:
            playerName "¿Sabes cómo puedo conseguir un permiso de despegue?"
            kabe "Se consiguen en el sistema Arkanis, antes de venir a provincias, claro. Me extraña que el Imperio te haya dejado aterrizar en Tatooine sin uno."
            playerName "Yo tenía un permiso de despegue, pero parece haberse perdido en las bases de datos. ¿Cómo puedo recuperarlo?"
            kabe "Desde luego, no en la Oficina Imperial; esto no es un trámite sin importancia. Podrías contactar con la gobernadora para que te lo apruebe; no te escuchará."
            kabe "Necesitas a alguien que se meta en bases de datos imperiales sin que el Imperio se dé cuenta, cortando su criptografía y sus cortafuegos."
            kabe "Necesitas un rebanador. Necesitas a Hyp."
            playerName "¿Hyp?"
            kabe "Hawk Hyperhalo. No encontrarás un rebanador mejor en todo el sector. Ha entrado en archivos del Imperio, de la Rebelión y de los Hutts. Dicen que le enseñó la legendaria rebanadora Shenir Rix."
            playerName "Tiene buena pinta. ¿Dónde puedo encontrar a Hawk Hyperhalo?"
            kabe "Vive cerca de la antigua finca de Sedi Fisk, en una pequeña casa aislada. Rara vez sale al exterior. Los demás nos bronceamos bajo los soles gemelos; pero los rebanadores pasan su tiempo delante de monitores de ordenador."
            playerName "Gracias, Gorlok."
            $ preguntarPermisoEnCantina = 2
            jump hablarKabe
        "¿Sabes cómo puedo conseguir un cazarrecompensas?" if preguntarKabePorCazador == 1:
            playerName "Necesito encontrar un cazarrecompensas. ¿No frecuentan las cantinas?"
            kabe "Sí, claro. Yo debo ser el legendario Cad Bane. ¿De dónde sacas esas ideas? La gente viene a las cantinas a emborracharse y jugar. ¿Cómo hacen en tu planeta?"
            playerName "Creí que los cazadores, para relajarse..."
            kabe "Cero: Si alguien está relajándose después del trabajo, lo peor que puedes hacer es hablarle de trabajo. Uno: Los cazarrecompensas no se relajan."
            kabe "Lo mejor que puedes hacer es ir a la Oficina Imperial. Podrás ofrecer una recompensa, se asegurarán de que todo es legal y te cobrarán el depósito."
            playerName "La recompensa ya está puesta, es imperial. Sólo necesito que un cazarrecompensas vaya tras el blanco. ¿No hay cazarrecompensas... independientes?"
            kabe "Desde la muerte de Jabba, el crimen organizado ya no está {i}organizado{/i}. Sin un líder claro, nadie sabe quién es de fiar. Ahora mismo, un tipo con un rifle bláster a cuestas no es de fiar."
            kabe "Hazme caso, ve a la oficina. Los imperiales te pondrán en contacto con algún cazarrecompensas. Son unos inútiles, pero al menos eso sigue funcionando."
            $ preguntarKabePorCazador = 2
            jump hablarKabe

        "¿Cómo puedo retirar la investigación de mi nave?" if jugarLabria == 1:
            playerName "Gorlok, el Imperio ha acusado a mi nave de contrabando y está incautada. ¿Sabes cómo podría hacer que retirasen la investigación?"
            kabe "Una investigación imperial... Eso es complicado. Si se empeñan en seguir los procedimientos, te pueden declarar inocente al final pero te tendrán un montón de días inmovilizad[tuO]..."
            "El kaminoano ebrio levanta la cabeza y se mete en la conversación."
            labria "Creo que yo podría ayudarte, viajer[tuO] espacial."
            kabe "¡Vasail Tai, viejo borracho! ¿Qué sabrás tú?"
            "¿Hablar con Vasail Tai?"
            menu:
                "Sí, hablar con Vasail Tai.":
                    jump hablarLabria
                "Ahora mismo no.":
                    labria "Tienes mucho que hacer, claro. No te preocupes, estaré por aquí si cambias de opinión."
                    jump hablarKabe
                    
# Jugaste Con Labria: 0 aún no aparece Labria, 1 Labria ya aparece, no has hablado con él;
# 2 jugaste y perdiste (otro diálogo), 3 Has ganado; si le hablas te dice alguna chorrada; 4 Labria ya no aparece.

        "¿Quién es el tipo nuevo?" if jugarLabria == 1:
            playerName "Gorlok, ¿quién es ese tipo? El nuevo."
            kabe "¿Vasail Tai? Es un borracho inofensivo. No le hagas caso."
            kabe "Llegó hace un par de días. Hace apuestas con la gente que se cruza pero, cuando gana, ni siquiera les pide dinero."
            kabe "Hasta el momento, muy poca gente le ha ganado, pero no sé cuál es el premio. Hay algo que sí sé: Cómo ganarle."
            playerName "¿Qué?"
            kabe "Sus juegos son tan fáciles que te podría adelantar los resultados. Hace trucos de naipes previsibles y apuestas en las carreras."
            kabe "Te podría dar un pronóstico para ganar en cualquiera de ellos."
            playerName "¿Y por qué no juegas tú con él?"
            kabe "Porque no creo que él pueda darme nada que necesito. Y más importante:"
            kabe "Ese tipo {i}apesta{/i} a vino sacorrano barato. No quiero acercarme a él si puedo evitarlo."
            "¿Quieres hablar ahora con Vasail Tai?"
            menu:
                "Sí, hablar con Vasail Tai.":
                    jump hablarLabria
                "Ahora mismo no.":
                    pass
                    jump hablarKabe
        "Quiero ganar a Vasail Tai. ¿Me ayudas?" if jugarLabria == 2 and pronostico == 0:
            playerName "Gorlok, quiero jugar contra Vasail Tai y ganarle. ¿Me ayudas?"
            kabe "Claro. ¿Qué necesitas?"
            menu:
                "El pronóstico de las carreras de swoops.":
                    playerName "Quiero el pronóstico de las carreras de swoops."
                    kabe "Sabes cómo van esas carreras, ¿no? Cada piloto corre en solitario, sin los otros pilotos en la pista, para evitar que se ataquen unos a otros. El mejor tiempo gana."
                    kabe "Hay obstáculos pero también cojinetes de aceleración. Tres virtudes pueden ser decisivas: La habilidad del piloto, la precisión de sus movimientos, y la potencia de su máquina."
                    playerName "Entiendo. ¿Quién crees que ganará la próxima de Telos?"
                    $ pronostico = renpy.random.randint(4, 6)
                    if pronostico == 4:
                        scene bg cantina piloto1
                        show kabe
                        kabe "Sin duda Kimmi Chyler. Ella tiene talento y sensatez, mucho más que esos pilotos atrevidos."
                    elif pronostico == 5:
                        scene bg cantina piloto2
                        show kabe
                        kabe "Sin duda Dengar. El coreliano ha mejorado sus motores. Los 600 kilómetros/hora se le quedan cortos."
                    else:
                        scene bg cantina piloto3
                        show kabe
                        kabe "Sin duda RX-24. La precisión de movimientos de un droide se nota en un trabajo como éste."
                        $ pronostico = 6
                    scene bg cantina
                    show kabe
                "Un truco para el sabacc.":
                    playerName "Dame un truco para ganarle al sabacc."
                    kabe "Supongo que sabes jugar al sabacc, ¿no? La variante estándar de Bespin."
                    playerName "Sí, claro. Cada jugador tiene tres cartas, una de ellas descubierta. Se suman los valores de las cartas. El jugador que esté más cerca del 23, positivo o negativo, gana la mano."
                    playerName "Las cartas normales de los cuatro palos tienen un valor de 1 a 15, positivo o negativo según cómo hayan salido, y los arcanos tienen un valor negativo fijo."
                    playerName "En el primer turno, cada jugador elige cambiar una o dos cartas ocultas si quiere. Después hay más turnos mientras todos los jugadores quieren cambiar cartas."
                    playerName "En cuanto un jugador decide no cambiar nada, todos revelan sus manos. Después están los detalles: El sabacc puro, la Serie del Idiota..."
                    kabe "Oh, {i}poodoo{/i}... Tai te va a destrozar."
                    kabe "Has descrito las matemáticas del juego. No creo que hayas jugado una mano en tu vida. Eres como un ingeniero pilotando una nave: No tienes ni idea de cómo funciona."
                    kabe "A ver cómo arreglo este desastre llamado [playerName]."
                    $ pronostico = renpy.random.randint(1, 3)
                    if pronostico == 1:
                        kabe "Si su carta visible es un as, y tú tienes menos de 18, pide una carta. Pero si tienes 18 o más, plántate."
                    elif pronostico == 2:
                        kabe "La carta del Idiota vale cero. La Serie del Idiota es el Idiota, un dos y un tres, y siempre gana porque es un veintitrés."
                        kabe "Pero es casi imposible que salga. Descarta siempre el Idiota, y sólo el Idiota."
                    else:
                        kabe "Las parejas son un desastre, salvo las altas. Si tienes dos sietes, o dos ochos, deshazte de uno inmediatamente."
                        kabe "Por supuesto, si tienes dos de valor once, aunque una sea un arcano, quédatelas. Con dos onces, has ganado... y con dos ases, has perdido."
                        $ pronostico = 3
            jump hablarKabe
        "¿Qué sabes de ratas womp?":
            playerName "¿Qué sabes sobre ratas womp, Gorlok?"
            kabe "No sé nada de ratas womp. Ése es tu campo."
            kabe "Tengo la suerte de vivir en una ciudad y no tengo problemas con las alimañas."
            jump hablarKabe
        "Hasta luego.":
            playerName "Cielos despejados, Gorlok."
            kabe "No uses argot de los pilotos. Ni tú ni yo somos pilotos, y así sólo suenas rar[tuO]."

    jump siguesEnCantina

label hablarLabria:
# Jugaste Con Labria: 0 aún no aparece Labria, 1 Labria ya aparece, no has hablado con él;
# 2 jugaste y perdiste (otro diálogo), 3 Has ganado; si le hablas te dice alguna chorrada; 4 Labria ya no aparece.
# Existe además JugandoConLabria

    if jugarLabria == 1 or jugarLabria == 0:
        labria "Me llamo Vasail Tai. Soy empresario, venido del Laberinto Rishi. Creo que hay grandes oportunidades de negocio en el territorio imperial ahora mismo."
        playerName "Conozco tu mundo, kaminoano. Fabricais tecnología ilegal. Armas, clones..."
        labria "¿Ilegal dónde? Cumplimos estrictamente las normas de los territorios donde estemos. A veces vendemos a clientes que nos han engañado, claro, pero no seas tan duro con nosotros."
        labria "Ni siquiera sabes qué estoy haciendo aquí. Quizá soy un simple pescador..."
        playerName "¿Pescador? ¿En el desierto?"
        labria "Pesca{i}dero.{/i} Exportador de pescado. Pero hablemos de negocios."
        labria "Claramente eres una persona excepcional, nada parecida a estos meros viandantes de aquí. Tienes experiencia, tienes habilidades, has viajado, quizá más lejos que yo."
        playerName "Deja de darme coba. ¿Qué quieres de mí?"
        labria "Creo que eres una persona astuta e importante. Un pez gordo. Permíteme proponerte una apuesta..."
        playerName "No soy aficionad[tuO] al juego."
        labria "Considera que la primera es de prueba, sólo para que yo vea tus capacidades. Si pierdes, no pagarás nada, prometido ante testigos. Si ganas, podrás hablar de negocios con mis jefes."
        playerName "(Otro pesado que no callará hasta que yo pase por el aro)."
        $ jugarLabria = 2
        jump jugandoConLabria

    if jugarLabria == 2:
        "Hola otra vez, [playerName]. ¿Te apetece volver a jugar? ¡Grandes premios te esperan!"
        menu:
            "Claro, juguemos.":
                jump jugandoConLabria
            "Ahora mismo no me apetece.":
                playerName "No, gracias, ahora mismo no me apetece jugar."
                labria "Sin problemas, otra vez será."

    if jugarLabria == 3:
        labria "Enhorabuena: Has ganado. Pasa por la puerta del fondo para disfrutar de tu premio. Los demás invitados ya han llegado."
        menu:
            "Ir ahora a la puerta del fondo.":
                jump Trastienda
            "Preguntar a la camarera.":
                playerName "Duquesa, ¿qué hay detrás de la puerta del fondo?"
                camarero "Yo no puedo hacer nada. Han alquilado esa habitación para lo que sea que estén haciendo. Pagaban bien."
                camarero "No creo que te maten ahí dentro."
            "Quizá luego.":
                playerName "Quizá vaya luego; ahora tengo otras cosas que hacer."
                labria "No te preocupes, pero deberías ir pronto."
                
    jump go_Cantina

label jugandoConLabria:
    playerName "De acuerdo, juguemos. ¿Qué me ofreces?"
    labria "Sabacc y carreras de swoops. ¿Qué prefieres?"
    menu:
        "Juguemos al sabacc.":
            if pronostico == 0:
                $ pronostico = renpy.random.randint(1, 3)
            if pronostico == 1:
                "Empieza el juego y recibes una mano discreta. En tu mano está la Reina del Aire y la Oscuridad, que tiene un valor de 2 negativo, y el 11 de oros. El 9 de sables es tu carta visible."
                "Tienes un total de exactamente 18, una cifra complicada. Puedes cambiar cartas o plantarte; pero el primer movimiento es suyo. Ha cambiado una carta."
                "Tu cabeza piensa en probabilidades, en estadística, pero muy rara vez has estado en una situación así, en una mesa de juego real. Esto te pone más nervios[tuO] de lo que habías esperado."
                "Miras a Tai a los ojos. Te sonríe sutilmente y te devuelve la mirada, pero no puedes averiguar nada sobre su mano, excepto la carta que tiene bocarriba: El as de bastos invertido, que vale 15 negativo."
                menu:
                    "Pide carta, cambia la Reina.":
                        "Visiblemente, tocas el dorso de la Reina. La carta lanzará destellos que Tai pueda ver, para indicar que está cambiando su contenido. En tu lado, múltiples palos y números se suceden."
                        "La carta se estabiliza y muestra a la Dama de Sables, invertida. Ella tiene un valor de 13 negativo."
                        "Eso elimina todo lo que tenías con el 11 positivo de oros. Tu total es de sólo 7."
                        labria "Yo no quiero cambiar nada más. Revela tus cartas, [playerName]."
                        "Tai tiene el 10 de oros y el comandante de bastos invertido, con un valor de negativo 12. Con los 15 puntos de su as visible, él suma 17 negativo."
                        playerName "Has ganado claramente, Tai."
                        labria "No te preocupes, no te cobraré nada por ahora. Me la guardo y puedes pedir la revancha cuando quieras. No irás a ninguna parte"
                        playerName "¡Pero si soy viajer[tuO] espacial!"
                        labria "Sí, sí, eso dicen todos. Nadie escapa de Tatooine."
                        $ pronostico = 0
                        jump go_Cantina
                    "Pide carta, cambia el 11.":
                        "Visiblemente, tocas el dorso del 11. La carta lanzará destellos que Tai pueda ver, para indicar que está cambiando su contenido. En tu lado, múltiples palos y números se suceden."
                        "La carta se estabiliza y muestra a la Dama de Sables, invertida. Ella tiene un valor de 13 negativo."
                        "Eso es más que lo que tenías con el 9 positivo de sables. Tu total ahora es de 6 negativo."
                        labria "Yo no quiero cambiar nada más. Revela tus cartas, [playerName]."
                        "Tai tiene el 10 de oros y el comandante de bastos invertido, con un valor de negativo 12. Con los 15 puntos de su as visible, él suma 17 negativo."
                        playerName "Has ganado claramente, Tai."
                        labria "No te preocupes, no te cobraré nada por ahora. Me la guardo y puedes pedir la revancha cuando quieras. No irás a ninguna parte"
                        playerName "¡Pero si soy viajer[tuO] espacial!"
                        labria "Sí, sí, eso dicen todos. Nadie escapa de Tatooine."
                        $ pronostico = 0
                        jump go_Cantina
                    "Pide dos cartas, cambia ambas.":
                        "Visiblemente, tocas el dorso de la Reina y del 11. Ambas cartas lanzarán destellos que Tai pueda ver, para indicar que está cambiando su contenido. En tu lado, múltiples palos y números se suceden en cada naipe."
                        "Las cartas se estabilizan y muestran a la Dama de Sables, invertida, con un valor de 13 negativo; y el 3 de bastos."
                        "Eso ha sido bastante desastroso. 13 negativo, 3 positivo y el 9 de sables positivo te dan un 1 negativo."
                        labria "Yo no quiero cambiar nada más. Revela tus cartas, [playerName]."
                        "Tai tiene el 10 de oros y el comandante de bastos invertido, con un valor de negativo 12. Con los 15 puntos de su as visible, él suma 17."
                        playerName "Has ganado claramente, Tai."
                        labria "No te preocupes, no te cobraré nada por ahora. Me la guardo y puedes pedir la revancha cuando quieras. No irás a ninguna parte"
                        playerName "¡Pero si soy viajer[tuO] espacial!"
                        labria "Sí, sí, eso dicen todos. Nadie escapa de Tatooine."
                        $ pronostico = 0
                        jump go_Cantina
                    "Plántate.":
                        playerName "Me planto. Veamos tus cartas."
                        "Tai abre sus párpados de par en par; sus ojos alienígenas tienen un aspecto aún más exótico con la expresión de sorpresa."
                        labria "Tienes agallas, [playerName]. Veamos qué más tienes."
                        "Tai muestra primero una carta: El comandante de bastos invertido, que vale 12 negativo. Eso le pondría en 27 negativo."
                        "Pero su última carta es el 10 de oros positivo, con lo que su resultado final es de 17 negativa. Es un total bastante bueno. Tai sonríe con petulante satisfacción."
                        "Intentas adoptar una pose similar, que seguramente no te sale tan bien, mientras revelas tus cartas: 11 de oros y la Reina del Aire y la Oscuridad. Tu total es de 18."
                        labria "¡Vaya, vaya! Estoy impresionado."
                        jump ganasteALabria
            if pronostico == 2:
                "Empieza el juego y tu carta visible es el 3 de botellas invertido. En tu mano caen otras dos cartas: El 1 de bastos (que no es el as), invertido y... el Idiota."
                "Es una decisión complicada. La Serie del Idiota gana siempre porque es un 23 para tontos: El Idiota, que vale 0, con una de valor 2 y una de valor 3. Y ya tienes el 3."
                "No es ninguna locura. Hay cuatro treses en la baraja. La probabilidad de que salga uno debe ser de... ¿una entre dieciséis? Oh, ¿dónde está Jako cuando le necesitas?"
                "El Idiota no sirve para nada más. La Serie del Idiota es arriesgarse a todo o nada; pero esas cartas te dan sólo un 4 negativo. Hay que tomar una decisión."
                "¿Qué tiene Tai visible? Dedicas una mirada y ves el 2 de oros. Sólo hay un Idiota en la baraja; él no puede ir también a Serie del Idiota."
                menu:
                    "Pide carta, cambia el 1.":
                        "Visiblemente, tocas el dorso del 1. La carta lanzará destellos que Tai pueda ver, para indicar que está cambiando su contenido. En tu lado, múltiples palos y números se suceden."
                        "Ha sido un movimiento audaz, sólo un 2 te podría resolver la vida... y te ha salido el 5 de sables, positivo. Tu total ahora es de 2."
                        labria "Yo no quiero cambiar nada más. Revela tus cartas, [playerName]."
                        "Sus cartas ocultas eran el señor de bastos, que vale 14, y el 2 de sables, todas positivas. Combinadas con su 2 de oros visible, él suma 18."
                        playerName "Si un jugador acaba con el Idiota en su mano, es porque lo es, ¿no, Tai?"
                        labria "Tú lo has dicho, no yo."
                        labria "No te preocupes, no te cobraré nada por ahora. Me la guardo y puedes pedir la revancha cuando quieras. No irás a ninguna parte"
                        playerName "¡Pero si soy viajer[tuO] espacial!"
                        labria "Sí, sí, eso dicen todos. Nadie escapa de Tatooine."
                        $ pronostico = 0
                        jump go_Cantina
                    "Pide carta, cambia el Idiota.":
                        "Visiblemente, tocas el dorso del Idiota. La carta lanzará destellos que Tai pueda ver, para indicar que está cambiando su contenido. En tu lado, múltiples palos y números se suceden."
                        "Hay quien dice que, cuando cambias la carta del Idiota, tienes más posibilidades de que te salga un arcano que cuando cambias otra carta. Nunca se ha demostrado estadísticamente..."
                        "...pero en este caso ha pasado. Tu nueva carta es el Maligno, que vale 15 puntos como un as, pero siempre negativo. Eso te viene bien porque tienes tres cartas negativas que suman 19."
                        labria "Yo no quiero cambiar nada más. Revela tus cartas, [playerName]."
                        "Sus cartas ocultas eran el señor de bastos, que vale 14, y el 2 de sables, todas positivas. Combinadas con su 2 de oros visible, él suma 18."
                        "La diferencia es de sólo un punto, pero has ganado al deshacerte del Idiota. Tai no ha visto al Idiota, así que no entiende porqué te quedas boquiabiert[tuO]."
                        jump ganasteALabria
                    "Pide dos cartas, cambia ambas.":
                        "Visiblemente, tocas el dorso del Idiota y del 1. Ambas cartas lanzarán destellos que Tai pueda ver, para indicar que está cambiando su contenido. En tu lado, múltiples palos y números se suceden en cada naipe."
                        "Las cartas se estabilizan y muestran el 5 de sables, positivo, y al Maligno, un arcano que vale 15 puntos como un as, pero siempre negativo."
                        "Combinados con tu 3 de botellas invertido, suman 13 negativo, otro número relacionado con el Maligno."
                        labria "Yo no quiero cambiar nada más. Revela tus cartas, [playerName]."
                        "Sus cartas ocultas eran el señor de bastos, que vale 14, y el 2 de sables, todas positivas. Combinadas con su 2 de oros visible, él suma 18."
                        playerName "Has ganado claramente, Tai."
                        labria "No te preocupes, no te cobraré nada por ahora. Me la guardo y puedes pedir la revancha cuando quieras. No irás a ninguna parte"
                        playerName "¡Pero si soy viajer[tuO] espacial!"
                        labria "Sí, sí, eso dicen todos. Nadie escapa de Tatooine."
                        $ pronostico = 0
                        jump go_Cantina
                    "Plántate.":
                        playerName "Me planto. Veamos tus cartas."
                        "Tai abre sus párpados de par en par; sus ojos alienígenas tienen un aspecto aún más exótico con la expresión de sorpresa."
                        labria "Tienes agallas, [playerName]. Veamos qué más tienes."
                        "Revelas tus cartas y él las suyas: El 2 de sables y el señor de bastos, que vale 14. Combinado con su 2 de oros visibles, todos positivos, él suma... ¿¡tanto!?"
                        "Tú tienes un modesto 4 negativo. Tai tiene un 18. Hacía mucho que ninguno de los dos veía una derrota con una diferencia tan grande."
                        playerName "Has ganado claramente, Tai."
                        labria "No te preocupes, no te cobraré nada por ahora. Me la guardo y puedes pedir la revancha cuando quieras. No irás a ninguna parte"
                        playerName "¡Pero si soy viajer[tuO] espacial!"
                        labria "Sí, sí, eso dicen todos. Nadie escapa de Tatooine."
                        $ pronostico = 0
                        jump go_Cantina
            if pronostico == 3:
                "Empieza el juego y tu carta visible es el 8 de oros, invertido. En tu mano hay otras dos cartas, también invertidas: El 4 de bastos y el 8 de sables. Tienes una pareja."
                "No sólo eso, sino que tu total es de 20 negativo. Eso está a sólo 1 punto del codiciado 21. Plantarse sería lo sensato, si fuese posible."
                "Pero es el primer movimiento y debes deshacerte de al menos una carta de tu mano."
                "Mientras meditas, te fijas en la carta visible de Tai. Es el 13 de botellas. Eso todavía no es decisivo."
                menu:
                    "Pide carta, cambia el 4.":
                        "Visiblemente, tocas el dorso del 4. La carta lanzará destellos que Tai pueda ver, para indicar que está cambiando su contenido. En tu lado, múltiples palos y números se suceden."
                        "La carta se estabiliza y muestra el 13 de sables, invertido. Todas tus cartas están invertidas y tienen un valor total de 29. Estás a 8 puntos del 21."
                        labria "Yo no quiero cambiar nada más. Revela tus cartas, [playerName]."
                        "Sus cartas ocultas eran el 10 de botellas y el 7 de botellas, invertido. Combinado con su 13 de botellas visibles, él suma 16, a sólo 5 puntos del 21."
                        playerName "Has ganado claramente, Tai."
                        labria "No te preocupes, no te cobraré nada por ahora. Me la guardo y puedes pedir la revancha cuando quieras. No irás a ninguna parte"
                        playerName "¡Pero si soy viajer[tuO] espacial!"
                        labria "Sí, sí, eso dicen todos. Nadie escapa de Tatooine."
                        $ pronostico = 0
                        jump go_Cantina
                    "Pide carta, cambia el 8 (Rompe la pareja).":
                        "Visiblemente, tocas el dorso del 8. La carta lanzará destellos que Tai pueda ver, para indicar que está cambiando su contenido. En tu lado, múltiples palos y números se suceden."
                        "La carta se estabiliza y muestra el 13 de sables, invertido. Combinado con tu 4 de oros positivo y los 8 puntos negativos del arcano, sumas un total de 17."
                        labria "Yo no quiero cambiar nada más. Revela tus cartas, [playerName]."
                        "Sus cartas ocultas eran el 10 de botellas y el 7 de botellas, invertido. Combinado con su 13 de botellas visibles, él suma 16, a 5 puntos del 21. Él pierde por un punto."                        
                        jump ganasteALabria
                    "Pide dos cartas, cambia ambas.":
                        "Visiblemente, tocas el dorso del 4 y del 8. Ambas cartas lanzarán destellos que Tai pueda ver, para indicar que está cambiando su contenido. En tu lado, múltiples palos y números se suceden en cada naipe."
                        "Las cartas se estabilizan y muestran el 13 y el 6, ambos de sables, ambos invertidos. Combinando ambas con tu arcano de 8 negativo, tienes un total de 27 negativo."
                        labria "Yo no quiero cambiar nada más. Revela tus cartas, [playerName]."
                        "Bueno, tienes una posibilidad. Estás a sólo 6 puntos del 21, es razonable."
                        "Las cartas ocultas de Tai eran el 10 de botellas y el 7 de botellas, invertido. Combinado con su 13 de botellas visibles, él suma 16."
                        "Vaya. Él está a 5 puntos del 21, así que te aventaja por un punto."
                        playerName "Has ganado claramente, Tai."
                        labria "No te preocupes, no te cobraré nada por ahora. Me la guardo y puedes pedir la revancha cuando quieras. No irás a ninguna parte"
                        playerName "¡Pero si soy viajer[tuO] espacial!"
                        labria "Sí, sí, eso dicen todos. Nadie escapa de Tatooine."
                        $ pronostico = 0
                        jump go_Cantina
                    "Plántate.":
                        playerName "Me planto. Veamos tus cartas."
                        "Tai abre sus párpados de par en par; sus ojos alienígenas tienen un aspecto aún más exótico con la expresión de sorpresa."
                        labria "Tienes agallas, [playerName]. Veamos qué más tienes."
                        "Revelas tus cartas y él las suyas: El 10 de botellas, y el 7 de botellas invertido. Combinado con su 13 de botellas visible, él suma 16."
                        "Tu total es un modesto 12 negativo."
                        playerName "Has ganado claramente, Tai."
                        labria "No te preocupes, no te cobraré nada por ahora. Me la guardo y puedes pedir la revancha cuando quieras. No irás a ninguna parte"
                        playerName "¡Pero si soy viajer[tuO] espacial!"
                        labria "Sí, sí, eso dicen todos. Nadie escapa de Tatooine."
                        $ pronostico = 0
                        jump go_Cantina
        "Apostemos en las carreras.":
            playerName "Quiero apostar en las carreras de swoops."
            labria "De acuerdo. Apostemos en la próxima carrera en el circuito de Telos IV; podemos verla desde aquí usando monitores."
            playerName "¿No había carreras locales en Tatooine?"
            labria "Sólo un circuito de aficionados en manos hutts, que hace muchos años que no se usa. Ahora, con la guerra de bandas, nadie se atreverá a meterse."
            scene bg cantina pilotos
            labria "Los pilotos que participan son: Kimmi Chyler, campeona del Pantano de Agrilat, montando su Fulgor-S de Mobquet. Ella es quizá la mejor piloto de swoop del momento."
            labria "Dengar, el veterano cazarrecompensas, pilotando un modelo de Ferini. Dengar ha demostrado sus capacidades también como piloto de caza en su extensa carrera."
            labria "Por último, el droide RX-24 de Reubens Robótica, antiguo piloto del Star Tours que ha esquivado desde asteroides hasta naves piratas e imperiales."
            if pronostico == 0:
                $ pronostico = renpy.random.randint(4, 6)
            menu:
                "Apuesto por Kimmi Chyler.":
                    if pronostico == 4:
                        $ varComodin = renpy.random.randint(0, 1)
                        if varComodin == 0:
                            $ varComodin = 0
                            call swoopChylerDengarRX from _call_swoopChylerDengarRX
                        else:
                            $ varComodin = 0
                            call swoopChylerRXDengar from _call_swoopChylerRXDengar
                        labria "Vaya, vaya. Has ganado la apuesta."
                        jump ganasteALabria
                    else:
                        $ varComodin = renpy.random.randint(0, 3)
                        if varComodin == 0:
                            $ varComodin = 0
                            call swoopDengarChylerRX from _call_swoopDengarChylerRX
                        elif varComodin == 1:
                            $ varComodin = 0
                            call swoopDengarRXChyler from _call_swoopDengarRXChyler
                        elif varComodin == 2:
                            $ varComodin = 0
                            call swoopRXChylerDengar from _call_swoopRXChylerDengar
                        else:
                            $ varComodin = 0
                            call swoopRXDengarChyler from _call_swoopRXDengarChyler
                        labria "Has perdido."
                        labria "No te preocupes, no te cobraré nada por ahora. Me la guardo y puedes pedir la revancha cuando quieras. No irás a ninguna parte"
                        playerName "¡Pero si soy viajer[tuO] espacial!"
                        labria "Sí, sí, eso dicen todos. Nadie escapa de Tatooine."
                        $ pronostico = 0
                        jump go_Cantina

                "Apuesto por Dengar.":
                    if pronostico == 5:
                        $ varComodin = renpy.random.randint(0, 1)
                        if varComodin == 0:
                            $ varComodin = 0
                            call swoopDengarChylerRX from _call_swoopDengarChylerRX_1
                        else:
                            $ varComodin = 0
                            call swoopDengarRXChyler from _call_swoopDengarRXChyler_1
                        labria "Vaya, vaya. Has ganado la apuesta."
                        jump ganasteALabria
                    else:
                        $ varComodin = renpy.random.randint(0, 3)
                        if varComodin == 0:
                            $ varComodin = 0
                            call swoopChylerDengarRX from _call_swoopChylerDengarRX_1
                        elif varComodin == 1:
                            $ varComodin = 0
                            call swoopChylerRXDengar from _call_swoopChylerRXDengar_1
                        elif varComodin == 2:
                            $ varComodin = 0
                            call swoopRXChylerDengar from _call_swoopRXChylerDengar_1
                        else:
                            $ varComodin = 0
                            call swoopRXDengarChyler from _call_swoopRXDengarChyler_1
                        labria "Has perdido."
                        labria "No te preocupes, no te cobraré nada por ahora. Me la guardo y puedes pedir la revancha cuando quieras. No irás a ninguna parte"
                        playerName "¡Pero si soy viajer[tuO] espacial!"
                        labria "Sí, sí, eso dicen todos. Nadie escapa de Tatooine."
                        $ pronostico = 0
                        jump go_Cantina
                "Apuesto por RX-24.":
                    if pronostico == 6:
                        $ varComodin = renpy.random.randint(0, 1)
                        if varComodin == 0:
                            $ varComodin = 0
                            call swoopRXChylerDengar from _call_swoopRXChylerDengar_2
                        else:
                            $ varComodin = 0
                            call swoopRXDengarChyler from _call_swoopRXDengarChyler_2
                        labria "Vaya, vaya. Has ganado la apuesta."
                        jump ganasteALabria
                    else:
                        $ varComodin = renpy.random.randint(0, 3)
                        if varComodin == 0:
                            $ varComodin = 0
                            call swoopChylerDengarRX from _call_swoopChylerDengarRX_2
                        elif varComodin == 1:
                            $ varComodin = 0
                            call swoopChylerRXDengar from _call_swoopChylerRXDengar_2
                        elif varComodin == 2:
                            $ varComodin = 0
                            call swoopDengarChylerRX from _call_swoopDengarChylerRX_2
                        else:
                            $ varComodin = 0
                            call swoopDengarRXChyler from _call_swoopDengarRXChyler_2
                        labria "Has perdido."
                        labria "No te preocupes, no te cobraré nada por ahora. Me la guardo y puedes pedir la revancha cuando quieras. No irás a ninguna parte"
                        playerName "¡Pero si soy viajer[tuO] espacial!"
                        labria "Sí, sí, eso dicen todos. Nadie escapa de Tatooine."
                        $ pronostico = 0
                        jump go_Cantina
    jump go_Cantina

label ganasteALabria:
    scene bg cantina
    show labria
    labria "Ya sabía yo que eras alguien con recursos. Estoy seguro de que vale la pena que estés informad[tuO]."
    labria "Tu premio está en la puerta del fondo de la cantina. Los otros invitados ya han llegado. La contraseña es THX-1138."
    $ jugarLabria = 3
    menu:
        "Cruzar la puerta.":
            jump Trastienda
        "Preguntar a la camarera.":
            playerName "Duquesa, ¿qué hay detrás de la puerta del fondo?"
            camarero "Yo no puedo hacer nada. Han alquilado esa habitación para lo que sea que estén haciendo. Pagaban bien."
            camarero "No creo que te maten ahí dentro."
        "Quedarse en la cantina.":
            playerName "Quizá vaya luego; ahora tengo otras cosas que hacer."
            labria "No te preocupes, pero deberías ir pronto."
            jump siguesEnCantina
            $ jugarLabria = 3
            
    jump go_Cantina

label hablarMonjes:
    if hablarCazador == 0:
        monje1 "Saludos, herman[tuO]. Bienvenid[tuO] al Templo de [bomarr]. Percibo una mente poderosa en ti, con potencial para la iluminación."
        monje1 "Es bueno que tus viajes te hayan traido hasta aquí. Aquí podrás prescindir de las distracciones del mundo físico para alcanzar la iluminación."
        playerName "¿Qué?"
        monje1 "Podrás trascender en lo más profundo de tu propio ser hasta alcanzar cierto tipo de equilibrio."
        playerName "(Jum... Casi nadie fuera de la Orden [bomarr] ha entendido realmente a los Monjes. Quizá yo pueda descubrir algo valioso sobre ellos...)"
        monje1 "El poder de la mente debe ser mejorado. Te centras demasiado en el mundo físico. Debes prescindir de sus ataduras y de sus comodidades, y embarcarte en el viaje mental y espiritual."
        jump proselitismoMonje
    elif hablarCazador == 1:
        monje1 "Saludos, herman[tuO]. Bienvenid[tuO] al Templo de [bomarr]. Percibo una mente poderosa en ti, con potencial para la iluminación."
        monje1 "Es bueno que tus viajes te hayan traido hasta aquí. Aquí podrás prescindir de las distracciones del mundo físico para alcanzar..."
        playerName "No, no, nada de eso. Vengo con una misión clara."
        monje1 "¿Eres entonces [tuUn] misioner[tuO]?"
        playerName "Sé que estáis escondiendo a un fugitivo de la justicia. Es un criminal peligroso, y vengo a pediros que me lo entreguéis."
        monje2 "Em... No sé de qué me hablas."
        playerName "Thondo Qo, un mercenario y asesino aqualish, se esconde en esta zona. Un cazarrecompensas me ha dado el soplo. ¿Le habéis dado cobijo?"
        play sound "sound/motojet.mp3"
        "El rugido de una moto-jet ahoga vuestra conversación. Pronto oyes cómo baja el volumen: La moto se está alejando."
        playerName "Es él, ¿verdad? Me ha oído y está escapando."
        $ asustasteBandido = 1
        jump go_PalacioJabbaInt
    else:
        monje1 "Saludos, herman[tuO]. Bienvenid[tuO] al Templo de [bomarr]. Percibo una mente poderosa en ti, con potencial para la iluminación."
        monje2 "Oh, déjalo, colega. Es [playerName]. [tuPronombreMayus] nos pilló ocultando a un fugitivo."
        monje1 "Ah, sí. Realmente nunca creí que Qo pudiese alcanzar la iluminación."
        monje2 "Eres un hipócrita. En cuanto a ti, [playerName], ya te hemos pedido disculpas. ¿Qué más quieres de nosotros?"
        jump proselitismoMonje
    jump go_PalacioJabbaInt
    
label proselitismoMonje:
    menu:
        "Háblame de la iluminación." if preguntaIluminacion == 0:
            playerName "Háblame de la iluminación."
            monje1 "Cuando alcanzas la iluminación, tu mente habrá alcanzado la cúspide de su capacidad. Tú estarás en paz con el cosmos y podrás dedicar todo tu potencial a meditar sobre los misterios del universo."
            monje1 "Los misterios son metafísicos, por lo que están más allá del mundo perceptible. Para poder contemplar los misterios, debes prescindir de las necesidades físicas y dedicar todo tu esfuerzo cerebral a ello."
            monje2 "El habla es una restricción del mundo físico. Debes comunicarte con el poder de la mente para alcanzar la iluminación."
            monje1 "Los sentidos son sólo una distracción del mundo físico. Debes renunciar a los sentidos para alcanzar la iluminación."
            monje2 "Las comodidades sólo sirven para potenciar tus sentimientos hedonistas. Debes renunciar a tus posesiones para alcanzar la iluminación."
            monje1 "El dolor es otra distracción del mundo físico a la que debes insensibilizarte. Debes resistir el sufrimiento para alcanzar la iluminación."
            monje2 "Los textos sagrados de los [bomarr] te guiarán a la verdad suprema de la iluminación. Debes conocer los textos sagrados al dedillo para alcanzar la iluminación."
            playerName "Espera, volvamos a la parte en que esto va a doler..."
            monje1 "No dolerá. Cuando alcances la iluminación, no necesitarás cuerpo físico."
            playerName "¿Qué?"
            monje2 "Entonces nuestros cirujanos extraerán tu cerebro y lo meterán en un frasco de nutrientes carmesíes. Así, libre de las distracciones del universo, podrás dedicar todo tu tiempo a actividades mentales."
            monje1 "No te preocupes, herman[tuO]. Se utiliza anestesia para asegurar que el procedimiento es indoloro."
            playerName "¿Pero no habíais dicho que los monjes resisten el sufrimiento?"
            monje1 "Las tradiciones son las tradiciones, y si empiezas a discutirlas, nunca alcanzarás la iluminación."
            $ preguntaIluminacion = 1
            jump proselitismoMonje
        "¿Qué hacéis con los cerebros de los... iluminados?" if preguntaIluminacion == 1 and preguntaIluminacion1 == 0:
            playerName "¿Qué hacéis con los cerebros de quienes han alcanzado la iluminación?"
            monje1 "Los cerebros más iluminados se guardan en la Gran Sala de los Iluminados, en estantes, meditando sobre el infinito por los siglos de los siglos."
            monje1 "Los auténticos iluminados no encuentran necesidad de abandonar sus lugares, porque eso es meramente el deseo de contactar con el mundo físico."
            monje2 "Los monjes que aún no han alcanzado la iluminación retienen sus cuerpos físicos y sirven a las necesidades que pueda tener la Orden."
            monje1 "Los cerebros extirpados que aún pueden alcanzar una mayor iluminación..."
            monje2 "Ésos somos nosotros. Yo creo que en dos o tres siglos más, alcanzaremos la iluminación. Yo ya soy Pequeño Maestre."
            monje1 "Cállate, Frank. Los monjes como nosotros podemos pasear por el monasterio, sirviendo las necesidades de la Orden, en droides de perímetro, diseñados por la Orden [bomarr]."
            playerName "¿No es un modelo de Industrias Arakyd?"
            monje1 "Bueno, pero un ingeniero de Arakyd estaba en la Orden. Creo."
            $ preguntaIluminacion1 = 1
            jump proselitismoMonje
        "¿Y si se extrae el cerebro de alguien que no está iluminado?" if preguntaIluminacion == 1 and preguntaIluminacion2 == 0:
            playerName "¿Qué sucede si se extrae el cerebro de un Monje que aún no ha alcanzado la iluminación? ¿Ha pasado antes?"
            monje2 "¿Me está mirando a mí mientras dice eso? Yo ya no tengo sentido de la vista, pero creo que me está mirando."
            monje1 "Si el monje sobrevive, entonces el cerebro es susceptible de sufrir varios problemas mentales."
            monje1 "Sicosis, por ejemplo. Es muy desagradable cuando no tienes boca y debes gritar. Además, como no tienes que respirar, gritas sin cesar, literalmente."
            monje1 "En el caso de Frank, su problema es la ludopatía."
            monje2 "Oh, cállate."
            monje1 "Pero no pasa nada. Se le puede volver a poner el cerebro en el cuerpo anterior. O, si hemos reciclado ya el cuerpo de ese monje, pues en algún otro cuerpo que esté disponible."
            $ preguntaIluminacion2 = 1
            jump proselitismoMonje
        "Háblame de la Más Perfecta Orden de K'vin." if preguntaIluminacion3 == 0:
            playerName "He sabido que hay otra secta [bomarr] en Tatooine, la Más Perfecta Orden de K'vin."
            monje1 "No tenemos nada que ver con esos disidentes. Los K'vin son unos desdichados que han perdido el rumbo y nunca alcanzarán la iluminación."
            playerName "¿Cuál es la diferencia entre los K'vin y vosotros?"
            monje1 "Esos... ¡Esos herejes! Ellos toman los cerebros de sus monjes y los meten en jarras con líquidos de nutrientes..."
            playerName "Igual que vosotros."
            monje1 "¡Sí, pero ellos usan un líquido {i}verde{/i}!"
            monje1 "De ese modo, nunca alcanzarán auténtica iluminación. Los pergaminos sagrados del Heraldo Etéreo describen el color con precisión, debe ser rojo."
            monje2 "Se llama el Heraldo {i}Estéreo{/i}."
            monje1 "Cállate, Frank. Ése es un detalle irrelevante de la traducción. Se aceptan ambas formas. Lo importante es el color del líquido de nutrientes."
            $ preguntaIluminacion3 = 1
            jump proselitismoMonje
        "He oído que también curáis heridos." if preguntaIluminacion4 == 0:
            playerName "Se cuenta que curáis a los heridos que llegan a vuestras puertas."
            monje1 "Los grandes misterios del universo no se van a resolver solos. Cualquier persona que llegue a nuestra puerta tiene el potencial de desarrollar su mente..."
            monje2 "También se trata de ser buena persona. Una cosa es estar aislados, y otra negar ayuda a alguien que literalmente está delante de nosotros."
            monje2 "No somos cenobitas, pero el aislamiento del templo no es perfecto porque está en el universo físico. Quien llegue a nuestras puertas puede pedirnos asilo."
            monje1 "Pero para ello, esa persona tendrá que jurar nuestros votos y entrar en la Orden [bomarr]."
            monje1 "Nuestras reglas dicen que toda vida inteligente es sagrada porque toda mente puede alcanzar la iluminación."
            $ preguntaIluminacion4 = 1
            jump proselitismoMonje
        "Hasta luego.":
            playerName "Ya me voy. Hasta luego."
    jump go_PalacioJabbaInt

label hablarTuskens:
    # AUNQUE NO HABLES CON ELLOS, CUENTA COMO QUE LO HAS HECHO; NO VOLVERÁS A HABLAR CON TUSKEN JOE.
    $ hablarTuskens = 1
    show tuskens
    "Entre dos montañas y cerca de un oasis, los nómadas tusken han montado un campamento con un centener de cabañas portátiles hechas de pieles de animales."
    "Es el poblado más grande que has visto nunca. Un clan grande de moradores tendría sólo unas veinte cabañas. Además, abundan las cajas de municiones y de armas."
    "Lo que curiosamente escasean son los banthas. Cada morador adulto está ligado a un bantha, y esos animales no se pueden esconder. Hay muchos menos banthas que moradores."
    "Junto a las hogueras con utensilios de cocina, moradores varones y mujeres, incluso los más jóvenes, se preparan para física y mentalmente para el combate, con rituales y rutinas."
    menu:
        "Vamos a hablar con los tuskens.":
            show tuskens
            playerName "{i}Aargh. Eyaak urk urk.{/i}('Saludos. No quiero haceros daño' en lengua tusken)."
            play sound "sound/risatusken.mp3"
            tuskens "¿Cómo podrías hacernos daño, pisaverde desarmad[tuO] y solitari[tuO]?"
            playerName "Exacto. No soy una amenaza para los tusken. Sólo quiero saber más sobre vosotros. ¿Por qué vais a la guerra?"
            tuskens "¡Ah, miserable espía! Buscas averiguar nuestras tácticas para emboscarnos con fuerzas superiores. ¿Crees acaso que somos ignorantes salvajes?"
            playerName "¡No, no! Quiero saber qué motiva a los moradores. Quiero saber qué buscáis para poder dároslo. Quiero saber por qué hay tan pocos banthas aquí."
            tuskens "Extrañ[tuO], tú eres... extrañ[tuO]. Yo no sé cómo tratar contigo. Habla con el cacique, GRu'uu'h'rRr. Él te dará respuestas, si quiere."
            "Te señalan a un morador de las arenas con insignias de prestigio en su ropa protectora y que los demás tratan con respeto. No mide más de metro sesenta y es más delgado que los otros."
            show tuskens at left
            show joe with dissolve
            joe "{i}Aargh,{/i} viajer[tuO]. Soy GRu'uu'h'rRr. No eres jawa, no eres granjer[tuO] de humedad. No eres enemigo de los moradores de las arenas. ¿Qué buscas aquí?"
            playerName "Busco la verdad, GRu'uu'h'rRr. ¿Por qué los jawas y los granjeros de humedad son enemigos de los moradores de las arenas?"
            play sound "sound/rugidotusken.mp3"
            joe "¿Por qué ellos han buscado nuestra enemistad, viajer[tuO]? ¿Por qué desintegran a nuestras tribus? ¿Por qué degüellan a nuestros hermanos banthas y dejan atrás sus carcasas?"
            joe "¡Mira a tu alrededor, viajer[tuO]! Verás cuatro tribus combinadas bajo mi mismo mando. ¿Por qué hay sólo dos banthas para cada tres tuskens?"
            joe "¡Si los tusken no van a la guerra, pronto no habrá tusken!"
            playerName "¿Quién ha hecho eso? ¿Los jawas o los granjeros? ¿Cómo lo han conseguido?"
            joe "Sin duda ha sido con sus brujerías y sus máquinas. Los jawas tienen grandes máquinas."
            joe "Otras tribus acusan a los granjeros de humedad, pero yo no lo creo: Granjeros de humedad y comerciantes nunca habían sido tan audaces."
            menu:
                "Discutir si hay pruebas contra los jawas.":
                    playerName "¿Estás seguro de que han sido los jawas? ¿Tienes pruebas contra ellos?"
                    joe "No hay pruebas, pero han tenido que ser ellos."
                    joe "Los hutts han atacado a los moradores en el pasado, pero Jabba está muerto y ningún hutt tiene controla Tatooine desde entonces. Los monjes [bomarr] controlan su palacio, pero nunca han sido agresivos."
                    joe "¿El Imperio quiza? Son poderosos, pero nunca han tenido problemas con los tusken. ¿Quién entonces? ¿Los ermitaños inofensivos, o los borrachos de las tabernas?"
                    joe "No hay más sospechosos. Créeme, viajer[tuO]: Han sido los jawas."
                    menu:
                        "Quizá sea mejor pensárselo un poco.":
                            playerName "Quizá sea mejor pensárselo un poco, replanteárselo y estar seguro antes de actuar..."
                            joe "¿Qué? ¡Eres [tuUn] enviad[tuO] de los jawas! ¡Has venido a envenenar nuestras mentes con planes hostiles! ¡Realmente eres enemig[tuO]!"
                            play sound "sound/batalla.mp3"
                            "Los moradores de las arenas caen sobre ti en grupo. Una docena de palos gaffi te golpean, ora con la púa, ora con la porra."
                            "Entre los alaridos de los tusken, oyes disparos de rifle. Seguramente alguien te ha disparado. En este momento, todo duele tanto que ni siquiera sabes si han acertado."
                            jump HasMuerto
                            return
                        "Pedir una tregua." if primerWassak == 1:
                            playerName "¿Qué dirías a una tregua para parlamentar con los jawas?"
                            joe "¿Qué? ¡Eres [tuUn] enviad[tuO] de los jawas! ¡Has venido a envenenar nuestras mentes con planes hostiles! ¡Realmente eres enemig[tuO]!"
                            play sound "sound/batalla.mp3"
                            "Los moradores de las arenas caen sobre ti en grupo. Una docena de palos gaffi te golpean, ora con la púa, ora con la porra."
                            "Entre los alaridos de los tusken, oyes disparos de rifle. Seguramente alguien te ha disparado. En este momento, todo duele tanto que ni siquiera sabes si han acertado."
                            jump HasMuerto
                            return
                        "Desearle buena suerte.":
                            playerName "Buena suerte en tu guerra."
                            joe "Ojalá la guerra termine pronto, pero no aceptaré una derrota."
                            joe "{i}Koroght gaghgt Takt.{/i}{p}('Sea afortunada tu marcha de entre nosotros.')"
                            jump go_ZonaTusken1
                "Pedir una tregua." if primerWassak == 1:
                    playerName "¿Qué me dirías de una tregua para parlamentar con los jawas?"
                    joe "¿Qué? ¡Eres [tuUn] enviad[tuO] de los jawas! ¡Has venido a envenenar nuestras mentes con planes hostiles! ¡Realmente eres enemig[tuO]!"
                    play sound "sound/batalla.mp3"
                    "Los moradores de las arenas caen sobre ti en grupo. Una docena de palos gaffi te golpean, ora con la púa, ora con la porra."
                    "Entre los alaridos de los tusken, oyes disparos de rifle. Seguramente alguien te ha disparado. En este momento, todo duele tanto que ni siquiera sabes si han acertado."
                    jump HasMuerto
                    return
                "Desearle buena suerte.":
                    playerName "Buena suerte en tu guerra."
                    joe "Ojalá la guerra termine pronto, pero no aceptaré una derrota."
                    joe "{i}Koroght gaghgt Takt.{/i}{p}('Sea afortunada tu marcha de entre nosotros.')"
                    jump go_ZonaTusken1
        "Qué gran momento para ir a otro sitio.":
            jump go_ZonaTusken1



label hablarBob:

    # "TBA: hablarBob %(hablarBob)d. itemCabezaDroide %(itemCabezaDroide)d. crimelord1Activo %(crimelord1Activo)d."

    if hablarBob == 3:
        "Aquí no hay nadie. UOu'uu'h'rRr es ahora cacique y debe estar muy ocupado."
    else:
        show bob
        play music "music/etnica.mp3"
        "Al borde de un acantilado, un morador de las arenas solitario está tocando una marimba con su gaffi mientras contempla el paisaje. Te ve y te saluda. Incluso parece sonreír bajo su vendaje y su respirador."

    if hablarBob == 0:
        playerName "Saludos, trovador. Nunca había escuchado la música que tocas."
        tuskens "Es una historia, viajer[tuO]. Trata sobre dos hermanos, hijos de un gran jefe tusken. Se esperaba que el mayor heredase el manto de su padre."
        tuskens "Pero el hermano más joven era más agresivo, más audaz, más apuesto. El joven se entrenó como líder y como soldado, mientras su hermano dejaba pasar los años."
        tuskens "Finalmente, el hermano joven desafió a un colosal wraid, una enorme criatura del desierto. Al cazar a ese coloso, el joven alcanzó la madurez, mientras su hermano más viejo era aún un niño."
        tuskens "El hermano viejo no ansiaba el poder. No quería su nombre mentado en las leyendas, porque él habría preferido cantar las leyendas. Él era un poeta."
        tuskens "Cuando murió anciano el gran jefe, el hermano mayor no podía optar a su puesto. ¡Él ni siquiera había cazado una gran bestia! ¡Era sólo un niño! El hermano menor fue el nuevo cacique."
        tuskens "Se concedió al hermano mayor el puesto de narrador de historias. El hermano mayor estaba feliz, satisfecho con su lugar en la vida. ¿Qué crees tú que pasó entonces, viajer[tuO]?"
        playerName "Creo que llegaron tiempos difíciles. El nuevo jefe, el hermano menor, tomó una decisión que el narrador no compartía. Quizá quiso ir al sendero de guerra contra un enemigo."
        tuskens "Así es. El hermano mayor creía que su jefe se equivocaba, pero no podía demostrarlo todavía. Aunque pudiese demostrarlo, el jefe era muy testarudo. El hermano mayor no tenía apoyo para discutir con el jefe."
        playerName "Dime, narrador. ¿Qué necesitaba el narrador para conseguir ese apoyo?"
        tuskens "Si su hermano había cazado un wraid, el narrador debía cazar un monstruo aún más grande para superarle; pero tales bestias no se encuentran fácilmente; y el sarlacc es invencible."
        playerName "Gracias por tu canción y por tu relato; sé que no es costumbre contárselos a un extraño."
        tuskens "Este relato no está terminado, aún no forma parte de nuestras leyendas. No terminará pronto, ni terminará bien."
        playerName "Quizá te sorprendas, eh, ¿cuál es tu nombre?"
        tuskens "Me llamo UOu'uu'h'rRr... como el hermano mayor en mi historia."
        playerName "Sea afortunada tu marcha de entre nosotros, UOu'uu'h'rRr."
        $ hablarBob = 1

    if dragon == 1 and hablarBob == 1:
        # LO PRIMERO QUE LE ENTREGAS ES UN DRAGÓN
        playerName "{i}Aargh,{/i} UOu'uu'h'rRr. Debo contarte algo que puede animarte. Es algo que podrías incluir en tu próxima canción."
        bob "Mi canción trata de los moradores de las arenas y de los portentos en su camino. ¿Estás segur[tuO] de que tiene cabida en ella?"
        playerName "Los dragones son portentos. Hace bastantes años que apenas se dejan ver, y un dragón podría ser una oportunidad de pasar a la madurez."
        "UOu'uu'h'rRr te mira con renovada atención, inclinándose hacia adelante y con una mano en la cara."
        playerName "He encontrado un dragón krayt en el Mar de Dunas, cerca del cañón Desfiladero del Peñón Mellado. Pienso que, quizá, si un cazador tusken se pasase por allí, podría desafiarlo y ganar prestigio."
        bob "Agradezco tu ayuda, [playerName]. Recordaré tu nombre. Ahora, mis disculpas pero deseo estar en otro lugar con otra compañía."
        hide bob
        "UOu'uu'h'rRr echa a correr hacia el campamento tusken, claramente para salir. Le sigues, pero en seguida le pierdes. Se ha subido a una montura bantha con una cabriola y está cabalgando. ¡Qué rápido se mueve un bantha!"
        scene bg zona tusken 1
        $ dragon = 2
        $ hablarBob = 2
        # "TBA: hablarBob %(hablarBob)d. itemCabezaDroide %(itemCabezaDroide)d. crimelord1Activo %(crimelord1Activo)d."
        jump ZonaTusken1

    elif itemCabezaDroide == 1 and hablarBob == 1:
        # LO PRIMERO QUE LE ENTREGAS ES UNA CABEZA DE DROIDE
        bob "{i}Aargh,{/i} [playerName]. Debes saber que ya son tres las tribus que siguen a GRu'uu'h'rRr en su insensata guerra contra los jawas."
        playerName "Si condenas la guerra contra los jawas, trovador, hay algo que debes saber. Puedo probar que ni los jawas ni los granjeros de humedad os han afrontado."
        bob "El cacique GRu'uu'h'rRr no escucha cuando ha tomado una decisión, pero yo aspiro a la verdad."
        playerName "La responsable se llama Vykan Fenn. Es una jefa del crimen espacial. Secuestra a tribus enteras para liberarlas en otros planetas y que se enfrenten a los enemigos que ella elige."
        playerName "Sus secuaces son weequays. Ellos han degollado a los banthas siguiendo rituales para aplacar a sus dioses sangrientos."
        bob "Aunque nunca he conocido un weequay, he oído sobre su religión. Lo que dices tiene sentido. ¿Pero me ofreces sólo palabras?"
        show cabezadroide at left
        "Ofreces la cabeza de droide a UOu'uu'h'rRr y la activas para que muestre el holograma grabado."
        show weequay amarillo at right with dissolve
        droidemalo "Espero que estéis satisfechos. Habéis podido cazar los banthas de los moradores de las arenas para sacrificarlos a vuestros dioses."
        droidemalo "Las tribus tusken os habrían aplastado si yo no hubiese ocultado vuestra implicación. En vez de eso, yo hice que los guiaseis a una trampa para capturarles. ¿Están bien retenidos en el sótano?"
        droidemalo "Ahora los moradores se enfrentarán a los granjeros de humedad y a los jawas, y Vykan Fenn les venderá armas a todos ellos. La guerra es buen negocio."
        hide weequay with dissolve
        hide cabezadroide with dissolve
        bob "¿Te das cuenta de lo que me estás ofreciendo, [playerName]? Esto no traerá la paz. Esto sólo nos da un nuevo enemigo."
        playerName "Pero trae la paz entre tusken y jawa, ¿no es cierto?"
        bob "Ojalá fuese así. No tengo suficiente prestigio para ocupar el puesto de mi hermano. Él venció a un enorme wraid. Sólo si yo cazo a un monstruo aún más grande, podré detener la guerra."
        playerName "Sé que nunca quisiste escribir la historia con tus actos, UOu'uu'h'rRr. No todos pueden elegir su camino. Eliges sin embargo cómo recorrerlo."
        bob "Sea afortunada tu marcha de entre nosotros."
        $ itemCabezaDroide = 2
        $ hablarBob = 2
        # "TBA: hablarBob %(hablarBob)d. itemCabezaDroide %(itemCabezaDroide)d. crimelord1Activo %(crimelord1Activo)d."
        jump go_ZonaTusken2

    if dragon == 1 and hablarBob == 2:
        # HAS ENTREGADO LA CABEZA DE DROIDE, PERO ÉL NO ES CACIQUE. AHORA LE OFRECES EL DRAGÓN PARA QUE LO SEA
        bob "{i}Aargh,{/i} [playerName]. Quizá quieras saber que mi canción continúa con tristes estrofas. El hermano mayor consiguió pruebas de que su cacique se equivocaba, y se las presentó humildemente."
        bob "Era un portento que señalaba al auténtico enemigo de la tribu. Pero el cacique no quería escuchar y continuó sus preparativos obstinadamente."
        bob "Bajo los soles gemelos, el hermano mayor lamenta no tener suficientes apoyos en su tribu y ruega por que un portento se le aparezca."
        playerName "Debo contarte algo que puede animarte. Es algo que podrías incluir en tu próxima canción."
        bob "Mi canción trata de los moradores de las arenas y de los portentos en su camino. ¿Estás segur[tuO] de que tiene cabida en ella?"
        playerName "Los dragones son portentos. Hace bastantes años que apenas se dejan ver, y un dragón podría ser una oportunidad de pasar a la madurez."
        "UOu'uu'h'rRr te mira con renovada atención, inclinándose hacia adelante y con una mano en la cara."
        playerName "He encontrado un dragón krayt en el Mar de Dunas, cerca del cañón Desfiladero del Peñón Mellado. Pienso que, quizá, si un cazador tusken se pasase por allí, podría desafiarlo y ganar prestigio."
        bob "Agradezco tu ayuda, [playerName]. Recordaré tu nombre. Ahora, mis disculpas pero deseo estar en otro lugar con otra compañía."
        playerName "Antes de partir, dime, UOu'uu'h'rRr, ¿merecen los jawas saber que ha terminado su guerra?"
        bob "Los jawas merecen más que eso. Los moradores serán desde hoy amigos de los jawas y compensarán sus pérdidas, cuando hayamos vencido a esa Vykan Fenn."
        bob "Toma el estandarte de Fuerte Tusken, [playerName]. Dáselo a los jawas. Eso demostrará que no tenemos ya nada contra ellos. Gracias por tu ayuda."
        show estandarte at right
        playerName "Sea afortunada tu marcha de entre nosotros."
        hide bob
        "UOu'uu'h'rRr echa a correr hacia el campamento tusken, claramente para salir. Le sigues, pero en seguida le pierdes. Se ha subido a una montura bantha con una cabriola y está cabalgando. ¡Qué rápido se mueve un bantha!"
        scene bg zona tusken 1
        $ dragon = 2
        $ crimelord1Activo = 2
        $ itemEstandarte = 1
        $ hablarBob = 3
        # "TBA: hablarBob %(hablarBob)d. itemCabezaDroide %(itemCabezaDroide)d. crimelord1Activo %(crimelord1Activo)d."
        jump ZonaTusken1

    elif itemCabezaDroide == 1 and hablarBob == 2:
        # HAS ENTREGADO EL DRAGÓN ANTES, ASÍ QUE ES CACIQUE. AHORA LE ENTREGAS LA CABEZA DE DROIDE
        bob "{i}Aargh,{/i} [playerName]. Debes saber que ahora UOu'uu'h'rRr es, a su pesar, el cacique de la tribu. Otras tres tribus siguen a UOu'uu'h'rRr en la guerra contra los jawas."
        playerName "Si condenas la guerra contra los jawas, cacique, hay algo que debes saber. Puedo probar que ni los jawas ni los granjeros de humedad os han afrontado."
        bob "Tienes mi atención, que es más de lo que te habría dado GRu'uu'h'rRr, pero mi paciencia no es mucho mayor que la suya."
        playerName "La responsable se llama Vykan Fenn. Es una jefa del crimen espacial. Secuestra a tribus enteras para liberarlas en otros planetas y que se enfrenten a los enemigos que ella elige."
        playerName "Sus secuaces son weequays. Ellos han degollado a los banthas siguiendo rituales para aplacar a sus dioses sangrientos."
        bob "Aunque nunca he conocido un weequay, he oído sobre su religión. Lo que dices tiene sentido. ¿Pero esperas que el antiguo narrador convenza a su ejército sólo con palabras"
        show cabezadroide at left
        "Ofreces la cabeza de droide a UOu'uu'h'rRr y la activas para que muestre el holograma grabado."
        show weequay amarillo at right with dissolve
        droidemalo "Espero que estéis satisfechos. Habéis podido cazar los banthas de los moradores de las arenas para sacrificarlos a vuestros dioses."
        droidemalo "Las tribus tusken os habrían aplastado si yo no hubiese ocultado vuestra implicación. En vez de eso, yo hice que los guiaseis a una trampa para capturarles. ¿Están bien retenidos en el sótano?"
        droidemalo "Ahora los moradores se enfrentarán a los granjeros de humedad y a los jawas, y Vykan Fenn les venderá armas a todos ellos. La guerra es buen negocio."
        hide weequay with dissolve
        hide cabezadroide with dissolve
        bob "¿Te das cuenta de lo que me estás ofreciendo, [playerName]? Esto no trae la paz. Esto sólo nos da un nuevo enemigo."
        playerName "Pero trae la paz entre tusken y jawa, ¿no es cierto? Dime, UOu'uu'h'rRr, ¿merecen los jawas saber que ha terminado su guerra?"
        bob "Los jawas merecen más que eso. Los moradores serán desde hoy amigos de los jawas y compensarán sus pérdidas, cuando hayamos vencido a esa Vykan Fenn."
        bob "Toma el estandarte de Fuerte Tusken, [playerName]. Dáselo a los jawas. Eso demostrará que no tenemos ya nada contra ellos. Gracias por tu ayuda."
        show estandarte at right
        playerName "Sé que nunca quisiste escribir la historia con tus actos, UOu'uu'h'rRr. No todos pueden elegir su camino. Eliges sin embargo cómo recorrerlo."
        playerName "Sea afortunada tu marcha de entre nosotros."
        $ itemCabezaDroide = 2
        $ crimelord1Activo = 2
        $ itemEstandarte = 1
        $ hablarBob = 3
        # "TBA: hablarBob %(hablarBob)d. itemCabezaDroide %(itemCabezaDroide)d. crimelord1Activo %(crimelord1Activo)d."

    elif hablarBob < 3:
        playerName "Me gustaría ofrecerte mi apoyo en tu gesta, UOu'uu'h'rRr. Intentaré ayudarte a conseguir lo que necesitas."
        bob "No sé de qué me hablas. Yo sólo compongo un cantar sobre los moradores de las arenas y los prodigios que encuentran en su camino."
        jump go_ZonaTusken2
        
#    "Sea afortunada tu marcha de entre nosotros."
#    No te preocupes: Si Bob se está yendo para ir al dragón, hay un JUMP y no pasas por aquí después de haberle ocultado.
    
    jump go_ZonaTusken2