const axios = require("axios");
var fs = require("fs");
var https = require("https");

async function getInstagramFollowers() {
  console.log("running insta script");
  const { data } = await axios.get(
    "https://www.instagram.com/" + process.argv[2] + "/?__a=1"
  );

  //Node.js Function to save image from External URL.

  const userName = data.graphql.user.username;
  const name = data.graphql.user.full_name;
  const image = data.graphql.user.profile_pic_url_hd;
  const followers = data.graphql.user.edge_followed_by.count;

  await saveImageToDisk(image, userName);

  console.log(`name:${name}  -  username:${userName} - followers:${followers}`);
}

async function saveImageToDisk(url, localPath) {
  var file = fs.createWriteStream(localPath + ".jpg");
  var request = https.get(url, function(response) {
    response.pipe(file);
  });
}

async function go() {
  await getInstagramFollowers();
}

go();
