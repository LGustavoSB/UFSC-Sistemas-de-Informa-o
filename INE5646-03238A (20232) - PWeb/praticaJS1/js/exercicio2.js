function tratadorDeCliqueExercicio2() {
    // atualize esta função para
    // exibir um alerta com a hora 
    // atual no seguinte formato:
    // Horário: 8 PM : 40m : 28s
    let dataAtual = new Date();
    ampm = Date.getHours >= 12 ? 'AM' : 'PM'
    hora = dataAtual.getHours > 12 ? dataAtual.getHours() : dataAtual.getHours() - 12
    minuto = dataAtual.getMinutes()
    segundo = dataAtual.getSeconds()
    horaAtual = ` ${hora} ${ampm} : ${minuto} m : ${segundo} s `;
    alert(horaAtual);
    console.log('adicionar código na função tratadorDeCliqueExercicio2() em ./js/exercicio2.js');
}