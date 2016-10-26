import web
import urllib
import sys, StringIO


urls = (
  '/', 'index',
  '/pyinject', 'pyinject'
)

class index:
    def GET(self):
        return "Hello World"

class pyinject:
    def GET(self):

        #redir sys.stdout
        stdout = sys.stdout
        sys.stdout = reportSIO = StringIO.StringIO()
        try:
            #get_input = web.input(_method='get')
            get_input = web.input()
            #print type(cookie1)
            #print type(get_input)
            #decoded_all = urllib.unquote(get_input)
            try:
                cookie1 = web.cookies().get('c1')
            except:
                cookie1 = None
            try:
                param1 = get_input.param1
            except:
                param1 = None
            try:
                param2 = get_input.param2
            except:
                param2 = None
            
            #seth = eval(param1)
            #print type(param1)
            #print param2
            #print param3
            #print name
            #print decoded_all
            
            
            #decoded_cookie = urllib.unquote(cookie1)
            #print type(decoded1)
            #print type(decoded_cookie)
            #x=1
            #print type(decoded1)
            #print dir(decoded1)
            #x = eval(decoded.decode("utf-8"))
            if (param1):
                #decoded1 = urllib.unquote(param1)
                #x = eval(decoded1)
                x = eval(param1)
            if (param2):
                #decoded2 = urllib.unquote(param2)
                #y = eval(decoded2)
                y = eval(param2)
            if (cookie1):
                z = eval(cookie1)
            #print x, y, z
            #print type(x)
            #exec x
            reportStr = reportSIO.getvalue()
            #restore sys.stdout so we can print
            sys.stdout = stdout
            return reportStr
        except Exception as error: 
            print(error)
            return error

app = web.application(urls, globals())

if __name__ == "__main__":
    
    app.run()
