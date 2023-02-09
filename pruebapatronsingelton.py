from threading import Lock, Thread


class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """

    _instances = {}

    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        # Now, imagine that the program has just been launched. Since there's no
        # Singleton instance yet, multiple threads can simultaneously pass the
        # previous conditional and reach this point almost at the same time. The
        # first of them will acquire lock and will proceed further, while the
        # rest will wait here.
        with cls._lock:
            # The first thread to acquire the lock, reaches this conditional,
            # goes inside and creates the Singleton instance. Once it leaves the
            # lock block, a thread that might have been waiting for the lock
            # release may then enter this section. But since the Singleton field
            # is already initialized, the thread won't create a new object.
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    value: str = None
    """
    We'll use this property to prove that our Singleton really works.
    """

    def __init__(self, value: str) -> None:
        self.value = value

    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """


def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == "__main__":
    # The client code.

    print("If you see the same value, then singleton was reused (yay!)\n"
          "If you see different values, "
          "then 2 singletons were created (booo!!)\n\n"
          "RESULT:\n")

    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()
    
    #EXPLICACIÓN:
    """
    Thread = hilo
    Lock: función que devuelve una instancia de la clase Lock 
    con la versión más eficiente soportada por la plataforma

    Thread.Lock bloquea el Thread

    __call__(self,[args])
Se utiliza para hacer que el objeto pueda ser llamado (como una función), 
de modo que si tenemos una instancia x que define __call__(self, valor) 
podemos hacer x(valor), lo que en realidad es un atajo a x.__call__(valor)

Métodos de instancia: 
    solo pueden ser llamados desde una instancia existente.
    se usa cls para referirse a la clase
Métodos de clase:
    solo pueden ser llamados desde la clase sin instanciar.
    se usa self para referirse a la instancia
    Clases abstractas -> interfaces
    """
    class h():
        v = 0
        def __call__(self, valor):
            self.v = valor
            return self
    holas  = h()
    holas.__call__(334)
    print(holas.v)

   
