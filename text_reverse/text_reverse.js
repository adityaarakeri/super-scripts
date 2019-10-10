$(function() {
    $('#reverse').click(function(){
        var text = $('#reverseText').val();
        var reversed = text.split("").reverse().join("");
        $('#result').text(reversed);
    });
});