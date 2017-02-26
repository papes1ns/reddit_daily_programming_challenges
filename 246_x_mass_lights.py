BATTERY_VOLTAGE = 9
BATTERY_MILI_AMPS = 1200
LEAD_VOLTAGE = 1.7
LEAD_MILI_AMPS = 20
MAX_LEADS_ROW = int(BATTERY_VOLTAGE/LEAD_VOLTAGE)  # 5
HOURS = 20


def calculate_leads():
    amps_per_hr = BATTERY_MILI_AMPS/HOURS
    rows = amps_per_hr/LEAD_MILI_AMPS
    return rows * MAX_LEADS_ROW


def calculate_resistance():
    amps = float(((BATTERY_MILI_AMPS/HOURS) * 0.001))
    return 0.5 / amps


def draw_circuit(leads):
    diagram = ''

    for i in xrange(0, leads):
        if i == 0:
            diagram += '*'
        if i == MAX_LEADS_ROW:
            diagram += '*'

        if (i % MAX_LEADS_ROW) == 0 and i != 0:
            diagram += '-\n |\t\t\t      |\n'
            diagram += '--|>|-'
        else:
            diagram += '--|>|-'

    return diagram


print "Resistance: {0:.3f} Ohms".format(calculate_resistance())
print draw_circuit(calculate_leads())
