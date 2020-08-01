from lang import eden

while True:
    text = input('eden shell >>> ')
    result, error = eden.run(text, '<stdin>')
    if error:
        print(error.as_string())
    else:
        print(result)
