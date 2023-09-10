function tratadorDeCliqueExercicio4(){
    let numeroInformado = prompt("Escolha um numero: ")
    numeroInformado = parseInt(numeroInformado, 10)
    if (numeroInformado >= 30 && numeroInformado <= 50){
        console.log(`${numeroInformado} está no intervalo [30, 50]`)
    }
    else if (numeroInformado >= 60 && numeroInformado <= 100){
    console.log(`${numeroInformado} está no intervalo [60, 100]`)
    }
    else{ console.log("O número informado não está em nenhum dos dois intervalos.")
    }
}