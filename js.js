const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Digite o seu nome: ', (nomeUsuario) => {
    rl.question('Digite a sua idade: ', (idadeUsuario) => {
        if (nomeUsuario && idadeUsuario) {
            console.log(`Seu nome é ${nomeUsuario}`);
        } else {
            console.log('Desculpe, você deixou campos vazios');
        }
        rl.close();
    });
});
