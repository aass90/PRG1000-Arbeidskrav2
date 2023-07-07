#PRG1000-Oblig2-AAA
#Oppgave: Studieadministrativt studiesystem

#Starter med å importere "os" for fremtidige funksjoner
import os

#Her er meny-funksjonen for å visualisere valgmulighetene for bruker
def meny():
    print('[1] Registrere student')
    print('[2] Slette student')
    print('[3] Skriv ut karakterliste')
    print('[9] Avslutt programmet')

#Funksjon som legger til studentopplysninger fra bruker til fil
def registrere():

    #Legger inn ei startpånytt-løkke
    start_pa_nytt='j'
    while start_pa_nytt=='j':

        #Bolsk variabel
        funnet=False

        #Input fra bruker hva gjelder student
        sok=input('Angi studentnummer på studenten du vil registrere: ')
        ny_fornavn=input('Fornavn: ')
        ny_etternavn=input('Etternavn: ')
        ny_studium=input('Studium: ')

        #Åpner fil for bruk
        student_fil=open('student.txt','r')

        #Leser første linje i student.txt
        studnr=student_fil.readline()

        #Leser så resten av posten
        while studnr!='':
            fornavn=student_fil.readline()
            etternavn=student_fil.readline()
            studium=student_fil.readline()

            #Stripper
            studnr=studnr.rstrip('\n')
            fornavn=fornavn.rstrip('\n')
            etternavn=etternavn.rstrip('\n')
            studium=studium.rstrip('\n')

            #Sjekker søket mot student
            if studnr==sok:
                #Viser svar
                print()
                print('Studenten finnes fra før, studenten blir ikke registrert')
                
                #Justerer den bolske variabelen
                funnet=True

            #Leser neste post
            studnr=student_fil.readline()
            fornavn=student_fil.readline()
            etternavn=student_fil.readline()
            studium=student_fil.readline()

        #Stenger student.txt
        student_fil.close()
        
        #Hvis søket ikke gir svar, så
        if not funnet:
            #Åpner student.txt igjen
            student_fil=open('student.txt','a')
            print('Studenten ble lagt i "student.txt"')

            #Skriver så input til student.txt
            student_fil.write(sok + '\n')
            student_fil.write(ny_fornavn + '\n')
            student_fil.write(ny_etternavn + '\n')
            student_fil.write(ny_studium + '\n')
        
        #Stenger student.txt igjen
        student_fil.close()

        #Spør bruker om funksjonen skal starte på nytt
        start_pa_nytt=input('Vil du starte registreringen på nytt?'+'(Tast "j" for ja: ')
    
#Denne funksjonen tar for seg hvordan man kan slette filinnhold
def slette():

    #Legger inn ei startpånytt-løkke
    start_pa_nytt='j'
    while start_pa_nytt=='j':

        #Bolsk variabel
        funnet=False

        #Input fra bruker hva gjelder sletting av student
        sok=input('Angi studentnummer på studenten du ønsker å slette: ')

        #Åpner fil for bruk
        eksamen_fil=open('eksamensresultat.txt','r')

        #Leser første linje i eksamensfil
        emne_kode=eksamen_fil.readline()

        #Leser så resten av posten
        while emne_kode!='':
            studnr=eksamen_fil.readline()
            karakter=eksamen_fil.readline()

            #Stripper
            emne_kode=emne_kode.rstrip('\n')
            studnr=studnr.rstrip('\n')
            karakter=karakter.rstrip('\n')

            #Sjekker søket mot student
            if studnr==sok:
                #Viser svar
                print()
                print('Studenten finnes fra før, med eksamensresultat')

                #Justerer bolsk variabel
                funnet=True
            
            #Leser
            emne_kode=eksamen_fil.readline()
            studnr=eksamen_fil.readline()

        #Stenger eksamensfil
        eksamen_fil.close() 

        if funnet==False:
                
            #Åpner studentfil
            student_fil=open('student.txt')
            
            #Søker input i studentfila
            sok_2=input('Angi studentnummer igjen for å sikre sletting: ')

            #Åpner midlertidig fil
            mid_fil=open('mid_1.txt','w')

            #Lese første linje i studentfil
            studnr_stud=student_fil.readline()

            #leser resten av posten i student
            while studnr_stud!='':
                fornavn=student_fil.readline()
                etternavn=student_fil.readline()
                studium=student_fil.readline()

                #Stripper
                studnr_stud=studnr_stud.rstrip('\n')
                fornavn=fornavn.rstrip('\n')
                etternavn=etternavn.rstrip('\n')
                studium=studium.rstrip('\n')

                #Hvis input ikke stemmer for sletting så skriver jeg til midlertidig fil
                if studnr_stud != sok_2:
                    #Skriv over til midlertidig fil
                    mid_fil.write(studnr_stud + '\n')
                    mid_fil.write(fornavn + '\n')
                    mid_fil.write(etternavn + '\n')
                    mid_fil.write(studium + '\n')
                else:
                    funnet=True

                #Leser neste post
                studnr_stud=student_fil.readline()

            #Lukker student og midlertidig fil
            student_fil.close()
            mid_fil.close()

            #Sletter studentfil
            os.remove('student.txt')

            #Gir nytt navn til midlertidig fil
            os.rename('mid_1.txt','student.txt')

            #Hvis søket ikke ga svar
            if funnet:
                print('Studenten ble slettet')
            else:
                print('Studenten finnes ikke. Sletting vil ikke utføres')

        #Setter på en if for å avslutte if-setningen for ikke å gå i loop        
        if funnet==True:

            #Setter her en input på loop for å spørre bruker om den vil starte på nytt
            start_pa_nytt=input('Ønsker du å starte på nytt '+' Tast "j" for ja: ')

