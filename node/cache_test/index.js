#!/usr/bin/env node

apis = require("./factory");

var callback_func = function (error, response, body) {
  if (!error && response.statusCode == 200) {
    console.log(body);  
  }
};

/* Without argument */
apis.globalApi.listPosts(callback_func);

/* With argument */
apis.globalApi.getPost(10, callback_func);


