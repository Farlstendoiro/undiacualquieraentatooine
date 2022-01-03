# opening

label alInicio:

# introduce el nombre del personaje
# (Strip sólo elimina los espacios, no puntos y cosas raras)

    scene bg disclaimer
    $ renpy.pause(35)

    play music "music/inicial.mp3"
    scene bg inicio
    show jako with dissolve

    droide "Zzz..."
    droide "...zzz..."
    droide "...zzzaludozzz... perzzzeptorrr..."
    droide "Yo zzzoy el droide azzzignado a ti... Me llamo J4-KO."
    playerName "Así que K.O..."
    jako "Puedezzz llamarme Jako."
    jako "¿Cómo debo llamarte?"
    

    # introduce el nombre del personaje
    # (Strip sólo elimina los espacios, no puntos y cosas raras)

    $ playerName = renpy.input("¿Cómo debo llamarte?","Farlstendoiro")

    if playerName == "Jako":
        jako "No, hay una confuzzzión. {b}Yo{/b} zzzoy Jako."
        $ playerName = ""

    while playerName == "":
        $ playerName = renpy.input("Error: Introduzzze tu nombre, por favor.","Farlstendoiro")

    jump eligeTuAspecto


label eligeTuAspecto:

    $ playerName  = playerName.strip()

    jako "Encantado de conozzzerte, [playerName]."

    # introduce tu aspecto

    scene bg_eligecabezas
    show jako at left
    jako "Para ajuzzztar mizzz zzzenzzorezzz, por favor identifica cuál de ézzztozzz ezzz tu azzzpecto... Ezzz una medida de zzzeguridazzz ezzztándar..."

    window hide None

    $ result = renpy.imagemap("bg_eligecabezas.png","bg_eligecabezasselect.png",[(590, 66, 765, 231, "1"),(883, 66, 1059, 231, "2"),(590, 299, 765, 461, "3"),(883, 299, 1059, 461, "4")])

    if result == "1":
        jako "Azzpecto elegido. Varón humano."
        $ tuAspecto = 1

    if result == "2":
        jako "Azzpecto elegido. Mujer humana."
        $ tuAspecto = 2

    if result == "3":
        jako "Azzpecto elegido. Varón alienígena."
        $ tuAspecto = 3

    if result == "4":
        jako "Azzpecto elegido. Mujer alienígena."
        $ tuAspecto = 4

#   IMPORTANTE:

    jump eligeTuNave
    
label eligeTuNave:

# PRIMERO LOS DETALLES DE ELIGE TU ASPECTO, TU ARTÍCULO, TU PRONOMBRE

# ELEGIR CABEZAS. NO ESTÁ HECHO.

# DE MOMENTO: 1 VARÓN HUMANO. 2 MUJER HUMANA. 3 VARÓN MONCAL. 4 MUJER TWI'LEK 
#    $ tuAspecto = renpy.imagemap("choosechar_ground.png","choosechar_hover.png",[(468,94, 683,290, 1), (468,382, 683,577 ,2), (853,94, 1068,290 ,3), (853,382, 1068,577 ,4)])

    if tuAspecto < 1:
        $ tuAspecto = 1
    elif tuAspecto > 4:
        $ tuAspecto = 1
        
    # Aquí los determinantes:
    if tuAspecto == 2 or tuAspecto == 4:
        $ tuEl = "la"
        $ tuUn = "una"
        $ tuUnMayus = "Una"
        $ tuO = "a"
        $ tuPronombre = "ella"
        $ tuPronombreMayus = "Ella"
        $ tuEste = "esta"
        $ tuEse = "esa"
        $ tuLe = "la"
        $ tuEmpollon = "empollona"
    else:
        $ tuEl = "el"
        $ tuUn = "un"
        $ tuUnMayus = "Un"
        $ tuO = "o"
        $ tuPronombre = "él"
        $ tuPronombreMayus = "Él"
        $ tuEste = "este"
        $ tuEse = "ése"
        $ tuLe = "le"
        $ tuEmpollon = "empollón"

        
    if tuAspecto < 3:
        $ tuEspecie = "humano"
    elif tuAspecto == 3:
        $ tuEspecie = "calamariano"
    else:
        $ tuEspecie = "twi'lek"
        
    # introduce el nombre de TU NAVE
    # (Strip sólo elimina los espacios, no puntos y cosas raras)

    scene bg tu nave
    show jako
    $ tuNave = renpy.input("¿Y cómo quierezzzz llamar a la nave que nos han azzzignado?","Shantipole")

    if tuNave == "Tormenta de Melocotón" or tuNave == "Halcón Milenario" or tuNave == "Esclavo I":
        jako "Ezzze nombre ya ezzztá regizzztrado. Por favor, elige otro."
        $ tuNave = ""

    while tuNave == "":
        $ tuNave = renpy.input("Error: Introduzzze el nombre de la nave.","Shantipole")
        
    $ tuNave = tuNave.strip()
    $ tuNave = "{i}" + tuNave + "{/i}"
    jako "Nombre regizzztrado de la nave: [tuNave].{p}Podemozzz empezzzar."

    hide jako

    jump personajeDefinido

