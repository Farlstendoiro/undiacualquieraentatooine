label go_CallePrincipal:

    menu:
        "Ir a tu hangar.":
            jump Hangar
        "Ir a la cantina.":
            jump Cantina
        "Ir a la Oficina Imperial.":
            jump OficinaImperial
        "Ir a las afueras de la ciudad.":
            jump TiendaJawa
        "Cancelar.":
            jump CallePrincipal

label go_Cantina:

#    "jugarLabria %(jugarLabria)d." 
    menu:
        "Ir a la trastienda." if jugarLabria > 2:
            jump Trastienda
        "Salir a la calle.":
            jump CallePrincipal
        "Cancelar.":
            jump Cantina

label go_Hangar:

    menu:
        "Ver declaración de Wenny Boggs.":
            scene bg hangar with None
            show boggs amarillo with dissolve
            boggs "Me llamo Wenny Boggs. Nací en Tatooine y sé que aquí moriré. Soy un granjero de humedad, como lo fue mi padre y el padre de mi padre."
            boggs "He aprendido a proteger mi granja de ladrones y bandidos, de moradores de las arenas y de alimañas."
            boggs "En el Colectivo de Granjas de Humedad, a veces hemos contratado cazadores para ocupares de los animales que dañan nuestro equipo."
            boggs "A veces, yo mismo he cogido mi rifle y mi deslizador, y he buscado manadas de ratas womp que ponían en peligro mi medio de vida."
            boggs "No busco problemas con nadie. Bueno, excepto con Darklighter. Si él sigue expandiendo su territorio, pronto todas las granjas le pertenecerán."
            boggs "¡Hasta los moradores de las arenas tienen un código de comportamiento! Darklighter devora todo lo que puede encontrar. Es como las ratas womp."
            boggs "Oh, no encontrarás ratas womp en las granjas de humedad, porque las eliminamos a conciencia y nos libramos de sus cadáveres. No hay nada, más allá de algún granjero que quiera enseñarte una rata especial que haya encontrado."
            boggs "Los moradores de las arenas son igual de drásticos matando las ratas. Cuidan mucho sus pocos recursos y no aceptan a esas alimañas. Jabba, por el contrario, no era tan limpio y su palacio estaba lleno de sabandijas... y de ratas womp también."
            boggs "No verás ratas en las ruinas de Mos Gamos, más allá de las granjas. No sé qué le hicieron a ese pueblo, pero hasta las ratas lo evitan. El borrachín Gor Kolomo hablaba de ratas de Mos Gamos que lanzan relámpagos desde los ojos, pero Kolomo no es de fiar."
            boggs "El mejor lugar para encontrar ratas womp es la zona que menos bípedos frecuentan: El Mar de Dunas, más allá del palacio... del {i}antiguo{/i} palacio de Jabba."
            boggs "Creo eso que es todo lo que te puedo decir. Buena suerte en tus viajes, foraster[tuO]."
            hide boggs with dissolve
        "Ver declaración de Ghana Gleemort.":
            scene bg hangar with None
            show ghana amarillo with dissolve
            ghana "Soy Ghana Gleemort. Antes trabajaba como guardia para Jabba el Hutt, pero decidí desertar."
            ghana "La humana llamada Profetisa me reveló, por cien créditos, que el poder de Jabba llegaba a su fin y que me arrastraría en su caída."
            ghana "Así que me acerqué a los monjes [bomarr] del palacio. Ellos han acogido fugitivos y criminales en el pasado y me ayudaron..."
            ghana "¿Ah, no es esto lo que te interesa? Es lo que me suele preguntar la gente. ¿Ratas womp? Sí, sí."
            ghana "Desde la muerte de Jabba, trabajo como cazador. Murciélagos-dragón, wraids, ese tipo de cosas me dan para comer varios meses."
            ghana "Normalmente el problema que tiene la gente son las ratas womp. Una rata es poca cosa, pero si son muchas, pueden destrozar tu cosecha."
            ghana "Con Jabba, el trabajo era más complicado, pero aprendí algo útil para un cazador: Averigua de dónde viene tu presa. Rastréala."
            ghana "He aprendido a rastrearlas. Este hocico no está ahí sólo para hacer bonito. Las ratas tiene un olor característico por sus heces."
            ghana "Por eso no creo a Gor Kolomo. Él habla de ratas que lanzan rayos iónicos por los ojos, pero él no olía a rata. No había {i}estado{/i} con ratas."
            ghana "¿Ratas inteligentes? La rata media es bastante tonta, pero algunas se han escapado de trampas cerradas o me han pillado por sorpresa."
            ghana "Sobre todo conozco a las womp pantanosas de Cularin. Oyen la vibración de tus repulsores y cuando te acercas, caen sobre ti en oleadas."
            ghana "Ah, sí, te aseguro que las womp del sistema Cularin son muy parecidas a las de aquí. Huelen igual, saben igual."
            ghana "He visto ratas extrañas. He visto ratas verdes de tres metros y medio de altura en el Mar de Dunas. Cacé una viva para un tal Tikfolpaack."
            ghana "No sé quién es... Un cliente. Era un calamariano que trabajaba de biólogo para el Imperio. Metió la rata en una nave y se la llevó."
            ghana "Sí, claro que puedes escanear mis trofeos y equipo. Me has pagado unas buenas copas, y el negocio es lento esta temporada."
            ghana "Hay demasiada inestabilidad desde la muerte de Jabba. Hasta que haya un jefe principal del crimen, Tatooine será un desastre. Quizá me vaya..."
            hide ghana with dissolve
        "Ver declaración de Wassak.":
            scene bg hangar with None
            show wassak amarillo with dissolve
            wassak "M'um m'aloo. Yo, Wassak. Oye, ¿cuánto pides por el grabador?"
            wassak "¿No lo vendes? Oh. ¿Y si te ofrezco unos macrobinoculares y un par de medpacs casi sin estrenar?"
            wassak "(Sigh) Yo, Wassak, del clan Nkik."
            wassak "Paso mucho tiempo en el desierto, buscando tesoros. He visto muchas ratas womp. Tengo incluso un bláster para protegerme."
            "Wassak levanta sus manos mostrando los dedos."
            wassak "Hace diez veces cuatro soles (dos soles por día), yo me fijé en una pieza de tecnología medio enterrada en una duna."
            wassak "Eran los restos un probot Víbora de Arakyd. Roto, inoperativo, echando chispas, apagado. ¡Yo tenía que echar mano de ese tesoro!"
            wassak "Por supuesto para devolvérselo a sus legítimos propietarios, las autoridades imperiales. Ésa era mi motivación."
            wassak "Mientras yo iba hacia allí, la arena escupió cuatro ratas womp. Corrieron hacia mí y me atacaron. ¡Intentaban impedirme llegar al droide!"
            wassak "Dos de ellas rodearon el armazón del droide para arrastrarlo mientras las otras se me acercaban. Nunca había visto tanta coordinación en ratas."
            wassak "Vi que las que iban a por mí tenían una mirada muy inteligente, ¡y pulgares! Las ratas womp no tienen pulgares."
            wassak "Antes de tenerlas cerca, yo saqué mi bláster. Las ratas se detuvieron, como si supieran que ese objeto cambiaba las reglas del juego."
            wassak "Una de las ratas cercanas me atacó. Le disparé a quemarropa y la maté. La otra rata cercana se detuvo y silbó. ¡Silbó!"
            wassak "Las ratas del fondo dejaron de arrastrar al droide y las tres fueron donde su colega caído."
            wassak "A partir de ese momento, ignoraron al droide, recogieron el cadáver y se retiraron. Yo estaba demasiado sorprendido para detenerles."
            wassak "Cuando ya no las vi, recogí el droide sonda. Lo desmonté y... lo devolví en la Oficina Imperial."
            $ visteDeclaracionWassak = 1
            hide wassak with dissolve
