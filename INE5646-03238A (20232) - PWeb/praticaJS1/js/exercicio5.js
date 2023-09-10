function convertCelciusToFahrenheit(celcius) {
	var temperaturaFahrenheit = (celcius * (9/5)) + 32
	return temperaturaFahrenheit
}





// -- Não edite abaixo!

function conversaoCtoF() {
	let textCelcius = document.getElementById("celciusText")
	let textFahrenheit = document.getElementById("resultFahrenheit")
	textFahrenheit.textContent = convertCelciusToFahrenheit(textCelcius.value) + 
								 "ºF"
}