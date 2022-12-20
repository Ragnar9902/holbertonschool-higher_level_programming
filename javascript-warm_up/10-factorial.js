#!/usr/bin/node
let process = require('process')

function factorial(n){
    if ( n===1 ){
        return 1;
    }
    if (n>89){
        return 'Infinity'
    }
    return n * factorial(n-1);
}
if (parseInt(process.argv[2])){    
    let num = parseInt(process.argv[2]);
    
    console.log(factorial(num));
}
else{
    console.log(1)
}