# from infos_cole import dias
import webbrowser
import time
import sys



dias = {
    1: [
        ['07:00', ['Geschichte', 'meet.google.com/ffr-ystt-nzt']],
        ['08:15', ['Physik', 'meet.google.com/pmo-qzhf-fqq']],
        ['09:45', ['Chemie', 'meet.google.com/jgh-ntpd-ayx']],
        ['11:15', ['Castellano', 'meet.google.com/iwa-wjwp-ajx']],
    ],

    2: [
        ['07:00', ['Ethik', 'meet.google.com/gdz-mdmz-egu?authuser=0']], # Link de Classroom
        ['08:15', ['Deutsch', 'meet.google.com/ujt-oghz-vxp']],
        ['09:45', ['Frances', 'classroom.google.com']],
        ['11:15', ['English', 'meet.google.com/tch-pnrd-krt']],
    ],

    3: [
        ['07:00', ['Mathe', 'classroom.google.com']],
        ['08:15', ['Kunst', 'meet.google.com/lookup/ernnqog6c4?authuser=0&hs=179']],
        ['09:45', ['Geografia', 'meet.google.com/vib-yhbv-oab']],
        ['10:20', ['Geschichte', 'meet.google.com/cqk-jbug-tao']],
        ['11:15', ['Deutsch', 'meet.google.com/jsm-tvjo-ctb']],
        ['11:50', ['Geopraphie', 'meet.google.com/jqw-amrf-gdn']]
    ],


    4: [
        ['07:00', ['Castellano', 'meet.google.com/owf-dcuh-bdi']],
        ['08:15', ['Mathe', 'classroom.google.com']],
        ['08:50', ['Frances', 'classroom.google.com']],
        ['09:45', ['Formacion Civico', 'meet.google.com/ykg-uwne-mci']],
        ['11:15', ['Biologie', 'classroom.google.com']],
        ['12:45', ['Sport', 'meet.google.com/vig-tsmt-uxb']],
    ],

    5: [
        ['07:00', ['Catedra Bolivariana', 'meet.google.com/vny-tymq-vjv']],
        ['08:15', ['English', 'meet.google.com/aqj-sbtb-nox']],
        ['09:45', ['Mathe', 'meet.google.com/knk-jjcv-aec']],
        ['11:15', ['English', 'meet.google.com/twz-pbex-hmn']],
    ],
}



def zeit_vor_min():
    '''
    :return: Time 1 minute ago in str and then int
    '''

    minutes = str(int(time.ctime(time.time())[14:16]) + 1)
    hours = time.ctime(time.time())[11:13]

    if minutes == '60':
        minutes = str(00)
        hours = str(int(hours) + 1)
    if int(minutes) < 10:
        minutes = '0' + minutes

    zahlzeit = int(hours + minutes)
    number_zahlzeit = str(zahlzeit)

    if len(str(zahlzeit)) == 3:
        uhrzeit = '0' + number_zahlzeit[0] + ':' + number_zahlzeit[1:]
    else:
        uhrzeit = number_zahlzeit[0:2] + ':' + number_zahlzeit[2:4]
    return uhrzeit, zahlzeit
print('En este momento son las', zeit_vor_min()[0])


dia_semana = time.localtime(time.time())[6] + 1
if 0 < dia_semana < 6:
    numero_de_hora = 0
                        # Todo: si llego despues de la ultima clase, meteme
                        # todo: o quizas no
    proxima_clase_hora = int(str(dias[dia_semana][numero_de_hora][0][0:2]) + str(dias[dia_semana][numero_de_hora][0][3:5]))
    while zeit_vor_min()[1] > proxima_clase_hora:
        numero_de_hora += 1
        try:
            proxima_clase_hora = int(str(dias[dia_semana][numero_de_hora][0][0:2]) + str(dias[dia_semana][numero_de_hora][0][3:5]))
        except:
            if dia_semana == 4:
                if zeit_vor_min()[1] < 2000:
                    webbrowser.open("https:\\" + dias[dia_semana][numero_de_hora - 1][1][1])
                    print("Esta es tu ultima clase, pero estas llegando tarde, que no se repita! ")
                    sys.exit()
            elif 1 <= dia_semana <= 5:
                if zeit_vor_min()[1] < 1215:
                    webbrowser.open("https:\\" + dias[dia_semana][numero_de_hora - 1][1][1])
                    print("Esta es tu ultima clase, pero estas llegando tarde, que no se repita! ")
                    sys.exit()
            print(f"Mano, son las {zeit_vor_min()[0]}, por que mierda te quieres meter a clases ahorita?")
            sys.exit()

    if zeit_vor_min()[1] < 659:
        numero_de_hora += 1
    numero_de_hora -= 1
    current_url = dias[dia_semana][numero_de_hora][1][1]


                                                                                            # checks wether day is in week
    llegando_tarde = True
    while True:

        if zeit_vor_min()[0] == dias[dia_semana][numero_de_hora][0] or llegando_tarde and zeit_vor_min()[1] > 658 :                                                   # if current time = class time
            webbrowser.open('https:\\' + current_url)
            numero_de_hora += 1
            current_url = dias[dia_semana][numero_de_hora][1][1]
            llegando_tarde = False
            # time.sleep(60)
        time.sleep(60)                                                                                                  # esperar
else:
    print(f"It is the day #{dia_semana} of the week and the current time is {time.ctime()[11:16]}")
    print("Estas en fin de semana asi que relajate, hoy no hay clase.")
