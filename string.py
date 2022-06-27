print("Hello")
print('Hello')

a = "dhrumil"
print(a)

# multi string #
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)

# string are array #
c = "hello, world!"
print(c[4])

# looping through string #
for x in "banana":
  print(x)

# string lenght #
d = "dhrumil!"
print(len(d))

# txt present #
txt = "The best things in life are free!"
print("free" in txt)

# txt is not presernt #
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

  # slicing #
h = "hellow"
print(h[2:4])

# scling from the start #
g = 'dhrumil'
print(g[:4])

# scling to end #
j = 'DHRUMIL PATEL'
print(j[3:])

# negative indexing #
k = 'djrumil, patel$'
print(k[-3:-1])

# upper case #
a = "Hello, World!"
print(a.upper())

# lower case #
b = "Dhrumil Patel"
print(b.lower())

# remove white space #
c = "  dhrumil  patel$  "
print(c.strip())
# replace string #
d = 'savan axat'
print(d.replace("a","h"))

# split string #
f = 'dhrumil, patel, $'
print(f.split(","))

# String Concatenation #
a = 'dhrumil'
b = 'patel'
c = a+b
d = a + " " + b
print(c)
print(d)

# string formate #
age = 22
txt = "my name dhrumil, i am {}"
print(txt.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders #
quantity = 4
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


