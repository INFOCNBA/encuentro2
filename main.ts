let contador_de_cosas = 0
input.onButtonPressed(Button.A, function () {
    contador_de_cosas = contador_de_cosas + 3
    basic.showNumber(contador_de_cosas)
})
input.onButtonPressed(Button.B, function () {
    while (contador_de_cosas > 0) {
        if (contador_de_cosas >= 6) {
            contador_de_cosas = contador_de_cosas - 3
        } else {
            contador_de_cosas = contador_de_cosas - 1
        }
        basic.showNumber(contador_de_cosas)
    }
})
