# Singelton 
## Singelton patttern
Patron de diseño que pretende crear una sola instancia de una clase de acceso global.
## Singelton en Python
Es una metaclase. Singleton(metaclass=ABCMeta)

Python no permite la creacion de este patrón en entornos donde existe multi-threading. Inconveniente solucionado en pruebapatronsingelton.py con la sentencia "with cls._lock: line 27" (explicado en comentarios).
