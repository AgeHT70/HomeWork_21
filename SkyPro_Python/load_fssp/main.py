import datetime

# from oraconnect import OraConnect
# import cx_Oracle


def main():
    # case1 = OraConnect('case1', 'case319s1', cx_Oracle.makedsn('10.248.9.13', '1521', service_name='upmo2005'))

    with open('UII_1.csv', encoding="866") as file:
        headers = file.readline().strip().split(';')
        next_string = file.readline().strip().split(';')

    if next_string[12]:
        fio = next_string[12]
    else:
        fio = ''

    if next_string[0]:
        d_rojd, m_rojd, y_rojd = map(int, next_string[0].split('.'))
    else:
        d_rojd, m_rojd, y_rojd = '', '', ''

    if next_string[0]:
        d_resh, m_resh, y_resh = map(int, next_string[14].split('.'))
    else:
        d_resh, m_resh, y_resh = '', '', ''
    if next_string[6]:
        d_sover, m_sover, y_sover = map(int, next_string[6].split('.'))
    else:
        d_sover, m_sover, y_sover = '', '', ''

    if next_string[15]:
        raz_nak = int(next_string[15])
    else:
        raz_nak = ''

    if next_string[11]:
        n_prot = next_string[11]
    else:
        n_prot = ''

    mesto_rojd = next_string[1].split(',')
    resp = mesto_rojd[1]
    kraj = mesto_rojd[2]
    rajon = mesto_rojd[3]
    kw_punkt = mesto_rojd[4] if mesto_rojd[4] else mesto_rojd[5]
    ulica = mesto_rojd[6]
    n_dom = mesto_rojd[7]
    korpus = mesto_rojd[8]
    kw = mesto_rojd[9]

    psp_s = next_string[4]
    psp_n = next_string[3]
    vydan = next_string[7]

    if next_string[16]:
        uin = int(next_string[16])
    else:
        uin = ''

    dt_reg = dt_izm = datetime.date.today()
    kodrai = 'ФССП'
    kodrai1_kod = 22
    kodreg = 72
    sh_polz = 22
    sh_polz1 = 22
    dostup = 1
    ibd_arx = 1
    if next_string[10]:
        d_oplat, m_oplat, y_oplat = map(int, next_string[10].split('.'))
    else:
        d_oplat, m_oplat, y_oplat = '', '', ''
    kateg = 1
    vid_doc = 1
    n_post = next_string[11]
    dt_reg_resh = next_string[14]
    if next_string[9]:
        d_zakon, m_zakon, y_zakon = map(int, next_string[9].split('.'))
    else:
        d_zakon, m_zakon, y_zakon = '', '', ''
    fabula = next_string[18] + '||' + next_string[19]
    slugba_sost = 52
    y_vvod = datetime.date.today().year
    m_vvod = datetime.date.today().month
    d_vvod = datetime.date.today().day
    slugba = 52
    print(
        f'''
        fio={fio},
        --------------------
        d_rojd = {d_rojd},
        m_rojd = {m_rojd},
        y_rojd = {y_rojd},
        ---------------------
        d_sover = {d_sover},
        m_sover = {m_sover},
        y_sover = {y_sover},
        ---------------------
        pr_vid1 = 
        pr_vid2 = 
        ---------------------
        slugba = {slugba}
        ---------------------
        mera_nak = 
        raz_nak = {raz_nak}
        ---------------------
        n_prot = {n_prot}
        org_resh = 
        ----------------------
        resp = {resp},
        kraj = {kraj},
        rajon = {rajon},
        kw_punkt = {kw_punkt},
        ulica = {ulica},
        n_dom = {n_dom},
        korpus = {korpus},
        kw = {kw},
        ----------------------
        psp_s = {psp_s},
        psp_n = {psp_n},
        vydan = {vydan},
        ---------------------
        d_resh = {d_resh},
        m_resh = {m_resh},
        y_resh = {y_resh},
        ---------------------
        dt_reg = {dt_reg},
        dt_izm = {dt_izm},
        ---------------------
        kodrai = {kodrai},
        kodrai1_kod = {kodrai1_kod},
        kodreg = {kodreg},
        ---------------------
        sh_polz = {sh_polz}
        sh_polz1 = {sh_polz1}
        dostup = {dostup},
        ibd_arx = {ibd_arx},
        ---------------------
        y_oplat = {y_oplat},
        m_oplat = {m_oplat},
        d_oplat = {d_oplat},
        ---------------------
        kateg = {kateg},
        vid_doc = {vid_doc},
        n_post = {n_post},
        dt_reg_resh = {dt_reg_resh},
        ---------------------
        y_zakon = {y_zakon},
        m_zakon = {m_zakon},
        d_zakon = {d_zakon},
        ---------------------
        fabula = {fabula},
        slugba_sost = {slugba_sost},
        ---------------------
        y_vvod = {y_vvod},
        m_vvod = {m_vvod},
        d_vvod = {d_vvod},
        ---------------------
        uin = {uin}
''')


if __name__ == '__main__':
    main()
