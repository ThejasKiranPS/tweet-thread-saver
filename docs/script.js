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

//tweet click effects
container=document.getElementById("main-element-container");

container.onclick = clicked


function clicked(event) {
    if (event.target.className === "main-element-container") return;
    deselect();
    event.target.className+=" selected";
    children=Array.from(container.children);

    conversationId=  children.findIndex(c => c==event.target);
    console.log(conversationId);
}

function deselect() {
    children=Array.from(container.children)
    for(let i=0; i<children.length; i++) {
        children[i].classList.remove('selected');
    }
}

downloadBtn= document.getElementById("b3");
downloadBtn.onclick = sendReq;

//send req to django
function sendReq(){
    console.log('test');
    let form = document.getElementById("request-form");
    form.convoId.value = conversationId;
    console.log('te');
    form.submit();
}