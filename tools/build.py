#!/usr/bin/env python3
"""
Genera index.html y las páginas por especialidad a partir de los datos de
abajo. Todas las páginas comparten assets/estilos.css y assets/app.js.

    python3 tools/build.py

Editá los datos de este archivo (profesionales, especialidades, estudios) y
volvé a correrlo: el HTML se regenera solo y queda consistente entre páginas.
"""
import os, html
from urllib.parse import quote

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPRITE = open(os.path.join(RAIZ, 'tools/_sprite.html'), encoding='utf-8').read()

TEL = '595982420735'
TEL_VISIBLE = '0982 420 735'
DIR1 = 'Fulgencio Yegros 872 casi Río Bermejo'
DIR2 = 'Barrio Valle Apua — Lambaré, Paraguay'
HORARIO = 'Lunes a sábado, de 09:00 a 20:00 hs'
LAT, LNG = '-25.3465404', '-57.6000046'

def wa(msg):
    return 'https://wa.me/%s?text=%s' % (TEL, quote('Hola, %s' % msg, safe=''))

def e(t):
    return html.escape(t, quote=True)

# ---------------------------------------------------------------- datos ----
PROFESIONALES = [
    dict(slug='ginecologia-obstetricia', esp='Ginecología y Obstetricia',
         foto='fotos/equipo/ginecologia-obstetricia.jpeg',
         titulo='Ginecología y Obstetricia en Lambaré',
         intro='Controles ginecológicos, Papanicolaou y seguimiento del embarazo, en la Policlínica Sanitas.',
         motivos=['Control ginecológico de rutina', 'Papanicolaou (PAP)',
                  'Seguimiento del embarazo', 'Dolor pélvico o molestias',
                  'Alteraciones del ciclo menstrual'],
         estudios=['Papanicolaou (PAP)', 'Laboratorio']),
    dict(slug='traumatologia', esp='Traumatología',
         foto='fotos/equipo/traumatologia.jpeg',
         titulo='Traumatología en Lambaré',
         intro='Dolores, lesiones, caídas, golpes y problemas en las articulaciones.',
         motivos=['Dolor de rodilla, hombro o columna', 'Caídas y golpes',
                  'Esguinces y fracturas', 'Lesiones haciendo deporte',
                  'Colocación de férulas y yesos', 'Infiltraciones'],
         estudios=['Colocación de férulas y yesos', 'Infiltraciones']),
    dict(slug='medicina-familiar', esp='Clínica General y Medicina Familiar',
         foto='fotos/equipo/medicina-familiar.jpeg',
         titulo='Médico clínico en Lambaré',
         intro='Chequeos, control de presión y diabetes, e indicación de a qué especialista corresponde tu caso.',
         motivos=['Chequeo general', 'Control de presión alta', 'Control de diabetes',
                  'Síntomas que no sabés a qué especialidad llevar',
                  'Inspección médica y certificados', 'Seguimiento de tratamientos'],
         estudios=['Electrocardiograma', 'Laboratorio']),
    dict(slug='pediatria', esp='Pediatría',
         foto='fotos/equipo/pediatria.jpeg',
         titulo='Pediatra en Lambaré',
         intro='Controles de crecimiento, fiebre, cuadros respiratorios y las dudas de todos los días.',
         motivos=['Control de crecimiento y desarrollo', 'Fiebre', 'Tos y cuadros respiratorios',
                  'Dolor de panza', 'Dudas sobre alimentación y sueño'],
         estudios=['Laboratorio']),
    dict(slug='psicologia', esp='Psicología',
         foto='fotos/equipo/psicologia.jpeg',
         titulo='Psicólogo en Lambaré',
         intro='Atención psicológica para niños y adultos: ansiedad, estrés, depresión y acompañamiento escolar.',
         motivos=['Ansiedad', 'Estrés', 'Depresión', 'Apoyo psicológico infantil',
                  'Dificultades escolares', 'Motricidad fina',
                  'Recuperación cognitiva en adultos mayores'],
         estudios=[]),
    dict(slug='cardiologia', esp='Cardiología',
         foto='fotos/equipo/cardiologia.jpg',
         titulo='Cardiólogo en Lambaré',
         intro='Control de presión, palpitaciones y estudios del corazón, en la Policlínica Sanitas.',
         icono='i-heart',
         motivos=['Control de presión alta', 'Palpitaciones',
                  'Control del corazón', 'Electrocardiograma',
                  'Ecocardiograma', 'Seguimiento de un estudio previo'],
         estudios=['Electrocardiograma', 'Ecocardiograma']),
    dict(slug='nutricion', esp='Nutrición',
         foto='fotos/equipo/nutricion.jpeg',
         titulo='Nutricionista en Lambaré',
         intro='Orientación de alimentación para distintas etapas y situaciones de salud.',
         motivos=['Plan de alimentación', 'Control de peso', 'Alimentación en el embarazo',
                  'Alimentación de niños', 'Alimentación en diabetes e hipertensión'],
         estudios=['Laboratorio']),
]
PRO_POR_SLUG = {p['slug']: p for p in PROFESIONALES}

ESPECIALIDADES = [
    ('i-venus',   'Ginecología y Obstetricia', 'Controles, Papanicolaou, salud femenina y seguimiento del embarazo.', 'ginecologia-obstetricia'),
    ('i-bone',    'Traumatología',             'Dolores, lesiones, caídas, golpes y problemas en las articulaciones.', 'traumatologia'),
    ('i-stetho',  'Clínica General y Medicina Familiar', 'Chequeos, control de presión y diabetes, y a qué especialista ir.', 'medicina-familiar'),
    ('i-smile',   'Pediatría',                 'Crecimiento, fiebre, cuadros respiratorios y controles de tu hijo.', 'pediatria'),
    ('i-mind',    'Psicología',                'Ansiedad, estrés, depresión y apoyo psicológico para niños y adultos.', 'psicologia'),
    ('i-apple',   'Nutrición',                 'Alimentación, control de peso y orientación para distintas etapas.', 'nutricion'),
    ('i-heart',   'Cardiología',               'Presión alta, palpitaciones, control del corazón y electrocardiograma.', 'cardiologia'),
]