label personajeDefinido:

# finca Sedi Fisk Mensaje
# Calles Mos mensaje
# Cantina mensaje
# hangar mensaje

    # Opening, escena especial.
    $ renpy.movie_cutscene("videos/opencrawl.ogv")

    # LAS LINEAS DEBERÍAN SER play movie "start.ogg" loop Y DESPUÉS show movie with fade"
    # "El texto espacial es algo así."
    # "STAR WARS: Un día cualquiera en Tatooine (Y HACERLO CON ZZZETAS)"
    # "Han pasado varias semanas desde la batalla de Endor. El emperador ha muerto sin heredero claro, pero el Imperio tiene todavía la superioridad militar y casi todos los sistemas estratégicos. La Alianza Rebelde está lejos de acabar con sus enemigos y terminar así la guerra."
    # "Los imperiales también tienen sus problemas: Cada vez más, este ministro y aquel general deciden escindirse y autoproclamarse señor de la guerra y líder de su pequeña potestad personal, tras lo cual se niega a enviar refuerzos a los que sólo un par de días antes eran sus aliados de toda la vida."
    # "La guerra de las galaxias afecta a prácticamente todos los habitantes de cualquier momento en sus vidas diarias, pese a que muchos de ellos simplemente quieren seguir con sus vidas, mantenerse al margen de estos colosales conflictos y escribir sus propias historias. Ésta es una de esas historias..."
    # "Un pequeño droide aparece viajando por el espacio, aterriza en Tatooine. Posiblemente en el puerto. Jako manda un mensaje. Enfocamos finca de Sedi Fisk por dentro***"
    # "Escena espacial. La tienes que meter en un archivo de video, formato OGV, en imágenes. Digamos que fuese pyke16.ogv"
    # "Con este código, se ejecuta una vez, a pantalla completa, hasta que termine o hasta que el usuario haga clic."
    # $ renpy.movie_cutscene("pyke16.ogv")

    scene bg sedi fisk oscuro
    with dissolve
    play music "music/ambiental.mp3"
    
    playerName "Grabando. Trabajo de campo de [playerName] en Tatooine para la investigación sobre ratas womp. Día ocho."
    playerName "Estoy en las ruinas de la finca de Sedi Fisk. Su estado respalda los rumores de que Fisk se levantó un día hace cinco años y se fue de su mansión sin decir nada a nadie."
    playerName "Hay daños y señales de deterioro, pero pocas de violencia. Restos palos gaffi, el arma de los moradores de las arenas; pero el escaneo del polvo dice que son de hace sólo tres años. Quizá se llevaron algo."
    playerName "Sin duda también hubo saqueadores jawas, porque no hay casi tecnología. Pero ni ellos ni los moradores me contarán lo que han descubierto. No puedo saber qué personas estuvieron aquí." 
    playerName "No todas las formas de vida abandonaron la finca. El alien que he venido a estudiar lleva años aquí, como demuestra la capa de guano que cubre el suelo: Hay restos de hace cuatro años, y otros tan frescos como para ser de esta mañana."
    scene bg sedi fisk linterna
    play sound "sound/ratas.ogg"
    playerName "Mis amiguitas han elegido este lugar porque sigue bajo techo: Ellas creen dormir a la sombra en una cueva durante las horas de dos soles abrasadores."
    playerName "Si dirijo una barra brillante a una zona oscura, aquéllas a las que la luz toca directamente se despiertan y se ponen violentas al ser descubiertas. Las otras, aún las más cercanas, siguen durmiendo y no reaccionan."
    scene bg sedi fisk oscuro
    playerName "Sólo en este edificio hay unos sesenta, en tres grupos distintos. Las manadas variadas, peleadas entre sí, también proporcionan una variabilidad genética..."
    show mensajero at left
    playerName "¿Qué? Un droide mensajero interestelar... Debe tener un mensaje para mí..."
    show jako amarillo with dissolve
    jako "Zzzaludozzz, [playerName]. Zzze ha rezzzibido un menzzzaje zzzubezzzpazzzial para ti, marcado como urgente. ¿Quierezzz que te lo pazzze?"
    playerName "Claro, Jako. Visualízamelo.{p}Eh, detener grabación."
    hide jako with dissolve
    show keyan amarillo with dissolve
    playerName "Oh-oh. Es el jefe."
    keyan "[playerName], tengo una misión importante para ti. Necesito que pongas rumbo al sector Moddell de inmediato. Me reuniré contigo allí."
    show ewok at right with dissolve
    playerName "Maldita sea. ¿Otra vez esos ursinos bajitos de las capuchas? Desde hace unas semanas, su sistema está atrayendo turistas sin dos neuronas por grupo..."
    keyan "Deja lo que sea que estás haciendo. Esto es prioritario. Ve a tu nave y despega lo antes posible. Recibirás nueva información cuando llegues al sistema Annaj. Es todo lo que puedo decirte por ahora."
    hide ewok
    playerName "Eso me queda donde Mandalore el Indómito perdió el casco. Ni me imagino cuántas hiperrutas tendré que recorrer... Menos mal que tengo un droide que pilota..."
    keyan "Lo siento, no tengo elección. Sé que has dedicado mucho esfuerzo al asunto de las ratas womp. Espero que tengas suficiente información para darme algo que publicar. Corto y cierro."
    hide keyan with dissolve
    playerName "Este tipo nunca ha entendido la importancia del trabajo de campo... En fin..."
    show jako amarillo with dissolve
    playerName "Jako, pon a punto la nave. Me vuelvo al puerto espacial de Mos Eisley y despegaremos en cuanto yo esté a bordo."
    jako "Zzzí, [playerName], pero lozzz orgánicozzz como tú no pueden entrar a lozzz muellezzz hazzzta que abran por la mañana en horario comerzzzial. Nezzzezzzitazzz que la torre de control autorizzze tu dezzzpegue."
    playerName "Qué incivilizados. Bueno, buscaré algo que hacer hasta entonces."

    scene bg calle principal with fade

    "Calle principal de Mos Eisley. El hangar está a apenas unos pasos de aquí. Exploras tus alrededores en busca de algún sitio donde puedas pasar un rato."
    playerName "Taberna de la Duquesa que Ríe. Al menos esto ya está abierto. Tomaré algo."
    jako "¿Con quién hablazzz? ¿Te lo cuentazzz a ti mizzzm[tuO]? ¿Ezzz que no zzzabezzz lo que vazzz a hazzzer?"
    playerName "Comunicadores: Ignorar a Jako durante una hora."

    scene bg cantina
    show kabe at left
    show camarero

    "Los precios anunciados parecen razonables, el local está bastante limpio y se mantiene abierto las 23 horas locales. Parece una buena elección."
    camarero "Hola, viajer[tuO] espacial. Bienvenid[tuO] a la Duquesa que Ríe. Soy la Duquesa. ¿Qué te pongo?"
    playerName "Hola, viajera de Polis Massa. Ponme un jugo jawa para hacer tiempo."
    camarero "Marchando jugo jawa y algo de conversación. ¿Eres un piloto espacial? ¿Carguero independiente?"
    playerName "Curiosa actitud la tuya, Duquesa. Muchos pilotos aterrizan en sitios como Tatooine para escapar de sus pasados más que contar sus orígenes."
    playerName "Tú misma eres una kallidahin de Polis Massa. Rara vez se ve a tu especie en el Borde Exterior. Seguro que muchos quieren conocer tus raíces."
    camarero "¿Eres detective?"
    playerName "No hago ese tipo de investigación. Soy xenobiólog[tuO]. He venido a Tatooine a estudiar las ratas womp."
    camarero "¡Pero si son una plaga! Animales asquerosos e inmundos."
    playerName "Exacto. Pretendo ir a una empresa médica como BioTech o Chiewab e intenter convencerles para que utilicen mis estudios y fabriquen repelentes o les de un uso comercial a las ratas."
    camarero "Eh, eso es interesante. Atraería más naves al planeta, y vendrían con tripulantes sedientos."
    playerName "Pero no debería aburrirte con batallitas de viajer[tuO] espacial. Seguro que las oyes constantemente."
    camarero "Ah, si no me gustase oírlas, no me dedicaría a esto."
    "Un par de horas después..."
    playerName "Bueno, ya deben haber abierto los hangares. Me voy a mi nave. Gracias por el trago."
    camarero "Quizá volvamos a coincidir, viajer[tuO] espacial."

    scene bg hangar
    with fade
    show funcionario

    show trooper at left
    show trooper2 at right

    "Has llegado al hangar donde has dejado tu nave, pero hay gente esperándote, y ninguno de ellos es tu droide piloto."
    playerName "Buenos días, amable oficial imperial. Gracias por custodiar mi nave espacial contra posibles problemas. Si me disculpa, quisiera iniciar mi viaje. Aquí tengo mi permiso de despegue autorizándome a abandonar el planeta."
    funcionario "Eso no va a ser posible, [playerName]. Me temo que hay varios asuntos que resolver."
    playerName "¿Perdón?"
    funcionario "Hemos confirmado que usted es [playerName] y su nave es {i}[tuNave]{/i}. Incluso sabemos que el droide a bordo es un dron trabajador J4 de Roche designado J4-KO."
    playerName "Es un diseño de clase tres con capacidades técnicas, y es mi piloto. Llamarlo 'dron' es insultante."
    funcionario "El Imperio encuentra insultantes otras cosas. La delincuencia es un insulto a mi uniforme y no tengo paciencia para algo así."
    playerName "¿Se me acusa de algo?"
    funcionario "Su nave, o una con el mismo código transpondedor, ha sido identificada en Ryloth y se la relaciona con un caso de tráfico de... mercancías ilegales."
    playerName "Ryloth exporta especia ryll y... esclavos twi'lek. ¿Cree el Imperio que estoy implicad[tuO] en un caso de contrabando?"
    funcionario "Quizá no. Es posible que alguien haya utilizado su nave saberlo. De momento la acusación es sólo contra el {i}[tuNave]{/i}. Pero, mientras la investigación siga abierta, ni esta nave ni su contenido se van a mover del hangar, ni usted va a poder subir a bordo."
    funcionario "Nuestra gente está haciendo un escaneo exhaustivo del casco y de las cubiertas, en busca de pruebas. Hemos pedido un equipo más avanzado al sistema Arkanis, para acelerar el procedimiento. De momento, hemos hecho un descubrimiento muy interesante..."
    playerName "No tengo nada que ocultarles. Mi cargamento son muestras orgánicas que no les resultarán interesantes. Tengo varias ratas womp de diversos tipos en la bodega, ¡pero no las puedo dejar ahí indefinidamente!"
    funcionario "No, no hay nada contra usted, [playerName]. Pero hemos descubierto que el oscilador de cristal del {i}[tuNave]{/i} está roto. Así no puede regular la potencia del vehículo. Hasta que reemplace esa pieza, {i}[tuNave]{/i} no puede despegar."
    funcionario "El fallo ha sido por mala calidad. Podría aprovechar el tiempo de espera en buscar un repuesto en tiendas locales."
    playerName "Vaya, pues yo tenía prisa por irme..."
    funcionario "Su permiso de despegue no aparece en nuestras bases de datos. O se ha tramitado erróneamente, o es una falsificación. Debe pasarse por la oficina imperial para resolverlo."
    playerName "¡Oh, no me {i}kriff!{/i}"
    playerName "Entonces necesito: Un nuevo oscilador de cristal; resolver el fallo de mi permiso de despegue; y que cierren la investigación abierta sobre mi nave."
    playerName "Veamos qué llevo encima: Algo de dinero y un datapad con declaraciones de unas cuantas personas a las que he estado entrevistando estos últimos días."

    
    while varComodin == 0:
        menu:

            "Ir a otro lugar.":
                playerName "Hora de marcharse. Veamos a dónde se puede ir desde aquí..."
                $ varComodin = 1
    
    $ varComodin = 0
    
    jump go_Hangar
    
