let selected = document.querySelector('.main-element');
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
//send req to django
function sendReq(convId, formId="request-form"){
    let form = document.getElementById(formId);
    form.convoId.value = convId;
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
        selected=e;
    }
)

function deselect() {
    mElements.forEach(
        e => e.classList.remove("selected")
    )
}

//copy email to clipboard

function copyE(str){
    let email = document.getElementById("email");
    console.log(email);
    email.value=str;
    email.select();
    email.setSelectionRange(0,99999);
    document.execCommand("copy");
    console.log('success');
    alert('email copied');
}

// add tweet by url

function getInput() {
    let url = window.prompt('Enter the full tweet url');
    if (url.includes('status/')==false) {
       alert('Enter the full url');
       return; 
    }
    sendReq(convId);
}

//download

let filename = '';
function download() {
  var element = document.createElement('a');
  element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(processTweet()));
  element.setAttribute('download', filename);

  element.style.display = 'none';
  document.body.appendChild(element);

  element.click();

  document.body.removeChild(element);
}

function processTweet() {
    tName= selected.children[0].children[1].children[0].children[0].innerText;
    tUserName = selected.children[0].children[1].children[0].children[1].innerText;
    tTweet = selected.children[0].children[1].children[1].innerText;
    let processedTweet = tName + '  '+tUserName + '\n' + tTweet;
    filename='tweet_'+tUserName;
    return processedTweet;
}
function deleteT() {
    let convoId=selected.getAttribute('convoId');
    sendReq(convoId,'delete-thread');  
    }
function listen(e) {
    if (e.key===Delete) {
        deleteT();
        }
}
    document.onkeypress=listen;
