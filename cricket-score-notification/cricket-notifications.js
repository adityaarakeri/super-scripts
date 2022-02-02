const notifier = require('node-notifier');
const cricLive = require('cric-live');

function displayv2() {
  cricLive.getRecentMatches()
    .then(currentMatches => {
       const obj = currentMatches[0];
       const teams = []
       let i =0;
       for(let team in obj.teams){
         teams[i] = obj.teams[team].shortName 
         i+=1;
       }
      const target = obj.score.target ? `${obj.score.target}` : 'First Innings';
      const team = obj.score.detail.batting.shortName;
      const runs = obj.score.detail.batting.score;
      const wickets = obj.score.detail.batting.wickets;
      const overs = obj.score.detail.batting.overs;  
      notifier.notify({
        title: `${teams[0]} Vs ${teams[1]}`,
        message: `${team} ${runs}/${wickets} (${overs})\nTarget: ${target}`,
        timeout: 2,
      });
    }).catch(err => {
      notifier.notify({
        title: err.message,
        message: "",
        timeout: 2,
      });
    });
}

setInterval(function(){
  displayv2();
}, 1000 * 30 * 1)
displayv2();
