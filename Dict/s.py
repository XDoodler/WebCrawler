
# TIME TO STOP OUR CRAWLER. IT TAKES AROUND 30 MINUTES TO PERFORM.
#LETS JUST STOP AND GET OUR LIST :D

uniqlines = set(open('../Intern/spiders/auto/emails.csv').readlines())

bar = open('../Intern/spiders/auto/final.csv', 'w').writelines(sorted(uniqlines))

