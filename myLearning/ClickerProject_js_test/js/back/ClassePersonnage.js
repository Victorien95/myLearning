class Personnage {
    constructor(){
        this._hp = 10;
        this.hpMax = 10;
        this.accuracy = 70;
        this.armor = 50;
        this.dmgMin = 50;
        this.dmgMax = 100;
        this.pierceArmor = 1; // pas encore utilisé
        this._stamina = 10; // pas necore utilisé
        this.staminaMax = 20; // pas encore utilisé
        this.xp = 0; //pas encore utilisé !
    };

    get stamina(){
        return this._stamina;
    }

    test(){
        var span1Hp = document.getElementById('hp1');
        var span1TextNodeHp = document.createTextNode('HP : ' + this._hp + '/' + this.hpMax );
        span1Hp.appendChild(span1TextNodeHp);
    }

    set hp(modificator){
        console.log(modificator);
        this._hp += modificator;
        if(this._hp < 0){
            this._hp = 0;
        }else if(this._hp > this.hpMax){
            this._hp = this.hpMax;
        }
        this.test();
    };

    get hp(){
        return this._hp;
    };


    accuracyRoll(){
        let roll = Math.floor(Math.random()*100);
        if(roll <= this.accuracy){
            return true;
        }else{
            return false;
        }
    };


    dmgRoll(){
        let roll = (Math.floor(Math.random()*(this.dmgMax - this.dmgMin + 1)) + this.dmgMin);
        console.log(roll);
        return roll;
    };


    dmgAfterArmorReduc(target){
        let dmgRoll = this.dmgRoll();
        let prctReduc = target.armor * 0.5;
        if(prctReduc > 50){
            prctReduc = 50;
        }
        let dmgAfterArmorReduc = (dmgRoll - target.armor);
        dmgAfterArmorReduc -= Math.round((prctReduc / 100)*dmgAfterArmorReduc);
        console.log(dmgAfterArmorReduc + ' DAMAGE FINAL ')
        if(dmgAfterArmorReduc < 1){
            dmgAfterArmorReduc = 1;
            return -dmgAfterArmorReduc;
        }else{
            return -dmgAfterArmorReduc;
        }
    };


    attack(target){
        if(this.accuracyRoll()){
            console.log('attack reussi');
            target.hp = this.dmgAfterArmorReduc(target);
        }else{
            this.test();
            console.log('attack raté');
        }
    };


    staminaRegen() {
        let temp = this._stamina;
        console.log(temp+"VALEUR DE TEMP")
        console.log(this._stamina+"VALEUR DE STAMINA")
        setInterval(function(){
            temp += 1;
            console.log(temp);
            this._stamina = temp;
            console.log(this._stamina+ "VALEUR DE STAMINA APRES SET INTERVAL")
        }, 1000);
    };


}


//------------------------------------------------------FIN DE CLASSE------------------------------------------------------

alex = new Personnage();
vic = new Personnage();
console.log(vic.hp);
alex.attack(vic);
console.log(vic.hp);
alex.staminaRegen(alex);


//-------------------------------------------------------------------------




//PLAYER
/*span1Sta = document.getElementById('stamina1');
span1Hp = document.getElementById('hp1');
span1TextNodeSta = document.createTextNode('Stamina : ' + alex._stamina + '/' + alex.staminaMax );
span1TextNodeHp = document.createTextNode('HP : ' + alex._hp + '/' + alex.hpMax );

span1Sta.appendChild(span1TextNodeSta);
span1Hp.appendChild(span1TextNodeHp);

//VILAIN
span2Sta = document.getElementById('stamina2');
span2Hp = document.getElementById('hp2');
span2TextNodeSta = document.createTextNode('Stamina : ' + vic._stamina + '/' + vic.staminaMax );
span2TextNodeHp = document.createTextNode('HP : ' + vic._hp + '/' + vic.hpMax );

span2Sta.appendChild(span2TextNodeSta);
span2Hp.appendChild(span2TextNodeHp);*/



