pag = {
    "title1": "",
    "title": "INFRAESTRUCTURA RECARGA VEHICULO ELECTRICO",
    "logo": "",
    "descripcion": "INFRAESTRUCTURA RECARGA VEHICULO ELECTRICO  INFRAESTRUCTURA RECARGA VEHICULO ELECTRICOINFRAESTRUCTURA RECARGA VEHICULO ELECTRICOINFRAESTRUCTURA RECARGA VEHICULO ELECTRICO ",
}


formulario = "https://kcjysmt9s7.execute-api.eu-west-1.amazonaws.com/dev/recarga"
formulario = ""
links = [
    "https://ivehiculoelectrico.com/blog/ITC-BT%2052/1.%20OBJETO%20Y%20AMBITO%20DE%20APLICACION/",
    "https://ivehiculoelectrico.com/blog/ITC-BT_52/4._PREVISION_DE_CARGAS_SEGUN_EL_ESQUEMA_DE_LA_INSTALACION/",
    "https://ivehiculoelectrico.com/blog/ITC-BT%2052/3.%20ESQUEMAS%20DE%20INSTALACION%20PARA%20LA%20RECARGA%20DE%20VEHICULOS%20ELECTRICOS/",
    "https://ivehiculoelectrico.com/blog/ITC-BT%2052/4.%20PREVISION%20DE%20CARGAS%20SEGUN%20EL%20ESQUEMA%20DE%20LA%20INSTALACION/      ",
    "https://ivehiculoelectrico.com/blog/ITC-BT%2052/4.%20PREVISION%20DE%20CARGAS%20SEGUN%20EL%20ESQUEMA%20DE%20LA%20INSTALACION/  ",
    "https://ivehiculoelectrico.com/blog/ITC-BT%2052/6.%20PROTECCION%20PARA%20GARANTIZAR%20LA%20SEGURIDAD/",
    "https://ivehiculoelectrico.com/blog/ITC-BT%2052/7.%20CONDICIONES%20PARTICULARES%20DE%20INSTALACION/",
]


ddcolectivo = [
    # "especifico":"active",
    {
        "seccion":"",
        "especifico": "active",
        "headline1": "Contacto",
        "headline2": "Contacto",
        "content1": "holla caracola",
        "content2": "",
        "content3": "",
        "content4": "",
        "content5": "",
        "img1": "static/img/electric-car-4381728_640.jpg",
        "img2": "",
        "link1": links[1],
        "link2": "#",
        "pdf": "static/pdf/pp.pdf",
    },
]
o = -1
for i in ddcolectivo:
    o = o + 1
    i["n"] = "ddcolectivo_" + str(o)

ddcontrol = [
    # "especifico":"order-md-2",
    # https://www.mobilityhouse.com/int_en/charging-and-energy-management
    # https://fontawesome.com/v5.15/icons?d=gallery&p=2
    {
        "n": 0,
        "seccion":"",
        "especifico": "order-md-2",
        "headline1": "secure & local",
        "headline2": "Contacto",
        "content1": "The locally installed system guarantees maximum data security and full performance even if the Internet connection is interrupted.",
        "content2": "",
        "content3": "",
        "content4": "",
        "content5": "",
        "ico": "fa-shield-alt",
        "img2": "",
        "link1": "#",
        "link2": "#",
        "pdf": "",
    },
    {
        "n": 0,
        "seccion":"",
        "especifico": "order-md-2",
        "headline1": "modular & scalable",
        "headline2": "Contacto",
        "content1": "Ayudamos a nuestros clientes a MINIMIZANDO su inversion.",
        "content2": "",
        "content3": "",
        "content4": "",
        "content5": "",
        "ico": "fa-puzzle-piece",
        "img2": "",
        "link1": "#",
        "link2": "#",
        "pdf": "",
    },
    {
        "n": 0,
        "seccion":"",
        "especifico": "order-md-2",
        "headline1": "simple & intuitive",
        "headline2": "Contacto",
        "content1": "Control your charging infrastructure easily and intuitively via the ChargePilot Web Portal. Control and manage your charging stations conveniently from a distance.",
        "content2": "",
        "content3": "",
        "content4": "",
        "content5": "",
        "ico": "fa-child",
        "img2": "",
        "link1": "#",
        "link2": "#",
        "pdf": "",
    },
    {
        "n": 0,
        "seccion":"",
        "especifico": "order-md-2",
        "headline1": "independent & compatible",
        "headline2": "Contacto",
        "content1": "Don’t get locked with a certain manufacturer for charging stations. Combine ChargePilot with other systems via standardized interfaces.",
        "content2": "",
        "content3": "",
        "content4": "",
        "content5": "",
        "ico": "fa-unlock-alt",
        "img2": "",
        "link1": "#",
        "link2": "#",
        "pdf": "",
    },
]
o = -1
for i in ddcontrol:
    o = o + 1
    i["n"] = "ddcontrol_" + str(o)


