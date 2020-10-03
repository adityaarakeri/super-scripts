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
    text = `Seen_${diff}_min_ago_editing`
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

  

  #

  # ReadMeAutomation-gAction ▶
  
  Hello there ಠ_ಠ
  
  This is a Github Action built for github's **README automation**. The **VS Code Extensions** repo related to this action can be found [**here**](https://marketplace.visualstudio.com/items?itemName=rubenkharel.googlesheetlogger).
  
    
  
  # Demo
  
    
  
  *[![FileName!](https://raster.shields.io/badge/${text}--green?style=for-the-badge&color=${col})](https://github.com/rubenkharel)[![FileName!](https://raster.shields.io/badge/-${replaced1}-yellow?style=for-the-badge&logoColor=${col}&color=white&logo=canonical)](https://github.com/rubenkharel)[![WorkSpace!](https://raster.shields.io/badge/VScode-${replaced2}-blue?style=for-the-badge&logo=visual-studio-code)](https://github.com/rubenkharel)*
  
    
  
  ### There are 3 types..
  
  * Active <br />
  
  *[![FileName!](https://raster.shields.io/badge/Currently_Editing--green?style=for-the-badge&color=green)](https://github.com/rubenkharel)[![FileName!](https://raster.shields.io/badge/-main.py-yellow?style=for-the-badge&color=white&logoColor=green&logo=canonical)](https://github.com/rubenkharel)[![WorkSpace!](https://raster.shields.io/badge/VScode-Folder_name-blue?style=for-the-badge&logo=visual-studio-code)](https://github.com/rubenkharel)*
  
  * Offline <br />
  
  *[![FileName!](https://raster.shields.io/badge/Seen_20_Min_Ago_Editing--red?style=for-the-badge&color=red)](https://github.com/rubenkharel)[![FileName!](https://raster.shields.io/badge/-main.py-yellow?style=for-the-badge&logoColor=red&color=white&logo=canonical)](https://github.com/rubenkharel)[![WorkSpace!](https://raster.shields.io/badge/VScode-Folder_name-blue?style=for-the-badge&logo=visual-studio-code)](https://github.com/rubenkharel)*
  
  * Idle <br />
  
  *[![FileName!](https://raster.shields.io/badge/IDLE--orange?style=for-the-badge&color=orange)](https://github.com/rubenkharel)[![FileName!](https://raster.shields.io/badge/-No_file_Opened-yellow?style=for-the-badge&logoColor=orange&color=white&logo=canonical)](https://github.com/rubenkharel)[![WorkSpace!](https://raster.shields.io/badge/VScode-IDLE-blue?style=for-the-badge&logo=visual-studio-code)](https://github.com/rubenkharel)*
  
    
    
  
  ## Whats behind the curtain? 🦝
  
  Well, being a noob at these web services and stuff, I tried to pull off some ideas to make it work. And got a easy workaround! Thanks to github for providing this amazing Tool called Github Action. And Google Sheet is used as database. Yes, This action requires your Google sheet document and this [VS code extension](https://marketplace.visualstudio.com/items?itemName=rubenkharel.googlesheetlogger). Lot of stuff ayee..
  

  
    
  
  ## How do I use it? 💁‍♂️
  
  It's simple to use this action for yourself!
  
  Just follow these few simple (⊙_⊙;) steps
  
  *Oh did you complete the extension's instruction part yet? if not visit [here](https://github.com/rubenkharel/Google-Sheet-Logger) and do so.*
  
  * After extension stuff is complete, create a github repo, with your username on it. <br />
  Example https://github.com/rubenkharel/rubenkharel <br />
  * Add everything from this repo to your repo.
  * Go to repo settings, **Settings** > **Secrets** > **New Secret** 
  <br />
    Name: <br />
  > "API"
  <br /> 
    Value: <br />
  > https://sheets.googleapis.com/v4/spreadsheets/thatIdWhichYouCopyFromSpreedSheetLink/values/Sheet1?key=APIKEY
  <br />
  These info you got from the video instruction.	![Help](https://raw.githubusercontent.com/rubenkharel/README-VSCODE-Automation/master/notepad%2B%2B_HutsWWtMjl.png)
  
  And... I guess you are good to go. <br />
  Now modify index.js's readme as per your prefrence. 
  
    
  
  ## Work Flow ⚒💦💦💦💦
  
    
  
  [![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggTFJcbkFbVlMgQ29kZSBFeHRlbnNpb25dIC0tPiBCe2FwcGVuZH0gXG5CIC0tPiBDW0dvb2dsZSBTaGVldF1cbkRbR2l0aHViIEFjdGlvbl0gLS0-IEV7UmVxdWVzdH1cbkUgLS0-IENcbkMgLS0gYWZ0ZXIgcmVxdWVzdCAtLT4gRntSZXNwb25zZX1cbkYgLS0-IERcbkQgLS0-IEd7VXBkYXRlIFJlYWRtZX1cbiIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0IiwidGhlbWVWYXJpYWJsZXMiOnsiYmFja2dyb3VuZCI6IndoaXRlIiwicHJpbWFyeUNvbG9yIjoiI0VDRUNGRiIsInNlY29uZGFyeUNvbG9yIjoiI2ZmZmZkZSIsInRlcnRpYXJ5Q29sb3IiOiJoc2woODAsIDEwMCUsIDk2LjI3NDUwOTgwMzklKSIsInByaW1hcnlCb3JkZXJDb2xvciI6ImhzbCgyNDAsIDYwJSwgODYuMjc0NTA5ODAzOSUpIiwic2Vjb25kYXJ5Qm9yZGVyQ29sb3IiOiJoc2woNjAsIDYwJSwgODMuNTI5NDExNzY0NyUpIiwidGVydGlhcnlCb3JkZXJDb2xvciI6ImhzbCg4MCwgNjAlLCA4Ni4yNzQ1MDk4MDM5JSkiLCJwcmltYXJ5VGV4dENvbG9yIjoiIzEzMTMwMCIsInNlY29uZGFyeVRleHRDb2xvciI6IiMwMDAwMjEiLCJ0ZXJ0aWFyeVRleHRDb2xvciI6InJnYig5LjUwMDAwMDAwMDEsIDkuNTAwMDAwMDAwMSwgOS41MDAwMDAwMDAxKSIsImxpbmVDb2xvciI6IiMzMzMzMzMiLCJ0ZXh0Q29sb3IiOiIjMzMzIiwibWFpbkJrZyI6IiNFQ0VDRkYiLCJzZWNvbmRCa2ciOiIjZmZmZmRlIiwiYm9yZGVyMSI6IiM5MzcwREIiLCJib3JkZXIyIjoiI2FhYWEzMyIsImFycm93aGVhZENvbG9yIjoiIzMzMzMzMyIsImZvbnRGYW1pbHkiOiJcInRyZWJ1Y2hldCBtc1wiLCB2ZXJkYW5hLCBhcmlhbCIsImZvbnRTaXplIjoiMTZweCIsImxhYmVsQmFja2dyb3VuZCI6IiNlOGU4ZTgiLCJub2RlQmtnIjoiI0VDRUNGRiIsIm5vZGVCb3JkZXIiOiIjOTM3MERCIiwiY2x1c3RlckJrZyI6IiNmZmZmZGUiLCJjbHVzdGVyQm9yZGVyIjoiI2FhYWEzMyIsImRlZmF1bHRMaW5rQ29sb3IiOiIjMzMzMzMzIiwidGl0bGVDb2xvciI6IiMzMzMiLCJlZGdlTGFiZWxCYWNrZ3JvdW5kIjoiI2U4ZThlOCIsImFjdG9yQm9yZGVyIjoiaHNsKDI1OS42MjYxNjgyMjQzLCA1OS43NzY1MzYzMTI4JSwgODcuOTAxOTYwNzg0MyUpIiwiYWN0b3JCa2ciOiIjRUNFQ0ZGIiwiYWN0b3JUZXh0Q29sb3IiOiJibGFjayIsImFjdG9yTGluZUNvbG9yIjoiZ3JleSIsInNpZ25hbENvbG9yIjoiIzMzMyIsInNpZ25hbFRleHRDb2xvciI6IiMzMzMiLCJsYWJlbEJveEJrZ0NvbG9yIjoiI0VDRUNGRiIsImxhYmVsQm94Qm9yZGVyQ29sb3IiOiJoc2woMjU5LjYyNjE2ODIyNDMsIDU5Ljc3NjUzNjMxMjglLCA4Ny45MDE5NjA3ODQzJSkiLCJsYWJlbFRleHRDb2xvciI6ImJsYWNrIiwibG9vcFRleHRDb2xvciI6ImJsYWNrIiwibm90ZUJvcmRlckNvbG9yIjoiI2FhYWEzMyIsIm5vdGVCa2dDb2xvciI6IiNmZmY1YWQiLCJub3RlVGV4dENvbG9yIjoiYmxhY2siLCJhY3RpdmF0aW9uQm9yZGVyQ29sb3IiOiIjNjY2IiwiYWN0aXZhdGlvbkJrZ0NvbG9yIjoiI2Y0ZjRmNCIsInNlcXVlbmNlTnVtYmVyQ29sb3IiOiJ3aGl0ZSIsInNlY3Rpb25Ca2dDb2xvciI6InJnYmEoMTAyLCAxMDIsIDI1NSwgMC40OSkiLCJhbHRTZWN0aW9uQmtnQ29sb3IiOiJ3aGl0ZSIsInNlY3Rpb25Ca2dDb2xvcjIiOiIjZmZmNDAwIiwidGFza0JvcmRlckNvbG9yIjoiIzUzNGZiYyIsInRhc2tCa2dDb2xvciI6IiM4YTkwZGQiLCJ0YXNrVGV4dExpZ2h0Q29sb3IiOiJ3aGl0ZSIsInRhc2tUZXh0Q29sb3IiOiJ3aGl0ZSIsInRhc2tUZXh0RGFya0NvbG9yIjoiYmxhY2siLCJ0YXNrVGV4dE91dHNpZGVDb2xvciI6ImJsYWNrIiwidGFza1RleHRDbGlja2FibGVDb2xvciI6IiMwMDMxNjMiLCJhY3RpdmVUYXNrQm9yZGVyQ29sb3IiOiIjNTM0ZmJjIiwiYWN0aXZlVGFza0JrZ0NvbG9yIjoiI2JmYzdmZiIsImdyaWRDb2xvciI6ImxpZ2h0Z3JleSIsImRvbmVUYXNrQmtnQ29sb3IiOiJsaWdodGdyZXkiLCJkb25lVGFza0JvcmRlckNvbG9yIjoiZ3JleSIsImNyaXRCb3JkZXJDb2xvciI6IiNmZjg4ODgiLCJjcml0QmtnQ29sb3IiOiJyZWQiLCJ0b2RheUxpbmVDb2xvciI6InJlZCIsImxhYmVsQ29sb3IiOiJibGFjayIsImVycm9yQmtnQ29sb3IiOiIjNTUyMjIyIiwiZXJyb3JUZXh0Q29sb3IiOiIjNTUyMjIyIiwiY2xhc3NUZXh0IjoiIzEzMTMwMCIsImZpbGxUeXBlMCI6IiNFQ0VDRkYiLCJmaWxsVHlwZTEiOiIjZmZmZmRlIiwiZmlsbFR5cGUyIjoiaHNsKDMwNCwgMTAwJSwgOTYuMjc0NTA5ODAzOSUpIiwiZmlsbFR5cGUzIjoiaHNsKDEyNCwgMTAwJSwgOTMuNTI5NDExNzY0NyUpIiwiZmlsbFR5cGU0IjoiaHNsKDE3NiwgMTAwJSwgOTYuMjc0NTA5ODAzOSUpIiwiZmlsbFR5cGU1IjoiaHNsKC00LCAxMDAlLCA5My41Mjk0MTE3NjQ3JSkiLCJmaWxsVHlwZTYiOiJoc2woOCwgMTAwJSwgOTYuMjc0NTA5ODAzOSUpIiwiZmlsbFR5cGU3IjoiaHNsKDE4OCwgMTAwJSwgOTMuNTI5NDExNzY0NyUpIn19LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggTFJcbkFbVlMgQ29kZSBFeHRlbnNpb25dIC0tPiBCe2FwcGVuZH0gXG5CIC0tPiBDW0dvb2dsZSBTaGVldF1cbkRbR2l0aHViIEFjdGlvbl0gLS0-IEV7UmVxdWVzdH1cbkUgLS0-IENcbkMgLS0gYWZ0ZXIgcmVxdWVzdCAtLT4gRntSZXNwb25zZX1cbkYgLS0-IERcbkQgLS0-IEd7VXBkYXRlIFJlYWRtZX1cbiIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0IiwidGhlbWVWYXJpYWJsZXMiOnsiYmFja2dyb3VuZCI6IndoaXRlIiwicHJpbWFyeUNvbG9yIjoiI0VDRUNGRiIsInNlY29uZGFyeUNvbG9yIjoiI2ZmZmZkZSIsInRlcnRpYXJ5Q29sb3IiOiJoc2woODAsIDEwMCUsIDk2LjI3NDUwOTgwMzklKSIsInByaW1hcnlCb3JkZXJDb2xvciI6ImhzbCgyNDAsIDYwJSwgODYuMjc0NTA5ODAzOSUpIiwic2Vjb25kYXJ5Qm9yZGVyQ29sb3IiOiJoc2woNjAsIDYwJSwgODMuNTI5NDExNzY0NyUpIiwidGVydGlhcnlCb3JkZXJDb2xvciI6ImhzbCg4MCwgNjAlLCA4Ni4yNzQ1MDk4MDM5JSkiLCJwcmltYXJ5VGV4dENvbG9yIjoiIzEzMTMwMCIsInNlY29uZGFyeVRleHRDb2xvciI6IiMwMDAwMjEiLCJ0ZXJ0aWFyeVRleHRDb2xvciI6InJnYig5LjUwMDAwMDAwMDEsIDkuNTAwMDAwMDAwMSwgOS41MDAwMDAwMDAxKSIsImxpbmVDb2xvciI6IiMzMzMzMzMiLCJ0ZXh0Q29sb3IiOiIjMzMzIiwibWFpbkJrZyI6IiNFQ0VDRkYiLCJzZWNvbmRCa2ciOiIjZmZmZmRlIiwiYm9yZGVyMSI6IiM5MzcwREIiLCJib3JkZXIyIjoiI2FhYWEzMyIsImFycm93aGVhZENvbG9yIjoiIzMzMzMzMyIsImZvbnRGYW1pbHkiOiJcInRyZWJ1Y2hldCBtc1wiLCB2ZXJkYW5hLCBhcmlhbCIsImZvbnRTaXplIjoiMTZweCIsImxhYmVsQmFja2dyb3VuZCI6IiNlOGU4ZTgiLCJub2RlQmtnIjoiI0VDRUNGRiIsIm5vZGVCb3JkZXIiOiIjOTM3MERCIiwiY2x1c3RlckJrZyI6IiNmZmZmZGUiLCJjbHVzdGVyQm9yZGVyIjoiI2FhYWEzMyIsImRlZmF1bHRMaW5rQ29sb3IiOiIjMzMzMzMzIiwidGl0bGVDb2xvciI6IiMzMzMiLCJlZGdlTGFiZWxCYWNrZ3JvdW5kIjoiI2U4ZThlOCIsImFjdG9yQm9yZGVyIjoiaHNsKDI1OS42MjYxNjgyMjQzLCA1OS43NzY1MzYzMTI4JSwgODcuOTAxOTYwNzg0MyUpIiwiYWN0b3JCa2ciOiIjRUNFQ0ZGIiwiYWN0b3JUZXh0Q29sb3IiOiJibGFjayIsImFjdG9yTGluZUNvbG9yIjoiZ3JleSIsInNpZ25hbENvbG9yIjoiIzMzMyIsInNpZ25hbFRleHRDb2xvciI6IiMzMzMiLCJsYWJlbEJveEJrZ0NvbG9yIjoiI0VDRUNGRiIsImxhYmVsQm94Qm9yZGVyQ29sb3IiOiJoc2woMjU5LjYyNjE2ODIyNDMsIDU5Ljc3NjUzNjMxMjglLCA4Ny45MDE5NjA3ODQzJSkiLCJsYWJlbFRleHRDb2xvciI6ImJsYWNrIiwibG9vcFRleHRDb2xvciI6ImJsYWNrIiwibm90ZUJvcmRlckNvbG9yIjoiI2FhYWEzMyIsIm5vdGVCa2dDb2xvciI6IiNmZmY1YWQiLCJub3RlVGV4dENvbG9yIjoiYmxhY2siLCJhY3RpdmF0aW9uQm9yZGVyQ29sb3IiOiIjNjY2IiwiYWN0aXZhdGlvbkJrZ0NvbG9yIjoiI2Y0ZjRmNCIsInNlcXVlbmNlTnVtYmVyQ29sb3IiOiJ3aGl0ZSIsInNlY3Rpb25Ca2dDb2xvciI6InJnYmEoMTAyLCAxMDIsIDI1NSwgMC40OSkiLCJhbHRTZWN0aW9uQmtnQ29sb3IiOiJ3aGl0ZSIsInNlY3Rpb25Ca2dDb2xvcjIiOiIjZmZmNDAwIiwidGFza0JvcmRlckNvbG9yIjoiIzUzNGZiYyIsInRhc2tCa2dDb2xvciI6IiM4YTkwZGQiLCJ0YXNrVGV4dExpZ2h0Q29sb3IiOiJ3aGl0ZSIsInRhc2tUZXh0Q29sb3IiOiJ3aGl0ZSIsInRhc2tUZXh0RGFya0NvbG9yIjoiYmxhY2siLCJ0YXNrVGV4dE91dHNpZGVDb2xvciI6ImJsYWNrIiwidGFza1RleHRDbGlja2FibGVDb2xvciI6IiMwMDMxNjMiLCJhY3RpdmVUYXNrQm9yZGVyQ29sb3IiOiIjNTM0ZmJjIiwiYWN0aXZlVGFza0JrZ0NvbG9yIjoiI2JmYzdmZiIsImdyaWRDb2xvciI6ImxpZ2h0Z3JleSIsImRvbmVUYXNrQmtnQ29sb3IiOiJsaWdodGdyZXkiLCJkb25lVGFza0JvcmRlckNvbG9yIjoiZ3JleSIsImNyaXRCb3JkZXJDb2xvciI6IiNmZjg4ODgiLCJjcml0QmtnQ29sb3IiOiJyZWQiLCJ0b2RheUxpbmVDb2xvciI6InJlZCIsImxhYmVsQ29sb3IiOiJibGFjayIsImVycm9yQmtnQ29sb3IiOiIjNTUyMjIyIiwiZXJyb3JUZXh0Q29sb3IiOiIjNTUyMjIyIiwiY2xhc3NUZXh0IjoiIzEzMTMwMCIsImZpbGxUeXBlMCI6IiNFQ0VDRkYiLCJmaWxsVHlwZTEiOiIjZmZmZmRlIiwiZmlsbFR5cGUyIjoiaHNsKDMwNCwgMTAwJSwgOTYuMjc0NTA5ODAzOSUpIiwiZmlsbFR5cGUzIjoiaHNsKDEyNCwgMTAwJSwgOTMuNTI5NDExNzY0NyUpIiwiZmlsbFR5cGU0IjoiaHNsKDE3NiwgMTAwJSwgOTYuMjc0NTA5ODAzOSUpIiwiZmlsbFR5cGU1IjoiaHNsKC00LCAxMDAlLCA5My41Mjk0MTE3NjQ3JSkiLCJmaWxsVHlwZTYiOiJoc2woOCwgMTAwJSwgOTYuMjc0NTA5ODAzOSUpIiwiZmlsbFR5cGU3IjoiaHNsKDE4OCwgMTAwJSwgOTMuNTI5NDExNzY0NyUpIn19LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)
  
    
  
  *Readme Updated on: ${ctime}, UTC 0*
  `, 'utf8', function (err) {
    if (err) throw err;
    console.log('Saved!')
  })
});


