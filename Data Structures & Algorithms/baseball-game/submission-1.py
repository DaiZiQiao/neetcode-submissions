class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record, res = [], 0

        for i in range(len(operations)):
            if operations[i] == "+":
                res += record[-1] + record[-2]
                record.append(record[-1] + record[-2])
            
            elif operations[i] == "C":
                res -= record[-1]
                record.pop()
            elif operations[i] == "D":
                res += record[-1] * 2
                record.append(record[-1]* 2)
            else:
                res += int(operations[i])
                record.append(int(operations[i]))
        
        return sum(record)