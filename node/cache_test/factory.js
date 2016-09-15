
res = require("./resource");

/* All URL definitions */
url = "https://jsonplaceholder.typicode.com";
posts = new res(url + "/posts/{{post_id}}{{^post_id}}{{/post_id}}");

/* Defining all global functions here */
function globalApi() {
  return {
    listPosts : function(callback) { return posts.get({}, callback); },
    getPost : function(postId, callback) { return posts.get({post_id: postId}, callback); }
  };
}

/* Return global and account API */
module.exports = {
  globalApi: globalApi(),
};

