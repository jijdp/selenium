


def variable():
    name: str = "Brian"
    salary: int=1000
    isMarried: bool=True
    print("Hello World python ---- " , name)
    print("My Salary is " , salary)

configs = {
    "browser":"opera",
    "aut":"google site",
    "test":"Smoke",
    "log":True
}

def getDictionaryValue(key):
    return configs.get(key)

print(getDictionaryValue("aut"))


# if(name == "Brian"):
#     print("Yes")
# else:
#     print("No")

# if(salary == 1000):
#     print("1000")
# elif (salary < 1000):
#     print("Salary less than 1000")

# if isMarried == True: print("is married")

# browsers = ["chrome", "safari", "firefox","IE","Opera"]

# browsers.append("Unknown")

# for browser in browsers:
#     print(browser)




# #print(browsers[0:3])