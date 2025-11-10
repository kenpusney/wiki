
const markdownIt = require("markdown-it");

const mk = require("@vscode/markdown-it-katex").default;

const iterator = require("markdown-it-for-inline");

const {
  cnmd_handlers, highlight, fixStaticFileLink
} = require("./markup/helpers");

const md = markdownIt({
  html: true,
  highlight,  
});


md.use(mk);

md.use(iterator, 'cnmd_link', 'link_open', function (tokens, idx) {
    if (tokens[idx + 2]?.type !== 'link_close' || tokens[idx + 1]?.type !== 'text') {
      return;
    } else {
      const href = tokens[idx].attrGet('href')
      
      if (href === undefined || href === '') {
        // process cross links

        const link = tokens[idx + 1].content;
        let protocol = "";
        let target = "";
        if (link.startsWith(":")) {
          target = link.slice(1);
        } else {
          const parts = link.split(":");
          protocol = parts[0];
          target = parts[1];
        }
        cnmd_handlers[protocol](target, (link, content) => {
          tokens[idx].attrSet('href', link)
          tokens[idx + 1].content = content
        })          
      }
    }
});



md.use(iterator, 'cnmd_image', 'image', function (tokens, idx) {
  const src = tokens[idx].attrGet('src')
  tokens[idx].attrSet('src', fixStaticFileLink(src))
})


// TODO: fix all image captions
// format: ![alt-text](image.png 'caption')
md.use(require("@andatoshiki/markdown-it-image-caption"))

function markup(wikiItem, wiki) {

  let children = [];

  if (wikiItem.isCategory) {
    children = wiki.childPosts(wikiItem.visitPath);
  }

  return {
    ...wikiItem,
    marked: md.render(wikiItem.body),
    posts: children,
  };
}

module.exports = {
  markup
}
