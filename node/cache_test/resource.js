
request = require("request");
template = require("Mustache");

/* Define and working of resource generic layer */
function resource(url, data) {
  /* Store arguments to class variables for class methods to use */
  this.url = url;
  this.data = data;
}

resource.prototype.get = function(args, callback){
  /* Perform string template substitution */
  newUrl = template.render(this.url, args); 
  console.log("Url formed - ", newUrl);

  /* Perform the request opertation */
  req = request(newUrl, callback);
}
resource.prototype.update = function(){
  /* Perform string template substitution */

  /* Perform the request opertation */
}

/* Define the return */
module.exports = resource;
