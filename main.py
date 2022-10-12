contador_de_cosas = 0

def on_button_pressed_a():
    global contador_de_cosas
    contador_de_cosas = contador_de_cosas + 5
    basic.show_number(contador_de_cosas)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global contador_de_cosas
    while contador_de_cosas > 0:
        if contador_de_cosas >= 5:
            contador_de_cosas = contador_de_cosas - 5
        else:
            contador_de_cosas = contador_de_cosas + 1
        serial.write_number(contador_de_cosas)
input.on_button_pressed(Button.B, on_button_pressed_b)
