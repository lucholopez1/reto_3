# reto_3

- The first thing I did was making the class diagram of the exercise in mermaid:

```mermaid
classDiagram
    MenuItem <|-- Beverage
    MenuItem <|-- Appetizer
    MenuItem <|-- MainCourse
    Order --* MenuItem
    
    MenuItem : +String nombre
    MenuItem : +Float precio
    MenuItem : +Float calcular_precio_total()


    class Beverage{
      +String tamaño
    }

    class Appetizer{
      +String porcion
    }

    class MainCourse{
      +String coccion
    }

    class Order{
        +list items
        +añadir_item(item: MenuItem)
        +calcular_total_recibo()
        +aplicar_descuento(Float discount_percentage)
    }
