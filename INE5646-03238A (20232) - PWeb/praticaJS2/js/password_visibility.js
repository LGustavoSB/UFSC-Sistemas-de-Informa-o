
function mostrarSenha() {
    document.getElementById('login-password').type = 'text';
}

function ocultarSenha() {
    document.getElementById('login-password').type = 'password';
}

function alterarVisibilidade(){
    var senha = document.getElementById('login-password')
    if (senha.type == 'password'){
        mostrarSenha()
    }
    else{
        ocultarSenha()
    }
}