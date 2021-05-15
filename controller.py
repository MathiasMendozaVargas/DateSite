import web

urls = (
    '/', 'home',
    '/register', 'register'
)
render = web.template.render("Views/Templates", base="main")
app = web.application(urls, globals())

################
# CLASSES
################
class home:
    def GET(self):
        return render.home()
class register:
    def GET(self):
        return render.register()

###############
# RUN THE APP
###############
if __name__ == "__main__":
    app.run()