
const jieba = require("@node-rs/jieba");

const {load, cut, extract, tag, cutForSearch} = jieba;

load()

const fs = require("fs");

let text = fs.readFileSync("content/articles/a-failure-of-abstraction.md");


let result = cutForSearch(text)

console.log(result)