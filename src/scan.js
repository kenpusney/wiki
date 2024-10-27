
const glob = require("glob")

async function scan({patterns, ignore}) {
  return new Promise(function(resolve, reject) {
    glob(patterns, {ignore}, (err, matches) => {
      if (!err) {
        resolve(matches)
      } else {
        reject(err)
      }
    })
  })
}

module.exports = {
  scan
}
