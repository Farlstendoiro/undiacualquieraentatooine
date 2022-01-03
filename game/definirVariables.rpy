label defineVariables:

    # UPDATE: preguntarKabePorCazador sube a 4 cuando has hablado con un cazador.

    # NOTA: TODAS LAS VARIABLES EMPIEZAN POR MINÚSCULA. YA VALE, HOMBRE.

# variable comodín que debe estar a 1 para salir de algo; y se reinicia a 0 cuando terminas de usarla (como en Insert Name)
    default varComodin = 0

# Elige nombre
    default playerName = "tú"

# Elige aspecto (Sirve para cuando se dice "he" o "she")
    default tuAspecto = 0


# LIST: Objetos iniciales de inventario
# Algo de dinero. Cambia si compras arma de Wassak
# 1 = "tienes algo de dinero"; 2 = "tienes sólo un poco de dinero"
    default itemDinero = 1

# Cosas que sólo tienen que estar ahí y las puedes mirar:
# Datapad declaración Wassak. Sólo tienen que estar en el inventario.
    default itemDeclaraWassak = 1

# Datapad declaración Boggs. Sólo tienen que estar en el inventario.
    default itemDeclaraBoggs = 1

# Datapad declaración Ghana. Sólo tienen que estar en el inventario.
    default itemDeclaraGhana = 1

# Datapad declaración Jent. Se ve sólo si tienes Hablar con Jent a 1. Debería ser la misma variable, así que esa será declaraJent
# Hablar con Jent: Pasar por la Calle delante de la Cantina. Primera vez 0, segunda vez +1 y ves a Jent. Desde entonces suma, pero a partir de 2 da igual.
    default itemDeclaraJent = 0


# LIST: Objetos a conseguir que van al inventario:
# Oscilador de cristal.
    default itemOscilador = 0

# Permiso de despegue.
    default itemPermisoDespegue = 0

# Investigación cerrada.
    default itemInvestigacion = 0

# Ya puedes ir a tu nave (comprobar cada vez que consigues uno de los tres anteriores)
    default yaPuedesIrATuNave = 0

# Arma que te vende Wassak; cambia tu dinero.
    default itemArmaJawa = 0

# Estandarte tusken
    default itemEstandarte = 0

# Wanted Poster de Bandido
    default itemWantedPoster = 0

# Items. Diario del viejo hermitaño. No lo has visto 0, encontrado 1; pones a caldo a Jent 2.
    default itemDiarioErmitano = 0

# Obtienes rata muerta de Jent. No sirve para nada. Ya tienes de éstos.
    default itemRataMuerta = 0

# Ruta del Tormenta de Melocotón
# Si 0, no la tienes. Si 1, la tienes y no has hecho nada con ella. Si 2, las has mirado en ordenador ella sola - y sigue en tu Inventario
    default itemRutaMelocoton = 0

# Ruta Auténtica del Tormenta de Melocotón
# Si 0, no la tienes. Si 1, la tienes y no has hecho nada con ella. Si 2, las has mirado en ordenador - junto con la otra - y sigue en tu Inventario
    default itemRutaRealMelocoton = 0

# (objeto de inventario: Cabeza de droide = Tuskens rescatados )
# SI ESTÁ A 2, LA HAS PERDIDO!
#   Al entregar Cabeza a Tusken Bob inmediatamente: Crimelord 1 pasa a Inactivo; y además Crimelord Quest +1.
#   La verdad es que Crimelord Quest no lo veo.
    default itemCabezaDroide = 0


# LIST: Cosas que suceden. Hablaste con tal personaje y cosas (recuerda que hablar con Jent está en declaraJent)
# Primer hablar con Graf para presentarte
    default primerGraf = 0

# La primera vez que hablas con Wassak, sacas el tema del oscilador: Te lo daría, pero los jawas están siendo acosados por tusken raiders.
    default primerWassak = 0

# Si tienes Hablar con Jent a 1, existe tb variable Preguntar Wassak por Jent a 0, que te dirá que es buena piloto (+2 después de hablar)
    default preguntarWassakPorJent = 0

# Si tienes Hablar con Jent a 1, existe tb variable Preguntar Graf por Jent a 0, que te dirá que es buena piloto (+2 después de hablar)
    default preguntarGrafPorJent = 0

