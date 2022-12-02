eel.expose(update_controller_temp);
function update_controller_temp(x){
    console.log(x)
    document.getElementById("Controller_Temp").innerHTML = String(x).concat("&#176C");
}

eel.expose(update_charge);
function update_charge(x){
    console.log(x)
    document.getElementById("chargeValue").innerHTML = String(x).concat("%");
}

eel.expose(update_value);
function update_value(param, val){
    document.getElementById(param).innerHTML = val;
}