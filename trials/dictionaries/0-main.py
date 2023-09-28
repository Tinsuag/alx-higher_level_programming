#!/usr/bin/python3
family = {
    'tinsae': '0916584823581921',
    'areg': '0921232332',
    'mita': '094124808999'
}

print(family['mita'])
family['ema'] = '09219929911'
del family['tinsae']
for key in family:
    print(key, ":", family[key])