# Hablar con Bob el tusken, para que no sea dos veces, y que sepas sus problemas. Si es 1, es que has hablado con él.
# Si es 2, es que le has dado una de las dos cosas que pide, cualquiera de ellas. Si es 3, le has dado las dos.
    default hablarBob = 0

# Hablar con los otros tuskens antes de encontrar a Bob:
    default hablarTuskens = 0

# Intentar Obtener Permiso En Oficina Imperial
    default intentarPermisoEnOficina = 0

# Preguntar Por Permiso En Cantina: Si tienes Permiso de Despegue a 0, puedes hablar con Barman. Si tienes PPPEC a 1, puedes hablar con Kabe.
#   Si tienes PPPEC a 2, puedes hablar con Graff y puedes ver su casa
    default preguntarPermisoEnCantina = 0

# Preguntar Kabe por BH. Si tienes Wanted Poster: Variable para que sólo lo puedas hacer una vez, y para que no puedas si ya has hablado con un BH.
    default preguntarKabePorCazador = 0

# Hablaste con el cazarrecompensas
    default hablarCazador = 0

# Conocimiento de Clawdita +1 (puede que sea mejor individualmente)
# A: El diario del ermitaño. B: El crimelord 2 habla. C: El Contrabandista habla.
    default conoceClawditaA = 0
    default conoceClawditaB = 0
    default conoceClawditaC = 0

# Dragón: No lo has visto 0; encontrado 1; se lo soplas a Tusken Bob 2.
    default dragon = 0

# Activos Rebeldes: No lo has visto 0; encontrado 1. Cuando hables con Graf, 2.
    default activosRebeldes = 0

# Bandido capturado, pasa a 2, se lo puedes decir a Graf.
    default bandidoCapturado = 0

# Quest Reclutar Piloto: Sube a 1.
    default questReclutarPiloto = 0

# Crimelord 1 activo; Crimelord 2 activo. 0 no los conoces; 1 les conoces y están activos. 2 has eliminado a ese. 3 YA ESTÁ eliminado.
    default crimelord1Activo = 0
    default crimelord2Activo = 0

# Jugaste Con Labria: 0 aún no aparece Labria, 1 Labria ya aparece, no has hablado con él;
# 2 jugaste y perdiste (otro diálogo), 3 Has ganado; si le hablas te dice alguna chorrada; 4 Labria ya no aparece.
    default jugarLabria = 1

# Crimelord Quest: 0 no la tienes. 1 la tienes. 2 has eliminado a uno, el que sea. 3 has eliminado a dos. 4 Queda uno.
    default crimelordQuest = 0

# Hablaste con granjero genérico
    default hablarGranjero = 0

# Hablaste con Darklighter
    default hablarDarklighter = 0

# Hablaste con Papá de Jent
    default hablarLoquoy = 0

# Descubriste de dónde vienen los ataques tusken
    default descubrirDondeAtaques = 0

# Variable Te Han Apalizado Stroops: 0 a init; 1 cuando obtienes Crimelord Quest; cuando pasas por la calle que sea se ejecuta y sube a 2
#   Sólo te la pueden colocar allí.
    default apalizadoPorTropas = 0

# Ordenador de Navegación. Sólo tienes esa opción al hablar con Wassak si tienes cualquiera de las Rutas
# Pedir Ordenador de Navegación a Wassak. Sólo tienes esta opción al hablar con Graf si tienes una Ruta, y sólo una vez
# ¿Seguro? A ver. Si tienes la Ruta Real, lo pides y obtienes resultado. Si tienes la Ruta Falsa, lo pides y obtienes otro resultado.
# Esto hay que mirarlo en más detalle. Funciona, pero ya no sé qué significa cada valor.
    default ordenadorNav = 0

# Información Que Implica a Crimelord 2.
#   Si tienes Información Que Implica a Crimelord 2, se ejecutan cosas en sitios
#   Si tienes Información Que Implica a Crimelord 2 al entrar en cantina, está Crimelord 2 y le puedes hablar.
    default informacionImplicaCrimelord2 = 0

# Asustate al Bandido en el palacio [bomarr] y él huye hacia el desierto, dejando un rastro que puedes seguir.
    default asustasteBandido = 0