ESTUDIOS = [
    ('i-pulse',  'Electrocardiograma', 'Registro de la actividad eléctrica del corazón'),
    ('i-monitor','Ecocardiograma',     'Estudio por imágenes del corazón'),
    ('i-venus',  'Papanicolaou (PAP)', 'Control ginecológico de rutina'),
    ('i-syringe','Infiltraciones',     'Procedimiento realizado en consultorio'),
    ('i-cast',   'Férulas y yesos',    'Inmovilización de lesiones'),
    ('i-clip',   'Procedimientos menores', 'Consultá disponibilidad por WhatsApp'),
]

MOTIVOS = [
    ('i-stetho', 'Chequeo general',        'un chequeo general'),
    ('i-venus',  'Control ginecológico',   'un control ginecológico'),
    ('i-bone',   'Dolor o lesión',         'un dolor o una lesión'),
    ('i-clip',   'Inspección médica',      'una inspección médica'),
    ('i-cap',    'Apoyo escolar',          'apoyo escolar para un niño'),
    ('i-wind',   'Ansiedad',               'ansiedad'),
    ('i-sparkle','Estrés',                 'estrés'),
    ('i-cloud',  'Depresión',              'depresión'),
    ('i-bulb',   'Memoria en adultos mayores', 'recuperación cognitiva en un adulto mayor'),
]

# ------------------------------------------------------------ fragmentos ----
def head(titulo, descripcion, base, canonical):
    return f'''<!DOCTYPE html>
<html lang="es-PY">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(titulo)}</title>
<meta name="description" content="{e(descripcion)}">
<meta name="theme-color" content="#86151B">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://policlinicasanitas.com.py/{canonical}">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_PY">
<meta property="og:site_name" content="Policlínica Sanitas">
<meta property="og:title" content="{e(titulo)}">
<meta property="og:description" content="{e(descripcion)}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{base}fotos/logo.jpeg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Manrope:wght@500;600;700;800&display=swap">
<link rel="stylesheet" href="{base}assets/estilos.css">
</head>
<body>

<noscript><style>[data-reveal]{{opacity:1!important;transform:none!important}}</style></noscript>

{SPRITE}
'''

NAV = [('Inicio','#inicio'), ('Profesionales','#profesionales'), ('Especialidades','#especialidades'),
       ('Estudios','#estudios'), ('Turnos','#turnos'), ('Ubicación','#ubicacion')]

def header(base):
    ini = base + 'index.html' if base else ''
    links = '\n'.join(
        f'      <a href="{ini}{h}">{e(t)}</a>' for t, h in NAV)
    mlinks = '\n'.join(
        f'  <a href="{ini}{h}">{e(t)}</a>' for t, h in NAV)
    cta = wa('quiero consultar disponibilidad en la Policlínica Sanitas.')
    return f'''<header class="hdr" id="hdr">
  <div class="wrap">
    <a href="{ini or '#inicio'}" class="logo" aria-label="Policlínica Sanitas — inicio">
      <img class="logo-mark" src="{base}fotos/logo.jpeg" alt="" width="40" height="40" decoding="async">
      <span class="logo-txt"><b>SANITAS</b><span>Policlínica</span></span>
    </a>
    <nav class="nav" id="nav" aria-label="Navegación principal">
{links}
    </nav>
    <div class="hdr-cta">
      <a class="btn btn--brand" href="{cta}" target="_blank" rel="noopener">
        <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> Consultar por WhatsApp
      </a>
      <button class="burger" id="burger" aria-label="Abrir menú" aria-expanded="false" aria-controls="mnav">
        <svg class="ico" id="burger-i" aria-hidden="true"><use href="#i-menu"/></svg>
      </button>
    </div>
  </div>
</header>

<div class="mnav" id="mnav">
{mlinks}
  <a class="btn btn--brand btn--block" href="{cta}" target="_blank" rel="noopener">
    <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> Consultar por WhatsApp
  </a>
</div>
'''

def turnos(base=''):
    ini = base + 'index.html' if base else ''
    return f'''
<section class="sec sec--alt" id="turnos">
  <div class="wrap">
    <div class="sec-head center" data-reveal>
      <span class="eyebrow">Turnos</span>
      <h2>Cómo pedir un turno</h2>
      <p class="lead" style="margin-top:16px">No hace falta llamar ni completar formularios.</p>
    </div>
    <div class="pasos">
      <article class="paso" data-reveal>
        <h3>Escribinos por WhatsApp</h3>
        <p>Contanos qué necesitás consultar. Respondemos al {TEL_VISIBLE}.</p>
      </article>
      <article class="paso" data-reveal style="--d:90ms">
        <h3>Te decimos quién te atiende</h3>
        <p>Te confirmamos qué profesional corresponde a tu caso y qué horarios hay disponibles.</p>
      </article>
      <article class="paso" data-reveal style="--d:180ms">
        <h3>Venís a la consulta</h3>
        <p>{DIR1}, {DIR2.replace(' — ', ', ')}</p>
      </article>
    </div>
    <div class="paso-nota" data-reveal>
      <svg aria-hidden="true"><use href="#i-home"/></svg>
      <span>Si no podés trasladarte, también hacemos atención a domicilio en zonas cercanas de Lambaré.
      Escribinos con tu dirección y te confirmamos si llegamos a tu zona.
      <a href="{ini}#domicilio" style="color:var(--red-700);font-weight:600">Ver atención a domicilio</a></span>
    </div>
    <div class="center" style="margin-top:34px" data-reveal>
      <a class="btn btn--brand btn--lg" href="{wa('quiero pedir un turno en la Policlínica Sanitas.')}" target="_blank" rel="noopener">
        <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> Pedir un turno por WhatsApp
      </a>
    </div>
  </div>
</section>
'''

