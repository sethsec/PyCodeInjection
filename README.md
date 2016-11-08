# PyCodeInjection

The PyCodeInjection project contains two main components:

1. **PyCodeInjectionShell** - A tool to exploit web application based Python Code Injection
2. **PyCodeInjectionApp**  - A web application that is intentially vulnerable to Python Code Injection 

For a more in depth background on what Python Code Injection you can read [this post](http://sethsec.blogspot.com/2016/11/exploiting-python-code-injection-in-web.html)

# Installation
``` 
git clone https://github.com/sethsec/PyCodeInjection.git /opt/PythonCodeInjection
```

###Extra Step for PyCodeInjectionApp Installation

```
cd /opt/PythonCodeInjection/VulnApp
./install_requirements.sh
```

# Usage

###PyCodeInjectionShell
```
root@playground:/opt/PyCodeInjection# python PyCodeInjectionShell.py -h
Usage: python PyCodeInjectionShell.py -c command -p param -u URL
       python PyCodeInjectionShell.py -c command -p param -r request.file


Options:
  -h, --help    show this help message and exit
  -c CMD        Enter the OS command you want to run at the command line
  -i            Interactivly enter OS commands until finished
  -u URL        Specify the URL. URLs can use * or -p to set injection point
  -p PARAMETER  Specify injection parameter. This is used instead of *
  -r REQUEST    Specify locally saved request file instead of a URL. Works
                with * or -p
```

###PyCodeInjectionApp
```
root@playground:/opt/PyCodeInjection/VulnApp# python PyCodeInjectionApp.py
http://0.0.0.0:8080/
192.168.81.1:12637 - - [02/Nov/2016 22:02:28] "HTTP/1.1 POST /pyinject" - 200 OK
192.168.81.1:12639 - - [02/Nov/2016 22:02:37] "HTTP/1.1 POST /pyinject" - 200 OK
192.168.81.1:12640 - - [02/Nov/2016 22:02:38] "HTTP/1.1 POST /pyinject" - 200 OK
192.168.81.1:12641 - - [02/Nov/2016 22:02:39] "HTTP/1.1 POST /pyinject" - 200 OK
192.168.81.1:12642 - - [02/Nov/2016 22:02:39] "HTTP/1.1 POST /pyinject" - 200 OK
```
