const calculadora = (a, b, f) => {
    return f(a, b)
}
const soma = (a, b) => {    
    return a + b
}
const subtrai = (a, b) => {
    return a - b
}

const ex1btn = document.getElementById('ex1');
if (ex1btn != null){
    ex1btn.addEventListener("click", exercicioUm);
}
function exercicioUm(){
    console.log(calculadora(31, 12, soma));
    console.log(calculadora(11, 25, subtrai));
}