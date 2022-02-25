def timeToSecond(time):
    h, m, s = time.split(':')
    return int(h)*3600 + int(m)*60 + int(s)

def solution(play_time, adv_time, logs):
    play_time = timeToSecond(play_time)
    play = [0 for _ in range(play_time+1)]

    for log in logs:
        s, e = map(timeToSecond,log.split('-'))
        play[s] += 1
        play[e] -= 1
    for i in range(1,play_time+1):
        play[i] += play[i-1]
    
    minTime = 0
    adv_time = timeToSecond(adv_time)
    maxVal = sum(play[:adv_time])
    curVal = maxVal

    for i in range(1,play_time-adv_time+1):
        curVal = curVal-play[i-1]+play[i+adv_time-1]
        if curVal > maxVal:
            minTime = i
            maxVal = curVal

    h = ('0'+str(minTime//3600))[-2:]
    m = ('0'+str((minTime%3600)//60))[-2:]
    s = ('0'+str(minTime%60))[-2:]
    return h+':'+m+':'+s

play_time, adv_time, logs = "02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]
print(solution(play_time, adv_time, logs))