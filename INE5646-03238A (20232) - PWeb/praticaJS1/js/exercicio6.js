function tratadorDeCliqueExercicio6(){
    var stringRecebida = prompt("Digite uma string para ser invertida")
    var stringInvertida = inverterString(stringRecebida)
    console.log(stringInvertida)
}

function inverterString(stringNormal){
    stringInvertida = stringNormal.split('').reverse().join('');
    return stringInvertida
}
