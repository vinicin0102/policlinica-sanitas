# Landing Page — Policlínica Sanitas (Lambaré, Paraguay)

Página única, estática y autocontenida: `index.html`.
No requiere build, dependencias ni servidor: se puede subir tal cual a
cualquier hosting o CDN.

## Qué incluye

| Sección | Contenido |
|---|---|
| Header sticky | Logo, menú ancla, CTA «Agendar consulta», glassmorphism y reducción de altura al hacer scroll |
| Hero | Titular, subtítulo, CTA de WhatsApp + «Ver especialidades» y composición 3D (corazón, anillos orbitales, tarjeta de ECG y cards flotantes) |
| Barra de confianza | Atención integral · Cuidado familiar · En Lambaré · Atención a domicilio |
| Sobre Sanitas | Texto institucional + foto del lugar y cards flotantes |
| Conocé la policlínica | Galería de 5 fotos del local en grilla asimétrica |
| Especialidades | 7 especialidades + tarjeta CTA de orientación |
| Estudios y procedimientos | 6 servicios + escena 3D de cardiología |
| Laboratorio | Franja oscura con 4 cards de vidrio y CTA |
| Servicios más solicitados | Electrocardiograma · PAP · Atención psicológica infantil |
| Etapas de la vida | Niños · Adultos · Adultos mayores · Familias |
| Motivos de consulta | 9 accesos directos a WhatsApp con mensaje contextual |
| Atención psicológica | Sección dedicada con tags y CTA |
| Atención a domicilio | Ilustración 3D de casa + aclaración de disponibilidad por zona |
| Equipo profesional | Bloque institucional **sin datos inventados**; se convierte en grilla de profesionales al completar un array |
| Ubicación | Datos de contacto, mapa de Google diferido, botón «Cómo llegar» y nota de cobertura |
| CTA final | Franja azul profunda con el número de WhatsApp |
| Footer | Datos, enlaces y aviso de derechos |
| Flotantes | Botón de WhatsApp en desktop y barra fija inferior en mobile |

## WhatsApp

Todos los CTA abren `https://wa.me/595982420735` con un mensaje precargado
distinto según la sección (especialidad, laboratorio, domicilio, etc.).
Para cambiar el número, reemplazá `595982420735` en todo el archivo.

## Identidad

Rojo Sanitas sobre blanco, tomado del propio logo (#86151B). La paleta vive
en el bloque `:root` de `index.html`: `--red-700` es ese rojo, `--red-900` y
`--red-950` sostienen las franjas oscuras, y los neutros están sesgados hacia
el rojo para que nada se vea gris de catálogo. El grafito (`--graphite`)
aporta variedad sin ensuciar la marca.

El verde aparece en dos lugares y sólo con una función: los tildes de
confirmación (`--ok`) y el botón flotante de WhatsApp, que se deja verde
porque es el color con el que la gente reconoce ese canal. Todos los demás
CTA son rojo de marca. Para volver a tener los CTA en verde, cambiá
`btn--brand` por `btn--wa` en los botones.

## Fotografías

Las imágenes se cargan solas: cada lugar tiene un `<img>` apuntando a
`fotos/…` y, detrás, una composición de marca. Si el archivo todavía no
existe, el `<img>` se retira solo y queda la composición — la página nunca
muestra un ícono roto.

Los nombres de archivo, qué mostrar en cada uno y los tamaños sugeridos están
en **`fotos/README.md`**.

**Ya cargadas:** el logo (`fotos/logo.jpeg`, usado en el header y el footer) y
los 6 retratos del equipo en `fotos/equipo/`.

**Faltan 10:** las 5 de la galería «Conocé la policlínica», la de «Sobre
Sanitas» y las 4 de «Etapas de la vida». Mientras no exista `fotos/fachada.jpg`
la sección «Conocé la policlínica» se oculta sola, para que el visitante nunca
vea una fila de recuadros vacíos.

**No usar bancos de imágenes** para pasar fotos de desconocidos por el local o
por el equipo.

## Profesionales

Los 6 retratos ya están cargados en el array `SANITAS_PROFESIONALES` de
`index.html`, **identificados sólo por especialidad**: la policlínica todavía
no envió nombres ni registros profesionales, y no se inventa ninguno. Cuando
lleguen, se agregan al mismo array y la tarjeta pasa a mostrar el nombre como
título, la especialidad debajo y el registro en la línea de apoyo. El WhatsApp
de cada tarjeta se adapta solo:

```js
window.SANITAS_PROFESIONALES = [
  // hoy: sólo especialidad
  { foto:'fotos/equipo/ginecologia-obstetricia.jpeg',
    especialidad:'Ginecología y Obstetricia' },

  // cuando lleguen los datos:
  { foto:'fotos/equipo/ginecologia-obstetricia.jpeg',
    nombre:'Dra. [Nombre]', especialidad:'Ginecología y Obstetricia',
    registro:'Reg. Prof. [número]', formacion:'[Formación]' }
];
```

**No completar con datos inventados.**

## Mapa

Coordenadas en uso: **-25.3465404, -57.6000046** (Calle Tte. Cnel. Fulgencio
Yegros, Valle Apu'a II, Lambaré), provistas por el cliente. Alimentan tres
cosas: el embed de Google Maps con el marcador rotulado «Policlínica Sanitas»,
el destino del botón «Cómo llegar» y el campo `geo` de los datos
estructurados.

El embed no usa API key y se carga recién cuando el visitante se acerca a la
sección, para no penalizar el LCP. Si el iframe no carga, el bloque muestra
igual el nombre, la dirección y un enlace a Google Maps.

El punto corresponde a la calle, no al número de puerta. Si el marcador no cae
justo sobre la entrada, ajustá `LAT`/`LNG` buscando las tres apariciones de
`-25.3465404` en `index.html`.

## Detalles técnicos

- HTML + CSS + JS vanilla en un solo archivo; **cero dependencias de runtime**.
- Íconos SVG inline (sprite `<symbol>`): sin peticiones a CDN de íconos.
- Única petición externa: la hoja de fuentes de Google (Manrope + Inter),
  cargada de forma asíncrona con fallback en `<noscript>`.
- Animaciones con IntersectionObserver, parallax 3D con el mouse sólo en
  punteros finos y respeto completo de `prefers-reduced-motion`.
- Mobile first: barra fija de WhatsApp, botones de 54–62 px de alto y sin
  desplazamiento horizontal.
- SEO: title y meta description locales, Open Graph, canonical y datos
  estructurados `MedicalClinic` (sólo con información real provista).
- Accesibilidad: contraste alto, foco visible, `aria-label` en controles,
  menú con `aria-expanded` y cierre con `Escape`.
