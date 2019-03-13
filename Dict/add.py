uniqlines = list(open('../Intern/spiders/vae/sublink.csv').readlines())

bar = open('../Intern/spiders/vae/sublink.csv', 'w').writelines(["https://vae.ahk.de"+s for s in uniqlines])