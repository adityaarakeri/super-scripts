function fileSelectionCompleted(input) {
    if(input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            var imageURL = e.target.result;
            document.getElementById("img1").src = imageURL;
        }

        reader.readAsDataURL(input.files[0]);
    }
}
function loadImage(){
    document.getElementById("fileSelect").click();
}


