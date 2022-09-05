import math
class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        rooms = Rooms(n)
        t = math.inf

        d = dict()
        ready = []
        for i, m in enumerate(meetings):
            if m[0] not in d.keys():
                d[m[0]] = []
            d[m[0]].append(i)
        keys = sorted(d.keys())
        
        for k in keys:
            t = k
            ready.extend(d[t])
            
            rooms.removeUsage(t)
            r = rooms.getAvailableRoom()
            index = 0
            for i in ready:
                m = meetings[i]
            
                if r != -1 and m[0] <= t: 
                    rooms.setUsage(r, t + (m[1] - m[0]))
                    r = rooms.getAvailableRoom()
                    index += 1
                else:
                    break
                
            ready = ready[index:]
            k += 1
        
        del d
        del keys

        while len(ready):
            t = rooms.nextAvailable()
            rooms.removeUsage(t)
            r = rooms.getAvailableRoom()
            index = 0
            for i in ready:
                m = meetings[i]
            
                if r != -1 and m[0] <= t: 
                    rooms.setUsage(r, t + (m[1] - m[0]))
                    r = rooms.getAvailableRoom()
                    index += 1
                else:
                    break

            ready = ready[index:]

        # print(t, rooms.getMostUsed())
        return rooms.getMostUsed()
        
        
class Room:
    def __init__(self, room_number):
        self.no = room_number
        self.isUsed = False
        self.totalMeetingsHeld = 0
        self.waitTime = 0
        
class Rooms:
    def __init__(self, n):
        self.rooms = []
        self.mostUsed = -1
        self.inUse = []
        for i in range(n):
            self.rooms.append(Room(i))
            
    def getAvailableRoom(self):
        for r in self.rooms:
            # print(r.isUsed, r.no)
            if not r.isUsed: return r.no
        
        return -1
            
    def setUsage(self, i, end):
        # print(i, end)
        self.rooms[i].isUsed = True
        self.rooms[i].totalMeetingsHeld += 1
        self.rooms[i].waitTime = end
        self.inUse.append(i)
        
        if self.mostUsed < self.rooms[i].totalMeetingsHeld:
            self.mostUsed = self.rooms[i].totalMeetingsHeld
        
    def removeUsage(self, end):
        remove = []
        for r in self.inUse:
            if self.rooms[r].waitTime <= end:
                self.rooms[r].isUsed = False
                remove.append(r)
        for i in remove:
            self.inUse.remove(i)
                
    def getMostUsed(self):
        # print(self.mostUsed)
        for r in self.rooms:
            if r.totalMeetingsHeld == self.mostUsed: return r.no
        
        return -1
                
    def nextAvailable(self):
        if len(self.inUse) < len(self.rooms): return -1
        t = math.inf
        for r in self.inUse:
            if t > self.rooms[r].waitTime:
                t = self.rooms[r].waitTime
        return t