def ubicacion(con_cobertura=True):
    cobertura = '''
        <div class="cover-note">
          <b>Pacientes de Lambaré y zonas cercanas</b>
          <p>Atendemos principalmente pacientes de Lambaré y zonas cercanas. También hemos recibido pacientes provenientes de Limpio, Mariano Roque Alonso y San Lorenzo.</p>
          <div class="cover-pills">
            <span class="pill">Lambaré</span>
            <span class="pill">Limpio</span>
            <span class="pill">Mariano Roque Alonso</span>
            <span class="pill">San Lorenzo</span>
          </div>
        </div>''' if con_cobertura else ''
    return f'''
<section class="sec" id="ubicacion">
  <div class="wrap">
    <div class="sec-head center" data-reveal>
      <span class="eyebrow">Ubicación</span>
      <h2>Dónde estamos</h2>
      <p class="lead" style="margin-top:16px">Barrio Valle Apua, Lambaré. Acá está el mapa y el horario de atención.</p>
    </div>
    <div class="split" style="align-items:stretch">
      <div data-reveal>
        <div class="info-rows">
          <div class="info-row">
            <span class="itile"><svg class="ico" aria-hidden="true"><use href="#i-pin"/></svg></span>
            <div><b>Dirección</b><p>{DIR1}<br>{DIR2}</p></div>
          </div>
          <div class="info-row">
            <span class="itile itile--soft"><svg class="ico" aria-hidden="true"><use href="#i-clock"/></svg></span>
            <div><b>Horario de atención</b><p>{HORARIO}</p></div>
          </div>
          <div class="info-row">
            <span class="itile itile--accent"><svg class="ico" aria-hidden="true"><use href="#i-phone"/></svg></span>
            <div><b>WhatsApp</b><p><a href="{wa('quiero consultar disponibilidad en la Policlínica Sanitas.')}" target="_blank" rel="noopener">{TEL_VISIBLE}</a></p></div>
          </div>
        </div>
        <div class="btn-row">
          <a class="btn btn--brand btn--lg" href="https://www.google.com/maps/dir/?api=1&amp;destination={LAT}%2C{LNG}" target="_blank" rel="noopener">
            <svg class="ico" aria-hidden="true"><use href="#i-nav"/></svg> Cómo llegar
          </a>
          <a class="btn btn--ghost btn--lg" href="{wa('quiero consultar disponibilidad en la Policlínica Sanitas.')}" target="_blank" rel="noopener">
            <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> Consultar por WhatsApp
          </a>
        </div>{cobertura}
      </div>
      <div data-reveal style="--d:120ms">
        <div class="map-card" id="mapCard">
          <div class="map-ph">
            <span class="itile"><svg class="ico" aria-hidden="true"><use href="#i-pin"/></svg></span>
            <b>Policlínica Sanitas</b>
            <span>{DIR1}<br>{DIR2}</span>
            <a class="btn btn--ghost" href="https://www.google.com/maps/search/?api=1&amp;query={LAT}%2C{LNG}" target="_blank" rel="noopener">
              <svg class="ico" aria-hidden="true"><use href="#i-nav"/></svg> Abrir en Google Maps
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
'''

def cta_final(texto):
    enlace = wa('quiero consultar disponibilidad en la Policlínica Sanitas.')
    return f'''
<section class="sec dark cta-final" id="contacto">
  <div class="cta-orbs" aria-hidden="true">
    <span class="o" style="width:420px;height:420px;top:-140px;left:-90px"></span>
    <span class="o" style="width:640px;height:640px;bottom:-280px;right:-160px"></span>
    <svg class="cta-cross" style="width:90px;top:16%;right:9%" viewBox="0 0 24 24" aria-hidden="true"><use href="#i-cross"/></svg>
    <svg class="cta-cross" style="width:52px;bottom:14%;left:8%;animation-delay:1.4s" viewBox="0 0 24 24" aria-hidden="true"><use href="#i-cross"/></svg>
  </div>
  <div class="wrap">
    <span class="eyebrow" data-reveal>Consultas</span>
    <h2 data-reveal style="--d:70ms">¿Querés consultar tu caso?</h2>
    <p class="lead" data-reveal style="--d:140ms;color:rgba(250,236,238,.84);max-width:620px;margin-inline:auto">{e(texto)}</p>
    <div class="btn-row" data-reveal style="--d:210ms">
      <a class="btn btn--wa btn--lg" href="{enlace}" target="_blank" rel="noopener">
        <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> Escribir por WhatsApp
      </a>
    </div>
    <div data-reveal style="--d:280ms">
      <a class="cta-num" href="{enlace}" target="_blank" rel="noopener">
        <svg aria-hidden="true"><use href="#i-wa"/></svg> {TEL_VISIBLE}
      </a>
    </div>
  </div>
</section>
'''

def footer(base):
    ini = base + 'index.html' if base else ''
    enlace = wa('quiero consultar disponibilidad en la Policlínica Sanitas.')
    return f'''
<footer class="ftr">
  <div class="wrap">
    <div class="ftr-grid">
      <div>
        <a href="{ini or '#inicio'}" class="logo" aria-label="Policlínica Sanitas — inicio">
          <img class="logo-mark" src="{base}fotos/logo.jpeg" alt="" width="40" height="40" decoding="async">
          <span class="logo-txt"><b>SANITAS</b><span>Policlínica</span></span>
        </a>
        <p class="ftr-claim">Policlínica en Lambaré. Consultas de distintas especialidades, estudios y laboratorio en el mismo lugar.</p>
      </div>
      <div>
        <h4>Especialidades</h4>
        <ul>
{chr(10).join(f'          <li><a href="{base}especialidades/{p["slug"]}/index.html">{e(p["esp"])}</a></li>' for p in PROFESIONALES)}
        </ul>
      </div>
      <div>
        <h4>Contacto</h4>
        <div class="ftr-contact">
          <div><svg aria-hidden="true"><use href="#i-pin"/></svg><span>{DIR1}<br>{DIR2}</span></div>
          <div><svg aria-hidden="true"><use href="#i-clock"/></svg><span>{HORARIO}</span></div>
          <div><svg aria-hidden="true"><use href="#i-wa"/></svg><span><a href="{enlace}" target="_blank" rel="noopener">{TEL_VISIBLE}</a></span></div>
        </div>
        <a class="btn btn--brand" style="margin-top:22px" href="{enlace}" target="_blank" rel="noopener">
          <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> Consultar por WhatsApp
        </a>
      </div>
    </div>
    <div class="ftr-bottom">
      <span>© 2026 Policlínica Sanitas. Todos los derechos reservados.</span>
      <span>Lambaré, Paraguay</span>
    </div>
  </div>
</footer>

<a class="wa-float" href="{enlace}" target="_blank" rel="noopener" aria-label="Consultar disponibilidad por WhatsApp">
  <svg aria-hidden="true"><use href="#i-wa"/></svg>
  <span class="lbl">Consultá tu turno</span>
</a>

<div class="wa-bar">
  <a class="btn btn--wa btn--lg btn--block" href="{enlace}" target="_blank" rel="noopener">
    <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> Consultar por WhatsApp
  </a>
</div>
'''

