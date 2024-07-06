import simple_screen as ssc


with ssc.manager:
    ssc.resize_terminal(40, 25)
    ssc.pair(ssc.YELLOW, ssc.DARK_BLUE)
    ssc.Print("HOLA")
    nombre = ssc.Input("¿cómo te llamas? ")

    ssc.Print()
    ssc.Print(f"Encantado de conocerte, {nombre}")
    ssc.Input()
