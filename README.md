# Sistema de Agendamiento Médico (Landing Page & Búsqueda) 🏥

Este repositorio contiene la maquetación web de la interfaz de usuario para un sistema de citas médicas. El proyecto se centra en la fidelidad visual (Pixel Perfect) y el diseño responsivo, traduciendo directamente las especificaciones de diseño construidas en Figma a código puro.

## 🛠️ Tecnologías Utilizadas

* **Diseño UI/UX:** Figma (Prototipado, Auto Layout, Assets vectoriales).
* **Frontend:** HTML5 Semántico, CSS3 (Flexbox, CSS Grid, Scroll Snapping, Media Queries).
* **Control de Versiones:** Git y GitHub.

## 🧩 Arquitectura CSS y Trabajo Colaborativo

### Integrantes + Función
- Emilio Córdova: Diseño de escritorio `styles.css`
- Fernando Lema: Diseño de tablet `tablet.css`
- Carlos Ruíz: Diseño de teléfono `mobile.css`

Durante la fase de desarrollo, la estructuración de los estilos se dividió estratégicamente en tres archivos físicos independientes (`mobile.css`, `tablet.css` y el `styles.css` principal). Esta modularidad nos permitió dividir las tareas del equipo y trabajar de forma colaborativa en los distintos puntos de quiebre sin generar conflictos en el control de versiones.

Una vez finalizado el diseño, **el código fue unificado en un único archivo principal (`styles.css`)** utilizando `@media queries`. 

*Nota: Los archivos originales de tablet y teléfono continúan alojados en este repositorio exclusivamente como evidencia académica de la división del trabajo colaborativo y la evolución técnica del proyecto.*

## 🚀 Pasos a Futuro

* Integración de la vista de médicos (`search-results.html`) con una base de datos **MySQL**.
* Construcción del backend para renderizar dinámicamente la disponibilidad de horarios de los doctores mediante bucles de datos.
