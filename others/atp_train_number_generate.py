emuTypes = {
1    : '380H',
2    : '1A',
3    : '1B',
4    : '1E',
5    : '2A',
6    : '2B',
7    : '2C',
8    : '2E',
9    : '380A/AL',
10    : '380B/BL',
11    : '380CL',
12    : '380D'
                
}
index = 3
for item in emuTypes.items():
    for x in range(7):
        fmt_sql = "INSERT INTO `atpmis`.`TRAIN_NUM` (`ID`, `TRAIN_NUM`, `VALID`, `EMU_TYPE`) VALUES (%s, %s, '1', %s);"
        print fmt_sql % (index, "'" + item[1] + '-' + str(x) + "'", item[0])
        index += 1