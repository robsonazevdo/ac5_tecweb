/*console.log('olaaaaaaa mundo');
alert('ola mundo na janela');
console.log('olaaaa mundo');
document.write('Tecweb 2020')*/



/*var a;
a = 4;
var b = 5;
var c = a * c;
document.write(c);
console.log(c);*/


/*var idade = window.prompt("Insira sua idade");
if(idade < 18){
    document.write("Você é maior de idade.");
}
else{
    document.write("Você não é maior de idade.");
}*/


/*var numero = window.prompt('Insira um numero');
if(numero % 2 == 1)
    document.write('o numero ' + numero + ' é Impar')
else
    document.write('o numero ' + numero + ' é Par')*/


//for (var i = 1; i <= 100; i++){
//    console.log(i);
//}

//var i = 1;
//while (i <= 200){
 //   console.log(i);
 //   i++;
//}

/*function quadrado(x) {
    return x * x;
}

function multiplicacao(x,y){
    return x * y;
}

var n = quadrado(6);
console.log(n);

console.log(multiplicacao(5,8));*/


//var a = [5,2,7,8];
//console.log(a);

const app =document.getElementById('raiz')
//app.textContent = "oiiiiii";

const caixa = document.createElement('div');
//caixa.textContent = "Foi criado dinamicamente";
caixa.setAttribute('class','caixa');
app.appendChild(caixa);

for(var i = 1; i <= 10; i++){
    var c = document.createElement('div');
    c.setAttribute('class','artigos')
    caixa.appendChild(c);

    var t = document.createElement('h3');
    t.textContent = 'Título ' + i;
    c.appendChild(t);

    var p = document.createElement('p');
    p.textContent = 'The orphan Sheeta inherited a mysterious crystal that links her to the mythical sky-kingdom of Laputa.';
    c.appendChild(p);
}