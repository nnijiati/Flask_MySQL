var my_string = "this is a string"

console.log(my_string)

my_string = 345;

console.log(my_string)

var array = [];

array.push(my_string, "cat");

console.log(array)

for (var index = 0; index < array.length; index++){
    console.log("index", index, array[index])
}

for (var element in array){
    console.log(array[element])
}

for (var element in array){
    console.log("for-of",element)
}

var person = {
    hair: "brown",
    age: 40
}
person["weight"] =160;
console.log(person)


function sayHello(name){
    console.log("Hello " + name)
    console.log(`Hello ${name} --template`)
}

sayHello("Jason");