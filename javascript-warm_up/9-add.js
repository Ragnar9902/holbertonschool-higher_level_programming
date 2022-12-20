#!/usr/bin/node
let process = require('process')
if (parseInt(process.argv[2]) && parseInt(process.argv[3])){    
    let num_a = parseInt(process.argv[2]);
    let num_b = parseInt(process.argv[3]);
    
    console.log(num_a + num_b);
}
else{
    console.log(parseInt(process.argv[2]))
}