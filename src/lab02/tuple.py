def format_record(rec):
    if not isinstance(rec, tuple) or len(rec) != 3:
        return 'TypeError'

    fio, group, gpa = rec

    gpa = f'{gpa:.2f}'

    fio = fio.strip()
    while '  ' in fio:
        fio = fio.replace('  ', ' ')


    lastname_N_O = [list(word) for word in fio.split()]
    lastname_N_O[0][0] = lastname_N_O[0][0].upper()
    lastname_N_O[1][0] = lastname_N_O[1][0].upper()

    if len(lastname_N_O)>2:
        lastname_N_O[2][0] = lastname_N_O[2][0].upper()

    form1 = "".join(lastname_N_O[0])
    form2 = "".join(lastname_N_O[1][0])
    if len(lastname_N_O) > 2:
        form3 = "".join(lastname_N_O[2][0])
        return f'{form1} {form2}. {form3}., {group} {gpa}'
    else:
        return f'{form1} {form2}., {group} {gpa}'

print(format_record(("Петров пётр", "IKBO-12", 5.0)))
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))