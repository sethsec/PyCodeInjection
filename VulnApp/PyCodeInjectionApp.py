#!/usr/bin/env python

"""
 Authors: Seth Art (sethsec@gmail.com, @sethsec), Charlie Worrell (@decidedlygray, https://keybase.io/decidedlygray)
 Purpose: Web application intentinally vulnerable to Python Code Injection  
          
"""

import web
import urllib
import sys, StringIO


urls = (
  '/', 'index',
  '/pyinject', 'pyinject'
)
render = web.template.render('templates/')
app = web.application(urls, globals())

class index:
    def GET(self):
        return "Hello World. Go to /pyinject for the fun"
    def POST(self):
        return "Hello World. Go to /pyinject for the fun"

class pyinject:
    def POST(self):        
        eval_output = ''
        #redir sys.stdout, from https://joecodeswell.wordpress.com/2012/07/28/378/
        stdout = sys.stdout
        sys.stdout = reportSIO = StringIO.StringIO()
        try:
            get_input = web.input()
            param1 = get_input['param1'] if 'param1' in get_input else None
            param2 = get_input['param2'] if 'param2' in get_input else None            
            cookie1 = web.cookies().get('c1') if 'c1' in web.cookies() else None
            if not cookie1: 
                web.setcookie('c1','exploit_me', expires="", domain=None, secure=False)             
            if (param1):
                try:
                    x = eval(param1)
                    if (x):
                        eval_output = str(eval_output) + x                    
                except:
                    pass
            if (param2):
                try:
                    y = eval(param2)
                    if (y):
                        eval_output = str(eval_output) + y                    
                except:
                    pass
            if (cookie1):
                try:
                    z = eval(str(cookie1))
                    if (z):
                        eval_output = str(eval_output) + z 
                except:
                    pass
                                   
            reportStr = reportSIO.getvalue()
            #restore sys.stdout so we can print
            sys.stdout = stdout
            
            output = str(reportStr) + str(eval_output)
            #return output
            return render.index(output)
        except Exception as error: 
            print(error)
            return error

    def GET(self):
        
        eval_output = ''
        #redir sys.stdout, from https://joecodeswell.wordpress.com/2012/07/28/378/
        stdout = sys.stdout
        sys.stdout = reportSIO = StringIO.StringIO()
        try:
            get_input = web.input()
            param1 = get_input['param1'] if 'param1' in get_input else None
            param2 = get_input['param2'] if 'param2' in get_input else None            
            cookie1 = web.cookies().get('c1') if 'c1' in web.cookies() else None
            if not cookie1: 
                web.setcookie('c1','exploit_me', expires="", domain=None, secure=False)     

            if (param1):
                try:
                    x = eval(param1)
                    if (x):
                        eval_output = str(eval_output) + x                    
                except:
                    pass
            if (param2):
                try:
                    y = eval(param2)
                    if (y):
                        eval_output = str(eval_output) + y                    
                except:
                    pass
            if (cookie1):
                try:
                    z = eval(str(cookie1))
                    if (z):
                        eval_output = str(eval_output) + z 
                except:
                    pass
            
            reportStr = reportSIO.getvalue()
            #restore sys.stdout so we can print
            sys.stdout = stdout
            output = str(reportStr) + str(eval_output)
            #return output
            return render.index(output)
        except Exception as error: 
            print(error)
            return error

    
if __name__ == "__main__":
    
    
    app.run()
