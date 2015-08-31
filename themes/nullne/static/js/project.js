$(document).ready(function(){
href = window.location.pathname
if (href.toLowerCase().indexOf("suo-sui") <=0 ){
    $("#protect").remove()
}
function move(){
    console.log("sorry")
    var p = "dare for more".valueOf()
    if($("#password").val().valueOf() == p){
        $("#protect").remove()
        clearInterval(id)
    }
}
var id = setInterval(move, 100)
})
