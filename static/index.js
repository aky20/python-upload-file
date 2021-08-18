let img = document.getElementById("profile");
if(img.clientWidth > img.clientHeight){
    img.style.width = "auto"
    img.style.height = "100%"
}else{
    img.style.width = "100%"
    img.style.height = "auto"
}

