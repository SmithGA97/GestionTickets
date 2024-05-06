# GestionTickets
Api rest para gestionar los tickets de creación de transacciones en una aplicación de subida de fotos.

# Requerimientos del Sistema

Asegúrate de tener instalados los siguientes servicios:

- PostgreSQL 15
- RabbitMQ

Se crean un par de pruebas en el modulo Ticket, una para la obtención del Token de Auth y otra para la creación del Ticket.

Run: pytest tickets/tests.py