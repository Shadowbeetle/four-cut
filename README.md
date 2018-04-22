Easier credit card number input for non-autofillable online forms.

# The problem

A lot of password managers store credit card number as contiguous strings. And there are quite a lot of banks that provide secure online payment, but their forms are not autofillable. These cases you either ctr+c, ctrl+v your credit card number to a text editor, then ctrl+x. ctrl+v your number in chunks of four to these fields, or you can also use `sed -e 's/\(....\)/\1 /g' <<< <your contiguous credit card number>` and then copy them one by one.

four-cut provides a bit more simple way of doing that by cutting the provided string to chunks of four, printing it the smae way `sed` would, than copying the chunks one by one.

# Install

git clone