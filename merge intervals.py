Class Solution:
     def merge(self,intervels:list[list[int]])->list[list[int]]:
          intervals.sort(key=lambda i:i[0])
          output=[intervals[0]]
          for start,end in intervals[1:]:
               lastend=output[-1][1]
              if start<=lastend:
                  output[-1][1]=max(lastend,end)
              else:
                    output.append([start,end])
     return output
