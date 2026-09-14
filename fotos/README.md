# Fotos de la Policlínica Sanitas

Subí las imágenes con **exactamente estos nombres**. La página las toma sola:
si un archivo no existe todavía, queda la composición de marca en su lugar y
nada se rompe.

## Estado

| | |
|---|---|
| ✅ `logo.jpeg` | Header y footer |
| ✅ `equipo/` (6 retratos) | Sección de profesionales y páginas por especialidad |
| ⬜ Galería del local | 5 fotos — la sección se oculta hasta que exista `fachada.jpg` |

## Galería «Así es la policlínica»

| Archivo | Qué mostrar | Tamaño sugerido |
|---|---|---|
| `fachada.jpg` | Frente del local, con cartel visible | 1200 × 900 |
| `recepcion.jpg` | Recepción / admisión | 900 × 700 |
| `consultorio.jpg` | Un consultorio | 900 × 700 |
| `sala-espera.jpg` | Sala de espera | 900 × 700 |
| `laboratorio.jpg` | Sector de laboratorio | 900 × 700 |

La primera foto (`fachada.jpg`) funciona como sonda: mientras no exista, la
sección entera se oculta para no mostrar una fila de recuadros vacíos.

## Retratos → `fotos/equipo/`

Ya cargados: `ginecologia-obstetricia.jpeg`, `traumatologia.jpeg`,
`medicina-familiar.jpeg`, `pediatria.jpeg`, `psicologia.jpeg` y
`nutricion.jpeg`.

Se declaran en `PROFESIONALES`, dentro de `tools/build.py`.

Para sumar retratos nuevos: verticales, recorte cercano a 1:1.1 (por ejemplo
600 × 660), fondo limpio y encuadre parejo entre todos. La foto de pediatría
tiene un fondo distinto al resto; si consiguen una de estudio, queda más
parejo.

## Recomendaciones

- **JPG** o **WebP**, calidad 80, por debajo de 300 KB cada una.
- Horizontales para la galería, verticales para los retratos.
- Con personas identificables hace falta su autorización para publicarlas.
- No usar bancos de imágenes como si fueran del lugar o del equipo.