ddmarketing = [
    # "especifico":"order-md-2",
    # https://fontawesome.com/v5.15/icons?d=gallery&p=2
    {
        "seccion":"",
        "especifico": "order-md-2",
        "headline1": "ESTUDIO GRATUITO",
        "headline2": "Contacto",
        "content1": "Ayudamos a nuestros clientes a MINIMIZANDO su inversion.",
        "content2": "",
        "content3": "",
        "content4": "",
        "content5": "",
        "ico": "fa-pencil-ruler",
        "img2": "",
        "link1": "#",
        "link2": "#",
        "pdf": "",
    },
    {
        "n": 0,
        "seccion":"",
        "especifico": "",
        "headline1": "SUBVENCION",
        "headline2": "",
        "content1": "Gestionamos su subvencion de hasta el 40 % con el plan MOVES III",
        "content2": "",
        "content3": "",
        "content4": "",
        "content5": "",
        "ico": "fa-euro-sign",
        "img2": "",
        "link1": "#",
        "link2": "#",
        "pdf": "",
    },
    {
        "n": 0,
        "seccion":"",
        "especifico": "order-md-2",
        "headline1": "PROYECTO",
        "headline2": "",
        "content1": "Elaboramos y supervisamos los proyectos de nuestros clientes",
        "content2": "",
        "content3": "",
        "content4": "",
        "content5": "",
        "ico": "fa-project-diagram",
        "img2": "",
        "link1": "#",
        "link2": "#",
        "pdf": "",
    },
    {
        "n": 0,
        "seccion":"",
        "especifico": "order-md-2",
        "headline1": "INSTALACION",
        "headline2": "Contacto",
        "content1": "Ejecutamos proyectos llave en mano.",
        "content2": "",
        "content3": "",
        "content4": "",
        "content5": "",
        "ico": "fa-tools",
        "img2": "",
        "link1": "#",
        "link2": "#",
        "pdf": "",
    },
    {
        "n": 0,
        "seccion":"",
        "especifico": "order-md-2",
        "headline1": "CERTIFICACION",
        "headline2": "Contacto",
        "content1": "Legalizamos su instalacion",
        "content2": "",
        "content3": "",
        "content4": "",
        "content5": "",
        "ico": "fa-certificate",
        "img2": "",
        "link1": "#",
        "link2": "#",
        "pdf": "",
    },
    {
        "n": 0,
        "seccion":"",
        "especifico": "order-md-2",
        "headline1": "GARANTIA",
        "headline2": "Contacto",
        "content1": "Servicio garantia y mantenimiento",
        "content2": "cccoooonntetnnn   2",
        "content3": "",
        "content4": "",
        "content5": "",
        "ico": "fa-handshake",
        "img2": "",
        "link1": "#",
        "link2": "#",
        "pdf": "",
    },
]
o = -1
for i in ddmarketing:
    o = o + 1
    i["n"] = "ddmarketing_" + str(o)


ddmovesIII = [
    # "especifico":"order-md-2",
    {
        "seccion":"",
        "especifico": "order-md-2",
        "headline1": "Contacto1",
        "headline2": "Contacto1",
        "content1": "",
        "content2": "cccoooonntetnnn   0",
        "content3": "",
        "content4": "",
        "content5": "",
        "img1": "static/img/electric-car-4381728_640.jpg",
        "img2": "multi-storey-car-park-1271919_640.jpg",
        "link1": "https://www.esios.ree.es/es/insertado/termino-facturacion-energia-activa-pvpc",
        "link2": "#",
        "pdf": "static/pdf/pp.pdf",
    },
    {
        "seccion":"",
        "especifico": "order-md-2",
        "headline1": "Contacto1",
        "headline2": "Contacto1",
        "content1": "",
        "content2": "cccoooonntetnnn   0",
        "content3": "",
        "content4": "",
        "content5": "",
        "img1": "static/img/electric-car-4381728_640.jpg",
        "img2": "multi-storey-car-park-1271919_640.jpg",
        "link1": "https://www.esios.ree.es/es/insertado/generacion-libre-co2",
        "link2": "#",
        "pdf": "static/pdf/pp.pdf",
    },
    {
        "seccion":"",
        "especifico": "order-md-2",
        "headline1": "Contacto1",
        "headline2": "Contacto1",
        "content1": "",
        "content2": "cccoooonntetnnn   0",
        "content3": "",
        "content4": "",
        "content5": "",
        "img1": "static/img/electric-car-4381728_640.jpg",
        "img2": "multi-storey-car-park-1271919_640.jpg",
        "link1": "https://www.esios.ree.es/es/insertado/generacion-medida?locale=es",
        "link2": "#",
        "pdf": "static/pdf/pp.pdf",
    },
]