def jsonld(extra=''):
    servicios = ',\n    '.join(
        '{"@type":"MedicalSpecialty","name":"%s"}' % s[1] for s in ESPECIALIDADES)
    return '''
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"MedicalClinic",
  "name":"Policlínica Sanitas",
  "description":"Policlínica en Lambaré, Paraguay. Consultas de distintas especialidades, estudios, laboratorio y atención a domicilio en zonas cercanas.",
  "address":{
    "@type":"PostalAddress",
    "streetAddress":"%s, Barrio Valle Apua",
    "addressLocality":"Lambaré",
    "addressRegion":"Central",
    "postalCode":"110718",
    "addressCountry":"PY"
  },
  "geo":{"@type":"GeoCoordinates","latitude":%s,"longitude":%s},
  "hasMap":"https://www.google.com/maps/search/?api=1&query=%s%%2C%s",
  "areaServed":"Lambaré, Paraguay",
  "telephone":"+%s",
  "openingHoursSpecification":[{
    "@type":"OpeningHoursSpecification",
    "dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
    "opens":"09:00","closes":"20:00"
  }],
  "availableService":[
    %s
  ]%s
}
</script>
''' % (DIR1, LAT, LNG, LAT, LNG, TEL, servicios, extra)

def cierre(base, extra_ld=''):
    return footer(base) + jsonld(extra_ld) + f'''
<script src="{base}assets/app.js" defer></script>
</body>
</html>
'''

# ------------------------------------------------------------ profesionales ----
def tarjeta_pro(p, base='', delay=0):
    motivos = '\n'.join(f'          <li>{e(m)}</li>' for m in p['motivos'][:5])
    foto = ('          <img class="photo-img" src="%s%s" alt="Profesional de %s de la Policlínica Sanitas"\n'
            '               loading="lazy" decoding="async" width="600" height="660" onerror="this.remove()">'
            % (base, p['foto'], e(p['esp']))) if p.get('foto') else ''
    enlace = wa('quiero consultar disponibilidad de %s en la Policlínica Sanitas.' % p['esp'])
    return f'''      <article class="pro-card" data-reveal style="--d:{delay}ms">
        <div class="pro-photo">
          <span class="pro-ph"><svg aria-hidden="true"><use href="#{p.get('icono','i-user')}"/></svg></span>
{foto}
        </div>
        <div class="pro-body">
          <h3>{e(p['esp'])}</h3>
          <ul class="pro-motivos">
{motivos}
          </ul>
          <p class="pro-nota">Consultá días y horarios disponibles.</p>
          <a class="card-link" href="{enlace}" target="_blank" rel="noopener">Consultar disponibilidad <svg aria-hidden="true"><use href="#i-arrow"/></svg></a>
        </div>
      </article>'''

def seccion_profesionales(base=''):
    cards = '\n'.join(tarjeta_pro(p, base, i*70) for i, p in enumerate(PROFESIONALES))
    orientacion = wa('no sé con qué profesional tengo que consultar. Necesito orientación en la Policlínica Sanitas.')
    return f'''
<section class="sec" id="profesionales">
  <div class="wrap">
    <div class="sec-head center" data-reveal>
      <span class="eyebrow">Quién te atiende</span>
      <h2>Profesionales que atienden en Sanitas</h2>
      <p class="lead" style="margin-top:16px">Mirá qué profesional cubre lo que necesitás consultar y pedí un horario por WhatsApp.</p>
    </div>
    <div class="grid pro-grid">
{cards}
      <article class="pro-card" data-reveal style="--d:{len(PROFESIONALES)*70}ms;background:linear-gradient(160deg,var(--red-700),var(--red-950));border-color:transparent">
        <div class="pro-body" style="justify-content:center;padding:32px 26px">
          <span class="itile" style="background:rgba(255,255,255,.14);border-color:rgba(255,255,255,.2);color:#fff;margin-bottom:18px"><svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg></span>
          <h3 style="color:#fff">¿No sabés con quién consultar?</h3>
          <p style="color:rgba(250,236,238,.84);font-size:.92rem;margin-top:8px">Contanos qué te pasa y te decimos qué profesional puede evaluar tu caso.</p>
          <a class="btn btn--wa btn--block" style="margin-top:auto" href="{orientacion}" target="_blank" rel="noopener">
            <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> Escribir por WhatsApp
          </a>
        </div>
      </article>
    </div>
  </div>
</section>
'''

