#!/usr/bin/node
let process = require('process')
if (parseInt(process.argv[2])){    
    let n_times = parseInt(process.argv[2])
    let line = 'X'.repeat(n_times);
    for (let i = 1; i <= n_times; i++){
        console.log(line);
    }
}
else{
    console.log('Missing size')
}