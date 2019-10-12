var btns = document.querySelectorAll("button");
var i = 0;
 
setInterval(function(){
    if ( btns[i].textContent == "Invite" ) {
        btns[i].click();
        console.log( i + " buttons clicked." );
    }
    i++;
}, 200);