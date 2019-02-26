String.prototype.replaceAll = function (exp, newStr) {
    return this.replace(new RegExp(exp, "gm"), newStr);
};

String.prototype.format = function(args) {
    var result = this;
    if (arguments.length < 1) {
        return result;
    }

    var data = arguments; // 如果模板参数是数组
    if (arguments.length == 1 && typeof (args) == "object") {
        // 如果模板参数是对象
        data = args;
    }
    for ( var key in data) {
        var value = data[key];
        if (undefined != value) {
            result = result.replaceAll("\\{" + key + "\\}", value);
        }
    }
    return result;
}

function fn_auto_input(ip_port, db_user, db_passwd){
    login_form.pma_servername.value = ip_port;
    login_form.pma_username.value = db_user;
    login_form.pma_password.value = db_passwd;
    // login_form.submit();
}

function fn_get_url_args(key){
    query = window.location.search.substring(1);
    var vars = query.split("&");
    for (var i=0;i<vars.length;i++) {
        var pair = vars[i].split("=");
        if(pair[0] == key){return pair[1];}
    }
    return(false);
}

function fn_get_cred_detail_by_id(url, id, token){
    var xhr = new XMLHttpRequest(); 
    var resource_uri = "/api/v1/cred/{id}?/format=json".format({"id":id})
    return new Promise(function (resolve, reject) {
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                if (xhr.status === 200) {
                    resolve(xhr.responseText);
                } else {
                    reject(xhr.status);
                }
            }
            //else if(xhr.readyState === 0)
            //{
            //    console.log("UNSENT")
            //}
            //else if(xhr.readyState === 1)
            //{
            //    console.log("OPENED")
            //}
            //else if(xhr.readyState === 2)
            //{
            //    console.log("HEADERS_RECEIVED")
            //}
            //else if(xhr.readyState === 3)
            //{
            //    console.log("DONE")
            //}
        };
        console.log(token)
        xhr.open('GET', url + resource_uri);
        xhr.setRequestHeader('Authorization', 'ApiKey ' + token);
        //xhr.setRequestHeader('Content-Type' , 'application/json' );
        xhr.send();
    });
}

window.onload = function(){
    var url= "http://debug.pwd.xx.szylhd.com/";
    var cred_id = fn_get_url_args("cred_id");
    var token = fn_get_url_args("token");
    var req = fn_get_cred_detail_by_id(url, cred_id, token)

    req.then(function(text){
        //alert( text );
        var ip_port = "47.106.247.172 3306";
        var db_user = "root";   
        var db_passwd = "8e86e1895bc110107a";
        //fn_auto_input(ip_port, db_user, db_passwd);
        fn_auto_input("", "", "");

    }).catch(function(status){
        alert( "failure status : " + status );
    })

}

