# Policlínica Sanitas — Lambaré, Paraguay

Sitio estático, sin dependencias de runtime. Se sube tal cual a cualquier
hosting o CDN.

```
index.html                         página principal
especialidades/<slug>/index.html   una página por especialidad (campañas)
assets/estilos.css                 estilos compartidos por todas las páginas
assets/app.js                      scripts compartidos
fotos/                             logo y fotos (ver fotos/README.md)
tools/build.py                     genera el HTML a partir de los datos
```

## Cómo está pensada la página

El orden responde a lo que necesita alguien que llega de un anuncio con un
problema concreto, no a lo que la clínica quiere contar de sí misma:

**necesidad → profesional → especialidad → estudios → cómo agendar → dónde queda → CTA**

1. **Hero** — «¿Necesitás consultar con un médico?» y qué se hace al respecto.
2. **Datos concretos** — profesionales, horario, estudios en el lugar, dirección.
3. **Profesionales** — foto, especialidad y motivos de consulta de cada uno,
   con su propio WhatsApp.
4. **Especialidades** — descriptas por problema («Dolores, lesiones, caídas»),
   no por nombre técnico.
5. **Motivos de consulta** — accesos directos a WhatsApp por síntoma.
6. **Estudios y procedimientos** + **Laboratorio**.
7. **Atención a domicilio**.
8. **Cómo pedir un turno** — tres pasos.
9. **Así es la policlínica** — galería (se oculta hasta que haya fotos).
10. **Ubicación y horarios** + cobertura.
11. **CTA final**.

### Reglas de redacción

Cada frase tiene que ayudar al paciente a decidir si Sanitas resuelve lo que
necesita ahora. Si sólo dice que la clínica es «completa», «humana», «cercana»
o «de confianza», se reemplaza por información concreta.

Quedan fuera: «atención cercana y sin complicaciones», «cuidamos de vos en
cada etapa», «tu salud es nuestra prioridad», «atención humanizada», «la
solución que merecés». También quedan fuera las promesas de resultado médico
(«solucionamos tu problema de raíz»): se habla de evaluar, diagnosticar,
tratar y hacer seguimiento.

Español de Paraguay, con voseo, en tono directo.

## Páginas por especialidad

Una página por especialidad, para mandar tráfico segmentado sin obligar a
nadie a buscar dentro de la página general. Quien busca «ginecólogo en
Lambaré» cae en `especialidades/ginecologia-obstetricia/index.html` y ve de
entrada a la profesional, los motivos de consulta, los estudios relacionados y
el WhatsApp.

Hoy existen siete: ginecología y obstetricia, traumatología, medicina familiar,
pediatría, psicología, cardiología y nutrición.

## Editar el contenido

Todo el texto vive en `tools/build.py`, arriba de todo: `PROFESIONALES`,
`ESPECIALIDADES`, `ESTUDIOS`, `MOTIVOS` y `GALERIA`. Después de cambiar algo:

```bash
python3 tools/build.py
```

Regenera `index.html` y las seis páginas de especialidad, consistentes entre
sí. Editar el HTML a mano funciona, pero el próximo build lo pisa.

## Identidad

Rojo Sanitas (#86151B, tomado del logo) sobre blanco. Los tokens están en
`assets/estilos.css`, en el bloque `:root`. Los neutros están sesgados hacia
el rojo; el grafito da variedad sin ensuciar la marca.

El verde aparece sólo con función propia: los tildes de confirmación y el
botón flotante de WhatsApp, que se deja verde porque es el color con el que
la gente reconoce ese canal.

## Profesionales

Los siete retratos están cargados, **identificados sólo por especialidad**: la
policlínica todavía no envió nombres ni registros profesionales, y no se
inventa ninguno. Cuando lleguen, se agregan en `PROFESIONALES`:

```python
dict(slug='ginecologia-obstetricia', esp='Ginecología y Obstetricia',
     nombre='Dra. [Nombre]', registro='Reg. Prof. [número]',
     ...)
```

Falta también confirmar **días y horarios de atención de cada profesional**.
Mientras tanto cada tarjeta dice «Consultá días y horarios disponibles».

## Mapa

Coordenadas: **-25.3465404, -57.6000046**, provistas por el cliente.
Alimentan el embed de Google Maps, el botón «Cómo llegar» y el campo `geo` de
los datos estructurados. El embed no usa API key y se carga recién cuando el
visitante se acerca a la sección.

Si el iframe no carga, el bloque muestra igual el nombre, la dirección y un
enlace a Google Maps: el cartón queda debajo del iframe, sin ninguna detección
por JavaScript.

El punto corresponde a la calle, no al número de puerta. Para ajustarlo,
cambiá `LAT` y `LNG` en `tools/build.py` y volvé a generar.

## Lo que falta

- Nombres y registros profesionales de los siete profesionales.
- Días y horarios de atención de cada uno.
- Confirmar con la policlínica que el retrato de cardiología
  (`fotos/equipo/cardiologia.jpg`) corresponde al profesional que atiende
  ahí y que se puede publicar.
- Las fotos del local (ver `fotos/README.md`).
- Confirmar si «Clínica General» y «Medicina Familiar» son la misma área:
  hoy figuran unificadas en una sola tarjeta.
