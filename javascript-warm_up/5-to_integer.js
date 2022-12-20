#!/usr/bin/node
const process = require('process');

myargs = process.argv

if (parseInt(myargs[2])){
    console.log('My number: ' + myargs[2])
}
else{
    console.log('Not a number')
}