# ------------------------------------------------------------------ index ----
def pagina_index():
    esp_cards = []
    for i, (ico, nombre, desc, slug) in enumerate(ESPECIALIDADES):
        if slug:
            href, texto = f'especialidades/{slug}/index.html', 'Ver la especialidad'
        else:
            href = wa('quiero consultar por %s en la Policlínica Sanitas.' % nombre)
            texto = 'Consultar disponibilidad'
        ext = '' if slug else ' target="_blank" rel="noopener"'
        esp_cards.append(f'''      <article class="card" data-reveal style="--d:{i*70}ms">
        <span class="itile"><svg class="ico" aria-hidden="true"><use href="#{ico}"/></svg></span>
        <h3>{e(nombre)}</h3>
        <p>{e(desc)}</p>
        <a class="card-link" href="{href}"{ext}>{texto} <svg aria-hidden="true"><use href="#i-arrow"/></svg></a>
      </article>''')

    estudios = '\n'.join(
        f'''        <div class="proc"><span class="itile{' itile--accent' if i == 0 else ''}"><svg class="ico" aria-hidden="true"><use href="#{ico}"/></svg></span><div><b>{e(n)}</b><span>{e(d)}</span></div></div>'''
        for i, (ico, n, d) in enumerate(ESTUDIOS))

    motivos = '\n'.join(
        f'''      <a class="motivo" data-reveal style="--d:{i*50}ms" href="{wa('quiero consultar por %s en la Policlínica Sanitas.' % msg)}" target="_blank" rel="noopener"><span class="b"><svg class="ico" aria-hidden="true"><use href="#{ico}"/></svg></span> {e(t)} <svg class="arw" aria-hidden="true"><use href="#i-arrow"/></svg></a>'''
        for i, (ico, t, msg) in enumerate(MOTIVOS))

    return head(
        'Policlínica Sanitas | Médicos en Lambaré',
        'Profesionales de ginecología, traumatología, clínica general, pediatría, psicología y '
        'nutrición atendiendo en Lambaré. Laboratorio, electrocardiograma y PAP en el mismo lugar. '
        'Consultá horarios por WhatsApp.',
        '', '') + header('') + f'''
<main id="inicio">

<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <span class="badge" data-reveal><i class="dot"></i> Policlínica Sanitas · Lambaré</span>
      <h1 data-reveal style="--d:80ms">¿Necesitás consultar <span class="u">con un médico?</span></h1>
      <p class="hero-sub" data-reveal style="--d:160ms">
        Encontrá al profesional indicado en la Policlínica Sanitas. Distintas especialidades atendiendo
        en Lambaré para ayudarte a identificar y tratar tu problema de salud.
      </p>
      <p class="hero-note" data-reveal style="--d:220ms">
        {DIR1}, Barrio Valle Apua. {HORARIO}.
      </p>
      <div class="btn-row" data-reveal style="--d:280ms">
        <a class="btn btn--brand btn--lg" href="#profesionales">
          <svg class="ico" aria-hidden="true"><use href="#i-users"/></svg> Ver profesionales
        </a>
        <a class="btn btn--ghost btn--lg" href="{wa('quiero consultar disponibilidad en la Policlínica Sanitas.')}" target="_blank" rel="noopener">
          <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> Consultar disponibilidad
        </a>
      </div>
      <div class="hero-mini" data-reveal style="--d:340ms">
        <span><svg aria-hidden="true"><use href="#i-check-c"/></svg> {len(PROFESIONALES)} profesionales atendiendo</span>
        <span><svg aria-hidden="true"><use href="#i-check-c"/></svg> Laboratorio y estudios en el lugar</span>
        <span><svg aria-hidden="true"><use href="#i-check-c"/></svg> Atención a domicilio en zonas cercanas</span>
      </div>
    </div>

    <div class="scene" id="scene" aria-hidden="true">
      <div class="scene-in" id="sceneIn">
        <div class="glow"></div>
        <div class="ring ring--c"></div>
        <div class="ring ring--a"><i></i></div>
        <div class="ring ring--b"><i></i></div>
        <div class="pedestal"></div>
        <div class="heart-wrap">
          <svg class="ill" viewBox="0 0 200 190">
            <defs>
              <radialGradient id="hg" cx="34%" cy="26%" r="82%">
                <stop offset="0" stop-color="#FF9AA0"/><stop offset=".42" stop-color="#C0242E"/><stop offset="1" stop-color="#661017"/>
              </radialGradient>
              <linearGradient id="hs" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0" stop-color="#fff" stop-opacity=".85"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
              </linearGradient>
            </defs>
            <path fill="url(#hg)" d="M100 178C58 146 14 116 14 72 14 44 36 22 63 22c15 0 29 7 37 19 8-12 22-19 37-19 27 0 49 22 49 50 0 44-44 74-86 106Z"/>
            <ellipse cx="70" cy="58" rx="26" ry="17" fill="url(#hs)" transform="rotate(-24 70 58)" opacity=".75"/>
          </svg>
        </div>
        <div class="ecg-card">
          <div class="lbl"><span>Electrocardiograma</span><em>en el lugar</em></div>
          <svg viewBox="0 0 340 44"><path class="ecg-line" d="M0 30h48l10-18 12 30 10-26 9 14h30l10-16 12 28 10-24 9 12h34l10-18 12 30 10-26 9 14h84"/></svg>
        </div>
        <div class="chip3d chip3d--1"><span class="b"><svg class="ico" aria-hidden="true"><use href="#i-users"/></svg></span><span>{len(PROFESIONALES)} profesionales<small>distintas especialidades</small></span></div>
        <div class="chip3d chip3d--2"><span class="b"><svg class="ico" aria-hidden="true"><use href="#i-flask"/></svg></span><span>Laboratorio<small>en la policlínica</small></span></div>
        <div class="chip3d chip3d--3"><span class="b"><svg class="ico" aria-hidden="true"><use href="#i-home"/></svg></span><span>Atención a domicilio<small>zonas cercanas de Lambaré</small></span></div>
        <div class="chip3d chip3d--4"><span class="b"><svg class="ico" aria-hidden="true"><use href="#i-clock"/></svg></span><span>09:00 — 20:00 hs<small>de lunes a sábado</small></span></div>
        <div class="particles">
          <i style="width:7px;height:7px;top:16%;left:22%"></i>
          <i style="width:5px;height:5px;top:64%;left:14%;animation-delay:1.6s"></i>
          <i style="width:8px;height:8px;top:78%;left:72%;animation-delay:3.1s"></i>
          <i style="width:5px;height:5px;top:24%;left:82%;animation-delay:2.2s"></i>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec datos" style="padding-top:clamp(10px,2vw,26px)">
  <div class="wrap">
    <div class="grid datos-grid">
      <article class="card" data-reveal>
        <span class="itile"><svg class="ico" aria-hidden="true"><use href="#i-users"/></svg></span>
        <h3>{len(PROFESIONALES)} profesionales atendiendo</h3>
        <p>Ginecología, traumatología, clínica general, pediatría, psicología y nutrición.</p>
      </article>
      <article class="card" data-reveal style="--d:90ms">
        <span class="itile itile--soft"><svg class="ico" aria-hidden="true"><use href="#i-clock"/></svg></span>
        <h3>Lunes a sábado</h3>
        <p>De 09:00 a 20:00 hs, también los sábados.</p>
      </article>
      <article class="card" data-reveal style="--d:180ms">
        <span class="itile itile--accent"><svg class="ico" aria-hidden="true"><use href="#i-flask"/></svg></span>
        <h3>Estudios en el mismo lugar</h3>
        <p>Laboratorio, electrocardiograma, ecocardiograma, PAP y procedimientos de consultorio.</p>
      </article>
      <article class="card" data-reveal style="--d:270ms">
        <span class="itile"><svg class="ico" aria-hidden="true"><use href="#i-pin"/></svg></span>
        <h3>En Barrio Valle Apua</h3>
        <p>{DIR1}, Lambaré.</p>
      </article>
    </div>
  </div>
</section>
''' + seccion_profesionales('') + f'''
<section class="sec sec--alt" id="especialidades">
  <div class="wrap">
    <div class="sec-head center" data-reveal>
      <span class="eyebrow">Dónde encaja tu caso</span>
      <h2>Especialidades y problemas que atendemos</h2>
      <p class="lead" style="margin-top:16px">Si no sabés a qué especialidad corresponde lo tuyo, escribinos y te orientamos.</p>
    </div>
    <div class="grid esp-grid">
{chr(10).join(esp_cards)}
      <article class="card esp-cta" data-reveal style="--d:{len(ESPECIALIDADES)*70}ms;background:linear-gradient(160deg,var(--red-700),var(--red-950));border-color:transparent;color:#fff">
        <span class="itile itile--dark" style="background:rgba(255,255,255,.14);border-color:rgba(255,255,255,.2)"><svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg></span>
        <h3 style="color:#fff">¿No sabés a qué especialidad ir?</h3>
        <p style="color:rgba(250,236,238,.84)">Contanos qué te pasa y te decimos qué profesional puede evaluarte.</p>
        <a class="btn btn--wa btn--block" style="margin-top:20px" href="{wa('no sé a qué especialidad tengo que ir. Necesito orientación en la Policlínica Sanitas.')}" target="_blank" rel="noopener">
          <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> Consultar por WhatsApp
        </a>
      </article>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head center" data-reveal>
      <span class="eyebrow">Motivos de consulta</span>
      <h2>¿Qué necesitás consultar?</h2>
      <p class="lead" style="margin-top:16px">Tocá el motivo más parecido a lo tuyo y te respondemos por WhatsApp.</p>
    </div>
    <div class="motivos">
{motivos}
    </div>
  </div>
</section>

<section class="sec sec--sky" id="estudios">
  <div class="wrap split">
    <div data-reveal>
      <span class="eyebrow">En la policlínica</span>
      <h2>Estudios y procedimientos que hacemos acá</h2>
      <p class="lead" style="margin-top:16px;margin-bottom:32px">No tenés que ir a otro lugar para hacerte estos estudios.</p>
      <div class="proc-list">
{estudios}
      </div>
      <div class="btn-row" style="margin-top:30px">
        <a class="btn btn--brand" href="{wa('quiero consultar por un estudio en la Policlínica Sanitas.')}" target="_blank" rel="noopener">
          <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> Consultar por un estudio
        </a>
      </div>
    </div>
    <div class="media" data-reveal style="--d:120ms">
      <div class="scene" style="aspect-ratio:1/1;max-width:480px;margin-inline:auto" aria-hidden="true">
        <div class="scene-in">
          <div class="glow"></div>
          <div class="ring ring--a"><i></i></div>
          <div class="ring ring--b"></div>
          <div class="pedestal"></div>
          <div class="heart-wrap" style="width:44%">
            <svg class="ill" viewBox="0 0 200 190">
              <path fill="url(#hg)" d="M100 178C58 146 14 116 14 72 14 44 36 22 63 22c15 0 29 7 37 19 8-12 22-19 37-19 27 0 49 22 49 50 0 44-44 74-86 106Z"/>
              <ellipse cx="70" cy="58" rx="26" ry="17" fill="url(#hs)" transform="rotate(-24 70 58)" opacity=".75"/>
            </svg>
          </div>
          <div class="ecg-card" style="top:74%">
            <div class="lbl"><span>Electrocardiograma</span><em>registro</em></div>
            <svg viewBox="0 0 340 44"><path class="ecg-line" d="M0 30h48l10-18 12 30 10-26 9 14h30l10-16 12 28 10-24 9 12h34l10-18 12 30 10-26 9 14h84"/></svg>
          </div>
          <div class="chip3d chip3d--2" style="top:20%"><span class="b"><svg class="ico" aria-hidden="true"><use href="#i-monitor"/></svg></span><span>Ecocardiograma<small>estudio por imágenes</small></span></div>
          <div class="chip3d chip3d--3" style="top:44%;left:-6%"><span class="b"><svg class="ico" aria-hidden="true"><use href="#i-flask"/></svg></span><span>Laboratorio<small>en la policlínica</small></span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec dark">
  <div class="wrap split">
    <div data-reveal>
      <span class="eyebrow">Servicio</span>
      <h2>Laboratorio</h2>
      <p class="lead" style="margin-top:20px;color:rgba(250,236,238,.84)">
        Contamos con laboratorio en la misma policlínica. Consultá qué estudios están disponibles y
        qué preparación necesita cada uno antes de venir.
      </p>
      <div class="btn-row" style="margin-top:32px">
        <a class="btn btn--wa btn--lg" href="{wa('quiero consultar por el laboratorio de la Policlínica Sanitas.')}" target="_blank" rel="noopener">
          <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> Consultar por laboratorio
        </a>
      </div>
    </div>
    <div class="grid lab-grid" data-reveal style="--d:120ms">
      <div class="glass"><span class="itile"><svg class="ico" aria-hidden="true"><use href="#i-flask"/></svg></span><h3>Con la orden del profesional</h3><p>El médico que te atiende indica qué estudios necesitás.</p></div>
      <div class="glass"><span class="itile"><svg class="ico" aria-hidden="true"><use href="#i-micro"/></svg></span><h3>Análisis clínicos</h3><p>Consultá por los estudios disponibles antes de venir.</p></div>
      <div class="glass"><span class="itile"><svg class="ico" aria-hidden="true"><use href="#i-drop"/></svg></span><h3>Controles de rutina</h3><p>Seguimiento junto al profesional que lleva tu caso.</p></div>
      <div class="glass"><span class="itile"><svg class="ico" aria-hidden="true"><use href="#i-clock"/></svg></span><h3>De 09:00 a 20:00 hs</h3><p>De lunes a sábado, en el mismo horario de la policlínica.</p></div>
    </div>
  </div>
</section>

<section class="sec sec--sky" id="domicilio">
  <div class="wrap split rev">
    <div class="media" data-reveal>
      <div class="house-scene">
        <span class="shadow"></span>
        <div class="house-in">
          <svg class="ill" viewBox="0 0 220 200" aria-hidden="true">
            <defs>
              <linearGradient id="roofA" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#BE2730"/><stop offset="1" stop-color="#86151B"/></linearGradient>
              <linearGradient id="roofB" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#86151B"/><stop offset="1" stop-color="#4A0C11"/></linearGradient>
              <linearGradient id="wallA" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#F9E5E7"/></linearGradient>
              <linearGradient id="wallB" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#F2DDE0"/><stop offset="1" stop-color="#DCC2C6"/></linearGradient>
            </defs>
            <path d="M150 100l32-18v80l-32 18z" fill="url(#wallB)"/>
            <path d="M55 100h95v80H55z" fill="url(#wallA)"/>
            <path d="M160 102 102.5 55l32-18L192 84z" fill="url(#roofB)"/>
            <path d="M45 102 102.5 55 160 102z" fill="url(#roofA)"/>
            <rect x="68" y="120" width="21" height="21" rx="4" fill="#86151B" opacity=".26"/>
            <rect x="116" y="120" width="21" height="21" rx="4" fill="#86151B" opacity=".18"/>
            <rect x="159" y="105" width="14" height="20" rx="4" fill="#4A0C11" opacity=".16"/>
            <path d="M92 180v-26a10.5 10.5 0 0 1 21 0v26z" fill="#4A0C11" opacity=".22"/>
            <path d="M97 69h11v9h9v11h-9v9H97v-9h-9V78h9z" fill="#fff" opacity=".95"/>
            <path d="M40 180h145" stroke="#4A0C11" stroke-opacity=".18" stroke-width="3" stroke-linecap="round"/>
          </svg>
        </div>
        <div class="chip3d chip3d--h1"><span class="b"><svg class="ico" aria-hidden="true"><use href="#i-stetho"/></svg></span><span>Atención a domicilio<small>zonas cercanas de Lambaré</small></span></div>
        <div class="chip3d chip3d--h2"><span class="b"><svg class="ico" aria-hidden="true"><use href="#i-pin"/></svg></span><span>Consultá tu zona<small>según tu dirección</small></span></div>
      </div>
    </div>
    <div data-reveal style="--d:120ms">
      <span class="eyebrow">A domicilio</span>
      <h2>También vamos a tu casa</h2>
      <p class="lead" style="margin-top:20px">
        Hacemos atención a domicilio en zonas cercanas de Lambaré. Escribinos con tu dirección y te
        confirmamos si llegamos a tu zona y en qué horario.
      </p>
      <ul class="checklist">
        <li><svg aria-hidden="true"><use href="#i-check-c"/></svg> Para pacientes que no pueden trasladarse</li>
        <li><svg aria-hidden="true"><use href="#i-check-c"/></svg> Disponible en zonas cercanas de Lambaré</li>
        <li><svg aria-hidden="true"><use href="#i-check-c"/></svg> La disponibilidad depende de tu zona</li>
      </ul>
      <div class="btn-row" style="margin-top:32px">
        <a class="btn btn--brand btn--lg" href="{wa('quiero consultar por atención a domicilio. Mi zona es:')}" target="_blank" rel="noopener">
          <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> Consultar atención a domicilio
        </a>
      </div>
    </div>
  </div>
</section>
''' + turnos() + seccion_galeria() + ubicacion() + cta_final(
    'Escribinos por WhatsApp contando qué necesitás consultar y te decimos qué profesional '
    'te puede atender y qué horarios hay disponibles.'
) + '\n</main>\n' + cierre('')


