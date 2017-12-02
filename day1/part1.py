with open ('input', 'r') as f:
  captcha = f.readlines()
  captcha = captcha[0].strip()

captcha += captcha[0]
total = 0
for n in range((len(captcha)) - 1):
  if captcha[n] == captcha[n+1]: total += int(captcha[n])

print(total)
