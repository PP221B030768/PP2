from datetime import datetime, timedelta
import math
date1 = input()
date2 = input()
date1 = datetime.strptime(date1, "%d %m %Y")
date2 = datetime.strptime(date2, "%d %m %Y")
res = date2 - date1
s = abs(res.days) * 86400
print(s)