GALERIA = [
    ('fachada',      'Fachada',        'i-building', 'gal-item gal-item--lg', 'Fachada de la Policlínica Sanitas en Lambaré'),
    ('recepcion',    'Recepción',      'i-users',    'gal-item', 'Recepción de la Policlínica Sanitas'),
    ('consultorio',  'Consultorios',   'i-stetho',   'gal-item', 'Consultorio de la Policlínica Sanitas'),
    ('sala-espera',  'Sala de espera', 'i-home',     'gal-item', 'Sala de espera de la Policlínica Sanitas'),
    ('laboratorio',  'Laboratorio',    'i-flask',    'gal-item', 'Laboratorio de la Policlínica Sanitas'),
]

def seccion_galeria(base=''):
    """La sección se oculta sola mientras no exista fotos/fachada.jpg."""
    figs = []
    for i, (fn, cap, ico, cls, alt) in enumerate(GALERIA):
        sonda = (";var s=document.getElementById('policlinica');if(s)s.hidden=true" if i == 0 else '')
        carga = 'eager' if i == 0 else 'lazy'
        figs.append(f'''      <figure class="{cls}" data-reveal style="--d:{i*70}ms">
        <span class="gal-ph"><svg class="ico" aria-hidden="true"><use href="#{ico}"/></svg></span>
        <img class="photo-img" src="{base}fotos/{fn}.jpg" alt="{e(alt)}" loading="{carga}" decoding="async"
             width="900" height="700" onerror="this.remove(){sonda}">
        <figcaption>{e(cap)}</figcaption>
      </figure>''')
    return '''
<section class="sec" id="policlinica">
  <div class="wrap">
    <div class="sec-head center" data-reveal>
      <span class="eyebrow">El lugar</span>
      <h2>Así es la policlínica</h2>
      <p class="lead" style="margin-top:16px">Consultorios, sala de espera y laboratorio en Barrio Valle Apua.</p>
    </div>
    <!-- FOTOS: subí las imágenes a fotos/ con estos nombres y aparecen solas. -->
    <div class="gal">
''' + chr(10).join(figs) + '''
    </div>
  </div>
</section>
'''

