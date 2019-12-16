function loginAjax() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var object = new Object();
    object.username = username;
    object.password = password;
    var xhr = new XMLHttpRequest();
    var jsonStr = JSON.stringify(object);
    xhr.open("post", "index.php?r=Login/Login");
    xhr.setRequestHeader("Content-Type","application/json");
    xhr.send(jsonStr);
    console.log(jsonStr);
};
function checkResiger() {
    alert("注册功能尚未开放！");
}
