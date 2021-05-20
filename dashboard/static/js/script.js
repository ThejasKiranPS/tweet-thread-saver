function over(str) {
    document.getElementById('i'+str).className="no-display";
    document.getElementById('t'+str).className="";

}
function undo(str) {
    document.getElementById('i'+str).className="button-icon";
    document.getElementById('t'+str).className="no-display";
}