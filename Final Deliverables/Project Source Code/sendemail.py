import smtplib
ser = smtplib.SMTP('smtp.gmail.com',587);
ser.starttls();
ser.login('sthatchu246@gmail.com','uphtexijzypuywog')
ser.sendemail('sthatchu246@gmail.com','1915026@nec.edu.in','You Have one Job Request for English Proficiency!!');
print('mail sent');
    

