
function habilitaBotaoEnviar(){
    if (document.getElementById('login-name').value === "" || document.getElementById('login-password').value === ""){
        document.getElementById('botaoLogin').disabled = true
    }
    else{
        document.getElementById('botaoLogin').disabled = false
    }
}

function verificaEmail(){
    if (document.getElementById('login-name').value.indexOf('@', 0) == -1){
        document.getElementById('botaoLogin').disabled = true
        alert('Email deve conter @')
    }
}

function esvaziaCaixasDeTexto(){
    document.getElementById('login-name').value = ''
    document.getElementById('login-password').value = ''
}

function mostrarApenasHome(){
    document.getElementById('login-body').classList.add("displayNone")
    document.getElementById('nova-conta').classList.add("displayNone")
    document.getElementById("divHome").classList.remove("displayNone")
    esvaziaCaixasDeTexto()
}

function mostrarApenasLogin(){
    document.getElementById('divHome').classList.add("displayNone")
    document.getElementById('nova-conta').classList.add("displayNone")
    document.getElementById('login-body').classList.remove("displayNone")
    document.getElementById('botaoLogin').disabled = true
    esvaziaCaixasDeTexto()
}

function mostrarApenasConta(){
    document.getElementById('divHome').classList.add('displayNone')
    document.getElementById('login-body').classList.add('displayNone')
    document.getElementById('nova-conta').classList.remove("displayNone")
    esvaziaCaixasDeTexto()
}



