module.exports = {
  dateFormat: "YYYY-MM-DD",

  sourceDir: "content",
  targetDir: "public",
  staticDir: "static",

  site: {
    title: "Wiki",
    author: "Kimmy",
    copyright: "Copyright &copy; Kimmy",
    baseUrl: "https://wiki.kimleo.net/",
  },

  templates: {
    post: "template/index.html.ejs",
    sitemap: "template/sitemap.xml.ejs"
  }
}