#Denne funksjonen tar for seg printen av studentopplysninger
def skrive():

    #Legger inn ei startpånytt-løkke
    start_pa_nytt='j'
    while start_pa_nytt=='j':
        
        funnet=False

        #Input
        sok=input('Angi studentnummer: ')

        #Åpner filer
        student_fil=open('student.txt','r')
        emne_fil=open('emne.txt','r')
        eksamen_fil=open('eksamensresultat.txt','r')

        #Leser første linje
        studnr=student_fil.readline()

        #Leser resten av posten
        while studnr!='':
            fornavn=student_fil.readline()
            etternavn=student_fil.readline()
            studium=student_fil.readline()

            #Stripper studentfil
            studnr=studnr.rstrip('\n')
            fornavn=fornavn.rstrip('\n')
            etternavn=etternavn.rstrip('\n')
            studium=studium.rstrip('\n')

            #Sjekker søket mot student
            if studnr==sok:
                print()
                print('Studentnummer:',studnr)
                print('Navn:',fornavn,etternavn)
                print('Studium:',studium)
                print()
                
                funnet=True
            #leser ny linje
            studnr=student_fil.readline()

        if funnet==True:

            #Leser første linje i eksamensresultat
            emne_kode_2=eksamen_fil.readline()
            
            while emne_kode_2!='':
                studnr=eksamen_fil.readline()
                karakter=eksamen_fil.readline()

                #Stripper eksamensresultat
                emne_kode_2=emne_kode_2.rstrip('\n')
                studnr=studnr.rstrip('\n')
                karakter=karakter.rstrip('\n')

                #Sjekker søk
                if studnr==sok:
                    
                    #Leser første linje i emnefil
                    emne_kode=emne_fil.readline()

                    #Leser resten av posten
                    while emne_kode!='':
                        emne_inf=emne_fil.readline()

                        #Stripper emnefil
                        emne_kode=emne_kode.rstrip('\n')
                        emne_inf=emne_inf.rstrip('\n')
                        
                        #Kobler sammen filer
                        if emne_kode_2==emne_kode:
                            print('Emne Kode:',emne_kode)
                            print('Emne Informasjon:',emne_inf)
                            print('Karakter:',karakter)

                            funnet=True

                        #Leser ny linje emnefil
                        emne_kode=emne_fil.readline()
                        
                #Leser ny linje fra eksamenfil
                emne_kode_2=eksamen_fil.readline()

        #Stenger emnefil
        emne_fil.close()
        
        #Stenger eksamensfil
        eksamen_fil.close()

        #Stenger studentfila
        student_fil.close()

        if funnet==True:
            
            #Spør bruker via input om utskrift skal skje på nytt
            start_pa_nytt=input('Vil du starte utskriften på nytt ' + ' Tast "j" for ja: ')
            
        #Lager en print hvis bruker angir et ikke- eksisterende studentnummer
        if funnet==False:
            print('Studenten finnes ikke, vennligst prøv igjen')
            
            #Spør bruker via input om utskrift skal skje på nytt
            start_pa_nytt=input('Vil du starte utskriften på nytt ' + ' Tast "j" for ja: ')
    
meny()

valg=int(input('Tast inn ønsket valg: '))
print()

while valg!=9:
    if valg==1:
        registrere()
        print('Du valgte [1], "Registrere student"')
        print()
    else:
        if valg==2:
            slette()
            print('Du valgte [2], "slette student"')
            print()
        else:
            if valg==3:
                skrive()
                print('Du valgte [3], "skriv ut karakterliste"')
                print()
            else:
                print('Ugyldig valg, prøv på nytt')
                print()

    print() 
    meny()
    valg=int(input('Tast inn ønsket valg: '))
    
print('Takk for at du prøvde programmet')




