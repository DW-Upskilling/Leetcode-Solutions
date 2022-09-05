class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        N = len(stations)
        if not N and target != startFuel: return -1
        elif not N: return 1

        pitStops = 0
        current = 0
        lastIndex = 0

        while target - current > 0 and lastIndex < N:
            
            smax = stations[lastIndex]
            tempIndex = lastIndex + 1
            print(lastIndex, "--", stations[lastIndex::])
            if N > lastIndex:
                print("loop")
                for s in stations[lastIndex + 1::]:
                    if s[0] > target or s[0] > startFuel:
                        break
                        
                    if smax[1] <= s[1]:
                        smax = s
                    tempIndex += 1

            print(target, startFuel, current)
            print(smax, tempIndex, pitStops)
            startFuel -= smax[0]
            current += smax[0]
            pitStops += 1
            if startFuel < 0:
                break
            startFuel += smax[1]
            lastIndex = tempIndex

            if len(stations) - 1 == 0: break
        print(target, startFuel, current)    
        print(pitStops)
        print("----")
        return pitStops if target - (current + startFuel) <= 0 else -1

                
            
            