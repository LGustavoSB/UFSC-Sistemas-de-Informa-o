function obterRegiaoFiscalAtravesDoCPFInformado(cpfInformado) {
    
    //edite esta função!
    var regiaoFiscal = undefined
    console.log(cpfInformado)
    nonoNumero = cpfInformado.slice(8,9)
    console.log(nonoNumero)
    let regioesFiscais = new Map()
    regioesFiscais.set(1, 'DF, GO, MT, MS e TO');
    regioesFiscais.set(2, 'AC, AP, AM, PA, RO e RR');
    regioesFiscais.set(3, 'CE, MA e PI');
    regioesFiscais.set(4, 'AL, PB, PE e RN');
    regioesFiscais.set(5, 'BA e SE');
    regioesFiscais.set(6,'MG');
    regioesFiscais.set(7,'ES e RJ');
    regioesFiscais.set(8,'SP');
    regioesFiscais.set(9,'PR e SC');
    regioesFiscais.set(0,'RS');
    regioesFiscais[Symbol.iterator]
    for (const item of regioesFiscais){
        if (item[0] == nonoNumero){
            regiaoFiscal = item[1]
        }
    }

    //----------------------------
    return regiaoFiscal
}



function tratadorDeCliqueExercicio8() {
    let textCPF = document.getElementById("textCPF")
	let textRegiao = document.getElementById("regiaoFiscal")

    const regiaoFiscal = obterRegiaoFiscalAtravesDoCPFInformado(textCPF.value);
    textRegiao.textContent = "Região fiscal: "+regiaoFiscal
}
