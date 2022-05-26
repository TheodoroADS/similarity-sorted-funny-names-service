
function insertSuggestion(){

    const suggestion = document.getElementById("suggestion");
    if (!suggestion.value) return;

    const status = document.getElementById('suggestionstatus');

    fetch('/insert', {
        headers : new Headers({"Content-Type": "application/json"}),
        method: 'POST',
        body: JSON.stringify({"suggestion" : suggestion.value})
    }).then((_res) =>{
        if (_res.status == 204){
            
            status.innerText = " ✅";
        }else{
            console.log(_res.statusText);
            status.innerText = " ❌";
        }
    }).catch(() =>{
        status.innerText = "Il y a un problème, et c'est probablement ta faute";
    })

}
 

function getName(){

    const name = document.getElementById("name");
    if (!name.value) return;

    const status = document.getElementById('nameStatus');

    fetch('/get', {
        headers : new Headers({"Content-Type": "application/json"}),
        method: 'POST',
    body: JSON.stringify({"name" : name.value})
    }).then((_res) =>{
        _res.text().then((Resp_name) => status.innerText = ' '+Resp_name) 
    }).catch(() =>{
        status.innerText = "Il y a un problème, et c'est probablement ta faute";
    })


}