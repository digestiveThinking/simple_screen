import simple_screen as ssc


with ssc.manager:
    ssc.pair(ssc.YELLOW, ssc.DARK_BLUE)
    ssc.Print("HOLA")
    nombre = ssc.Input("¿cómo te llamas? ")

    ssc.Print()
    ssc.Print(f"Encantado de conocerte, {nombre}")
    ssc.Input()
