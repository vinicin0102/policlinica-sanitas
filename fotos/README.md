# Fotos de la Policlínica Sanitas

Subí las imágenes con **exactamente estos nombres**. La página las toma sola:
si un archivo no existe todavía, queda la composición de marca en su lugar y
nada se rompe.

## Estado

| | |
|---|---|
| ✅ `logo.jpeg` | En el header y el footer |
| ✅ `equipo/` (6 retratos) | En la sección del equipo |
| ⬜ Galería de la policlínica | 5 fotos — la sección se oculta hasta que exista `fachada.jpg` |
| ⬜ `recepcion.jpg` | Sección «Sobre Sanitas» |
| ⬜ `etapas/` | 4 fotos |

## Galería «Conocé la policlínica»

| Archivo | Qué mostrar | Tamaño sugerido |
|---|---|---|
| `fachada.jpg` | Frente del local, con cartel visible | 1200 × 900 |
| `recepcion-2.jpg` | Recepción / admisión | 900 × 700 |
| `consultorio.jpg` | Un consultorio | 900 × 700 |
| `sala-espera.jpg` | Sala de espera | 900 × 700 |
| `laboratorio.jpg` | Sector de laboratorio | 900 × 700 |

## Sección «Sobre Sanitas»

| Archivo | Qué mostrar | Tamaño sugerido |
|---|---|---|
| `recepcion.jpg` | La mejor foto del lugar: recepción o interior | 900 × 760 |

## Etapas de la vida → `fotos/etapas/`

| Archivo | Qué mostrar | Tamaño sugerido |
|---|---|---|
| `ninos.jpg` | Atención pediátrica | 640 × 480 |
| `adultos.jpg` | Control clínico de un adulto | 640 × 480 |
| `adultos-mayores.jpg` | Atención a un adulto mayor | 640 × 480 |
| `familias.jpg` | Familia en la policlínica | 640 × 480 |

## Profesionales → `fotos/equipo/`

Ya cargados: `ginecologia-obstetricia.jpeg`, `traumatologia.jpeg`,
`medicina-familiar.jpeg`, `pediatria.jpeg`, `psicologia.jpeg` y
`nutricion.jpeg`.

Se declaran en el array `SANITAS_PROFESIONALES` dentro de `index.html`. Hoy
sólo tienen especialidad; falta agregar nombre y registro profesional de cada
uno cuando la policlínica los envíe.

Para sumar retratos nuevos: verticales, recorte 1:1.1 (por ejemplo 600 × 660),
fondo limpio y encuadre parejo entre todos.

## Recomendaciones

- Formato **JPG** o **WebP**, calidad 80, por debajo de 300 KB cada una.
- Horizontales para la galería, verticales sólo para los retratos.
- Con personas identificables hace falta su autorización para publicarlas.
- No usar fotos de bancos de imágenes como si fueran del lugar o del equipo.
