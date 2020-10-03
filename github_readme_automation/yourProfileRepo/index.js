// Importing variables and modules
const fs = require('fs')
const axios = require('axios')

let api = process.env.Ap

//Date fixer?
function timeCalc(fetchedDate) {
  let time = new Date().getTime();
  let minute = 1000 * 60
  let now = Math.round(time / minute);
  let difference = now - fetchedDate
  if (difference <= 59) {
    return (difference)
  }
  let num = difference;
  let hours = (num / 60);
  let rhours = Math.floor(hours);
  let minutes = (hours - rhours) * 60;
  let rminutes = Math.round(minutes);
  if (difference > 59) {
    return rhours + "_hrs_and_" + rminutes;
  }

}

// Function to send api request and everything inside it...
axios.get(api).then(resp => {
  // reformat the returned data into stuff...........
  let file = resp.data.values[0][0]
  let workSpace = resp.data.values[0][1]
  let fetchedDate = resp.data.values[0][2]

  //test-------------test
  console.log(`${file} @  ${workSpace} time ${fetchedDate}`)

  //calculate the difference..
  let diff = timeCalc(fetchedDate)
  let text;
  let col;
  if (file === 'null' || workSpace === 'null') {
    text = "IDLE"
    col = 'orange'
    file = 'No_File_Opened'
    workSpace = "IDLE"
    diff = 69 // xD jk
  }
  else if (diff <= 6) {
    text = "Currently_Editing"
    col = 'green'
  }
  else {
    text = `Seen_${diff}min_ago_editing`
    col = 'red'
  }


  // Normalize text for url support
  var str1 = file;
  var replaced1 = str1.split(' ').join('+');
  var str2 = workSpace;
  var replaced2 = str2.split(' ').join('_');
  var replaced2 = replaced2.split('-').join('_'); //nice emojis ;)

  // get new data to keep it running.. 
  var ctime = new Date().toLocaleTimeString([], { hour: '2-digit', minute: "2-digit", hour12: true });
  console.log(ctime)
  // README.markdown file generation from the data we received.
  fs.writeFile('./README.md', `
## Hello, there ![hi](https://raw.githubusercontent.com/rubenkharel/rubenkharel.github.io/master/namaskaram-mini.gif)
*Welcome, I'm Ruben Kharel!* <br />
*Student at [Islington College](https://islington.edu.np)* <br />
*Building a webapp* <br />

You can Follow me on:<br />
[![DEV Profile!](https://raster.shields.io/badge/Dev.to--black?style=for-the-badge&logo=dev.to)](https://dev.to/rubenk) 
[![Twitter!](https://raster.shields.io/badge/Twitter--skyblue?style=for-the-badge&logo=twitter)](https://twitter.com/rub3nkhar3l) 
[![Linkedin!](https://raster.shields.io/badge/LinkedIn--blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/rubenkharel/) 


*[![FileName!](https://raster.shields.io/badge/${text}--green?style=for-the-badge&color=${col})](https://github.com/rubenkharel)[![FileName!](https://raster.shields.io/badge/-${replaced1}-yellow?style=for-the-badge&logoColor=${col}&color=white&logo=canonical)](https://github.com/rubenkharel)[![WorkSpace!](https://raster.shields.io/badge/VScode-${replaced2}-blue?style=for-the-badge&logo=visual-studio-code)](https://github.com/rubenkharel)*
<br />
**BETA** <br />
*Yes it's a realtime update! **(updates every 6 min)**. Automated with a VScode extension and Github Action. Information bridged with the help of Google Sheet API. You can find the extension and setup instruction [here](https://github.com/rubenkharel/README-VSCODE-Automation)*
### Stuff I play with!
[
![Python!](https://raster.shields.io/badge/Python--blue?style=for-the-badge&logo=python)](https://github.com/rubenkharel) 
[![Javascript!](https://raster.shields.io/badge/javascript--yellow?style=for-the-badge&logo=javascript)](https://github.com/rubenkharel) 
[![MongoDB!](https://raster.shields.io/badge/mongo_db--lightgreen?style=for-the-badge&logoColor=lightgreen&logo=mongodb)](https://github.com/rubenkharel) 
[![Express!](https://raster.shields.io/badge/Express--red?style=for-the-badge&logoColor=red&logo=npm)](https://github.com/rubenkharel) 
[![Nodejs!](https://raster.shields.io/badge/Node.js--yelloorange?style=for-the-badge&logoColor=green&logo=node.js)](https://github.com/rubenkharel) 
[![Bash!](https://raster.shields.io/badge/Bash--brightgreen?style=for-the-badge&logoColor=Green&logo=gnu-bash)](https://github.com/rubenkharel) 
[![HTML5!](https://raster.shields.io/badge/HTML5--critical?style=for-the-badge&logoColor=orange&logo=html5)](https://github.com/rubenkharel) 
[![CSS3!](https://raster.shields.io/badge/CSS3--green?style=for-the-badge&logo=css3)](https://github.com/rubenkharel) 
[![Git!](https://raster.shields.io/badge/Git--critical?style=for-the-badge&logoColor=orange&logo=git)](https://github.com/rubenkharel) 
[![GithubAction!](https://raster.shields.io/badge/Github_actions--9fc?style=for-the-badge&logoColor=deepskyblue&logo=github-actions)](https://github.com/rubenkharel) 
[![Linux!](https://raster.shields.io/badge/Linux--green?style=for-the-badge&logoColor=white&logo=linux)](https://github.com/rubenkharel) 
[![BugBounty!](https://raster.shields.io/badge/Bug_Bounty--green?style=for-the-badge&logo=hackerone)](https://github.com/rubenkharel) 
### Currently Learning <br />
[![react!](https://raster.shields.io/badge/react--9cf?style=for-the-badge&logo=react)](https://github.com/rubenkharel) 
[![LaTex!](https://raster.shields.io/badge/LaTex--9cf?style=for-the-badge&logo=latex)](https://github.com/rubenkharel) 
[![Typescript!](https://raster.shields.io/badge/Typescript--blue?style=for-the-badge&logo=typescript)](https://github.com/rubenkharel) 
<br />
*Readme Updated on: ${ctime}, UTC 0*
`, 'utf8', function (err) {
    if (err) throw err;
    console.log('Saved!')
  })
});


