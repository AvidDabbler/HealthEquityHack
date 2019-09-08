// const csvparser = require ('csv-parser')
const fs = require('fs');
const http = require ("https");
const file = fs.createWriteStream("all_in.json");
const results = [];
let csvToJson = require('convert-csv-to-json');
// require ('../bmf.js')
// require ('../altere_data.csv')
// var csv = require("csvtojson");


//   http.get("https://slalom-hackathon.s3.us-east-2.amazonaws.com/MO+BMF+6.10.2019.csv", response => {
//   response.pipe(file).on('data', (row) => {
//     console.log(row); 
//   })
//   .on('finish', (data) => {
//     console.log('CSV file successfully processed');

//   });
// });



//Use async / await
// csv()
//   .fromFile("./all.csv")
//   .then(function(jsonArrayObj){ //when parse finished, result will be emitted here.
//      console.log(jsonArrayObj); 
//      console.log(util.inspect(jsonArrayObj, {showHidden: false, depth: null}));
//    })

// const util = require('util')

// console.log(util.inspect(jsonArray, {showHidden: false, depth: null}))

// 

 
let json = csvToJson.formatValueByType().getJsonFromCsv("altere_data.csv");
for(let i=0; i<json.length;i++){
    console.log(json[i]);
}
