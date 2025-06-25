class Spreadsheet:

    def __init__(self, rows: int):
        self.ss={'A':[0]*rows,'B':[0]*rows,'C':[0]*rows,'D':[0]*rows,'E':[0]*rows,'F':[0]*rows,'G':[0]*rows,'H':[0]*rows,'I':[0]*rows,'J':[0]*rows,'K':[0]*rows,'L':[0]*rows,
                         'M':[0]*rows,'N':[0]*rows,'O':[0]*rows,'P':[0]*rows,'Q':[0]*rows,'R':[0]*rows,'S':[0]*rows,'T':[0]*rows,'U':[0]*rows,'V':[0]*rows,
                            'W':[0]*rows,'X':[0]*rows,'Y':[0]*rows,'Z':[0]*rows}
        

    def setCell(self, cell: str, value: int) -> None:
        key=cell[0]
        index=int(cell[1:])-1
        self.ss[key][index]=value

    def resetCell(self, cell: str) -> None:
        key=cell[0]
        index=int(cell[1:])-1
        self.ss[key][index]=0

    def getValue(self, formula: str) -> int:
        formula=formula[1:]
        parts=formula.split("+")
        total=0
        for i in parts:
            if i.isdigit():
                total+=int(i)
            else:
                total+=self.ss[i[0]][int(i[1:])-1]
        return total
        