# Has estado en ciertos sitios. Con estar una vez (y sobrevivir), revelas acceso a otro sitio, así que bien.
# Pero la segunda vez que pases por ahí, no tiene que salir el mismo mensaje, claro
    default visitasteRecientesAtaques = 0
    default visitasteMosGamos = 0
    default visitasteCamino1 = 0
    default visitasteCamino2 = 0
# La 3 no existe porque la variable "dragón" se ocupa de ello.
    default visitasteCamino4 = 0
    default visitasteCamino5 = 0

# Juegas con Vasail. Pierdes. Hablas con Gorlok. Te da un pronóstico - pero sólo uno. 1-3 es sabacc, 4-6 es swoops
    default pronostico = 0
    
# Nuevos:

# Para definir tu personaje (lo inicializo varón humano):
    default tuEspecie = "humano"
    default tuEl = "el"
    default tuUn = "un"
    default tuUnMayus = "Un"
    # tuO es fin de palabra: biólog-O biólog-A
    default tuO = "o"
    default tuPronombre = "él"
    default tuPronombreMayus = "Él"
    default tuEste = "este"
    default tuEse = "ése"
    default tuLe = "le"
    default tuEmpollon = "empollón"

# Nombre de tu nave:
    default tuNave = "Shantipole"

# La primera vez que entras en la trastienda, te dan el primer diálogo. Después se actualiza y cambian Crimelord Activo.
    default primeraVezTrastienda = 0
    
# Primera vez granja Loquoy, Jent te presenta a papá. Si no, te lo presenta cada vez que vas.
    default primeraVezEnGranjaLoquoy = 0

# Preguntar a Graf si te ayuda con la Investigación; que lo haga una sola vez
    default preguntarGrafInvestigacion = 0

# Jent te dice que no es pro imperial
    default hablarJentImperio = 0
    
# Para un rumor random de los granjeros
    default randomrumor = 1

# Si ves la Declaración de Wassak, puedes preguntarle por la rata womp y en la Oficina Imperial si saben del droid
    default visteDeclaracionWassak = 0

# Intentas dar a Tusken Bob la cabeza de droide antes de hablarle del dragón.
    default cabezaAntesQueDragon = 0
    
# Has preguntado a los [bomarr] por la iluminación.
    default preguntaIluminacion = 0
    default preguntaIluminacion1 = 0
    default preguntaIluminacion2 = 0
    default preguntaIluminacion3 = 0
    default preguntaIluminacion4 = 0

# Dónde eliminas a Crimelord 2. 0 aún no está eliminado. 1 en la cantina; 2 en la trastienda; 3 ya no importa
    default crimelord2EliminadoEnCantina = 0
    default sabenQueCrimelord2Eliminado = 0

# Saludar a la gente, para que un mensaje salga sólo la primera vez
    default saludarGraf = 0
    default saludarWassak = 0
    default saludarFenn = 0
    default saludarJesond = 0
    default saludarRadon = 0
    default saludarTresCrimelords = 0
    default saludarLoquoy = 0
    default saludarContrabandista = 0
    default explicaTai = 0
    default entrarOtroHangar = 0

    default turjindaHablaTrabajo = 0
    default turjindaHablaPuerto = 0
    default hablarJentPiloto = 0
    default hablarLornaMoradores = 0
    default hablarLornaJent = 0
    default hablarLornaAccidente = 0

    default hablarDarklighter1 = 0
    default hablarDarklighter2 = 0
    default hablarDarklighter3 = 0
    default hablarGrafDeJent = 0

# el apostrofo de bomarr es complicado
    default bomarr = "B'omarr"
    default UOuuuhrRr = "UOu'uu'h'rRr"
    default porcien = "%"
    
# Definir la música
    define sunshine = "/music/sunshine_a.mp3"
    define poofy = "/music/poofy_reel.mp3"
    define hiena = "/music/hyena-laugh_daniel-simion attribution 3.0 soundbible.wav"
    
# Definir los videos
    image movie = Movie(size=(800,800), xpos=0, ypos=0, xanchor=0, yanchor=100)
    
    
    define flash = Fade(.25, 0, .75, color="#fff")