import datetime as dt

l1 = [22, 59, 59]
l2 = [14, 10, 10]

main_time = []

h = l1[0] + l2[0]
m = l1[1] + l2[1]
s = l1[2] + l2[2]

main_time.append(h)
main_time.append(m)
main_time.append(s)

if s >= 60:
    m += 1
    s -= 60
    main_time.pop(1)
    main_time.insert(1, m)
    main_time.pop(2)
    main_time.insert(2, s)

if m >= 60:
    h += 1
    m -= 60
    main_time.pop(1)
    main_time.insert(1, m)
    main_time.pop(0)
    main_time.insert(0, h)

if h >= 24:
    h -= 24
    main_time.pop(0)
    main_time.insert(0, h)

t = dt.time(main_time[0], main_time[1], main_time[2])
print(t)