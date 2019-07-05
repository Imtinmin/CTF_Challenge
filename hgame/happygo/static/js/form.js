var onoff = true//根据此布尔值判断当前为注册状态还是登录状态
var confirm = document.getElementsByClassName("confirm")[0]
var user = document.getElementById("user")
var passwd = document.getElementById("passwd")
var con_pass = document.getElementById("confirm-passwd")

//自动居中title
var name_c = document.getElementById("title")
name = name_c.innerHTML.split("")
name_c.innerHTML = ""
for (i = 0; i < name.length; i++)
    if (name[i] != ",")
        name_c.innerHTML += "<i>" + name[i] + "</i>"
//引用hint()在最上方弹出提示
function hint() {
    let hit = document.getElementById("hint");
    hit.style.display = "block"
    setTimeout(()=>{hit.style.opacity = 1}, 0)
    setTimeout(()=>{hit.style.opacity = 0}, 2000)
    setTimeout(()=>{hit.style.display = "none"}, 3000)
}
//回调函数
function submit(callback) {
    if (passwd.value == con_pass.value) {
        let request = new XMLHttpRequest()
        let url = "/auth/register"
        request.open("post", url, true)
        let data = new FormData()
        data.append("username", user.value)
        data.append("password", passwd.value)
        data.append("confirmpass", con_pass.value)
        request.onreadystatechange = function() {
            if (this.readyState == 4) {
                callback.call(this, this.response)
            }
        }
        request.send(data)
    } else {
        hit.innerHTML = "两次密码不同"
        hitting()
    }
}
//注册按钮
function signin() {
    let status = document.getElementById("status").getElementsByTagName("i")
    let hit = document.getElementById("hint").getElementsByTagName("p")[0]
    if (onoff) {
        confirm.style.height = 51 + "px"
        status[0].style.top = 35 + "px"
        status[1].style.top = 0
        onoff = !onoff
    } else {
        if (!/^[A-Za-z0-9]+$/.test(user.value))
            hit.innerHTML = "账号只能为英文和数字"
        else if (user.value.length < 6)
            hit.innerHTML = "账号长度必须大于6位"
        else if (passwd.value.length < 6)
            hit.innerHTML = "密码长度必须大于6位"
        else if (passwd.value != con_pass.value)
            hit.innerHTML = "两次密码不相等"
        else if (passwd.value = con_pass.value) {
            submit(function(res) {
                if (res == "exist")
                    hit.innerHTML = "该账号已存在"
                else if (res == "success") {
                    hit.innerHTML = "账号注册成功，两秒后自动刷新页面"
                    setTimeout("window.location.reload()", 2000)
                } else
                    hit.innerHTML = "账号注册失败"
            })
        }
        hint()
    }
}

//登录按钮
function login() {
    if (onoff) {
        let request = new XMLHttpRequest()
        let url = "/auth/login"
        request.open("post", url, true)
        let data = new FormData()
        data.append("username", user.value)
        data.append("password", passwd.value)
        request.onreadystatechange = function() {
            if (this.readyState == 4) {
                if (this.responseText == "success")
                    window.location.href = "/"
                else
                    hint()
            }
        }
        request.send(data)
    } else {
        let status = document.getElementById("status").getElementsByTagName("i")
        confirm.style.height = 0
        status[0].style.top = 0
        status[1].style.top = 35 + "px"
        onoff = !onoff
    }
}