from abc import ABCMeta, abstractmethod

"""
La implementacion de la clase Singelton en Python no es segura con programación multihilo.
El patron de diseño Singelton busca crear una sola instancia  de forma global de una clase. 
Una implementacion para solucionar esto está en el archivo pruebapatronsingelton.py de este
repositorio, en este fragmento concretamente se elimina la condición de carrrera:

with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]  
"""

class SingletonABCMeta(ABCMeta):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonABCMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class GenericLogger(metaclass=SingletonABCMeta):

    @abstractmethod
    def SearchLink(self): pass


class Logger(GenericLogger):

    def SearchLink(self): return ''
