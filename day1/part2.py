with open ('input', 'r') as f:
  captcha = f.readlines()
  captcha = captcha[0].strip()

half_captcha = int(len(captcha) / 2)
captcha += captcha[0:half_captcha]
total = 0

for n in range(len(captcha)):
  if not n >= (len(captcha) - half_captcha):
    if captcha[n] == captcha[n+half_captcha]: total += int(captcha[n])

print(total)
