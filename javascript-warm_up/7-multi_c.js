#!/usr/bin/node
let process = require('process')
if (parseInt(process.argv[2])){    
    let line = 'C is fun';
    let n_times = parseInt(process.argv[2])
    for (let i = 0; i <= n_times; i++){
        console.log(line);
    }
}
else{
    console.log('Missing number of occurrences')
}