#        "TBA. Comunicar con Jako.":
#            "Comunicando con Jako."
        "Ir a la calle principal.":
            jump CallePrincipal
        "Ir a otro hangar cercano.":
            jump OtroHangar
        "Subir a tu nave." if yaPuedesIrATuNave == 1:
            jump TuNave
        "Cancelar.":
            jump Hangar

label go_OficinaImperial:

    menu:
        "Ir a la calle principal.":
            jump CallePrincipal
        "Cancelar.":
            jump OficinaImperial

label go_Trastienda:

    menu:
        "Volver a la cantina.":
            jump Cantina
        "Salir por la puerta de servicio." if crimelord2Activo == 1:
            jump Callejon
        "Cancelar.":
            jump Trastienda

label go_OtroHangar:

    menu:
        "Ir al hangar de tu nave.":
            jump Hangar
        "Cancelar.":
            jump OtroHangar

label go_Callejon:

    menu:
        "Ir a la calle principal.":
            jump CallePrincipal
        "Cancelar.":
            jump Callejon

label go_CasaGraf:

    menu:
        "Ir a la finca de Sedi Fisk.":
            jump SediFisk
        "Cancelar.":
            jump CasaGraf

label go_SediFisk:

    menu:
        "Ir a las afueras de la ciudad.":
            jump TiendaJawa
        "Ir hacia el Palacio de Jabba el Hutt.":
            jump PalacioJabbaExt
        "Ir a casa de Hawk Hyperhalo." if preguntarPermisoEnCantina == 2:
            jump CasaGraf
        "Cancelar.":
            jump SediFisk

label go_TiendaJawa:

    menu:
        "Ir hacia la ciudad.":
            jump CallePrincipal
        "Ir hacia la finca de Sedi Fisk.":
            jump SediFisk
        "Ir hacia las granjas de humedad.":
            jump Granjas
        "Ir hacia las Llanuras de Jundlandia.":
            jump ZonaTusken1
        "Cancelar.":
            jump TiendaJawa

label go_ZonaTusken1:

    menu:
        "Volver hacia la ciudad.":
            jump TiendaJawa
        "Adentrarse en las Llanuras de Jundlandia.":
            jump ZonaTusken2
        "Cancelar.":
            jump ZonaTusken1

