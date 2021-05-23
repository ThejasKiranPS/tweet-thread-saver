//main-right button hover effects
conversationId='';
function over(str) {
    document.getElementById('i'+str).className="no-display";
    document.getElementById('t'+str).className="";

}
function undo(str) {
    document.getElementById('i'+str).className="button-icon";
    document.getElementById('t'+str).className="no-display";
}
UNAME='';
function changeTo(str,id) {
    
    UNAME= document.getElementById(id).innerText;
    document.getElementById(id).innerText=str;
}
function undochangeTo(id) {
    document.getElementById(id).innerText=UNAME;
}
downloadBtn= document.getElementById("b3");
downloadBtn.onclick = sendReq;

//send req to django
function sendReq(){
    let form = document.getElementById("request-form");
    form.convoId.value = conversationId;
    form.submit();
}



//click effects
function tweetClicked() {
    element = this;
    console.log(element);
    this.classList.add(" selected");
}

mElements = document.querySelectorAll(".main-element");
mElements.forEach(
    (e) => e.onclick = () => {
        deselect();
        e.classList.add("selected");
    }
)

function deselect() {
    mElements.forEach(
        e => e.classList.remove("selected")
    )
}
