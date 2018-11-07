var system = require('system');
var args = system.args;
url = args[1]
output = args[2]

console.log("Converting to image...")

var page = require('webpage').create();
page.viewPort = {
    width: 382,
}
page.open(url, function() {
    page.render(output)
    phantom.exit();
});
