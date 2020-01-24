// Traitement du formulaire charactère supérieur à 2: Nom - Prénom - Pseudo
// ne pas oublier de reinitialiser name
npp = (function () {
    var name = [];
    //selection des input necessitant un char supérieur à 2
    var twoChar = document.querySelectorAll('.twochar');
    for(let i = 0; i < twoChar.length; i++){
        twoChar[i].addEventListener('keyup', function(e){
            // initialisation de la touche frapper par l'utilisateur
            myKeyCode = e.keyCode;
            if(myKeyCode !== 'undefined'){
                // si backspace on supprime le dernier index de name
                if(myKeyCode === 8){
                    name.pop();
                }else{
                    name.push(myKeyCode);
                }
            }
            // on change le css si name est inférieur ou superieur à 2 + ajout du span
            if(name.length < 2){
                span2 = document.querySelector('input:focus + span');
                span2.innerHTML = 'Attention requiert au moins deux charactères';
                span2.style.display = 'inline-block';
                twoChar[i].style.border = '2px red solid';
            }else{
                twoChar[i].style.border = '2px green solid';
                span2.style.display = 'none';
            }
        })
    }
    for(let i = 0; i < twoChar.length; i++){
        twoChar[i].addEventListener('blur', function(){
            name = [];
        })
        twoChar[i].addEventListener('focus', function(e){
            var temp = twoChar[i].value;
            var test2 = [];
            for(let i = 0; i < temp.length; i++){
                test = temp.charCodeAt(i);
                test2.push(test)
                name = test2;
            }
        })
    }
})
//==================================================================================
// Traitement du formulaire Âge:
age = (function(){
    var myKeyCode = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 8]
    var myAge = document.getElementById('age');
    var ageArray = [];
    myAge.addEventListener('keyup', function(e){
        span2 = document.querySelector('input:focus + span');
        let temp = e.keyCode;
        let temp2 = myKeyCode.indexOf(temp);
 
        if(temp2 !== -1){
            ageArray.push(temp);
            span2.style.display = 'none';
            if(temp === 8){
                ageArray.pop();
                ageArray.pop();
            }
            if(ageArray.length <= 3){
                for(let i = 0; i < ageArray.length; i++){
                    if(myKeyCode.indexOf(ageArray[i]) !== -1){
                        myAge.style.border = '2px green solid';
                    }else{
                        myAge.style.border = '2px red solid';
                        span2.style.display = 'none';
                    }
                }
            }
            if(ageArray.length > 3){
                span2.style.display = 'inline-block';
                myAge.style.border = '2px red solid';
                span2.innerHTML = 'Pas plus de trois chiffre !';
            }

        }else{
            span2.style.display = 'inline-block';
            myAge.style.border = '2px red solid';
            span2.innerHTML = 'Seulement les chiffres sont acceptés svp';
        }
    myAge.addEventListener('blur', function () {
        if(ageArray.length <= 3){
            for(let i = 0; i < ageArray.length; i++){
                if(myKeyCode.indexOf(ageArray[i]) !== -1){
                    myAge.style.border = '2px green solid';
                }else{
                    span2.style.display = 'none';
                }
            }
        }


    })
    })
})
//==================================================================================
// initialisation du check
check = (function(){
    myCheck = document.getElementById('newsletter');
    span2 = document.getElementById('checkSpan')
        myCheck.addEventListener('click', function(e){
        if(span2.style.display === 'none' || span2.style.display === ''){
            span2.style.display = 'inline-block'
            span2.innerHTML = 'Inscription Newsletter activée';
        }
        else if(span2.style.display === 'inline-block'){
            span2.style.display = 'none';
        }
    })
})
//==================================================================================
// initalisation des cookies pour la langue
lang = (function(){
    var myLang = document.getElementById('selPays');
    var span2 = document.querySelector('select + span');
    var langArray = ['espagne', 'allemagne', 'france', 'angleterre']
    var langArray2 = ['Espagnole', 'Allemande', 'Francaise', 'Anglaise']
    myLang.addEventListener('change', function(e){
        langVal = e.target.value
        indice = langArray.indexOf(langVal);
        if(langVal){
            span2.innerHTML = "Vous avez choisit la langue " + langArray2[indice];
        }else{
            span2.innerHTML = "Selectionner votre langue ";
        }
    })
})
//==================================================================================
mySubmit = (function(){
    var mySubmit = document.getElementById('mySubmit');
    var twoChar = document.querySelectorAll('.twochar');
    var password = document.getElementById('pass');
    var password2 = document.getElementById('pass2');
    mySubmit.addEventListener('click', function(e){
        for(let i = 0; i < twoChar.length; i++){
            twoChar[i].setAttribute('minlength', '2')
        }
        if(password.value !== password2.value){
        }
    })
})
//==================================================================================
//Fonction isole en action
npp();
age();
check();
lang();
mySubmit();



