function tratadorDeCliqueExercicio6(){
    var stringRecebida = prompt("Digite uma string para ser invertida")
    var stringInvertida = inverterString(stringRecebida)
    console.log(stringInvertida)
}


function inverterString(stringNormal){
    stringNormal = stringNormal.split('');
    stringInvertida = stringNormal.reverse()
    stringInvertida = stringInvertida.join('')
    return stringInvertida
}
