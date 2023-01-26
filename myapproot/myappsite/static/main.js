let select = document.getElementById("select");
let list = document.getElementById("list");
let selecttext = document.getElementById("selecttext");
let options = document.getElementsByClassName("options");
let form = document.getElementById("form");
let button = document.getElementById('button');
let submit = document.getElementById('submit');
let popup = document.getElementById('popup');
let ok = document.getElementById('ok');
let pointer = document.getElementById("pointer")

select.onclick = function() {
    list.classList.toggle("open");
    pointer.style.transform = 'scaleY(-1)';
}

pointer.onclick = function() {
    form.style.display= 'none';
}


for(option of options){
    option.onclick = function() {
        selecttext.innerHTML = this.innerHTML;
        form.style.display = 'block';
    }
} 
// form.onsubmit= function(e) {
//     e.preventDefault();
//     container.classList.add('show');
// };
    
ok.onclick= function() {
    container.classList.remove('show');
};