label go_ZonaTusken2:

    menu:
        "Regresar hacia la civilización.":
            play music "music/ambiental.mp3"
            jump ZonaTusken1
        "Cancelar.":
            jump ZonaTusken2

label go_RecientesAtaques:

# Ir hacia Mos Gamos no depende de una variable porque en cuanto llegues, te dan un mensaje y puedes ir."
    menu:
        "Volver a las granjas de humedad.":
            jump Granjas
        "Ir hacia Mos Gamos.":
            jump MosGamos
        "Cancelar.":
            jump RecientesAtaques

label go_MosGamos:

    menu:
        "Volver a la zona atacada por los tusken.":
            jump RecientesAtaques
        "Cancelar.":
            jump MosGamos

label go_PalacioJabbaExt:

    menu:
        "Volver a la finca de Sedi Fisk.":
            jump SediFisk
        "Alejarse hacia el Mar de Dunas." if asustasteBandido == 1:
            jump RutaDesierto1
        "Entrar en el Palacio de Jabba (!!!).":
            jump PalacioJabbaInt
        "Cancelar.":
            jump PalacioJabbaExt

label go_PalacioJabbaInt:

    menu:
        "Salir del Palacio por la puerta principal.":
            jump PalacioJabbaExt
        "Perseguir al Bandido hacia el Mar de Dunas." if asustasteBandido == 1 and bandidoCapturado == 0:
            "Desde las ventanas del Palacio de Jabba, puedes ver el rastro claro de una moto-jet. Las arenas se han quemado y cristalizado a su paso."
            playerName "Qo ha huído hacia el Mar de Dunas. {i}Tengo{/i} que perseguirle."
            monje1 "Lo siento, [playerName]. Tenemos un eopie; puedes usarlo como montura."
            hide monje2
            scene bg ruta desierto 1
            show monje1 at left
            show eopie at right with dissolve
            monje1 "En las arenas, el eopie es más versátil que una moto-jet y ganarás terreno rápidamente."
            "Sin más palabras reconocibles, te ahorcajas en la grupa de la bestia. Ahora puedes usar el eopie para recorrer la zona del Mar de Dunas."
            hide eopie
            jump RutaDesierto1
        "Salir hacia el Mar de Dunas." if asustasteBandido == 1 and bandidoCapturado == 1:
            "Pones rumbo hacia el Mar de Dunas, donde estuviste no hace mucho para capturar al bandido Thondo Qo."
            jump RutaDesierto1
        "Cancelar.":
            jump PalacioJabbaInt

label go_RutaDesierto1:

# Esto es sólo desierto.
    menu:
        "Volver al Palacio de Jabba.":
            jump PalacioJabbaExt
        "Adentrarse más en el Mar de Dunas.":
            jump RutaDesierto2
        "Cancelar.":
            jump RutaDesierto1

label go_RutaDesierto2:

# Es cosa tuya fijarte en la cabaña del hermitaño, pero no en el árbol de movimiento
    menu:
        "Retroceder en dirección al Palacio de Jabba.":
            jump RutaDesierto1
        "Adentrarse aún más en el Mar de Dunas.":
            jump RutaDesierto3
        "Cancelar.":
            jump RutaDesierto2

label go_RutaDesierto3:

# Aquí el dragón te bloquea
    menu:
        "Volver hacia la civilización.":
            jump RutaDesierto2
        "Adentrarse más allá de la guarida del dragón." if dragon == 2:
            jump RutaDesierto4
        "Cancelar.":
            jump RutaDesierto3

label go_RutaDesierto4:

# Es cosa tuya fijarte en los activos rebeldes; una vez más, no en el árbol de movimiento
    menu:
        "Retroceder hacia la guarida del dragón.":
            jump RutaDesierto3
        "Avanzar hacia el fondo del cañón.":
            jump RutaDesierto5
        "Cancelar.":
            jump RutaDesierto4

label go_RutaDesierto5:

    menu:
        "Volver atrás por el Mar de Dunas.":
            jump RutaDesierto4
        "Cancelar.":
            jump RutaDesierto5

label go_Granjas:

    menu:
        "Ir a la Granja de Darklighter.":
            jump GranjaDarklighter
        "Ir a la Granja de Loquoy.":
            jump GranjaLoquoy
        "Volver a la ciudad.":
            jump TiendaJawa
        "Ir a la zona de recientes ataques." if descubrirDondeAtaques == 1:
            jump RecientesAtaques
        "Cancelar.":
            jump Granjas

label go_GranjaDarklighter:

    menu:
        "Salir al exterior.":
            jump Granjas
        "Ir hacia la zona de recientes ataques." if descubrirDondeAtaques == 1:
            jump RecientesAtaques
        "Cancelar.":
            jump GranjaDarklighter

label go_GranjaLoquoy:

    menu:
        "Salir al exterior.":
            jump Granjas
        "Seguir en la granja.":
            jump GranjaLoquoy