o = -1
for i in ddmovesIII:
    o = o + 1
    i["n"] = "ddmovesIII_" + str(o)


ddindividual = [
    # "especifico":"active",
    {
        "nombre": "ddindividual",
        "n": "cards_0",
        "seccion":"",
        "especifico": "active",
        "headline1": "Contacto",
        "headline2": "Contacto",
        "content1": "holla caracola",
        "content2": "",
        "content3": "",
        "content4": "",
        "content5": "",
        "img1": "electric-car-4381728_640.jpg",
        "img2": "",
        "link1": "",
        "link2": "#",
        "pdf": "",
    },
]
o = -1
for i in ddindividual:
    o = o + 1
    i["n"] = "ddindividual_" + str(o)

menu = [
    # "especifico":"active",
    {
        "seccion":"",
        "especifico": "",
        "headline1": "COLECTIVO",
        "headline2": "Instalamos su Punto de Recarga en comunidades, hoteles, y  otros aparcamientos colectivos",
        "content1": "ddmovesIII",
        "content2": "",
        "content3": "",
        "content4": "",
        "content5": "",
        "img1": "electric-car-4381728_640.jpg",
        "img2": "",
        "link1": "https://ivehiculoelectrico.com/blog/ITC-BT%2052/5.REQUISITOS%20GENERALES%20DE%20LA%20INSTALACION/",
        "link2": "#",
        "pdf": "",
    },
    {
        "seccion":"",
        "especifico": "",
        "headline1": "INDIVIDUAL",
        "headline2": "Instalamos su Punto de Recarga en comunidades, hoteles, y  otros aparcamientos colectivos",
        "content1": "ddindividual",
        "content2": "",
        "content3": "",
        "content4": "",
        "content5": "",
        "img1": "electric-car-4381728_640.jpg",
        "img2": "",
        "link1": "https://ivehiculoelectrico.com/blog/ITC-BT%2052/5.REQUISITOS%20GENERALES%20DE%20LA%20INSTALACION/",
        "link2": "#",
        "pdf": "",
    },
    {
        "seccion":"",
        "especifico": "",
        "headline1": "SMART",
        "headline2": "Quieres asociarte a IVE ?",
        "content1": "ddcolectivo",
        "content2": "",
        "content3": "",
        "content4": "",
        "content5": "",
        "img1": "electric-car-4381728_640.jpg",
        "img2": "",
        "link1": "https://ivehiculoelectrico.com/blog/ITC-BT%2052/5.REQUISITOS%20GENERALES%20DE%20LA%20INSTALACION/",
        "link2": "#",
        "pdf": "",
    },
    {
        "seccion":"",
        "especifico": "",
        "headline1": "BLOG",
        "headline2": "Contacto",
        "content1": "CardsXL",
        "content2": "",
        "content3": "",
        "content4": "",
        "content5": "",
        "img1": "electric-car-4381728_640.jpg",
        "img2": "",
        "link1": formulario,
        "link2": "#",
        "pdf": "",
    },
    {
        "seccion":"",
        "especifico": "active",
        "headline1": "",
        "headline2": "INFRAESTRUCTURA RECARGA VEHICULO ELECTRICO",
        "content1": "Cards",
        "content2": "",
        "content3": "",
        "content4": "",
        "content5": "",
        "img1": "2021-05-30_19-38.png",
        "img2": "",
        "link1": formulario,
        "link2": "#",
        "pdf": "",
    },
    {
        "seccion":"",
        "especifico": "",
        "headline1": "MOVES III",
        "headline2": "Ayudas del 70 % para autónomos, particulares Comunidades de propietarios y administración sinactividad económica",
        "content1": "Cards",
        "content2": "",
        "content3": "",
        "content4": "",
        "content5": "",
        "img1": "Peek 2021-07-05 22-08.gif",
        "img2": "",
        "link1": formulario,
        "link2": "#",
        "pdf": "",
    },
]
o = -1
for i in menu:
    o = o + 1
    i["o"] = str(o)
o = -1
for i in menu:
    o = o + 1
    i["n"] = "menu_" + str(o)


menu_headline = []
for i in menu:
    print(i["headline1"])
    menu_headline.append(i["headline1"])

links = [{}]


parent_list = [{'A': 'val1', 'B': 'val2'}, {'C': 'val3', 'D': 'val4'}]
parent_list = menu

# ==================================================
