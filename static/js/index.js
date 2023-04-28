// https://responsivevoice.org/api/
function to_speakText(){
    var text = document.getElementById('to_text').value;
    responsiveVoice.speak(text);
    
}
function from_speakText(){
    var text = document.getElementById('from_text').value;
    responsiveVoice.speak(text);
    
}