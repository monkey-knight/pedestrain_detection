class Split_Msgs:
    def __init__(self, completemsg, msgname):
        self.msgname = msgname
        self.completemsg = completemsg
        self.Name_Length = len(msgname)
        self.One_Message_Size = 100000
        self.Message_Num = len(completemsg) // self.One_Message_Size
        self.Mod_Num = len(completemsg) % self.One_Message_Size
        if self.Mod_Num != 0:
            self.Message_Num += 1

    def getmsglist(self):

        ans = []
        Str_Msg_Size = self.intto10(self.Name_Length)
        Str_Msg_Num = self.intto10(self.Message_Num)
        for i in range(0, self.Message_Num - 1, 1):
            Msg_Ind = self.intto10(i)
            One_Msg = Str_Msg_Size + Str_Msg_Num + Msg_Ind + self.msgname
            One_Msg = One_Msg + self.completemsg[i * self.One_Message_Size:(i + 1) * self.One_Message_Size]

            ans.append(One_Msg)

        Msg_Ind = self.intto10(self.Message_Num - 1)
        One_Msg = Str_Msg_Size + Str_Msg_Num + Msg_Ind + self.msgname
        One_Msg = One_Msg + self.completemsg[(self.Message_Num - 1) * self.One_Message_Size:]
        ans.append(One_Msg)
        return ans

    # int 12 out 0000000012
    def intto10(self, intnum):
        strint = str(intnum)
        needzerolen = 10 - len(strint)
        needzero = ''
        for i in range(0, needzerolen, 1):
            needzero += '0'

        ans = needzero + strint
        return ans


class Merge_Msgs:
    def __init__(self):
        self.Need_Merge_Msgs = {}
        self.nowans = ""
        self.msgname = ""

    def ten2int(self, strint):
        zeronum = 0
        for i in range(0, 9, 1):
            if strint[i] == '0':
                zeronum += 1
            else:
                break

        ansstr = strint[zeronum:]
        return int(ansstr)

    def putmsg(self, onemsg):
        Name_Length = self.ten2int(onemsg[:10])
        Msg_Size = self.ten2int(onemsg[10:20])
        Msg_Index = self.ten2int(onemsg[20:30])
        Msg_Name = onemsg[30:30 + Name_Length]
        One_Msg = onemsg[30 + Name_Length:]

        if Msg_Name not in self.Need_Merge_Msgs:
            self.Need_Merge_Msgs[Msg_Name] = []

        self.Need_Merge_Msgs[Msg_Name].append(One_Msg)
        if len(self.Need_Merge_Msgs[Msg_Name]) == Msg_Size:
            self.setcompletemsg(Msg_Name)
            return True
        else:
            return False

    def setcompletemsg(self, Msg_Name):
        Will_Merge_Msg = self.Need_Merge_Msgs[Msg_Name]
        self.nowans = ""
        for msg in Will_Merge_Msg:
            self.nowans += msg

        del self.Need_Merge_Msgs[Msg_Name]
        self.msgname = Msg_Name

    def getcpmsg(self):
        return self.nowans

    def getmsgname(self):
        return self.msgname
