import pandas as pd
import smtplib

df = pd.read_html('https://www.worldometers.info/coronavirus/#countries')[0]
df = df.set_index('Country,Other')
df = df.fillna(0)
data = list(df.loc['Brazil']) 
data = list(map(str,data))
print('table ok')
total_cases = data[0]
new_cases = data[1]
total_deaths = data[2]
new_deaths = data[3]
active_cases = data[4]
total_recovered = data[5]
serious_critical = data[6]
print('data ok')
print('começo do email')
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

server.login('email', 'password')
print('login ok')
subject = 'Corongavirus no Brasil'

body = 'Hoje no ' + 'Brasil' + '\
    \nCasos totais: ' + total_cases +'\
    \nNovos casos: ' + new_cases + '\
    \nTotal de mortes: ' + total_deaths + '\
    \nNovas mortes: ' + new_deaths + '\
    \nCasos ativos: ' + active_cases + '\
    \nTotal recuperado: ' + total_recovered + '\
    \nCasos criticos: ' + serious_critical  + '\
    \nFontes: https://www.worldometers.info/coronavirus/' + '\
    \nLave as maos!'
print('body ok')
msg = f"Subject: {subject}\n\n{body}"
print('assunto ok')

to_emails = ['emails list']

server.sendmail(
    'Coronavirus',
    to_emails,
    msg
)
print('e-mail enviado')

server.quit()