function single(){
 fetch('/combo/single',{method:'POST',headers:{'Content-Type':'application/json'},
 body:JSON.stringify({match:document.getElementById('match').value})})
 .then(r=>r.text()).then(t=>document.getElementById('result').innerText=t)
}
function multi(){
 const matches=document.getElementById('multi').value.split('\n');
 fetch('/combo/multi',{method:'POST',headers:{'Content-Type':'application/json'},
 body:JSON.stringify({matches:matches})})
 .then(r=>r.text()).then(t=>document.getElementById('result').innerText=t)
}
