
name: str = "Brian"
salary: int=1000
isMarried: bool=True

print("Hello World python ---- " , type(name))

print("My Salary is " , type(salary))

if(name == "Brian"):
    print("Yes")
else:
    print("No")

if(salary == 1000):
    print("1000")
elif (salary < 1000):
    print("Salary less than 1000")

if isMarried == True: print("is married")

browsers = ["chrome", "safari", "firefox","IE","Opera"]

browsers.append("Unknown")

for browser in browsers:
    print(browser)

configs = {
    "browser":"opera",
    "ait":"google site",
    "test":"Smoke",
    "log":True
}

print(configs.get("test"))

for conf in configs.values():
    print(conf)

if "browser" in configs:
    print("Exist")
#print(browsers[0:3])