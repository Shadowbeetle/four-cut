# The problem

A lot of password managers store credit card number as contiguous strings. And there are quite a lot of banks that provide secure online payment, but their forms are not autofillable. These cases you either ctr+c, ctrl+v your credit card number to a text editor, then ctrl+x. ctrl+v your number in chunks of four to these fields, or you can also use `sed -e 's/\(....\)/\1 /g' <<< <your contiguous credit card number>` and then copy them one by one.

`fourcut` provides a bit more simple way of doing that by cutting the provided string to chunks of four then promtping the user and copying the chunks one by one.

# Dependencies

* `python3`
* `pip3`
* everything in `requirements.txt`

```sh
$ pip3 install -r requirements.txt
```

If you get the following error on OSX:

```sh
$ ./install.sh
Could not fetch URL https://pypi.python.org/simple/pyperclip/: There was a problem confirming the ssl certificate
```

it means that you are using an old version of pip and you need to update it:

``` sh
curl https://bootstrap.pypa.io/get-pip.py | python3
```

You can read more on the issue [here](https://mail.python.org/pipermail/python-announce-list/2018-April/011885.html)

# Install

The install script only works on Unix based systems. Pull requests are welcome for windows.

```sh
$ git clone git@github.com:Shadowbeetle/four-cut.git
$ ./install.sh <path-to-dir-in-your-$PATH>
```

# Usage

```sh
usage: fourcut [-h] [--print]

optional arguments:
  -h, --help   show this help message and exit
  -p, --print  print the output and exit
```