# --------------------------------------------------- páginas por especialidad ----
def pagina_especialidad(p):
    base = '../../'
    foto_hero = ('        <img class="photo-img" src="%s%s" alt="Profesional de %s de la Policlínica Sanitas"\n'
                 '             width="600" height="660" decoding="async" onerror="this.remove()">'
                 % (base, p['foto'], e(p['esp']))) if p.get('foto') else ''
    motivos = '\n'.join(
        f'''      <a class="motivo" data-reveal style="--d:{i*50}ms" href="{wa('quiero consultar por %s. Mi caso es: %s.' % (p['esp'], m.lower()))}" target="_blank" rel="noopener">
        <span class="b"><svg class="ico" aria-hidden="true"><use href="#i-check"/></svg></span> {e(m)}
        <svg class="arw" aria-hidden="true"><use href="#i-arrow"/></svg></a>'''
        for i, m in enumerate(p['motivos']))

    estudios = ''
    if p['estudios']:
        filas = '\n'.join(
            f'''        <div class="proc"><span class="itile"><svg class="ico" aria-hidden="true"><use href="#{dict(ESTUDIOS_ICO).get(x, 'i-flask')}"/></svg></span><div><b>{e(x)}</b><span>Se hace en la policlínica</span></div></div>'''
            for x in p['estudios'])
        estudios = f'''
<section class="sec sec--sky">
  <div class="wrap" style="max-width:760px">
    <div class="sec-head center" data-reveal>
      <span class="eyebrow">En el mismo lugar</span>
      <h2>Estudios relacionados</h2>
      <p class="lead" style="margin-top:16px">No tenés que ir a otro lugar para hacértelos.</p>
    </div>
    <div class="proc-list">
{filas}
    </div>
  </div>
</section>
'''
    enlace = wa('quiero consultar disponibilidad de %s en la Policlínica Sanitas.' % p['esp'])
    return head(
        '%s | Policlínica Sanitas' % p['titulo'],
        '%s Consultá días y horarios por WhatsApp. %s, Lambaré.' % (p['intro'], DIR1),
        base, 'especialidades/%s/' % p['slug']) + header(base) + f'''
<main id="inicio">

<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <a class="volver" href="{base}index.html"><svg aria-hidden="true"><use href="#i-arrow"/></svg> Todas las especialidades</a>
      <h1 data-reveal>{e(p['titulo'])}</h1>
      <p class="hero-sub" data-reveal style="--d:120ms">{e(p['intro'])}</p>
      <p class="hero-note" data-reveal style="--d:180ms">{DIR1}, Barrio Valle Apua. {HORARIO}.</p>
      <div class="btn-row" data-reveal style="--d:240ms">
        <a class="btn btn--brand btn--lg" href="{enlace}" target="_blank" rel="noopener">
          <svg class="ico" aria-hidden="true"><use href="#i-wa"/></svg> Consultar disponibilidad
        </a>
        <a class="btn btn--ghost btn--lg" href="#motivos">Ver motivos de consulta <svg class="ico" aria-hidden="true"><use href="#i-arrow"/></svg></a>
      </div>
      <div class="hero-mini" data-reveal style="--d:300ms">
        <span><svg aria-hidden="true"><use href="#i-check-c"/></svg> Atención en Lambaré</span>
        <span><svg aria-hidden="true"><use href="#i-check-c"/></svg> Lunes a sábado, 09:00 a 20:00 hs</span>
      </div>
    </div>
    <div data-reveal style="--d:140ms">
      <div class="pro-hero">
        <span class="pro-ph"><svg aria-hidden="true"><use href="#{p.get('icono','i-user')}"/></svg></span>
{foto_hero}
        <div class="tag-esp">
          <b>{e(p['esp'])}</b>
          <span>Atiende en la Policlínica Sanitas, Lambaré</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="motivos">
  <div class="wrap" style="max-width:860px">
    <div class="sec-head center" data-reveal>
      <span class="eyebrow">Motivos de consulta</span>
      <h2>¿Con qué podés venir?</h2>
      <p class="lead" style="margin-top:16px">Tocá el motivo más parecido a tu caso y te respondemos por WhatsApp.</p>
    </div>
    <div class="motivos" style="grid-template-columns:repeat(2,1fr)">
{motivos}
    </div>
  </div>
</section>
{estudios}''' + turnos(base) + ubicacion(con_cobertura=False) + cta_final(
        'Escribinos contando tu caso y te confirmamos el horario disponible de %s.' % p['esp'].lower()
    ) + '\n</main>\n' + cierre(base)

ESTUDIOS_ICO = [(n, ico) for ico, n, _ in ESTUDIOS] + [('Laboratorio', 'i-flask')]

# ------------------------------------------------------------------ salida ----
def escribir(ruta, contenido):
    destino = os.path.join(RAIZ, ruta)
    os.makedirs(os.path.dirname(destino) or '.', exist_ok=True)
    open(destino, 'w', encoding='utf-8').write(contenido)
    print('  %-46s %6.1f KB' % (ruta, len(contenido.encode()) / 1024))

if __name__ == '__main__':
    print('Generando páginas:')
    escribir('index.html', pagina_index())
    for p in PROFESIONALES:
        escribir('especialidades/%s/index.html' % p['slug'], pagina_especialidad(p))
    print('Listo.')
