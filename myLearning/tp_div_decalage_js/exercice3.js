divSelect = document.querySelectorAll('.col');
containerSelect = document.querySelector('#container');
bodySelect = document.querySelector('#body');
containerSelect.style.display = 'flex';
br = document.createElement('br');

divcrea = document.createElement('div');


for(let i = 0; i < divSelect.length; i++){
    divSelect[i].textContent = 'DIV ' + (i+1);
}

//--------------------------------------
var myArray = [];

function couleurs() {
    let i = true;
    while(i){
        ask = prompt('Choisissez des couleurs en anglais... \nTapez stop pour arrêter').toLowerCase();
        if(ask === 'stop'){
            i = false;
        }
        else if(parseInt(ask)){
            ask = prompt('Attention chiffre non acceptés');
        }
        else{
            myArray.push(ask);
        }
    }

}
couleurs();
bodySelect.appendChild(br);
newcontainer = document.createElement('div');
newcontainer.classList.add('newcontainer');
bodySelect.appendChild(newcontainer);
newcontainerSelect = document.querySelector('.newcontainer');
newcontainerSelect.style.display = 'auto';

for(let i in myArray){
    let divcrea = document.createElement('div');
    divcrea.classList.add('coll');
    text = document.createTextNode('DIVBIS ' + i);
    divcrea.appendChild(text);
    newcontainerSelect.appendChild(divcrea);
}

function decalage() {
    let tempselect = document.querySelectorAll('.coll');
    if (myArray.length == 0) {
        document.write('Vous n\'avez saisi aucune couleurs');
    }
    else if (myArray.length % 3 == 0) {
        for(let i = 0; i < tempselect.length ; i++) {
            console.log(tempselect);
            tempselect[i].className = 'col-4';
            tempselect[i].style.backgroundColor = myArray[i];
        }
    } else if (myArray.length % 3 == 2) {
        for (let i = 0; i < tempselect.length; i++) {
            tempselect[i].className = 'col-4';
            tempselect[i].style.backgroundColor = myArray[i];
        tempselect[i].className = 'col-6';
        tempselect[i].style.backgroundColor = myArray[i];
        let k = myArray.length - 1;
        tempselect[k].className = 'col-6';
        tempselect[k].style.backgroundColor = myArray[k];
        }

    } else if (myArray.length % 3 == 1) {
        for (let i = 0; i < tempselect.length; i++) {
            tempselect[i].className = 'col-4';
            tempselect[i].style.backgroundColor = myArray[i];
            var gh = i;
        }
        let k = myArray.length -1;
        tempselect[gh].className = 'col';
        tempselect[gh].style.backgroundColor = myArray[gh];
    }
}

decalage();

