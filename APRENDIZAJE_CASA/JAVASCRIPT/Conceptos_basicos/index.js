// esto es un comentario
var numero = 18;

console.log(" Mi edad es: " + numero);

nuemro = 20;

console.log(" Mi edad ahora es: " + nuemro)

const miConstante = 3;

console.log(" El valor de mi constante es: " + miConstante)

var op1 = 2;
var op2 = 3;
var resultado = op1+op2;

console.log(" El resultado vale: " + resultado);

CONDICIONALES

let miNumero = 6;
let miNombre = "Santiago";
let resultadoPregunta = miNumero ==7;
console.log(resultadoPregunta)

if(miNumero <2 || miNombre == "santiago"){

    console.log("Si.")

}else{

    console.log("No.")

}

let miNumero2 = -5;

if (miNumero2 > 2){

    console.log(" Mi numero es positivo... ")

}else if(miNumero2 ===0){

    console.log(" Mi numero es zero... ")

}else{

    console.log(" Mi numeor es negativo.... ")
}


let contador = 0;

while(contador < 10){
    console.log(contador);

    contador = contador + 1
}

for(let i = 10; i >= 0; i --){

    console.log(i);
}

function Saludar(nombre, edad){

    console.log(" Hola mi nombre es: " + nombre)
    console.log(" Y mi edad es: " + edad)
}

function Multiplicar(num1, num2){

    let resultado = num1*num2;
    return resultado;
}

let recibidor = Multiplicar(2,5)

console.log(Multiplicar(2,5));

let miArrelgo = [" santi "," david "," kevin "," carlos "]

for(let i=0;i<4;i++){

    console.log(" Accediendo al indice: " + i);
    let mostrar= miArrelgo[i];
    console.log(mostrar);
}


let persona = {

    nombre : " Santiago. ", 
    edad : 18,
    masculino : true,

};

console.log(persona)
persona.nombre = "Nuevo Nombre";
console.log(persona)

let perosona2 = {
    nombre : "kevin",
    edad : 20,
    masculino : false,
};

console.log(persona);
console.log(perosona2);

length
let arregloDEObjetos = [persona, perosona2]