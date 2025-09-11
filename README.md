# Peticiones

Este repositorio forma parte de mi Trabajo de Fin de Grado (TFG) titulado:  
**"Implementación de un panel de control para mejorar la gestión de peticiones de reparación de piezas de inventario"**.

Aquí se encuentra alojado el **chatbot** desarrollado como parte de dicho trabajo. Su función principal es asistir en la gestión y seguimiento de las solicitudes de reparación de piezas de inventario, facilitando la interacción entre los usuarios y el sistema de mantenimiento.

## 📌 Objetivos del proyecto

- Optimizar el proceso de gestión de peticiones de reparación.
- Automatizar respuestas frecuentes mediante un asistente conversacional.
- Integrar el chatbot con una API para consultar y registrar información relevante del inventario.

## 🛠️ Tecnologías utilizadas

- Lenguaje: [Python]
- Frameworks / Librerías: [PandasAI]
- Base de datos: [Peticiones]
- Integración con API externa para gestión de datos

## 🛠️ Base de datos utilizada

Se ha realizado una consulta con ChatGPT con el siguiente prompt: "Teniendo estos campos: AbiertoCerrado	Planta	CosteTotal	Estado	NPantera	FechaAlta	Descripcion: Podrias inventarte unos datos de 1000 filas siguiendo estas directrices: AbiertoCerrado solo coge valores Abierto o Cerrado. Planta debe ser una entre Motores, Carrocerías, Montaje, MtoCentral, Pinturas. CosteTotal es lo que ha costado la pieza. Estado si la peticion es Cerrada recibe 6.Cerrado siempre, pero si es Abierta puede recibir 1.Por Tramitar, 2.Por Ofertar, 3.Por Aprobar, 4.Por Recibir, 5.Por Cerrar. NPantera es un ID de 9 caracteres donde los 2 primeros son letras. FechaAlta la fecha en formato DD/MM/YY. Descripcion es una descripción corta de la pieza. Ten en cuenta que son unos datos de una factoría de coches". De esta forma, se ha obtenido una base de datos FICTICIA que EMULA la base de datos original para comprobar su uso en un entorno real. NADA DE LO INCLUIDO EN LA BASE DE DATOS ES VERÍDICO.

Carlos Torregrosa Alcayde
