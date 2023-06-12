const hljs = require("highlight.js");

const cnmd_handlers = 
{
  "": (postfix, render) => render(`/${postfix}`, postfix),
  "github": (postfix, render) => render(`https://github.com/${postfix}`, postfix),
  "\\": (postfix, render) => render(`:${postfix}`, postfix),
  "twitter": (postfix, render) => render(`https://twitter.com/${postfix}`, postfix),
  "wiki": (postfix, render) => render(`https://en.wikipedia.org/wiki/${postfix}`, postfix),
}

function highlight(code, lang) {
  if (lang && hljs.listLanguages().includes(lang)) {
    return hljs.highlight(lang, code, true).value;
  } else {
    return hljs.highlightAuto(code).value;
  }
}

function fixStaticFileLink(href) {
  if (href.startsWith("../"))
    return href.substring(href.search("static") + "static".length);
  return href;
}

module.exports = {
  cnmd_handlers, highlight, fixStaticFileLink
}