label creditos:
    
#    scene bg cr calle principal
#    show kaminoano at left
#    show bob at left
#    show ewok at left
#    show ratamuerta
#    show trooper
#    show r5d4
#    show bandido at right
#    show wassak at right
#    $ renpy.pause(3)
#    ""

    scene bg cr producido
    $ renpy.pause(5)
    
    scene bg cr callejon
    show contrabandista at left
    $ renpy.pause(5)

    scene bg cr eligecabezas
    $ renpy.pause(5)

    scene bg cr espacio
    show mensajero at left
    $ renpy.pause(5)

    scene bg cr inicio
    show jako at right
    $ renpy.pause(5)

    scene bg cr palacio jabba ext
    show graf at right
    $ renpy.pause(10)

    scene bg cr zona tusken 1
    show bob at right
    $ renpy.pause(5)

    scene bg cr muerte
    $ renpy.pause(10)

    scene bg cr tu nave
    show belia at right
    $ renpy.pause(5)

    scene bg cr oficina imperial
    show funcionario at left
    $ renpy.pause(5)
    
    scene bg cr espacio vacio
    $ renpy.pause(5)
    
    scene bg cr mos gamos
    $ renpy.pause(5)
    
    scene bg final

    wassak "Es un RA-7 de hace tres años. Encontré el cuerpo en Mos Gamos. Los moradores nos han dado la cabeza. Es el mismo original, fíjate en los arañazos y en el desgaste."
    wassak "Pero está hecho un desastre. El vocabulador está quemado y soldado así que no lo puedo reemplazar, los interfaces están rotos... No tiene forma de comunicarse."
    droidemalo "(¿Qué?)"
    wassak "Lo único que puedo hacer con él es ponerle un restrictor y encargarle el trabajo pesado. Limpiar establos y cargar chatarra."
    wassak "Por eso no me he molestado en borrarle la memoria. ¿Para qué? Si lo dejo así, podrá trabajar para el clan unos ochenta o noventa años."
    droidemalo "(¿¡QUÉ!?)"
    
    scene bg cr meriner
    $ renpy.pause(5)
    
    scene bg cr skippy
    $ renpy.pause(10)
    
    scene bg calle principal
    show trooper at left
    show trooper2 at right
    show trooper3
    trooper "Ya está. La partida ha terminado. Retírese, [playerName], o tendremos que arrestarle."