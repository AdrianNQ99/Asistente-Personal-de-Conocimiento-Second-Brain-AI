"""
Paquete de Servicios (Lógica de Negocio)
==========================================

Los servicios contienen la lógica de negocio SEPARADA de los endpoints.
Esto hace el código más limpio, testeable y reutilizable.

💡 Patrón: Endpoint → Service → Database
   El endpoint recibe la petición, el service hace la lógica, la DB guarda datos.
"""
