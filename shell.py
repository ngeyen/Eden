import eden

while True:
    text = input('eden > ')
    result, error = eden.run(text)
    if error: 
        print(error.as_string())
    else: 
        print (result)
    