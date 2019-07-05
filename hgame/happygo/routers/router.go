package routers

import (
	"catmsg/controllers"
	"github.com/astaxie/beego"
	"github.com/astaxie/beego/context"
	"os"
	"strings"
)

func init() {

	var FilterUser = func(ctx *context.Context) {
		_, ok := ctx.Input.Session("uid").(int)
		if !ok && !strings.Contains(ctx.Request.RequestURI,"auth") && !strings.Contains(ctx.Request.RequestURI,"install") {
			ctx.Redirect(302, "/auth")
		}
	}

	var FilterConf = func(ctx *context.Context) {
		_, err := os.Stat("conf/app.conf")
		if err != nil && os.IsNotExist(err) {
			if ctx.Request.RequestURI != "/install" {
				ctx.Redirect(302, "/install")
			}
		}
	}

	beego.InsertFilter("/*",beego.BeforeRouter,FilterUser)
	beego.InsertFilter("/*",beego.BeforeRouter,FilterConf)

    beego.Router("/", &controllers.MainController{})
	beego.Router("/auth", &controllers.LRController{})
	beego.Router("/auth/register", &controllers.RegisterController{})
    beego.Router("/auth/login", &controllers.LoginController{})
	beego.Router("/auth/logout", &controllers.LogoutController{})
	beego.Router("/admin", &controllers.AdminController{})
	beego.Router("/admin/user/del/:id([0-9]+", &controllers.UserDelController{})
    beego.Router("/userinfo", &controllers.UserInfoController{})
	beego.Router("/install", &controllers.InstallController{})
}
