function haOnzeDigitos(cpf) {
    verificaOnzeDigitos = cpf.length == 11 ? true : false
    return verificaOnzeDigitos
}

function todosOsOnzeDigitosSaoNumeros(cpf) {
    nums = ['0','1','2','3','4','5','6','7','8','9']
    for (const numero of cpf){
        if (nums.includes(numero) == false){
            return false
        }
    }
    return true
}

function osOnzeNumerosSaoDiferentes(cpf) {
    //---- edite aqui para a validação do exercício 9c
    primeiroNumero = cpf[0]
    for (let numero of cpf){
        if (numero != primeiroNumero){
            return true
        }
    }
    return false
}

function oPrimeiroDigitoVerificadorEhValido(cpf) {
    //---- edite aqui para a validação do exercício 9d
    var soma = 0
    let pos = 0
    for (let i = 10; i > 1 ; i--){
        soma = soma + cpf[pos]*(i)
        pos += 1
    }
    let primeiroDigitoVerificador = (soma*10)%11
    let decimoNumero = parseInt(cpf[9], 10)
    let verificaPrimeiroDigitoVerificador = primeiroDigitoVerificador == decimoNumero ? true : false
    if (decimoNumero == 0 && primeiroDigitoVerificador == 10){
        verificaPrimeiroDigitoVerificador = true
    }
    return verificaPrimeiroDigitoVerificador
}

function oSegundoDigitoVerificadorEhValido(cpf) {
    //---- edite aqui para a validação do exercício 9e
    var soma = 0
    let pos = 0
    for (let i = 11; i > 1 ; i--){
        soma = soma + cpf[pos]*1
        pos += 1
    }
    let segundoDigitoVerificador = (soma*10)%11
    let decimoPrimeiroNumero = parseInt(cpf[10], 10)
    let verificaSegundoDigitoVerificador = segundoDigitoVerificador == decimoPrimeiroNumero ? true : false
    if (decimoPrimeiroNumero == 0 && segundoDigitoVerificador == 10){
        verificaSegundoDigitoVerificador = true
        console.log(decimoPrimeiroNumero, segundoDigitoVerificador)
    }
    return verificaSegundoDigitoVerificador
}





//------------------- Não edite abaixo ----------------------------
function validarCPF(validacao, cpf) {
    switch (validacao) {
        case "onzeDigitos": return haOnzeDigitos(cpf)
        case "onzeSaoNumeros": return todosOsOnzeDigitosSaoNumeros(cpf) && validarCPF("onzeDigitos", cpf)
        case "naoSaoTodosIguais": return osOnzeNumerosSaoDiferentes(cpf) && validarCPF("onzeSaoNumeros", cpf)
        case "verificador10": return oPrimeiroDigitoVerificadorEhValido(cpf) && validarCPF("naoSaoTodosIguais", cpf)
        case "verificador11": return oSegundoDigitoVerificadorEhValido(cpf) && validarCPF("verificador10", cpf)

        default:
            console.error(validacao+" é um botão desconhecido...")
            return false
    }
}


function tratadorDeCliqueExercicio9(nomeDoBotao) {
    const cpf = document.getElementById("textCPF").value

    const validacao = (nomeDoBotao === "validade") ? "verificador11": nomeDoBotao
    const valido = validarCPF(validacao, cpf)
    const validoString = valido ? "valido": "inválido"
    const validadeMensagem = "O CPF informado ("+cpf+") é "+ validoString
    console.log(validadeMensagem)

    if (nomeDoBotao !== "validade") {
        let divResultado = document.getElementById(validacao);
        divResultado.textContent = validoString
        divResultado.setAttribute("class", valido ? "divValidadeValido": "divValidadeInvalido")    
    } else {
        window.alert(validadeMensagem)
    }

    
}