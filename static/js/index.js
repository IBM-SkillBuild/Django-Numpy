{
  if (history.forward(1))
    location.replace(history.forward(1))
}

const texto = document.querySelector('h1');

function cambiartextoh1() {
  texto.innerHTML = "Has seleccionado " +$("#numeros").val()
}