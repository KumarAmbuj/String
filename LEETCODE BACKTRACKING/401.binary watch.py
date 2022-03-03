class Solution:
    def findhours(self, i, hours, n, h, sm, li):

        if i == 0:
            if sm <= 11:
                h.append(sm)

            return

        for k in range(li + 1, n):
            self.findhours(i - 1, hours, n, h, sm + hours[k], k)

    def findmins(self, i, mins, n, m, sm, li):
        if i == 0:
            if sm <= 59:
                m.append(sm)
            return

        for k in range(li + 1, n):
            self.findmins(i - 1, mins, n, m, sm + mins[k], k)

    def readBinaryWatch(self, num: int) -> List[str]:
        hours = [1, 2, 4, 8]
        mins = [1, 2, 4, 8, 16, 32]

        res = []

        for i in range(num, -1, -1):
            h = []
            if i > 0:

                self.findhours(i, hours, 4, h, 0, -1)
            else:
                h.append(0)

            m = []
            if num - i > 0:
                self.findmins(num-i, mins, 6, m, 0, -1)
            else:
                m.append(0)

            for x in h:

                for z in m:

                    hr = str(x)
                    mn = str(z)

                    if len(mn) == 1:
                        res.append("{}:{}".format(hr, '0' + mn))
                    else:
                        res.append("{}:{}".format(hr, mn))
        return res



