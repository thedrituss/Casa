class Calculadora:
    def __init__(self, numero1 = 0, numero2 = 0):
        self._numero1 = numero1
        self._numero2 = numero2
    
    @property
    def numero1(self):
        return self._numero1
    
    @numero1.setter
    def numero1 (self, valor):
        if isinstance (valor, (int, float)):
            self.numero1 = valor
        else:
            raise ValueError ("El número debe ser entero o float")
    
    @property
    def numero2(self):
        return self._numero2
    
    @numero2.setter
    def numero2 (self, valor):
        if isinstance (valor, (int, float)):
            self.numero2 = valor
        else:
            raise ValueError ("El número debe ser entero o float")
        
    
    def sumar (self):
        return self._numero1 + self._numero2
    
    def restar (self):
        return self._numero1 - self._numero2
    
    def multiplicar (self):
        return self.numero1 * self._numero2
    
    def dividir (self):
        if self._numero2 == 0:
            raise ZeroDivisionError ("La división no puede ser entre 0")
        return self._numero1 / self._numero2
    
    
class Menu:
    def mostrar_menu(self):
        while True:
            print("\nCalculadora")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == 5:
                break
            
            
            try:
                num1 = float(input("Dame el primer número: "))
                num2 = float(input("Dame el primer número: "))
                calc = Calculadora(num1, num2)
                
                if opcion == 1:
                    return print(f"Resultado: ", calc.sumar())
                elif opcion == "2":
                    print("Resultado:", calc.restar())
                elif opcion == "3":
                    print("Resultado:", calc.multiplicar())
                elif opcion == "4":
                    print("Resultado:", calc.dividir())
                else:
                    print("Opción no válida. Intente de nuevo.")
                
            except ValueError:
                print("Ingresa valores numéricos")
                
            except ZeroDivisionError:
                print("Error: La division no puede ser entre 0")
    
if __name__ == "__main__":
   menu = Menu()
   menu.mostrar_menu() 